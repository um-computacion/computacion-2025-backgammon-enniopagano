import unittest
from unittest.mock import patch
from core.cli.cli import VistaConsola
from core.controlador.acciones import (
    Accion,
    AccionLanzar,
    AccionMover,
    AccionPoner,
    AccionSalir
)

class TestVistaConsola(unittest.TestCase):
    """Testea sólo la lógica de la interfaz"""

    def setUp(self):
        self.vista = VistaConsola()

    def test_obtener_posicion_vacia(self):
        """Testea cuando mide una posición vacía"""
        self.assertEqual(self.vista.obtener_posicion([]), '...')

    def test_obtener_posicion_una_ficha(self):
        """Teste cuando mide una posición con una ficha"""
        self.assertEqual(self.vista.obtener_posicion(['B']), 'B1 ')

    def test_obtener_posicion_varias_fichas(self):
        """Teste cuando mide una posición con más de una ficha"""
        self.assertEqual(self.vista.obtener_posicion(['N', 'N', 'N', 'N']), 'N4 ')

    def test_obtener_posicion_mas_de_diez(self):
        """Teste cuando mide una posición con más de diez fichas"""
        self.assertEqual(self.vista.obtener_posicion(['B'] * 11), 'B11')

    @patch('builtins.print')
    @patch('builtins.input', return_value='lanzar')
    def test_obtener_entrada_lanzar(self, input_patched, print_patched):
        """Testea que 'lanzar' devuelva una AccionLanzar"""
        accion = self.vista.obtener_entrada()
        self.assertIsInstance(accion, AccionLanzar)

    @patch('builtins.print')
    @patch('builtins.input', return_value='mover 3 4')
    def test_obtener_entrada_mover(self, input_patched, print_patched):
        """Testea que 'move 3 4' devuelva una AccionMover(3, 4)"""
        accion = self.vista.obtener_entrada()
        self.assertIsInstance(accion, AccionMover)
        self.assertEqual(accion.origen, 3)
        self.assertEqual(accion.dado, 4)

    @patch('builtins.print')
    @patch('builtins.input', return_value='mover 2')
    def test_obtener_entrada_mover_incompleto(self, input_patched, print_patched):
        """Testea que 'mover 2' devuelva None al estar incompleto"""
        # Acá el BackgammonGame debe lanzar un ValueError y este lo debe atrapar y devolver None
        accion = self.vista.obtener_entrada()
        self.assertEqual(accion, None)

    @patch('builtins.print')
    @patch('builtins.input', return_value='mover 22')
    def test_obtener_entrada_mover_valores_no_valido(self, input_patched, print_patched):
        """Testea que mover con valores no válidos devuelva None"""
        # Acá el BackgammonGame debe lanzar un ValueError y este lo debe atrapar y devolver None
        accion = self.vista.obtener_entrada()
        self.assertEqual(accion, None)

    @patch('builtins.print')
    @patch('builtins.input', return_value='poner 4')
    def test_obtener_entrada_poner(self, input_patched, print_patched):
        """Testea que 'poner 4' devuelva una AccionPoner(4)"""
        accion = self.vista.obtener_entrada()
        self.assertIsInstance(accion, AccionPoner)
        self.assertEqual(accion.dado, 4)

    @patch('builtins.print')
    @patch('builtins.input', return_value='salir')
    def test_obtener_entrada_salir(self, input_patched, print_patched):
        """Testea que 'salir' devuelva una AccionSalir"""
        accion = self.vista.obtener_entrada()
        self.assertIsInstance(accion, AccionSalir)

    @patch('builtins.print')
    @patch('builtins.input', return_value='papulince')
    def test_obtener_entrada_comando_no_valido(self, input_patched, print_patched):
        """Testea que un comando inexistente devuelva una None sin explotar"""
        accion = self.vista.obtener_entrada()
        self.assertEqual(accion, None)

    