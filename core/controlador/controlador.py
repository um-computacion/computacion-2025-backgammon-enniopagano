from core.src.backgammon import BackgammonGame, EstadoJuego
from .vista_juego import IVistaJuego
from core.src.exceptions import (
    PosicionOcupadaException,
    PrimerCuadranteIncompletoException,
    PosicionVaciaException,
    MovimientoNoPosibleException,
    TiradaInicialEmpateException,
    NoEsMomentoException,
    FichaContrariaException
)
from .acciones import (
    Accion,
    AccionLanzar,
    AccionMover,
    AccionPoner,
    AccionSalir
)


class ControladorJuego:
    """
    Conecta la Vista con el Juego
    """
    def __init__(self, juego: BackgammonGame, vista: IVistaJuego):
        self.__juego__ = juego
        self.__vista__ = vista

    def run(self):
        """Inicia y mantiene el bucle principal del juego"""

        running = True
        self.__vista__.inicializar()

        while running:
            # Dibuja el tablero
            self.__vista__.dibujar_tablero(
                self.__juego__.tablero,
                self.__juego__.dados_valores,
                self.__juego__.turno_actual
            )
            # Comprueba si hay un ganador
            if self.__juego__.estado_actual == EstadoJuego.FIN_JUEGO:
                self.__vista__.mostrar_mensaje(f'{self.__juego__.ganador.nombre}')
                running = False

            # Obtiene la entrada del jugador
            accion = self.__vista__.obtener_entrada()

            if accion == None:
                pass
            
            # Interpreta la accion recibida
            try:
                if isinstance(accion, AccionSalir):
                    running = False
                elif isinstance(accion, AccionLanzar):
                    # Tira los dados
                    resultado = self.__juego__.lanzar_dados()
                    if 'ganador' in resultado:
                        dado_j1 = resultado['dado_j1']
                        dado_j2 = resultado['dado_j2']
                        ganador = resultado['ganador']
                        mensaje = (
                            f'Tirada inicial: '
                            f'{self.__juego__.jugador1.nombre}:{dado_j1} - '
                            f'{self.__juego__.jugador2.nombre}:{dado_j2}'
                        )
                        self.__vista__.mostrar_mensaje(mensaje)
                        self.__vista__.mostrar_mensaje(f'Empieza {ganador}')
                    
                    
                    self.__vista__.mostrar_mensaje(f'Dados: {resultado['dados']}')

                    if resultado['turno_saltado']:
                        self.__vista__.mostrar_error('No hay movimientos disponibles, turno saltado')
                
                elif isinstance(accion, AccionMover):
                    self.__juego__.intentar_mover_ficha(accion.origen, accion.dado)

                elif isinstance(accion, AccionPoner):
                    self.__juego__.intentar_poner_ficha(accion.dado)
            
            # Este error es particular porque no es un fallo como tal, es más una instrucción de repetir
            except TiradaInicialEmpateException as e:
                self.__vista__.mostrar_error(e)

            except (PosicionOcupadaException, PrimerCuadranteIncompletoException,
                    PosicionVaciaException, ValueError, Exception) as e:
                self.__vista__.mostrar_error(e)

        self.__vista__.cerrar()

