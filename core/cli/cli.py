import os # Para limpiar la consola

from core.controlador.vista_juego import IVistaJuego
from core.controlador.acciones import (
    Accion,
    AccionLanzar,
    AccionMover,
    AccionPoner,
    AccionSalir
)

class VistaConsola(IVistaJuego):
    """Implementación de la interfaz de vista para jugar en la terminal"""

    def __init__(self):
        # Detecta el sistema operativo para saber qué comando usar
        self.comando_limpiar = 'cls' if os.name == 'nt' else 'clear'
    
    def limpiar_pantalla(self) -> None:
        # Limpia la pantalla de la terminal
        os.system(self.comando_limpiar)
    
    def obtener_posicion(self, posicion: list) -> str:
        """Obtiene la informacion de una posición del tablero"""
        if len(posicion) == 0:
            return '...'

        ficha = posicion[0]
        cuenta = len(posicion)

        return f'{ficha}{cuenta}'.ljust(3) # Retorna en el formato 'B3', 'N11', 'B9'

    def inicializar(self) -> None:
        """Método de la interfaz abstracta que inicializa la vista"""
        self.limpiar_pantalla()
        print('Bienvenido a Backgammon')
        print('-' * 60)
        print('\n')

    def dibujar_tablero(self, tablero, dados, turno) -> None:
        """Dibuja el tablero completo del juego"""
        self.limpiar_pantalla()

        # Fila superior
        print(" 12  11  10   9   8   7   |   6   5   4   3   2   1")
        print("+" + "-" * 27 + "+" + "-" * 27 + "+")
        top_line = " ".join([self.obtener_posicion(tablero.posiciones[i]) for i in range(11, 5, -1)])
        top_line += " | "
        top_line += " ".join([self.obtener_posicion(tablero.posiciones[i]) for i in range(5, -1, -1)])
        print(f"| {top_line} |")
        
        print("|                         |                         |")
        
        # Barra y Fichas Fuera
        barra_b = f"B: {tablero.barra[0]}"
        barra_n = f"N: {tablero.barra[1]}"
        print(f"| BARRA: {barra_b.ljust(8)} | {barra_n.ljust(8)}         |")
        
        fuera_b = f"B: {tablero.fuera[0]}"
        fuera_n = f"N: {tablero.fuera[1]}"
        print(f"| FUERA: {fuera_b.ljust(8)} | {fuera_n.ljust(8)}         |")
        
        print("|                         |                         |")

        # Fila inferior
        bot_line = " ".join([self.obtener_posicion(tablero.posiciones[i]) for i in range(12, 18)])
        bot_line += " | "
        bot_line += " ".join([self.obtener_posicion(tablero.posiciones[i]) for i in range(18, 24)])
        print(f"| {bot_line} |")
        
        print("+" + "-" * 27 + "+" + "-" * 27 + "+")
        print(" 13  14  15  16  17  18  |  19  20  21  22  23  24")
        
        print("=" * 60)

        # Información del juego
        if turno:
            print(f'Turno de: {turno.nombre}')
        else:
            print('Tirada inicial para definir quién empieza')

        print(f'Dados disponibles: {dados}')
        print('-' * 60)

    def obtener_entrada(self):
        """Espera la entrada del jugador y la interpreta para devolver la acción correspondiente"""
        try:
            # Pide el comando al jugador
            print('Comandos:\nlanzar | mover <origen> <dado> | poner <dado> | salir')
            entrada = input('Tu comando: ').strip().lower()
            partes = entrada.split()

            if not partes:
                return None
            
            comando = partes[0]

            if comando == 'lanzar':
                return AccionLanzar()
            
            elif comando == 'mover':
                if len(partes) != 3:
                    self.mostrar_error('Formato: mover <posicion_origen> <dado_a_usar>')
                    return None
                origen = int(partes[1])
                dado = int(partes[2])
                return AccionMover(origen, dado)
            
            elif comando == 'poner':
                if len(partes) != 2:
                    self.mostrar_error('Formato: poner <dado_a_usar>')
                    return None
                dado = int(partes[1])
                return AccionPoner(dado)
            
            elif comando == 'salir':
                return AccionSalir()
            
            else:
                self.mostrar_error(f'Comando desconocido {comando}')
        
        except ValueError:
            # En caso de que se pasen mal los números
            self.mostrar_error('Error: Asegurate usar números enteros para las posiciones y dados')
            return None

    def mostrar_mensaje(self, mensaje: str) -> None:
        """Muestra un mensaje informativo al jugador"""
        print(f'INFO: {mensaje}')
    
    def mostrar_error(self, error: str) -> None:
        """Muestra un mensaje de error al jugador"""
        print(f'ERROR: {error}')
        input("\n...Presiona Enter para continuar...")

    def cerrar(self) -> None:
        """Limpia la consola y muestra un mensaje al salir"""
        self.limpiar_pantalla()
        print('\nGracias por jugar Backgammon. Nos vemos')

