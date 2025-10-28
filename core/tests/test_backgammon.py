import unittest
from unittest.mock import patch
from core.src.backgammon import BackgammonGame, EstadoJuego
from core.src.board import Board
from core.src.dados import Dice
from core.src.jugador import Jugador
from core.src.exceptions import (
    PosicionOcupadaException, 
    PrimerCuadranteIncompletoException, 
    PosicionVaciaException,
    MovimientoNoPosibleException,
    TiradaInicialEmpateException,
    NoEsMomentoException
)

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

    def test_lanzar_dados_momento_incorrecto(self):
        self.juego.__estado_juego__ = EstadoJuego.MOVIENDO
        with self.assertRaises(NoEsMomentoException):
            self.juego.lanzar_dados()

    @patch('random.randint', side_effect=[4, 4])
    def test_lanzar_dados_tirada_inicial_iguales(self, tirada_patched):
        with self.assertRaises(TiradaInicialEmpateException):
            self.juego.lanzar_dados()

    @patch('random.randint', side_effect=[5, 4])
    def test_lanzar_dados_tirada_inicial_jugador1_gana(self, tirada_patched):
        # Testea lo que retorna al controlador
        self.assertEqual(self.juego.lanzar_dados(), {'dado_j1': 5, 'dado_j2': 4, 'ganador': self.juego.__turno__.__nombre__})
        # Testea como quedaron los valores afectados
        self.assertEqual(self.juego.__turno__, self.juego.__jugador1__)
        self.assertEqual(self.juego.__dados__.__valores__, [5, 4])
        self.assertEqual(self.juego.__primer_turno__, False)
        self.assertEqual(self.juego.__estado_juego__, EstadoJuego.MOVIENDO)
        
    @patch('random.randint', side_effect=[1, 4])
    def test_lanzar_dados_tirada_inicial_jugador2_gana(self, tirada_patched):
        # Testea lo que retorna al controlador
        self.assertEqual(self.juego.lanzar_dados(), {'dado_j1': 1, 'dado_j2': 4, 'ganador': self.juego.__turno__.__nombre__})
        # Testea como quedaron los valores afectados
        self.assertEqual(self.juego.__turno__, self.juego.__jugador2__)
        self.assertEqual(self.juego.__dados__.__valores__, [1, 4])
        self.assertEqual(self.juego.__primer_turno__, False)
        self.assertEqual(self.juego.__estado_juego__, EstadoJuego.MOVIENDO)

    @patch('random.randint', side_effect=[1, 4])
    def test_lanzar_dados_normal(self, tirada_patched):
        self.juego.__primer_turno__ = False
        # Testea lo que retorna al controlador
        self.assertEqual(self.juego.lanzar_dados(), {'dados': self.juego.__dados__.__valores__})
        # Testea como quedó el estado
        self.assertEqual(self.juego.__estado_juego__, EstadoJuego.MOVIENDO)
