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
    NoEsMomentoException
)

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

    def lanzar_dados(self) -> None:
        """Tira los dados, si es el primer turno, decide quien empieza, si no, es una tirada normal.
        
        Raises
        ------
        NoEsMomentoException
            El estado del juego no es tirar los dados
        TiradaInicialEmpateException
            Se dio un empate en la tirada inicial
        """

        if self.__estado_juego__ != EstadoJuego.TIRANDO_DADOS:
            raise NoEsMomentoException('No es el momento de tirar los dados')

        if self.__primer_turno__ == True:
            dado_j1 = random.randint(1, 6)
            dado_j2 = random.randint(1, 6)

            if dado_j1 == dado_j2:
                raise TiradaInicialEmpateException('Empate, hay que tirar de nuevo')
            elif dado_j1 > dado_j2:
                self.__turno__ = self.__jugador1__
            else:
                self.__turno__ = self.__jugador2__

            self.__dados__.set_valores([dado_j1, dado_j2])
            self.__primer_turno__ = False
            self.__estado_juego__ = EstadoJuego.MOVIENDO

            return {
                'dado_j1': dado_j1,
                'dado_j2': dado_j2,
                'ganador': self.__turno__.__nombre__
            }
        else:
            self.__dados__.tirar()
            self.__estado_juego__ = EstadoJuego.MOVIENDO
            return {
                'dados': self.__dados__.valores
            }

            

    

