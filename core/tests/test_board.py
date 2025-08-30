import unittest
from src.board import Board

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

    def test_primer_cuadrante_blancas(self):
        """Testea si todas las fichas de un jugador estan en su primer cuadrante, en este caso las fichas blancas"""
        # Test con el tablero inicial
        self.assertEqual(self.board.primer_cuadrante('B'), False)
        # Vacia el tablero
        for p in range(len(self.board.__posiciones__)):
            self.board.__posiciones__[p] = []
        # Test con 15 fichas en una posicion
        self.board.__posiciones__[18] = ['B'] * 15
        self.assertEqual(self.board.primer_cuadrante('B'), True)

        for p in range(len(self.board.__posiciones__)):
            self.board.__posiciones__[p] = []
        # Test con fichas distribuidas
        self.board.__posiciones__[18] = ['B'] * 2
        self.board.__posiciones__[20] = ['B'] * 3
        self.board.__posiciones__[22] = ['B'] * 2
        self.board.__posiciones__[23] = ['B'] * 8
        self.assertEqual(self.board.primer_cuadrante('B'), True)
        # Test con fichas negras de por medio
        self.board.__posiciones__[19] = ['N'] * 5
        self.board.__posiciones__[21] = ['N'] * 3
        self.assertEqual(self.board.primer_cuadrante('B'), True)
        # Test con fichas fuera del tablero
        self.board.__posiciones__[20] = []
        self.board.__fuera__[0] += 3
        self.assertEqual(self.board.primer_cuadrante('B'), True)

    def test_primer_cuadrante_negras(self):
        """Testea si todas las fichas de un jugador estan en su primer cuadrante, en este caso las fichas negras"""
        # Test con el tablero inicial
        self.assertEqual(self.board.primer_cuadrante('N'), False)
        # Vacia el tablero
        for p in range(len(self.board.__posiciones__)):
            self.board.__posiciones__[p] = []
        # Test con 15 fichas en una posicion
        self.board.__posiciones__[5] = ['N'] * 15
        self.assertEqual(self.board.primer_cuadrante('N'), True)

        for p in range(len(self.board.__posiciones__)):
            self.board.__posiciones__[p] = []
        # Test con fichas distribuidas
        self.board.__posiciones__[5] = ['N'] * 2
        self.board.__posiciones__[3] = ['N'] * 3
        self.board.__posiciones__[1] = ['N'] * 2
        self.board.__posiciones__[0] = ['N'] * 8
        self.assertEqual(self.board.primer_cuadrante('N'), True)
        # Test con fichas blancas de por medio
        self.board.__posiciones__[4] = ['B'] * 5
        self.board.__posiciones__[2] = ['B'] * 3
        self.assertEqual(self.board.primer_cuadrante('N'), True)
        # Test con fichas fuera del tablero
        self.board.__posiciones__[3] = []
        self.board.__fuera__[1] += 3
        self.assertEqual(self.board.primer_cuadrante('N'), True)

if __name__ == '__main__':
    unittest.main()

