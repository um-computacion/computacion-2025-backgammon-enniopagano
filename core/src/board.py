class Board:
    """
    La clase que representa el tablero

    ...

    Atributos
    ----------
    __posiciones__ : List[List[str]]
        Una lista de listas para representar las posiciones del tablero
    barra : List[int, int]
        Una lista que representa las fichas capturadas, indice 0 para Blancas e indice 1 para Negras (default [0, 0])
    fuera : List[int, int]
        Una lista que representa las fichas fuera del tablero, indice 0 para Blancas e indice 1 para Negras (default [0, 0])
    

    Métodos
    -------
    setup_posicion_inicial()
        Inicializa el tablero con las posiciones iniciales
    """

    def __init__(self):
        """
        Parametros
        ----------
        None
        """

        self.__posiciones__ = [[] for _ in range(24)]
        self.__barra__ = [0, 0]
        self.__fuera__ = [0, 0]
        self.setup_posicion_inicial()

    def setup_posicion_inicial(self) -> None:
        """Inicializa el tablero con las posiciones iniciales"""
        # Jugador 1 ('B'lancas) - índices en la lista (0-based)
        self.__posiciones__[0] = ['B', 'B']      # Posicion 1: 2 fichas
        self.__posiciones__[11] = ['B'] * 5     # Posicion 12: 5 fichas
        self.__posiciones__[16] = ['B'] * 3     # Posicion 17: 3 fichas
        self.__posiciones__[18] = ['B'] * 5     # Posicion 19: 5 fichas
        
        # Jugador 2 ('N'egras) - posiciones espejo
        self.__posiciones__[23] = ['N', 'N']     # Posicion 24: 2 fichas
        self.__posiciones__[12] = ['N'] * 5     # Posicion 13: 5 fichas
        self.__posiciones__[7] = ['N'] * 3      # Posicion 8: 3 fichas
        self.__posiciones__[5] = ['N'] * 5      # Posicion 6: 5 fichas

    def mover_ficha(self, posicion: int, dado: int, turno: str) -> None:
        """Mueve una ficha desde su posición actual a otra

        Parametros
        ----------
        posicion: int
            La posición de la ficha que se va a mover
        dado: int
            El valor de uno de los dados
        turno: str
            Puede ser 'B' o 'N' dependiendo del turno actual
        
        Raises
        ------
        PosicionOcupadaException
            En la posición destino de la ficha hay 2 o más fichas contrarias
        """

        pos_origen = self.__posiciones__[posicion - 1]
        if turno == 'B':
            movimiento = dado
        else:
            movimiento = dado * -1
        pos_destino = self.__posiciones__[posicion + movimiento - 1]
        if pos_destino[0] == turno:
            pos_origen.pop(0)
            pos_destino.insert(0, turno)
        elif pos_destino.len() == 0:
            pos_origen.pop(0)
            pos_destino.insert(0, turno)
        else:
            if pos_destino.len() == 1:
                pos_origen.pop(0)
                pos_destino.pop(0)
                pos_destino.insert(0, turno)
                if turno == 'B':
                    self.__barra__[0] += 1
                else:
                    self.__barra__[1] += 1
            else:
                raise PosicionOcupadaException("Hay más de dos fichas contrarias")
            

    def primer_cuadrante(self, turno: str) -> bool:
        """Analiza el primer cuadrante de un jugador y determina si todas sus fichas se encuetran en él

        Devuelve True si todas sus fichas están en el cuadrante y False si no lo están
        
        Parametros
        ----------
        turno: str
            Puede ser 'B' o 'N' dependiendo del turno actual
        """
        if turno == 'N':
            rango1 = 0
            rango2 = 6
            fuera = self.__fuera__[1]
        else:
            rango1 = 18
            rango2 = 24
            fuera = self.__fuera__[0]
        contador = 0
        for i in range(rango1, rango2):
            if len(self.__posiciones__[i]) != 0:
                if self.__posiciones__[i][0] == turno:
                    contador += len(self.__posiciones__[i])
        if contador == 15 - fuera:
            return True
        else:
            return False



        
        