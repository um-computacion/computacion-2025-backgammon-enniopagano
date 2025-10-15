from core.src.board import Board
from abc import ABC, abstractmethod

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
    def __init__(self):
        self.__tablero__ = Board()
        self.__dados__ = Dados()
        self.__jugador1__ = ''
        self.__jugador2__ = ''
        self.__turno__ = ''
        self.__juego_terminado__ = False



