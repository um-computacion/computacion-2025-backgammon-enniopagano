from core.src.exceptions import PosicionOcupadaException, PrimerCuadranteIncompletoException, PosicionVaciaException
from typing import List # Usado para el type hinting

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
    mover(posicion: int, dado: int, turno: str)
        Maneja la lógica del movimiento de las fichas
    mover_ficha(pos_origen: List[], pos_destino: List[], turno: str)
        Mueve una ficha desde su posición actual a otra
    comer_ficha(pos_origen: List[], pos_destino: List[], turno: str)
        Mueve una ficha a una posicion donde haya una ficha contraria y la mueve a la barra
    sacar_ficha(pos_origen: List[], turno: str)
        Saca una ficha del tablero y la suma al contador del jugador
    primer_cuadrante(turno: str)
        Verifica el primer cuadrante de un jugador y determina si todas sus fichas se encuetran en él
    condicion_victoria(turno: str)
        Verifica si algún jugador ganó la partida contando sus fichas fuera del tablero
    poner_ficha(dado: int, turno: str)
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

    @property
    def posiciones(self) -> List:
        """Devuelve las posiciones actuales"""
        return self.__posiciones__

    @property
    def barra(self) -> List:
        """Devuelve la cantidad de fichas en la barra de ambos jugadores"""
        return self.__barra__

    @property
    def fuera(self) -> List:
        """Devuelve la cantidad de fichas fuera de ambos jugadores"""
        return self.__fuera__

    def mover(self, posicion: int, dado: int, turno: str) -> None:
        """Maneja la lógica del movimiento de las fichas

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

        Ver Tambien
        -----------
        primer_cuadrante : Verifica el primer cuadrante de un jugador y determina si todas sus fichas se encuetran en él
        mover_ficha : Mueve una ficha desde su posición actual a otra
        comer_ficha : Mueve una ficha contraria a la barra del otro jugador
        sacar_ficha : Saca una ficha del tablero y la suma al contador del jugador
        """
        
        pos_origen = self.__posiciones__[posicion - 1]
        
        # Calcular destino
        if turno == 'B':
            indice_destino = (posicion - 1) + dado
        else:
            indice_destino = (posicion - 1) - dado
        
        # Ejecutar el movimiento común
        self._ejecutar_movimiento(indice_destino, turno, es_desde_barra=False)
        
        # Quitar ficha del origen
        pos_origen.pop(0)

    def mover_ficha(self, pos_origen: List[str], pos_destino: List[str], turno: str) -> None:
        """Mueve una ficha desde su posición actual a otra

        Parametros
        ----------
        pos_origen: List[]
            Es la lista con la posicion actual de la ficha
        pos_destino: List[]
            Es la lista con la posicion a donde se va a mover la ficha
        turno: str
            Puede ser 'B' o 'N' dependiendo del turno actual
        """

        pos_origen.pop(0)
        pos_destino.insert(0, turno)
    
    def comer_ficha(self, pos_destino: List[str], turno: str) -> None:
        """Mueve una ficha contraria a la barra del otro jugador
        
        Parametros
        ----------
        pos_destino: List[]
            Es la lista con la posicion a donde se va a mover la ficha
        turno: str
            Puede ser 'B' o 'N' dependiendo del turno actual
        """
        pos_destino.pop(0)
        if turno == 'B':
            self.__barra__[1] += 1
        else:
            self.__barra__[0] += 1

    def ficha_sacada(self, turno: str) -> None:
        """Suma una ficha al contador de fichas fuera del jugador
        
        Parametros
        ----------
        turno: str
            Puede ser 'B' o 'N' dependiendo del turno actual
        """
        if turno == 'B':
            self.__fuera__[0] += 1
        else:
            self.__fuera__[1] += 1

    def primer_cuadrante(self, turno: str) -> bool:
        """Verifica el primer cuadrante de un jugador y determina si todas sus fichas se encuetran en él
        
        Parametros
        ----------
        turno: str
            Puede ser 'B' o 'N' dependiendo del turno actual

        Retorna
        -------
        bool
            'True' si todas sus fichas están en el cuadrante(sin contar las fichas fuera del tablero)
            y 'False' si no lo están
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

    def condicion_victoria(self, turno: str) -> bool:
        """Verifica si algún jugador ganó la partida contando sus fichas fuera del tablero
        
        Parametros
        ----------
        turno: str
            Puede ser 'B' o 'N' dependiendo del turno actual

        Retorna
        -------
        bool
            'True' si el contador llega a 15 y 'False' si es menor a 15
        """

        if turno == 'B':
            if self.__fuera__[0] == 15:
                return True
            else:
                return False
        else:
            if self.__fuera__[1] == 15:
                return True
            else:
                return False

    def get_ficha(self, posicion: int, turno: str) -> bool:
        """
        Verifica si hay una ficha del respectivo turno en la posicion dada
        
        Parametros
        ----------
        posicion: int
            Es la posicion que se quiere verificar
        turno: str
            Puede ser 'B' o 'N' dependiendo del turno actual

        Retorna
        -------
        bool
            'True' si hay una ficha del respectivo turno y 'False' si es del turno contrario
        
        Raises
        ------
        PosicionVaciaException
            En la posición dada no hay ninguna ficha
        """

        posicion = self.__posiciones__[posicion - 1]
        if len(posicion) == 0:
            raise PosicionVaciaException
        else:
            if posicion[0] == turno:
                return True
            else:
                return False