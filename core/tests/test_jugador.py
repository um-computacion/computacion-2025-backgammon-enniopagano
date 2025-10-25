import unittest
from core.src.jugador import Jugador

class TestJugador(unittest.TestCase):

    def test_setUp(self):
        """Testea que se cree un jugador correctamente"""
        self.jugador = Jugador('Luis', 'B')
        self.assertEqual(self.jugador.__nombre__, 'Luis')
        self.assertEqual(self.jugador.__color__, 'B')
        self.jugador = Jugador('1234', 'N')
        self.assertEqual(self.jugador.__nombre__, '1234')
        self.assertEqual(self.jugador.__color__, 'N')

    def setUp(self):
        self.jugador = Jugador('Luis', 'B')

    def test_getter_nombre(self):
        """Testea que el getter del nombre devuelva el atributo correcto"""
        self.assertEqual(self.jugador.nombre, 'Luis')

    def test_getter_color(self):
        """Testea que el getter del color devuelva el atributo correcto"""
        self.assertEqual(self.jugador.color, 'B')