import unittest
from unittest.mock import patch
from core.src.dados import Dice


class TestDice(unittest.TestCase):
    
    def setUp(self):
        self.dice = Dice()

    def test_setUp(self):
        """Testea que se inicie correctamente la clase Dice"""
        self.assertEqual(self.dice.__valores__, [])

    @patch('random.randint', side_effect=[3, 4])
    def test_tirar_distintos(self, randint_patched):
        """Testea el lanzamiento con un resultado de 3 y 4"""
        dados = self.dice.tirar()
        self.assertEqual(len(dados), 2)
        # Testea la copia que retorna la función
        self.assertEqual(dados[0], 3)
        self.assertEqual(dados[1], 4)
        # Testea los valores guardados en el atributo
        self.assertEqual(self.dice.__valores__[0], 3)
        self.assertEqual(self.dice.__valores__[1], 4)
        self.assertTrue(randint_patched.called)
        self.assertEqual(randint_patched.call_count, 2)

    @patch('random.randint', return_value=5)
    def test_tirar_iguales(self, randint_patched):
        """Testea el lanzamiento con un resultado de 1 y 1"""
        dados = self.dice.tirar()
        self.assertEqual(len(dados), 4)
        # Testea la copia que retorna la función
        self.assertEqual(dados[0], 5)
        self.assertEqual(dados[1], 5)
        self.assertEqual(dados[2], 5)
        self.assertEqual(dados[3], 5)
        # Testea los valores guardados en el atributo
        self.assertEqual(self.dice.__valores__[0], 5)
        self.assertEqual(self.dice.__valores__[1], 5)
        self.assertEqual(self.dice.__valores__[2], 5)
        self.assertEqual(self.dice.__valores__[3], 5)
        self.assertTrue(randint_patched.called)
        self.assertEqual(randint_patched.call_count, 2)

    def test_getter_valores(self):
        """Testea que el getter de valores devuelva el atributo correcto"""
        self.assertEqual(self.dice.valores, self.dice.__valores__)

    @patch('random.randint', side_effect=[3, 4])
    def test_usar(self, randint_patched):
        """Testea que se descarten los dados"""
        tirada = self.dice.tirar()
        self.dice.usar(3)
        self.assertEqual(self.dice.__valores__, [4])
        self.dice.usar(4)
        self.assertEqual(self.dice.__valores__, [])

    def test_dados_disponibles(self):
        """Testea si quedan valores disponibles para usar"""
        self.dice.__valores__ = [5, 1]
        # Test con dados disponibles
        self.assertEqual(self.dice.dados_disponibles(), True)
        # Test sin dados disponibles
        self.dice.__valores__ = []
        self.assertEqual(self.dice.dados_disponibles(), False)

    def test_resetear(self):
        """Testea si se eliminan todos los valores"""
        self.dice.__valores__ = [5, 1]
        self.dice.resetear()
        self.assertEqual(self.dice.__valores__, [])

    def test_fueron_dobles(self):
        with patch('random.randint', side_effect=[5, 2]) as randint_patched:
            tirada = self.dice.tirar()
            self.assertEqual(self.dice.fueron_dobles(), False)

        with patch('random.randint', return_value=4) as randint_patched:
            tirada = self.dice.tirar()
            self.assertEqual(self.dice.fueron_dobles(), True)
