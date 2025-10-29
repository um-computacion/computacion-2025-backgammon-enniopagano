import unittest
from core.src.board import Board
from core.src.exceptions import (
    PosicionOcupadaException,
    PrimerCuadranteIncompletoException,
    PosicionVaciaException
)

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_setup_posicion_inicial(self):
        """Testea que inicie el tablero correctamente"""
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

    def test_getter_posiciones(self):
        """Testea que el getter de posiciones devuelva el atributo correcto"""
        self.assertEqual(self.board.posiciones, self.board.__posiciones__)

    def test_getter_barra(self):
        """Testea que el getter de barra devuelva el atributo correcto"""
        self.assertEqual(self.board.barra, self.board.__barra__)

    def test_getter_fuera(self):
        """Testea que el getter de fuera devuelva el atributo correcto"""
        self.assertEqual(self.board.fuera, self.board.__fuera__)

    def test_mover_posicion_vacia(self):
        """Testea mover dando una posicion vacia como parametro"""
        with self.assertRaises(PosicionVaciaException):
            self.board.mover(2, 4, 'B')

    def test_mover_blancas(self):
        """
        Testea que siga la correcta lógica de movimiento, es decir,
        todos los caminos posibles de las fichas blancas
        """
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
        # Test queriendo sacar una ficha del tablero
        # sin tener todas las fichas en el primer cuadrante
        with self.assertRaises(PrimerCuadranteIncompletoException):
            self.board.mover(19, 6, 'B')
        # Test sacando una ficha del tablero
        self.board.__posiciones__[18] = ['B'] * 15
        self.board.mover(19, 6, 'B')
        # self.assertEqual(self.board.__posiciones__[18], ['B'] * 14)
        self.assertEqual(self.board.__fuera__[0], 1)

    def test_mover_negras(self):
        """
        Testea que siga la correcta lógica de movimiento, es decir,
        todos los caminos posibles de las fichas negras
        """
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
        # Test queriendo sacar una ficha del tablero
        # sin tener todas las fichas en el primer cuadrante
        with self.assertRaises(PrimerCuadranteIncompletoException):
            self.board.mover(6, 6, 'N')
        # Test sacando una ficha del tablero
        self.board.__posiciones__[5] = ['N'] * 15
        self.board.mover(6, 6, 'N')
        # self.assertEqual(self.board.__posiciones__[5], ['N'] * 14)
        self.assertEqual(self.board.__fuera__[1], 1)

    def test_poner_ficha(self):
        """Testea que se coloque correctamente una ficha desde la barra al tablero"""
        # Test con ficha blanca
        self.board.__barra__[0] = 2
        self.board.poner_ficha(3, 'B')
        self.assertEqual(self.board.__barra__[0], 1)
        self.assertEqual(self.board.__posiciones__[21], ['B'])
        # Test con ficha negra
        self.board.__barra__[1] = 2
        self.board.poner_ficha(3, 'N')
        self.assertEqual(self.board.__barra__[1], 1)
        self.assertEqual(self.board.__posiciones__[2], ['N'])

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

    def test_ficha_sacada(self):
        """Testea que se sume al contador del jugador la ficha que salió del tablero"""
        # Test de ficha blanca saliendo del tablero
        self.board.ficha_sacada('B')
        self.assertEqual(self.board.__fuera__[0], 1)
        # Saca otra ficha
        self.board.ficha_sacada('B')
        self.assertEqual(self.board.__fuera__[0], 2)
        # Test de ficha negra saliendo del tablero
        self.board.ficha_sacada('N')
        self.assertEqual(self.board.__fuera__[1], 1)
        # Saca otra ficha
        self.board.ficha_sacada('N')
        self.assertEqual(self.board.__fuera__[1], 2)


    def test_primer_cuadrante_blancas(self):
        """
        Testea si todas las fichas de un jugador estan en su primer cuadrante,
        en este caso las fichas blancas
        """
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
        """
        Testea si todas las fichas de un jugador estan en su primer cuadrante,
        en este caso las fichas negras
        """
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

    def test_condicion_victoria(self):
        """Testea si algún jugador ganó la partida"""
        # Test con tablero inicial (ningun jugador ganador)
        self.assertEqual(self.board.condicion_victoria('B'), False)
        self.assertEqual(self.board.condicion_victoria('N'), False)
        # Test con jugador blanco ganador
        self.board.__fuera__[0] = 15
        self.assertEqual(self.board.condicion_victoria('B'), True)
        # Test con jugador negro ganador
        self.board.__fuera__[1] = 15
        self.assertEqual(self.board.condicion_victoria('N'), True)

    def test_get_ficha_blanca(self):
        """Testea que devuelva correctamente si hay una ficha blanca en la posicion dada"""
        # Test con jugador blanco donde hay una ficha blanca
        self.assertEqual(self.board.get_ficha(0, 'B'), True)
        self.assertEqual(self.board.get_ficha(11, 'B'), True)
        # Test con jugador blanco donde hay una ficha negra
        self.assertEqual(self.board.get_ficha(5, 'B'), False)
        # Test con jugador blanco donde no hay ninguna ficha
        with self.assertRaises(PosicionVaciaException):
            self.board.get_ficha(2, 'B')

    def test_get_ficha_negra(self):
        """Testea que devuelva correctamente si hay una ficha negra en la posicion dada"""
        # Test con jugador negro donde hay una ficha negra
        self.assertEqual(self.board.get_ficha(23, 'N'), True)
        self.assertEqual(self.board.get_ficha(12, 'N'), True)
        # Test con jugador negro donde hay una ficha blanca
        self.assertEqual(self.board.get_ficha(18, 'N'), False)
        # Test con jugador negro donde no hay ninguna ficha
        with self.assertRaises(PosicionVaciaException):
            self.board.get_ficha(2, 'N')

    def test_movimiento_posible_blancas(self):
        """Testea que los movimientos a fuera del tablero estén permitidos"""
        self.board.__posiciones__[23] = []
        self.board.__posiciones__[21] = ['B']
        self.assertEqual(self.board.movimiento_posible('B', 21), False)
        self.assertEqual(self.board.movimiento_posible('B', 18), True)
        self.board.__posiciones__[18] = []
        self.assertEqual(self.board.movimiento_posible('B', 21), True)

    def test_movimiento_posible_negras(self):
        """Testea que los movimientos a fuera del tablero estén permitidos"""
        self.board.__posiciones__[0] = []
        self.board.__posiciones__[2] = ['N']
        self.assertEqual(self.board.movimiento_posible('N', 2), False)
        self.assertEqual(self.board.movimiento_posible('N', 5), True)
        self.board.__posiciones__[5] = []
        self.assertEqual(self.board.movimiento_posible('N', 2), True)

    def test_barra_vacia_blancas(self):
        """Testea que la barra del jugador blanco este vacia"""
        self.assertEqual(self.board.barra_vacia('B'), True)
        self.board.__barra__[0] = 1
        self.assertEqual(self.board.barra_vacia('B'), False)

    def test_barra_vacia_negras(self):
        """Testea que la barra del jugador negro este vacia"""
        self.assertEqual(self.board.barra_vacia('N'), True)
        self.board.__barra__[1] = 1
        self.assertEqual(self.board.barra_vacia('N'), False)


