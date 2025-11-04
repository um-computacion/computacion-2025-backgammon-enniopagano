## Claude Sonnet 4 - 26/8/2025

### Prompt:
Estoy empezando un proyecto de programación en python orientado a objetos, el proyecto es un emulador del juego de mesa backgammon, lo realizaré a través de github, empezaré por crear el tablero. Cómo harías algo lo más parecido a un tablero de backgammon que se pueda mostrar por consola? Qué forma le darías?

No hubo instrucciones del sistema

Resultado de la IA:


La parte en **negrita** o encerrado entre asteriscos dobles **, será la salida que está presente en el código
La salida está en el codigo con modificaciones 


**class BackgammonBoard:
    def __init__(self):
        # Inicializar el tablero con 24 puntos (cada punto es una lista de fichas)
        self.points = [[] for _ in range(24)]
        
        # Bar para fichas capturadas [jugador1, jugador2]
        self.bar = [0, 0]
        
        # Fichas que han salido del tablero [jugador1, jugador2]
        self.bear_off = [0, 0]
        
        # Símbolos para cada jugador        | Esta parte no está en el código
        self.player_symbols = ['X', 'O']    |
        
        # Inicializar posición inicial del backgammon
        self.setup_initial_position()
    
    def setup_initial_position(self):
        """Configura la posición inicial estándar del backgammon"""
        # Jugador 1 (X) - índices en la lista (0-based)
        self.points[0] = ['X', 'X']      # Punto 1: 2 fichas
        self.points[11] = ['X'] * 5     # Punto 12: 5 fichas
        self.points[16] = ['X'] * 3     # Punto 17: 3 fichas
        self.points[18] = ['X'] * 5     # Punto 19: 5 fichas
        
        # Jugador 2 (O) - posiciones espejo
        self.points[23] = ['O', 'O']     # Punto 24: 2 fichas
        self.points[12] = ['O'] * 5     # Punto 13: 5 fichas
        self.points[7] = ['O'] * 3      # Punto 8: 3 fichas
        self.points[5] = ['O'] * 5      # Punto 6: 5 fichas **
    
    def display_board(self):
        """Muestra el tablero en consola"""
        print(f"\nJugador 2 (O) - Salida: {self.bear_off[1]}")
        print(" 12  11  10   9   8   7     6   5   4   3   2   1")
        
        # Mostrar la parte superior del tablero (puntos 12-7 y 6-1)
        for row in range(5):  # 5 filas máximo por punto
            line = ""
            
            # Puntos 12 a 7 (índices 11 a 6)
            for point_idx in range(11, 5, -1):
                symbol = self.get_symbol_at_position(point_idx, row)
                line += f"[{symbol}]"
            
            # Separador y bar
            bar_symbol = self.get_bar_symbol(1, row) if row < 2 else " "
            line += f"|{bar_symbol}|"
            
            # Puntos 6 a 1 (índices 5 a 0)
            for point_idx in range(5, -1, -1):
                symbol = self.get_symbol_at_position(point_idx, row)
                line += f"[{symbol}]"
            
            print(line)
        
        # Línea central con BAR
        print("                        BAR")
        
        # Mostrar la parte inferior del tablero (puntos 13-18 y 19-24)
        for row in range(5):
            line = ""
            
            # Puntos 13 a 18 (índices 12 a 17)
            for point_idx in range(12, 18):
                symbol = self.get_symbol_at_position(point_idx, 4-row)
                line += f"[{symbol}]"
            
            # Separador y bar
            bar_symbol = self.get_bar_symbol(0, row) if row < 2 else " "
            line += f"|{bar_symbol}|"
            
            # Puntos 19 a 24 (índices 18 a 23)
            for point_idx in range(18, 24):
                symbol = self.get_symbol_at_position(point_idx, 4-row)
                line += f"[{symbol}]"
            
            print(line)
        
        print(" 13  14  15  16  17  18    19  20  21  22  23  24")
        print(f"Jugador 1 (X) - Salida: {self.bear_off[0]}")
        
        # Mostrar fichas en el bar si las hay
        if self.bar[0] > 0 or self.bar[1] > 0:
            print(f"Fichas en BAR - X: {self.bar[0]}, O: {self.bar[1]}")
    
    def get_symbol_at_position(self, point_idx, row):
        """Obtiene el símbolo a mostrar en una posición específica"""
        point = self.points[point_idx]
        
        if row < len(point):
            return point[row]
        elif len(point) > 5 and row == 0:
            # Si hay más de 5 fichas, mostrar el número en la primera fila
            return str(len(point))
        else:
            return " "
    
    def get_bar_symbol(self, player, row):
        """Obtiene el símbolo del bar para un jugador y fila específica"""
        if row < self.bar[player]:
            return self.player_symbols[player]
        return " "
    
    def move_piece(self, from_point, to_point, player):
        """Mueve una ficha de un punto a otro"""
        # Esta función se implementará más adelante
        pass
    
    def is_valid_move(self, from_point, to_point, player):
        """Verifica si un movimiento es válido"""
        # Esta función se implementará más adelante
        pass

    # Ejemplo de uso
    if __name__ == "__main__":
        board = BackgammonBoard()
        board.display_board()

REFERNCIA DE ARCHIVOS: core/src/board.py

## Claude Sonnet 4.5 - 12/10/2025

### Prompt:
Estoy programando la clase tablero, que es la que se encarga de conocer la posición de las fichas, este es el archivo: **Archivo board.py el 12/10/25**

Resultado de la IA:

Problemas de Diseño Actuales
    # ❌ Usar índices 0-23 pero recibir posiciones 1-24 es confuso
    pos_origen = self.__posiciones__[posicion - 1]

    # ❌ Strings 'B' y 'N' son "magic values"
    if turno == 'B':

    # ❌ Modificar listas directamente es peligroso
    pos_origen.pop(0)
    pos_destino.insert(0, turno)

    # ❌ Lógica duplicada
    if turno == 'B':
        self.__barra__[0] += 1
    else:
        self.__barra__[1] += 1

### Prompt:
Tengo un par de dudas respecto a tus observaciones, qué son magic values? cuál sería la alternativa a modificar las listas directamente? y cuál sería la solución para que no haya lógica duplicada?

Resultado de la IA:

1 Magic Values
Son valores "mágicos" que aparecen en el código sin contexto claro. En tu caso:
    # ❌ ¿Qué significa 'B'? ¿'N'? No es obvio
    if turno == 'B':
        ...

    # ❌ ¿Por qué índice 0 y 1? ¿Cuál es cuál?
    self.__barra__[0] += 1
    self.__barra__[1] += 1

Solución: Usar Enums o constantes
    from enum import Enum

    class Color(Enum):
        BLANCO = "B"
        NEGRO = "N"

    # Ahora es mucho más claro:
    if turno == Color.BLANCO:
        self.__barra__[Color.BLANCO.value] += 1

    # O mejor aún, usar un diccionario:
    self.__barra__ = {Color.BLANCO: 0, Color.NEGRO: 0}
    self.__barra__[turno] += 1  # Mucho más legible

2 Modificar Listas Directamente
El problema es que estás mutando listas que son parte de tu estado interno:
    # ❌ Esto modifica directamente la lista interna
    pos_origen.pop(0)
    pos_destino.insert(0, turno)

Alternativas:
Opción A: Métodos específicos del Board
    def mover_ficha(self, pos_origen_idx: int, pos_destino_idx: int, turno: str):
        """El Board maneja sus propias listas internamente"""
        ficha = self.__posiciones__[pos_origen_idx].pop(0)
        self.__posiciones__[pos_destino_idx].insert(0, ficha)

Opción B: Clase Position/Point
    class Point:
        def __init__(self, index: int):
            self.index = index
            self._checkers = []
        
        def add_checker(self, color: Color):
            self._checkers.insert(0, color)
        
        def remove_checker(self) -> Color:
            return self._checkers.pop(0)
        
        def count(self, color: Color = None) -> int:
            if color is None:
                return len(self._checkers)
            return sum(1 for c in self._checkers if c == color)

    # Uso:
    point_origen.remove_checker()
    point_destino.add_checker(turno)

3 Lógica Duplicada
Tu código tiene este patrón repetido:
    # En varios métodos:
    if turno == 'B':
        self.__barra__[0] += 1
        # o self.__fuera__[0] += 1
    else:
        self.__barra__[1] += 1
        # o self.__fuera__[1] += 1

Soluciones:
Opción 1: Usar diccionarios (la más simple)
    def __init__(self):
        # En lugar de listas con índices
        self.__barra__ = {Color.BLANCO: 0, Color.NEGRO: 0}
        self.__fuera__ = {Color.BLANCO: 0, Color.NEGRO: 0}

    def comer_ficha(self, pos_destino: List[str], turno: Color):
        pos_destino.pop(0)
        # ¡Una sola línea! Sin if/else
        contrario = Color.NEGRO if turno == Color.BLANCO else Color.BLANCO
        self.__barra__[contrario] += 1

Opción 2: Método helper
    def _get_indice_jugador(self, turno: str) -> int:
        """Convierte el turno en índice: B->0, N->1"""
        return 0 if turno == 'B' else 1

    def comer_ficha(self, pos_destino: List[str], turno: str):
        pos_destino.pop(0)
        indice_contrario = 1 - self._get_indice_jugador(turno)
        self.__barra__[indice_contrario] += 1

Opción 3: Enum con método (la más elegante)
    class Color(Enum):
        BLANCO = 0
        NEGRO = 1
        
        def contrario(self) -> 'Color':
            return Color.NEGRO if self == Color.BLANCO else Color.BLANCO

    # Uso:
    self.__barra__[turno.contrario()] += 1  # ¡Súper limpio!

### Prompt:
Antes de encargarme de estos problemas tengo otro primero, y es que en base a lo que tengo quería implementar la función poner_ficha, que serviría para incorporar fichas desde la barra, esto lo entiendo como un caso particular de la función mover, pero aún así no sé cómo implementarla

Resultado de la IA:

    def poner_ficha(self, dado: int, turno: str) -> None:
        """Pone una ficha desde la barra al tablero
        
        En Backgammon, las fichas en la barra deben entrar por el cuadrante del oponente:
        - Blancas entran por posiciones 24, 23, 22... (índices 23, 22, 21...)
        - Negras entran por posiciones 1, 2, 3... (índices 0, 1, 2...)
        
        Parametros
        ----------
        dado: int
            El valor del dado que determina dónde entra la ficha
        turno: str
            Puede ser 'B' o 'N' dependiendo del turno actual
        
        Raises
        ------
        PosicionOcupadaException
            Si la posición de entrada está bloqueada (2+ fichas contrarias)
        ValueError
            Si no hay fichas en la barra para ese jugador
        """
        
        # Verificar que hay fichas en la barra
        indice_jugador = 0 if turno == 'B' else 1
        if self.__barra__[indice_jugador] == 0:
            raise ValueError(f"No hay fichas en la barra para el jugador {turno}")
        
        # Calcular posición de entrada según las reglas de Backgammon
        if turno == 'B':
            # Blancas entran desde la posición 24 hacia atrás
            posicion_destino = 24 - dado  # dado=1 -> pos 23, dado=6 -> pos 18
            pos_destino = self.__posiciones__[posicion_destino]
        else:
            # Negras entran desde la posición 1 hacia adelante
            posicion_destino = dado - 1  # dado=1 -> pos 0, dado=6 -> pos 5
            pos_destino = self.__posiciones__[posicion_destino]
        
        # Validar que la posición no esté bloqueada
        if len(pos_destino) >= 2 and pos_destino[0] != turno:
            raise PosicionOcupadaException("La posición de entrada está bloqueada")
        
        # Si hay una ficha enemiga solitaria, comerla
        if len(pos_destino) == 1 and pos_destino[0] != turno:
            self.comer_ficha(pos_destino, turno)
        
        # Poner la ficha desde la barra
        self.__barra__[indice_jugador] -= 1
        pos_destino.insert(0, turno)

### Prompt:
En base a tú respuesta de cómo implementar la función poner_ficha, veo el problema con el que me encontré yo al querer escribirla, y es que poner_ficha estaría analizando lo mismo que mover, es decir tiene una lógica similar e idéntica en algunos tramos,quizás no exactamente la misma, pero sí que evalúa lo mismo(calcular la posición de entrada, ver que no hayan fichas en la posición destino, si no hay una ficha comerla), entonces eso mismo no sería un caso de lógica duplicada, y por tanto, algo a evitar?

Resultado de la IA:

    def mover(self, posicion: int, dado: int, turno: str) -> None:
        """Mueve una ficha desde una posición del tablero"""
        pos_origen = self.__posiciones__[posicion - 1]
        
        # Validar que hay una ficha del jugador en origen
        if len(pos_origen) == 0 or pos_origen[0] != turno:
            raise PosicionVaciaException("No hay ficha propia en esa posición")
        
        # Calcular destino
        if turno == 'B':
            indice_destino = (posicion - 1) + dado
        else:
            indice_destino = (posicion - 1) - dado
        
        # Ejecutar el movimiento común
        self._ejecutar_movimiento(indice_destino, turno, es_desde_barra=False)
        
        # Quitar ficha del origen
        pos_origen.pop(0)


    def poner_ficha(self, dado: int, turno: str) -> None:
        """Pone una ficha desde la barra al tablero"""
        
        # Verificar que hay fichas en la barra
        indice_jugador = 0 if turno == 'B' else 1
        if self.__barra__[indice_jugador] == 0:
            raise ValueError("No hay fichas en la barra")
        
        # Calcular posición de entrada
        if turno == 'B':
            indice_destino = 24 - dado  # Entran desde el lado negro
        else:
            indice_destino = dado - 1    # Entran desde el lado blanco
        
        # Ejecutar el movimiento común
        self._ejecutar_movimiento(indice_destino, turno, es_desde_barra=True)
        
        # Quitar ficha de la barra
        self.__barra__[indice_jugador] -= 1


    def _ejecutar_movimiento(self, indice_destino: int, turno: str, es_desde_barra: bool) -> None:
        """Lógica común para mover/poner fichas
        
        Parametros
        ----------
        indice_destino: int
            Índice (0-23) de la posición destino
        turno: str
            'B' o 'N'
        es_desde_barra: bool
            Si es True, se está poniendo desde barra. Si es False, es movimiento normal.
        """
        
        # Caso especial: sacar ficha del tablero (bear off)
        if indice_destino >= 24 or indice_destino < 0:
            if not es_desde_barra and self.primer_cuadrante(turno):
                self.sacar_ficha(None, turno)  # Ajustar sacar_ficha para no necesitar pos_origen
                return
            else:
                raise PrimerCuadranteIncompletoException("No puedes sacar fichas aún")
        
        pos_destino = self.__posiciones__[indice_destino]
        
        # Validar destino
        if len(pos_destino) >= 2 and pos_destino[0] != turno:
            raise PosicionOcupadaException("Posición bloqueada por el oponente")
        
        # Comer ficha si hay una sola enemiga
        if len(pos_destino) == 1 and pos_destino[0] != turno:
            self.comer_ficha(pos_destino, turno)
        
        # Añadir ficha al destino
        pos_destino.insert(0, turno)


## ChatGPT GPT-5 - 27/10/2025

### Prompt:
Cómo sería un ejemplo sencillo de la máquina de estados que mencionaste que funcione en mí proyecto?

Resultado de la IA:

La salida está en el código sin modificaciones

class EstadoJuego(Enum):
    """Define los estados posibles del juego para la máquina de estados."""
    TIRANDO_DADOS = auto()
    MOVIENDO = auto()
    FIN_JUEGO = auto()

## Gemini 2.5 Pro - 27/10/2025

### Prompt:
Cómo se testea un print, hay forma de hacerlo sin que se imprima en la consola?

Resultado de la IA:

Funcion de Ejemplo:
    def saludar(nombre):
        print(f"Hola, {nombre}!")

Test
    import unittest
    from unittest.mock import patch
    from io import StringIO
    from core.src.modulo import saludar  # por ejemplo

    class TestSaludar(unittest.TestCase):
        @patch('sys.stdout', new_callable=StringIO)
        def test_saludar(self, mock_stdout):
            saludar("Ennio")
            salida = mock_stdout.getvalue().strip()
            self.assertEqual(salida, "Hola, Ennio!")

    if __name__ == '__main__':
        unittest.main()

## Gemini 2.5 Pro - 31/10/2025

### Prompt:
Necesito para mí interfaz de VistaConsola, una función que limpie la consola de comandos, cómo puedo hacerla?

Resultado de la IA:

El prompt se encuentra en el código sin modificaciones relevantes
class VistaConsola:

    def __init__(self):
        # Detecta el sistema operativo para saber qué comando usar
        self.clear_command = 'cls' if os.name == 'nt' else 'clear'

    def _limpiar_pantalla(self) -> None:
        """Limpia la pantalla de la terminal."""
        os.system(self.clear_command)

## Gemini 2.5 Pro - 31/10/2025

### Prompt:
Cómo puedo implementar una función que dibuje el tablero en la consola? Tenía pensado usar una función que dibuje una posicion a la vez y después otra función que dibuje al tablero completo llamando a la anterior y recibiendo los parametros tablero (el objeto tablero que conoce las posiciones), dados (el objeto dados que conoce los valores) y jugador_actual(el jugador que le toca jugar), si tienes una idea mejor acepto recomendaciones


Resultado de la IA:

El prompt se encuentra en el código sin modificaciones relevantes
    def _format_punto(self, punto: list) -> str:
        """Helper para formatear una sola posición del tablero."""
        if not punto:
            return "..." # Vacío
        
        ficha = punto[0] # 'B' o 'N'
        count = len(punto)
        
        # Formato: "B2 ", "N5 ", "N12" (se corta si > 9)
        return f"{ficha}{count}".ljust(3)

    def dibujar_tablero(self, tablero: Board, dados: Dice, jugador_actual: Optional[Jugador]) -> None:
        """Dibuja el estado completo del juego en arte ASCII."""
        self._limpiar_pantalla()
        
        # --- Puntos 12 al 1 (Fila superior) ---
        print(" 12  11  10   9   8   7   |   6   5   4   3   2   1")
        print("+" + "-" * 27 + "+" + "-" * 27 + "+")
        top_line = " ".join([self._format_punto(tablero.posiciones[i]) for i in range(11, 5, -1)])
        top_line += " | "
        top_line += " ".join([self._format_punto(tablero.posiciones[i]) for i in range(5, -1, -1)])
        print(f"| {top_line} |")
        
        print("|                         |                         |")
        
        # --- Barra y Fichas Fuera ---
        barra_b = f"B: {tablero.barra[0]}"
        barra_n = f"N: {tablero.barra[1]}"
        print(f"| BARRA: {barra_b.ljust(8)} | {barra_n.ljust(8)}         |")
        
        fuera_b = f"B: {tablero.fuera[0]}"
        fuera_n = f"N: {tablero.fuera[1]}"
        print(f"| FUERA: {fuera_b.ljust(8)} | {fuera_n.ljust(8)}         |")
        
        print("|                         |                         |")

        # --- Puntos 13 al 24 (Fila inferior) ---
        bot_line = " ".join([self._format_punto(tablero.posiciones[i]) for i in range(12, 18)])
        bot_line += " | "
        bot_line += " ".join([self._format_punto(tablero.posiciones[i]) for i in range(18, 24)])
        print(f"| {bot_line} |")
        
        print("+" + "-" * 27 + "+" + "-" * 27 + "+")
        print(" 13  14  15  16  17  18  |  19  20  21  22  23  24")
        
        print("=" * 60)

## Gemini 2.5 Pro - 1/11/2025

### Prompt:
En base al código cómo harías la implementación de la interfaz de pygame?
Le pasé todos los archivos de código al día de la fecha

Resultado de la IA:

import pygame
from typing import Optional, List, Tuple, Dict, Any

# --- Importaciones del Controlador (para la Interfaz y Acciones) ---
# (Ajusta la ruta si es necesario, basándome en 'main.py' parece que
# necesitas 'core.controlador...')
from core.controlador.vista_juego import IVistaJuego
from core.controlador.acciones import (
    Accion,
    AccionLanzar,
    AccionMover,
    AccionPoner,
    AccionSalir
)

# --- Importaciones del Modelo (para Type Hinting) ---
from core.src.board import Board
from core.src.jugador import Jugador

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
        self.screen: Optional[pygame.Surface] = None
        self.font: Optional[pygame.font.Font] = None
        self.clock: Optional[pygame.time.Clock] = None

        # --- Estado Interno de la Vista ---
        self.seleccion_origen: Optional[str | int] = None
        self.mensaje_info: Optional[Tuple[str, Tuple[int, int, int], int]] = None

        # --- Geometría Precalculada ---
        # Diccionarios que mapean IDs de elementos a sus Rects de Pygame
        # para facilitar la detección de clics y el dibujado.
        self.rects_puntos: Dict[int, pygame.Rect] = {}
        self.rects_dados: List[pygame.Rect] = []
        self.rect_barra_b: Optional[pygame.Rect] = None
        self.rect_barra_n: Optional[pygame.Rect] = None
        self.rect_fuera_b: Optional[pygame.Rect] = None
        self.rect_fuera_n: Optional[pygame.Rect] = None
        self.puntos_triangulos: List[Tuple] = []

    # --- 1. Métodos de la Interfaz (IVistaJuego) ---

    def inicializar(self) -> None:
        """Inicializa Pygame, la ventana y calcula la geometría."""
        pygame.init()
        pygame.font.init()
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Backgammon")
        self.font = pygame.font.SysFont(None, 30)
        self.clock = pygame.time.Clock()

        self._calcular_geometria()
        print("Vista de Pygame inicializada.")

    def dibujar_tablero(self, tablero: Board, dados: List[int], jugador_actual: Optional[Jugador]) -> None:
        """Dibuja el estado completo del juego en la ventana."""
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
        for i, puntos in enumerate(self.puntos_triangulos):
            color = COLOR_TRIANGULO_1 if i % 2 == 0 else COLOR_TRIANGULO_2
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

    def obtener_entrada(self) -> Optional[Accion]:
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
                        dado_valor = valor_clic
                        origen = self.seleccion_origen
                        self.seleccion_origen = None # Resetear selección
                        
                        if isinstance(origen, int):
                            # Es un movimiento desde el tablero
                            posicion_1_24 = origen + 1
                            return AccionMover(origen=posicion_1_24, dado=dado_valor)
                        
                        elif origen.startswith('barra'):
                            # Es una puesta desde la barra
                            return AccionPoner(dado=dado_valor)
                    
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
        
        # Puntos (Triángulos)
        for i in range(12):
            # Fila superior (12 a 1)
            base_x = MARGEN_LATERAL + (ANCHO_PUNTO * (11-i))
            if i >= 6:
                base_x -= ANCHO_BARRA # Offset por la barra
            
            rect_sup = pygame.Rect(base_x, MARGEN_VERTICAL, ANCHO_PUNTO, ALTO_PUNTO)
            puntos_sup = [
                (rect_sup.left, rect_sup.top),
                (rect_sup.right, rect_sup.top),
                (rect_sup.centerx, rect_sup.bottom)
            ]
            self.rects_puntos[11 - i] = rect_sup
            self.puntos_triangulos.append(tuple(puntos_sup))

            # Fila inferior (13 a 24)
            base_x = MARGEN_LATERAL + (ANCHO_PUNTO * i)
            if i >= 6:
                base_x += ANCHO_BARRA # Offset por la barra

            rect_inf = pygame.Rect(base_x, SCREEN_HEIGHT - MARGEN_VERTICAL - ALTO_PUNTO, ANCHO_PUNTO, ALTO_PUNTO)
            puntos_inf = [
                (rect_inf.left, rect_inf.bottom),
                (rect_inf.right, rect_inf.bottom),
                (rect_inf.centerx, rect_inf.top)
            ]
            self.rects_puntos[12 + i] = rect_inf
            self.puntos_triangulos.append(tuple(puntos_inf))

        # Barra
        self.rect_barra_n = pygame.Rect(SCREEN_WIDTH // 2 - ANCHO_BARRA // 2, MARGEN_VERTICAL, ANCHO_BARRA, SCREEN_HEIGHT // 2 - MARGEN_VERTICAL)
        self.rect_barra_b = pygame.Rect(SCREEN_WIDTH // 2 - ANCHO_BARRA // 2, SCREEN_HEIGHT // 2, ANCHO_BARRA, SCREEN_HEIGHT // 2 - MARGEN_VERTICAL)

        # Fichas Fuera (a la derecha de la barra)
        self.rect_fuera_n = pygame.Rect(SCREEN_WIDTH - MARGEN_LATERAL + 5, MARGEN_VERTICAL, MARGEN_LATERAL - 10, SCREEN_HEIGHT // 2 - MARGEN_VERTICAL)
        self.rect_fuera_b = pygame.Rect(SCREEN_WIDTH - MARGEN_LATERAL + 5, SCREEN_HEIGHT // 2, MARGEN_LATERAL - 10, SCREEN_HEIGHT // 2 - MARGEN_VERTICAL)

    def _coords_a_elemento(self, pos: Tuple[int, int]) -> Optional[Tuple[str, Any]]:
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

    def _id_a_coords_ficha(self, id_elemento: str | int, num_ficha: int) -> Tuple[int, int]:
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

    def _dibujar_fichas_tablero(self, posiciones: List[List[str]]):
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

    def _dibujar_fichas_barra(self, barra: List[int]):
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

    def _dibujar_fichas_fuera(self, fuera: List[int]):
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

    def _dibujar_dados(self, dados: List[int]):
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

    def _dibujar_turno(self, jugador_actual: Optional[Jugador]):
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