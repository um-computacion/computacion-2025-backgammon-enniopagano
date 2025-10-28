import unittest
from unittest.mock import patch
from core.src.backgammon import BackgammonGame, EstadoJuego
from core.src.board import Board
from core.src.dados import Dice
from core.src.jugador import Jugador
from io import StringIO
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
        self.assertEqual(self.juego.__jugador_actual__, None)
        self.assertEqual(self.juego.__ganador__, None)
        self.assertEqual(isinstance(self.juego.__estado_juego__, EstadoJuego), True)
        self.assertEqual(self.juego.__estado_juego__, EstadoJuego.TIRANDO_DADOS)
        self.assertEqual(self.juego.__primer_turno__, True)

    def test_getter_turno(self):
        self.juego.__jugador_actual__ = 'B'
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
        """Testea la tirada inicial con dados iguales"""
        with self.assertRaises(TiradaInicialEmpateException):
            self.juego.lanzar_dados()

    @patch('random.randint', side_effect=[5, 4])
    def test_lanzar_dados_tirada_inicial_jugador1_gana(self, tirada_patched):
        """Testea la tirada inicial donde el jugador 1 gana"""
        # Testea lo que retorna al controlador
        self.assertEqual(self.juego.lanzar_dados(), {'dado_j1': 5, 'dado_j2': 4, 'ganador': self.juego.__jugador_actual__.__nombre__})
        # Testea como quedaron los valores afectados
        self.assertEqual(self.juego.__jugador_actual__, self.juego.__jugador1__)
        self.assertEqual(self.juego.__dados__.__valores__, [5, 4])
        self.assertEqual(self.juego.__primer_turno__, False)
        self.assertEqual(self.juego.__estado_juego__, EstadoJuego.MOVIENDO)
        
    @patch('random.randint', side_effect=[1, 4])
    def test_lanzar_dados_tirada_inicial_jugador2_gana(self, tirada_patched):
        """Testea la tirada inicial donde el jugador 2 gana"""
        # Testea lo que retorna al controlador
        self.assertEqual(self.juego.lanzar_dados(), {'dado_j1': 1, 'dado_j2': 4, 'ganador': self.juego.__jugador_actual__.__nombre__})
        # Testea como quedaron los valores afectados
        self.assertEqual(self.juego.__jugador_actual__, self.juego.__jugador2__)
        self.assertEqual(self.juego.__dados__.__valores__, [1, 4])
        self.assertEqual(self.juego.__primer_turno__, False)
        self.assertEqual(self.juego.__estado_juego__, EstadoJuego.MOVIENDO)

    @patch('random.randint', side_effect=[1, 4])
    def test_lanzar_dados_normal(self, tirada_patched):
        """Testea una tirada normal"""
        self.juego.__primer_turno__ = False
        # Testea lo que retorna al controlador
        self.assertEqual(self.juego.lanzar_dados(), {'dados': self.juego.__dados__.__valores__})
        # Testea como quedó el estado
        self.assertEqual(self.juego.__estado_juego__, EstadoJuego.MOVIENDO)

    @patch('sys.stdout', new_callable=StringIO)
    def test_cambiar_turno_de_1_a_2(self, mock_stdout):
        """Testea que se intercambie el turno correctamente, en este caso de jugador 1 a 2"""
        # Define los valores para verificar sus cambios
        self.juego.__jugador_actual__ = self.juego.__jugador1__
        self.juego.__estado_juego__ = EstadoJuego.MOVIENDO
        self.juego.__dados__.__valores__ = [2, 3] # Definir valores para verificar que se borren
        # Cambia de turno
        self.juego.cambiar_turno()
        salida = mock_stdout.getvalue().strip()
        self.assertEqual(self.juego.__jugador_actual__, self.juego.__jugador2__)
        self.assertEqual(self.juego.__estado_juego__, EstadoJuego.TIRANDO_DADOS)
        self.assertEqual(self.juego.__dados__.__valores__, [])
        # Testea el print
        self.assertEqual(salida, f'Turno de {self.juego.__jugador_actual__.__nombre__}')
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_cambiar_turno_de_2_a_1(self, mock_stdout):
        """Testea que se intercambie el turno correctamente, en este caso de jugador 2 a 1"""
        # Define los valores para verificar sus cambios
        self.juego.__jugador_actual__ = self.juego.__jugador2__
        self.juego.__estado_juego__ = EstadoJuego.MOVIENDO
        self.juego.__dados__.__valores__ = [2, 3] # Definir valores para verificar que se borren
        # Cambia de turno
        self.juego.cambiar_turno()
        salida = mock_stdout.getvalue().strip()
        self.assertEqual(self.juego.__jugador_actual__, self.juego.__jugador1__)
        self.assertEqual(self.juego.__estado_juego__, EstadoJuego.TIRANDO_DADOS)
        self.assertEqual(self.juego.__dados__.__valores__, [])
        # Testea el print
        self.assertEqual(salida, f'Turno de {self.juego.__jugador_actual__.__nombre__}')

    def test_saltar_turno_error(self):
        """Testea que se levante el error a no estar en estado de movimiento"""
        with self.assertRaises(NoEsMomentoException):
            self.juego.saltar_turno()

    @patch('sys.stdout', new_callable=StringIO)
    def test_saltar_turno_jugador1(self, mock_stdout):
        """Testea que el jugador 1 se salte el turno"""
        self.juego.__estado_juego__ = EstadoJuego.MOVIENDO
        self.juego.__jugador_actual__ = self.juego.__jugador1__
        self.juego.saltar_turno()
        salida = mock_stdout.getvalue().strip()
        self.assertEqual(self.juego.__jugador_actual__, self.juego.__jugador2__)
        self.assertEqual(salida, f'{self.juego.__jugador1__.__nombre__} salta el turno\nTurno de {self.juego.__jugador2__.__nombre__}')

    @patch('sys.stdout', new_callable=StringIO)
    def test_saltar_turno_jugador2(self, mock_stdout):
        """Testea que el jugador 2 se salte el turno"""
        self.juego.__estado_juego__ = EstadoJuego.MOVIENDO
        self.juego.__jugador_actual__ = self.juego.__jugador2__
        self.juego.saltar_turno()
        salida = mock_stdout.getvalue().strip()
        self.assertEqual(self.juego.__jugador_actual__, self.juego.__jugador1__)
        self.assertEqual(salida, f'{self.juego.__jugador2__.__nombre__} salta el turno\nTurno de {self.juego.__jugador1__.__nombre__}')

    @patch('core.src.board.Board.condicion_victoria', return_value=True)
    def test_comprobar_estado_post_movimiento_ganador(self, victoria_patched):
        """Testea que se encuentre un ganador después de un movimiento"""
        self.juego.__jugador_actual__ = self.juego.__jugador1__
        self.juego.comprobar_estado_post_movimiento()
        self.assertEqual(self.juego.__estado_juego__, EstadoJuego.FIN_JUEGO)
        self.assertEqual(self.juego.__ganador__, self.juego.__jugador_actual__)

    @patch('core.src.board.Board.condicion_victoria', return_value=False)
    @patch('sys.stdout', new_callable=StringIO)
    def test_comprobar_estado_post_movimiento_cambio_turno(self, mock_stdout, victoria_patched):
        """Testea que no haya ganador y se cambie de turno al no haber mas dados"""
        self.juego.__jugador_actual__ = self.juego.__jugador1__
        self.juego.__dados__.__valores__ = []
        self.juego.comprobar_estado_post_movimiento()
        salida = mock_stdout.getvalue().strip()
        self.assertEqual(self.juego.__jugador_actual__, self.juego.__jugador2__)
        self.assertEqual(salida, f'Turno de {self.juego.__jugador_actual__.__nombre__}')

