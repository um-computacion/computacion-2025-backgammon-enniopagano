import unittest
from board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_setup_posicion_inicial(self):
        """Testea inicie el tablero correctamente"""
        self.assertEqual(len(self.board.__posiciones__), 24)

        self.assertEqual(self.board.__barra__, [0, 0])

        self.assertEqual(self.board.__fuera__, [0, 0])

    def test_setup_posicion_inicial_fichas(self):
        """Testea las posiciones iniciales de las fichas"""
        # Test de fichas Blancas
        self.assertEqual(self.board.__posiciones__[0], ['B', 'B'])
        self.assertEqual(self.board.__posiciones__[11], ['B'] * 5)
        self.assertEqual(self.board.__posiciones__[16], ['B'] * 3)
        self.assertEqual(self.board.__posiciones__[18], ['B'] * 5)

        # Test de fichas Negras
        self.assertEqual(self.board.__posiciones__[23], ['N', 'N'])
        self.assertEqual(self.board.__posiciones__[12], ['N'] * 5)
        self.assertEqual(self.board.__posiciones__[7], ['N'] * 3)
        self.assertEqual(self.board.__posiciones__[5], ['N'] * 5)

if __name__ == '__main__':
    unittest.main()

