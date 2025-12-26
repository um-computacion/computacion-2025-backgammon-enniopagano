import random
from typing import List

class Dice:
    """Clase que maneja los dados
    
    Atributos
    ---------
    __valores__ : List[int]
        Lista con los valores de los dados disponibles
    """

    def __init__(self):
        self.__valores__ = []

    def tirar(self) -> List:
        """Tira dos dados de 6 caras, si son iguales, se pueden usar 4 veces

         Retorna
        -------
        List[int]
            Una copia de los valores de los dados (2 o 4 elementos si son dobles)
        """

        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)

        if dado1 == dado2:
            self.__valores__ = [dado1, dado1, dado1, dado1]
        else:
            self.__valores__ = [dado1, dado2]

        return self.__valores__.copy()

    def set_valores(self, valores: List[int]) -> None:
        """Establece manualmente los valores de los dados para la tirada inicial"""
        self.__valores__ = valores

    @property
    def valores(self) -> List:
        """Devuelve una copia de los valores actuales"""
        return self.__valores__.copy()

    def usar(self, dado: int) -> None:
        """Saca un dado de los valores una vez usado
        
        Parametros
        ----------
        dado: int
            El valor del dado que se va a descartar
        """

        self.__valores__.remove(dado)

    def dados_disponibles(self) -> bool:
        """Verifica si hay dados por usar"""
        if len(self.__valores__) > 0:
            return True
        else:
            return False

    def resetear(self) -> None:
        """Deja vacía la lista de valores"""
        self.__valores__ = []
    
    def fueron_dobles(self) -> bool:
        """Verifica si la última tirada fueron dobles"""
        return len(self.__valores__) == 4