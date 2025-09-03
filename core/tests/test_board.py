import unittest
from src.board import Board, PosicionOcupadaException, PrimerCuadranteIncompletoException

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

    def test_mover_blancas(self):
        """Testea que siga la correcta lógica de movimiento, es decir, todos los caminos posibles de las fichas blancas"""
        # Test de movimiento a una posición vacía
        self.board.mover(1, 4, 'B')
        self.assertEqual(self.board.__posiciones__[0], ['B'])
        self.assertEqual(self.board.__posiciones__[4], ['B'])
        # Test de movimiento a una posición con fichas de mismo color
        self.board.mover(12, 5, 'B')
        self.assertEqual(self.board.__posiciones__[11], ['B', 'B', 'B', 'B'])
        self.assertEqual(self.board.__posiciones__[16], ['B', 'B', 'B', 'B'])
        # Test de movimiento a una posicion con una ficha contraria
        self.board.__posiciones__[3] = ['N']
        self.board.mover(1, 3, 'B')
        self.assertEqual(self.board.__posiciones__[0], [])
        self.assertEqual(self.board.__posiciones__[3], ['B'])
        self.assertEqual(self.board.__barra__[1], 1)
        # Test de movimiento a una posicion con mas de una ficha contraria
        with self.assertRaises(PosicionOcupadaException):
            self.board.mover(4, 4, 'B')
        # Test queriendo sacar una ficha del tablero sin tener todas las fichas en el primer cuadrante
        with self.assertRaises(PrimerCuadranteIncompletoException):
            self.board.mover(19, 6, 'B')
        # Test sacando una ficha del tablero
        self.board.__posiciones__[18] = ['B'] * 15
        self.board.mover(19, 6, 'B')
        self.assertEqual(self.board.__posiciones__[18], ['B'] * 14)
        self.assertEqual(self.board.__fuera__[0], 1)

    def test_mover_negras(self):
        """Testea que siga la correcta lógica de movimiento, es decir, todos los caminos posibles de las fichas negras"""
        # Test de movimiento a una posición vacía
        self.board.mover(24, 4, 'N')
        self.assertEqual(self.board.__posiciones__[23], ['N'])
        self.assertEqual(self.board.__posiciones__[19], ['N'])
        # Test de movimiento a una posición con fichas de mismo color
        self.board.mover(13, 5, 'N')
        self.assertEqual(self.board.__posiciones__[12], ['N', 'N', 'N', 'N'])
        self.assertEqual(self.board.__posiciones__[7], ['N', 'N', 'N', 'N'])
        # Test de movimiento a una posicion con una ficha contraria
        self.board.__posiciones__[20] = ['B']
        self.board.mover(24, 3, 'N')
        self.assertEqual(self.board.__posiciones__[23], [])
        self.assertEqual(self.board.__posiciones__[20], ['N'])
        self.assertEqual(self.board.__barra__[0], 1)
        # Test de movimiento a una posicion con mas de una ficha contraria
        with self.assertRaises(PosicionOcupadaException):
            self.board.mover(21, 4, 'N')
        # Test queriendo sacar una ficha del tablero sin tener todas las fichas en el primer cuadrante
        with self.assertRaises(PrimerCuadranteIncompletoException):
            self.board.mover(6, 6, 'N')
        # Test sacando una ficha del tablero
        self.board.__posiciones__[5] = ['N'] * 15
        self.board.mover(6, 6, 'N')
        self.assertEqual(self.board.__posiciones__[5], ['N'] * 14)
        self.assertEqual(self.board.__fuera__[1], 1)

    def test_mover_ficha(self):
        """Testea el correcto movimiento de una ficha de una posicion a otra"""
        # Test del movimiento de una ficha a una posicion
        self.board.mover_ficha(self.board.__posiciones__[0], self.board.__posiciones__[4], 'B')
        self.assertEqual(self.board.__posiciones__[4], ['B'])
        # Test del movimiento de otra ficha a la misma posicion
        self.board.mover_ficha(self.board.__posiciones__[0], self.board.__posiciones__[4], 'B')
        self.assertEqual(self.board.__posiciones__[4], ['B', 'B'])

    def test_comer_ficha(self):
        """Testea que la ficha en la posicion de destino pase a la barra dependiendo la ficha"""
        # Test de ficha blanca comiendo a ficha negra
        self.board.__posiciones__[6] = ['N']
        pos_destino = self.board.__posiciones__[6]
        self.board.comer_ficha(pos_destino, 'B')
        self.assertEqual(pos_destino, [])
        self.assertEqual(self.board.__barra__[1], 1)
        # Test de ficha negra comiendo a ficha blanca
        self.board.__posiciones__[6] = ['B']
        pos_destino = self.board.__posiciones__[6]
        self.board.comer_ficha(pos_destino, 'N')
        self.assertEqual(self.board.__posiciones__[6], [])
        self.assertEqual(self.board.__barra__[0], 1)

    def test_sacar_ficha(self):
        """Testea que la ficha en la posicion de origen pase a fuera del tablero"""
        # Test de ficha blanca saliendo del tablero
        pos_origen = self.board.__posiciones__[18]
        self.board.sacar_ficha(pos_origen, 'B')
        self.assertEqual(pos_origen, ['B', 'B', 'B', 'B'])
        self.assertEqual(self.board.__fuera__[0], 1)
        # Saca otra ficha
        self.board.sacar_ficha(pos_origen, 'B')
        self.assertEqual(pos_origen, ['B', 'B', 'B'])
        self.assertEqual(self.board.__fuera__[0], 2)
        # Test de ficha negra saliendo del tablero
        pos_origen = self.board.__posiciones__[5]
        self.board.sacar_ficha(pos_origen, 'N')
        self.assertEqual(pos_origen, ['N', 'N', 'N', 'N'])
        self.assertEqual(self.board.__fuera__[1], 1)
        # Saca otra ficha
        self.board.sacar_ficha(pos_origen, 'N')
        self.assertEqual(pos_origen, ['N', 'N', 'N'])
        self.assertEqual(self.board.__fuera__[1], 2)

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

