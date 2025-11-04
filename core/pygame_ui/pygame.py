import pygame
from typing import Optional, List, Tuple, Dict, Any

from core.controlador.vista_juego import IVistaJuego
from core.controlador.acciones import (
    Accion,
    AccionLanzar,
    AccionMover,
    AccionPoner,
    AccionSalir
)


# --- Constantes de Colores y Geometría ---
# Colores
COLOR_FONDO = (0, 50, 0)       # Verde oscuro
COLOR_TABLERO = (200, 180, 140) # Beige
COLOR_TRIANGULO_1 = (120, 60, 20) # Marrón
COLOR_TRIANGULO_2 = (240, 230, 220) # Crema
COLOR_FICHA_B = (255, 255, 255) # Blanco
COLOR_FICHA_N = (0, 0, 0)       # Negro
COLOR_TEXTO = (255, 255, 255)
COLOR_ERROR = (255, 50, 50)
COLOR_HIGHLIGHT = (255, 255, 0, 100) # Amarillo semitransparente

# Geometría
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MARGEN_LATERAL = 40
MARGEN_VERTICAL = 40
ANCHO_BARRA = 50
RADIO_FICHA = 20
DIAMETRO_FICHA = RADIO_FICHA * 2
ANCHO_PUNTO = (SCREEN_WIDTH - (MARGEN_LATERAL * 2) - ANCHO_BARRA) // 12
ALTO_PUNTO = (SCREEN_HEIGHT // 2) - (MARGEN_VERTICAL * 1.5)


class VistaPygame(IVistaJuego):
    """
    Implementación de la interfaz de vista para jugar con Pygame.
    
    Maneja un estado interno simple para la selección de fichas:
    - self.seleccion_origen: Almacena la posición (0-23 o 'barra_b'/'barra_n')
      de la ficha que el usuario ha clickeado. Se resetea tras un
      movimiento válido.
    """

    def __init__(self):
        self.screen = None
        self.font = None
        self.clock = None

        self.dados_actuales = []

        # --- Estado Interno de la Vista ---
        self.seleccion_origen = None
        self.mensaje_info = None

        # --- Geometría Precalculada ---
        # Diccionarios que mapean IDs de elementos a sus Rects de Pygame
        # para facilitar la detección de clics y el dibujado.
        self.rects_puntos = {}
        self.rects_dados = []
        self.rect_barra_b = None
        self.rect_barra_n = None
        self.rect_fuera_b = None
        self.rect_fuera_n = None
        self.puntos_triangulos_top = []
        self.puntos_triangulos_bot = []

    # --- 1. Métodos de la Interfaz (IVistaJuego) ---

    def inicializar(self) -> None:
        """Inicializa Pygame, la ventana y calcula la geometría."""
        pygame.init()
        pygame.font.init()
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Backgammon")
        self.font = pygame.font.Font('assets/Roboto-Regular.ttf', 28)
        self.clock = pygame.time.Clock()

        self._calcular_geometria()
        print("Vista de Pygame inicializada.")

    def dibujar_tablero(self, tablero, dados, jugador_actual) -> None:
        """Dibuja el estado completo del juego en la ventana."""
        self.dados_actuales = dados
        
        if not self.screen:
            return

        # 1. Limpiar pantalla
        self.screen.fill(COLOR_FONDO)

        # 2. Dibujar fondo del tablero y barra
        rect_tablero = pygame.Rect(MARGEN_LATERAL, MARGEN_VERTICAL, SCREEN_WIDTH - MARGEN_LATERAL * 2, SCREEN_HEIGHT - MARGEN_VERTICAL * 2)
        pygame.draw.rect(self.screen, COLOR_TABLERO, rect_tablero)
        
        rect_barra_centro = pygame.Rect(SCREEN_WIDTH // 2 - ANCHO_BARRA // 2, MARGEN_VERTICAL, ANCHO_BARRA, SCREEN_HEIGHT - MARGEN_VERTICAL * 2)
        pygame.draw.rect(self.screen, COLOR_FONDO, rect_barra_centro)

        # 3. Dibujar Triángulos (Puntos)
        # Iterar sobre la lista de la FILA SUPERIOR (NUEVO)
        for i, puntos in enumerate(self.puntos_triangulos_top):
            # El primer triángulo (i=0) es Marrón
            color = COLOR_TRIANGULO_1 if i % 2 == 0 else COLOR_TRIANGULO_2
            pygame.draw.polygon(self.screen, color, puntos)
        
        # Iterar sobre la lista de la FILA INFERIOR (NUEVO)
        for i, puntos in enumerate(self.puntos_triangulos_bot):
            # El patrón de color se invierte
            # El primer triángulo (i=0) es Crema
            color = COLOR_TRIANGULO_2 if i % 2 == 0 else COLOR_TRIANGULO_1
            pygame.draw.polygon(self.screen, color, puntos)

        # 4. Dibujar Fichas, Barra y Fichas Fuera
        self._dibujar_fichas_tablero(tablero.posiciones)
        self._dibujar_fichas_barra(tablero.barra)
        self._dibujar_fichas_fuera(tablero.fuera)

        # 5. Dibujar UI (Dados, Turno, Mensajes)
        self._dibujar_dados(dados)
        self._dibujar_turno(jugador_actual)
        self._dibujar_mensajes()

        # 6. Dibujar Resaltado (Highlight)
        self._dibujar_seleccion()

        # 7. Actualizar pantalla
        pygame.display.flip()

    def obtener_entrada(self):
        """Procesa el bucle de eventos de Pygame de forma no bloqueante."""
        if not self.clock:
            return None

        # Limitar FPS para no consumir 100% de CPU
        self.clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return AccionSalir()
            
            # --- Entrada de Teclado ---
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Limpiar selección y mensaje al lanzar
                    self.seleccion_origen = None
                    self.mensaje_info = None
                    return AccionLanzar()
                if event.key == pygame.K_ESCAPE:
                    # Cancelar selección actual
                    self.seleccion_origen = None

            # --- Entrada de Mouse ---
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button != 1: # Solo clic izquierdo
                    return None

                pos_clic = event.pos
                
                # 1. Identificar qué se clickeó
                elemento_clic = self._coords_a_elemento(pos_clic)

                if elemento_clic is None:
                    # Clic en espacio vacío, cancelar selección
                    self.seleccion_origen = None
                    return None

                tipo_clic, valor_clic = elemento_clic

                # 2. Lógica de primer/segundo clic
                if self.seleccion_origen is None:
                    # --- PRIMER CLIC (Seleccionar Origen) ---
                    if tipo_clic == 'punto' or tipo_clic == 'barra':
                        self.seleccion_origen = valor_clic # Almacena el ID (0-23 o 'barra_b')
                        self.mensaje_info = None # Limpiar mensaje
                    return None
                
                else:
                    # --- SEGUNDO CLIC (Seleccionar Dado/Destino) ---
                    
                    # Clicó en un dado, vamos a mover/poner
                    if tipo_clic == 'dado':
                        indice_dado = valor_clic # Esto es un índice (0, 1...)
                        
                        try:
                            # --- FIX ---
                            # Busca el valor real del dado usando el índice
                            dado_valor_real = self.dados_actuales[indice_dado] 
                        except IndexError:
                            continue # Error, clic en un dado fantasma

                        origen = self.seleccion_origen
                        self.seleccion_origen = None # Resetear selección
                        
                        if isinstance(origen, int):
                            # Es un movimiento desde el tablero
                            posicion_1_24 = origen + 1
                            return AccionMover(origen=posicion_1_24, dado=dado_valor_real)
                        
                        elif origen.startswith('barra'):
                            # Es una puesta desde la barra
                            return AccionPoner(dado=dado_valor_real)
                    
                    # Clicó en otra ficha, la cambia
                    elif tipo_clic == 'punto' or tipo_clic == 'barra':
                        self.seleccion_origen = valor_clic
                        return None
                    
                    # Clicó en cualquier otra cosa, cancela
                    else:
                        self.seleccion_origen = None
                        return None

        return None # No hay acción en este frame

    def mostrar_mensaje(self, mensaje: str) -> None:
        """Muestra un mensaje informativo en pantalla."""
        # Almacena (texto, color, timestamp)
        self.mensaje_info = (mensaje, COLOR_TEXTO, pygame.time.get_ticks())

    def mostrar_error(self, error: str) -> None:
        """Muestra un mensaje de error en pantalla."""
        # Almacena (texto, color, timestamp)
        # El error se borrará automáticamente después de 3 segundos
        self.mensaje_info = (str(error), COLOR_ERROR, pygame.time.get_ticks())

    def cerrar(self) -> None:
        """Cierra Pygame."""
        print("\n--- Gracias por jugar. ¡Adiós! ---")
        pygame.quit()

    # --- 2. Métodos de Ayuda (Helpers) de Pygame ---

    def _calcular_geometria(self):
        """Calcula y almacena los Rects para clics y dibujado."""
        
        # Limpiar listas por si se recalcula
        self.puntos_triangulos_top.clear()
        self.puntos_triangulos_bot.clear()
        self.rects_puntos.clear()

        # Puntos (Triángulos)
        for i in range(12):
            # --- LÓGICA CORREGIDA PARA FILA SUPERIOR ---
            # Se calcula de izquierda a derecha, igual que la inferior
            base_x = MARGEN_LATERAL + (ANCHO_PUNTO * i)
            if i >= 6:
                base_x += ANCHO_BARRA # El offset se SUMA, igual que la inferior
            
            rect_sup = pygame.Rect(base_x, MARGEN_VERTICAL, ANCHO_PUNTO, ALTO_PUNTO)
            puntos_sup = [
                (rect_sup.left, rect_sup.top),  # Apuntan hacia abajo
                (rect_sup.right, rect_sup.top),
                (rect_sup.centerx, rect_sup.bottom)
            ]
            # El índice se guarda invertido (mapa 12-1)
            # El punto más a la izquierda (i=0) es el punto 12 (índice 11)
            self.rects_puntos[11 - i] = rect_sup 
            self.puntos_triangulos_top.append(tuple(puntos_sup)) # Usar la nueva lista

            # --- LÓGICA DE FILA INFERIOR (SIN CAMBIOS) ---
            base_x = MARGEN_LATERAL + (ANCHO_PUNTO * i)
            if i >= 6:
                base_x += ANCHO_BARRA # Offset por la barra

            rect_inf = pygame.Rect(base_x, SCREEN_HEIGHT - MARGEN_VERTICAL - ALTO_PUNTO, ANCHO_PUNTO, ALTO_PUNTO)
            puntos_inf = [
                (rect_inf.left, rect_inf.bottom), # Apuntan hacia arriba
                (rect_inf.right, rect_inf.bottom),
                (rect_inf.centerx, rect_inf.top)
            ]
            # El punto más a la izquierda (i=0) es el punto 13 (índice 12)
            self.rects_puntos[12 + i] = rect_inf
            self.puntos_triangulos_bot.append(tuple(puntos_inf)) # Usar la nueva lista

        # Barra
        self.rect_barra_n = pygame.Rect(SCREEN_WIDTH // 2 - ANCHO_BARRA // 2, MARGEN_VERTICAL, ANCHO_BARRA, SCREEN_HEIGHT // 2 - MARGEN_VERTICAL)
        self.rect_barra_b = pygame.Rect(SCREEN_WIDTH // 2 - ANCHO_BARRA // 2, SCREEN_HEIGHT // 2, ANCHO_BARRA, SCREEN_HEIGHT // 2 - MARGEN_VERTICAL)

        # Fichas Fuera (a la derecha de la barra)
        self.rect_fuera_n = pygame.Rect(SCREEN_WIDTH - MARGEN_LATERAL + 5, MARGEN_VERTICAL, MARGEN_LATERAL - 10, SCREEN_HEIGHT // 2 - MARGEN_VERTICAL)
        self.rect_fuera_b = pygame.Rect(SCREEN_WIDTH - MARGEN_LATERAL + 5, SCREEN_HEIGHT // 2, MARGEN_LATERAL - 10, SCREEN_HEIGHT // 2 - MARGEN_VERTICAL)

    def _coords_a_elemento(self, pos):
        """Convierte coordenadas (x, y) a un elemento del juego."""
        
        # 1. Comprobar Puntos (0-23)
        for i, rect in self.rects_puntos.items():
            if rect.collidepoint(pos):
                return ('punto', i) # Devuelve el índice (0-23)
        
        # 2. Comprobar Barras
        if self.rect_barra_b and self.rect_barra_b.collidepoint(pos):
            return ('barra', 'barra_b')
        if self.rect_barra_n and self.rect_barra_n.collidepoint(pos):
            return ('barra', 'barra_n')
        
        # 3. Comprobar Dados
        for i, rect in enumerate(self.rects_dados):
            if rect.collidepoint(pos):
                return ('dado', i) # Devuelve el índice del dado (0, 1, 2, 3)

        return None # Clic en espacio vacío

    def _id_a_coords_ficha(self, id_elemento, num_ficha):
        """Calcula el centro (x, y) para dibujar una ficha."""
        
        y_offset = (num_ficha * DIAMETRO_FICHA) + RADIO_FICHA + 5 # 5 de padding
        
        # Fichas en la barra
        if id_elemento == 'barra_b' and self.rect_barra_b:
            return (self.rect_barra_b.centerx, self.rect_barra_b.top + y_offset)
        if id_elemento == 'barra_n' and self.rect_barra_n:
            return (self.rect_barra_n.centerx, self.rect_barra_n.bottom - y_offset)
        
        # Fichas en el tablero
        if isinstance(id_elemento, int):
            rect = self.rects_puntos[id_elemento]
            if id_elemento < 12: # Fila superior
                return (rect.centerx, rect.top + y_offset)
            else: # Fila inferior
                return (rect.centerx, rect.bottom - y_offset)
        
        return (0, 0) # Fallback

    def _dibujar_fichas_tablero(self, posiciones):
        """Dibuja todas las fichas en los 24 puntos."""
        for i, lista_fichas in enumerate(posiciones):
            color = COLOR_FICHA_B if lista_fichas and lista_fichas[0] == 'B' else COLOR_FICHA_N
            for j in range(len(lista_fichas)):
                # Mostrar máx 5 fichas, luego un contador
                if j >= 5:
                    (x, y) = self._id_a_coords_ficha(i, j)
                    texto_surf = self.font.render(f"+{len(lista_fichas) - 5}", True, COLOR_ERROR)
                    self.screen.blit(texto_surf, (x - texto_surf.get_width() // 2, y - texto_surf.get_height() // 2))
                    break
                
                (x, y) = self._id_a_coords_ficha(i, j)
                pygame.draw.circle(self.screen, color, (x, y), RADIO_FICHA)
                pygame.draw.circle(self.screen, (100, 100, 100), (x, y), RADIO_FICHA, 2) # Borde

    def _dibujar_fichas_barra(self, barra):
        """Dibuja las fichas en la barra."""
        # Fichas Blancas ('B', índice 0)
        for i in range(barra[0]):
            (x, y) = self._id_a_coords_ficha('barra_b', i)
            pygame.draw.circle(self.screen, COLOR_FICHA_B, (x, y), RADIO_FICHA)
            pygame.draw.circle(self.screen, (100, 100, 100), (x, y), RADIO_FICHA, 2)
            
        # Fichas Negras ('N', índice 1)
        for i in range(barra[1]):
            (x, y) = self._id_a_coords_ficha('barra_n', i)
            pygame.draw.circle(self.screen, COLOR_FICHA_N, (x, y), RADIO_FICHA)
            pygame.draw.circle(self.screen, (100, 100, 100), (x, y), RADIO_FICHA, 2)

    def _dibujar_fichas_fuera(self, fuera):
        """Dibuja el contador de fichas fuera."""
        if not self.rect_fuera_b or not self.rect_fuera_n or not self.font:
            return
            
        pygame.draw.rect(self.screen, (50,50,50), self.rect_fuera_b)
        pygame.draw.rect(self.screen, (50,50,50), self.rect_fuera_n)

        # Contadores
        texto_b = self.font.render(f"B: {fuera[0]}", True, COLOR_FICHA_B)
        texto_n = self.font.render(f"N: {fuera[1]}", True, COLOR_FICHA_N)
        
        self.screen.blit(texto_b, self.rect_fuera_b.move(5, 5))
        self.screen.blit(texto_n, self.rect_fuera_n.move(5, 5))

    def _dibujar_dados(self, dados):
        """Dibuja los dados disponibles."""
        if not self.font:
            return
            
        self.rects_dados = [] # Limpiar rects de dados
        texto_base = self.font.render("Dados:", True, COLOR_TEXTO)
        self.screen.blit(texto_base, (MARGEN_LATERAL, 10))
        
        x_offset = texto_base.get_width() + 10
        for i, dado_val in enumerate(dados):
            texto_dado = self.font.render(str(dado_val), True, (0,0,0), (200,200,200))
            rect_dado = texto_dado.get_rect(topleft=(MARGEN_LATERAL + x_offset, 10))
            
            # Hacer el rect un poco más grande para el clic
            rect_clic = rect_dado.inflate(10, 10) 
            self.rects_dados.append(rect_clic)
            
            # Dibujar un fondo para el dado
            pygame.draw.rect(self.screen, (200,200,200), rect_clic)
            self.screen.blit(texto_dado, rect_dado)
            
            x_offset += rect_clic.width + 5

    def _dibujar_turno(self, jugador_actual):
        """Dibuja de quién es el turno."""
        if not self.font:
            return
            
        if jugador_actual:
            texto = f"Turno de: {jugador_actual.nombre} ({jugador_actual.color})"
        else:
            texto = "Tirada inicial..."
        
        surf = self.font.render(texto, True, COLOR_TEXTO)
        x_pos = SCREEN_WIDTH - surf.get_width() - MARGEN_LATERAL
        self.screen.blit(surf, (x_pos, 10))

    def _dibujar_mensajes(self):
        """Dibuja mensajes de error o info temporales."""
        if not self.font or not self.screen:
            return
            
        if self.mensaje_info:
            texto, color, timestamp = self.mensaje_info
            
            # Borrar mensaje después de 3 segundos
            if pygame.time.get_ticks() - timestamp > 3000:
                self.mensaje_info = None
                return
                
            surf = self.font.render(texto, True, color)
            x_pos = (SCREEN_WIDTH - surf.get_width()) // 2
            y_pos = SCREEN_HEIGHT - surf.get_height() - 10
            
            # Fondo semitransparente para el mensaje
            fondo_rect = surf.get_rect(topleft=(x_pos, y_pos)).inflate(10, 5)
            fondo_surf = pygame.Surface(fondo_rect.size, pygame.SRCALPHA)
            fondo_surf.fill((0, 0, 0, 150))
            self.screen.blit(fondo_surf, fondo_rect)
            
            self.screen.blit(surf, (x_pos + 5, y_pos + 2))

    def _dibujar_seleccion(self):
        """Dibuja un resaltado en la ficha/barra seleccionada."""
        if self.seleccion_origen is None or not self.screen:
            return

        try:
            # Crear una superficie semitransparente para el resaltado
            highlight_surf = pygame.Surface((DIAMETRO_FICHA, DIAMETRO_FICHA), pygame.SRCALPHA)
            pygame.draw.circle(highlight_surf, COLOR_HIGHLIGHT, (RADIO_FICHA, RADIO_FICHA), RADIO_FICHA)
            
            # Obtener coords de la *primera* ficha en la pila
            (x, y) = self._id_a_coords_ficha(self.seleccion_origen, 0)
            
            self.screen.blit(highlight_surf, (x - RADIO_FICHA, y - RADIO_FICHA))
        
        except Exception:
            # Fallback por si las coords no son válidas
            self.seleccion_origen = None