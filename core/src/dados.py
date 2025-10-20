import random

class Dice:
    """Clase que maneja los dados
    
    Atributos
    ---------
    __valores__ : List[int]
        Lista con los valores de los dados disponibles
    """

    def __init__(self):
        self.__valores__ = []

    def tirar(self) -> List[]:
        """Tira dos dados de 6 caras, si son iguales, se pueden usar 4 veces

         Retorna
        -------
        List[int]
            Una copia de los valores de los dados (2 o 4 elementos si son dobles)
        """

        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)

        if dado1 == dado2:
            self.__valores__ == [dado1, dado1, dado1, dado1]
        else:
            self.__valores__ == [dado1, dado2]

        return self.__valores__.copy()

    @property
    def valores(self) -> List:
        """Devuelve una copia de los valores actuales"""
        return self.__valores__.copy()

    

    
