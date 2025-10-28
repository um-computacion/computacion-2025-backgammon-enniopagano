import unittest
from unittest.mock import patch
from core.src.backgammon import BackgammonGame, EstadoJuego
from core.src.board import Board
from core.src.dados import Dice
from core.src.jugador import Jugador

class TestBackgammon(unittest.TestCase):

    def setUp(self):
        self.juego = BackgammonGame()

    def test_setup(self):
        """Teste que los atributos se inicien correctamente"""
        self.assertEqual(isinstance(self.juego.__tablero__, Board), True)
        self.assertEqual(isinstance(self.juego.__dados__, Dice), True)
        self.assertEqual(isinstance(self.juego.__jugador1__, Jugador), True)
        self.assertEqual(isinstance(self.juego.__jugador2__, Jugador), True)
        self.assertEqual(self.juego.__turno__, None)
        self.assertEqual(self.juego.__ganador__, None)
        self.assertEqual(isinstance(self.juego.__estado_juego__, EstadoJuego), True)
        self.assertEqual(self.juego.__estado_juego__, EstadoJuego.TIRANDO_DADOS)
        self.assertEqual(self.juego.__primer_turno__, True)

    def test_getter_turno(self):
        self.juego.__turno__ = 'B'
        self.assertEqual(self.juego.turno_actual, 'B')

    def test_getter_estado_actual(self):
        self.assertEqual(self.juego.estado_actual, EstadoJuego.TIRANDO_DADOS)

    def test_getter_dados(self):
        self.juego.__dados__.__valores__ = [2, 4]
        self.assertEqual(self.juego.dados, [2, 4])

    def test_getter_tablero(self):
        self.assertEqual(isinstance(self.juego.tablero, Board), True)
        self.assertEqual(self.juego.tablero, self.juego.__tablero__)

    def test_getter_ganador(self):
        self.assertEqual(self.juego.ganador, self.juego.__ganador__)