from core.src.board import Board
from core.src.dados import Dice
from core.src.jugador import Jugador
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import List # Para el type hinting
import random # Para la tirada inicial
from core.src.exceptions import (
    PosicionOcupadaException,
    PrimerCuadranteIncompletoException,
    PosicionVaciaException,
    MovimientoNoPosibleException,
    TiradaInicialEmpateException,
    NoEsMomentoException,
    FichaContrariaException
)

class EstadoJuego(Enum):
    """Define los estados posibles del juego para la máquina de estados."""
    TIRANDO_DADOS = auto()
    MOVIENDO = auto()
    FIN_JUEGO = auto()

class BackgammonGame:
    """
    Clase principal que maneja la lógica del juego de Backgammon

    Atributos
    ---------
    __tablero__ : Board
        El tablero del juego
    __dados__ : Dados
        Los dados del juego
    __jugador1__ : Jugador
        El jugador 1 del juego
    __jugador2__ : Jugador
        El jugador 2 del juego
    __jugador_actual__ : Jugador
        Jugador que está jugando
    __ganador__ : Jugador
        Jugador ganador del juego cuando lo haya (default=None)
    __estado_juego__ : EstadoJuego
        Estado del juego (Tirando, Moviendo o Terminado)
    __primer_turno__ : bool
        Flag que funciona para identificar la tirada inicial
    """
    def __init__(self, jugador1: str = 'Jugador 1', jugador2: str = 'Jugador 2'):
        self.__tablero__ = Board()
        self.__dados__ = Dice()

        self.__jugador1__ = Jugador(jugador1, 'B')
        self.__jugador2__ = Jugador(jugador2, 'N')
        self.__jugador_actual__ = None
        self.__ganador__ = None
        self.__estado_juego__ = EstadoJuego.TIRANDO_DADOS
        self.__primer_turno__ = True


    @property
    def turno_actual(self) -> Jugador:
        """Devuelve el jugador que le toca jugar"""
        return self.__jugador_actual__

    @property
    def estado_actual(self) -> EstadoJuego:
        """Devuelve el estado actual del juego"""
        return self.__estado_juego__

    @property
    def dados(self) -> List[int]:
        """Devuelve los valores actuales de los dados"""
        return self.__dados__.valores

    @property
    def tablero(self) -> Board:
        """Devuelve le tablero"""
        return self.__tablero__

    @property
    def ganador(self) -> Jugador:
        """Devuelve el ganador si es que lo hay"""
        return self.__ganador__

    @property
    def jugador1(self) -> Jugador:
        """Devuelve el jugador 1"""
        return self.__jugador1__

    @property
    def jugador2(self) -> Jugador:
        """Devuelve el jugador 2"""
        return self.__jugador2__

    def lanzar_dados(self) -> None:
        """Tira los dados, si es el primer turno, decide quien empieza, si no, es una tirada normal.

        Raises
        ------
        NoEsMomentoException
            El estado del juego no es tirar los dados
        TiradaInicialEmpateException
            Se dio un empate en la tirada inicial
        """

        if self.estado_actual != EstadoJuego.TIRANDO_DADOS:
            raise NoEsMomentoException('No es el momento de tirar los dados')

        if self.__primer_turno__ == True:
            dado_j1 = random.randint(1, 6)
            dado_j2 = random.randint(1, 6)

            if dado_j1 == dado_j2:
                raise TiradaInicialEmpateException('Empate, hay que tirar de nuevo')
            elif dado_j1 > dado_j2:
                self.__jugador_actual__ = self.jugador1
            else:
                self.__jugador_actual__ = self.jugador2

            self.__dados__.set_valores([dado_j1, dado_j2])
            self.__primer_turno__ = False
            self.__estado_juego__ = EstadoJuego.MOVIENDO

            return {
                'dado_j1': dado_j1,
                'dado_j2': dado_j2,
                'ganador': self.turno_actual.nombre
            }
        else:
            self.__dados__.tirar()
            self.__estado_juego__ = EstadoJuego.MOVIENDO
            return {
                'dados': self.dados
            }

    def intentar_mover_ficha(self, posicion: int, dado_usado: int) -> None:
        """Intenta mover una ficha desde una posición del tablero a otra, o a fuera del tablero

        Parametros
        ----------
        posicion : int
            La posición de origen de la ficha que se intenta mover (1-24)
        dado_usado : int
            El valor del dado que se desea usar

        Raises
        ------
        NoEsMomentoException
            Si el estado del juego no es moviendo
        ValueError
            Si el valor de la posicion no es válido (entre 1 y 24)
            Si el dado no está disponible
        Exception
            Si tienes fichas en la barra
        FichaContrariaException
            Si intentas mover una ficha del rival
        """

        if not (1 <= posicion <= 24):
            raise ValueError('La posición de origen debe estar entre 1 y 24')

        if self.estado_actual != EstadoJuego.MOVIENDO:
            raise NoEsMomentoException('No es el momento de mover fichas')

        if dado_usado not in self.dados:
            raise ValueError(f'El dado {dado_usado} no está disponible')

        turno_color = self.turno_actual.color
        if not self.tablero.barra_vacia(turno_color):
            raise Exception('Tienes fichas en la barra')

        try:
            if not self.tablero.get_ficha(posicion, turno_color):
                raise FichaContrariaException('Esa ficha no es tuya')

            self.tablero.mover(posicion, dado_usado, turno_color)
            self.__dados__.usar(dado_usado)
            self.comprobar_estado_post_movimiento()

        except (
            PosicionVaciaException,
            PosicionOcupadaException,
            PrimerCuadranteIncompletoException
        ):
            raise

    def cambiar_turno(self) -> None:
        """Pasa el turno al siguiente jugador y resetea los dados"""
        if self.turno_actual == self.jugador1:
            self.__jugador_actual__ = self.jugador2
        else:
            self.__jugador_actual__ = self.jugador1

        self.__estado_juego__ = EstadoJuego.TIRANDO_DADOS
        self.__dados__.resetear()
        print(f'Turno de {self.turno_actual.nombre}')

    def saltar_turno(self) -> None:
        """Permite al jugador saltar el turno si no le quedan movimientos válidos (Usado por el controlador)

        Raises
        ------
        NoEsMomentoException
            El estado del juego no es moviendo
        """
        if self.estado_actual != EstadoJuego.MOVIENDO:
            raise NoEsMomentoException('No puedes saltar turno si no estás moviendo fichas')
        print(f'{self.turno_actual.nombre} salta el turno')
        self.cambiar_turno()

    def comprobar_estado_post_movimiento(self) -> None:
        """Se llama después de cada movimiento para ver si el juego ha terminado o si se han agotado los dados"""
        turno_color = self.turno_actual.color

        if self.tablero.condicion_victoria(turno_color):
            self.__estado_juego__ = EstadoJuego.FIN_JUEGO
            self.__ganador__ = self.turno_actual
            return

        if not self.__dados__.dados_disponibles():
            self.cambiar_turno()





