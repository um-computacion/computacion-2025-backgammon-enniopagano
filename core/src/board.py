class Board:
    """
    La clase que representa el tablero

    ...

    Atributos
    ----------
    __posiciones__ : List[List[]]
        Una lista de listas para representar las __posiciones__ del tablero
    barra : List[int, int]
        Una lista que representa las fichas capturadas, un elemento para cada jugador (default [0, 0])
    fuera : List[int, int]
        Una lista que representa las fichas fuera del tablero, un elemento para cada jugador (default [0, 0])
    

    Métodos
    -------
    setup_posicion_inicial()
        Inicializa el tablero con las __posiciones__ iniciales
    """

    def __init__(self):
        """
        Parameters
        ----------
        None
        """

        self.__posiciones__ = [[] for _ in range(24)]
        self.__barra__ = [0, 0]
        self.__fuera__ = [0, 0]
        self.setup_posicion_inicial()

    def setup_posicion_inicial(self):
        """Inicializa el tablero con las __posiciones__ iniciales"""
        # Jugador 1 ('B'lancas) - índices en la lista (0-based)
        self.__posiciones__[0] = ['B', 'B']      # Posicion 1: 2 fichas
        self.__posiciones__[11] = ['B'] * 5     # Posicion 12: 5 fichas
        self.__posiciones__[16] = ['B'] * 3     # Posicion 17: 3 fichas
        self.__posiciones__[18] = ['B'] * 5     # Posicion 19: 5 fichas
        
        # Jugador 2 ('N'egras) - __posiciones__ espejo
        self.__posiciones__[23] = ['N', 'N']     # Posicion 24: 2 fichas
        self.__posiciones__[12] = ['N'] * 5     # Posicion 13: 5 fichas
        self.__posiciones__[7] = ['N'] * 3      # Posicion 8: 3 fichas
        self.__posiciones__[5] = ['N'] * 5      # Posicion 6: 5 fichas

        