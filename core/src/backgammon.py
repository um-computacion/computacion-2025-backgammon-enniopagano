from core.src.board import Board
from core.src.dados import Dice
from core.src.jugador import Jugador
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import List # Para el type hinting

class EstadoJuego(Enum):
    """Define los estados posibles del juego para la máquina de estados."""
    TIRANDO_DADOS = auto()
    MOVIENDO = auto()
    FIN_JUEGO = auto()

class BackgammonGame:
    """Clase principal que maneja la lógica del juego de Backgammon

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
    __turno__ : str
        Turno del jugador actual 'B' o 'N'
    __juego_terminado__ : bool
        Si el juego terminó o no
    """
    def __init__(self, jugador1: str = 'Jugador 1', jugador2: str = 'Jugador 2'):
        self.__tablero__ = Board()
        self.__dados__ = Dice()

        self.__jugador1__ = Jugador(jugador1, 'B')
        self.__jugador2__ = Jugador(jugador2, 'N')
        self.__turno__ = None
        self.__ganador__ = None
        self.__estado_juego__ = EstadoJuego.TIRANDO_DADOS
        self.__primer_turno__ = True


    @property
    def turno_actual(self) -> Jugador:
        """Devuelve el jugador que le toca jugar"""
        return self.__turno__

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

    

