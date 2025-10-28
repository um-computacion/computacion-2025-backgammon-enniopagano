from core.src.exceptions import (
    PosicionOcupadaException, 
    PrimerCuadranteIncompletoException, 
    PosicionVaciaException,
    MovimientoNoPosibleException
)
from typing import List # Usado para el type hinting

class Board:
    """
    La clase que representa el tablero

    ...

    Atributos
    ----------
    __posiciones__ : List[List[str]]
        Las posiciones del tablero
    barra : List[int, int]
        La barra de los jugadores, indice 0 para Blancas e indice 1 para Negras (default [0, 0])
    fuera : List[int, int]
        Fichas fuera del tablero, indice 0 para Blancas e indice 1 para Negras (default [0, 0])
    

    Métodos
    -------
    setup_posicion_inicial()
        Inicializa el tablero con las posiciones iniciales
    mover(posicion: int, dado: int, turno: str)
        Mueve una ficha desde una posicion del tablero a otra
    poner_ficha(dado: int, turno: str)
        Pone una ficha desde la barra al tablero
    ejecutar_movimiento(indice_destino: int, turno: str, es_desde_barra: bool)
        Lógica común para mover/poner fichas
    comer_ficha(pos_origen: List[], pos_destino: List[], turno: str)
        Mueve una ficha contraria a la barra del otro jugador
    ficha_sacada(turno: str)
        Suma una ficha al contador de fichas fuera del jugador
    primer_cuadrante(turno: str)
        Verifica el primer cuadrante de un jugador y determina si todas sus fichas se encuetran en él
    condicion_victoria(turno: str)
        Verifica si algún jugador ganó la partida contando sus fichas fuera del tablero
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
        """Mueve una ficha desde una posicion del tablero a otra/fuera del tablero  

        Parametros
        ----------
        posicion: int
            La posición de la ficha que se va a mover
        dado: int
            El valor de uno de los dados
        turno: str
            Puede ser 'B' o 'N' dependiendo del turno actual


        Ver Tambien
        -----------
        ejecutar_movimiento: Lógica común para mover/poner fichas
        """
        
        pos_origen = self.__posiciones__[posicion - 1]
        indice_posicion = posicion - 1
        
        # Calcular destino
        if turno == 'B':
            indice_destino = (indice_posicion) + dado
        else:
            indice_destino = (indice_posicion) - dado
        
        # Ejecutar el movimiento común
        self._ejecutar_movimiento(indice_destino, turno, indice_posicion, es_desde_barra=False)
        
        # Quitar ficha del origen
        pos_origen.pop(0)

    def poner_ficha(self, dado: int, turno: str) -> None:
        """Pone una ficha desde la barra al tablero
        
        Parametros
        ----------
        dado: int
            El valor de uno de los dados
        turno: str
            Puede ser 'B' o 'N' dependiendo del turno actual

        Ver Tambien
        -----------
        ejecutar_movimiento: Lógica común para mover/poner fichas
        """
        
        # Calcular posición destino
        if turno == 'B':
            indice_destino = 24 - dado  # Entran desde el lado negro
        else:
            indice_destino = dado - 1    # Entran desde el lado blanco
        
        # Ejecutar el movimiento común
        self._ejecutar_movimiento(indice_destino, turno, es_desde_barra=True)
        
        # Quitar ficha de la barra
        if turno == 'B':
            self.__barra__[0] -= 1
        else:
            self.__barra__[1] -= 1

    def _ejecutar_movimiento(self, indice_destino: int, turno: str, indice_posicion=0, es_desde_barra=False) -> None:
        """Lógica común para mover/poner fichas
        
        Parametros
        ----------
        indice_destino: int
            Índice de la posición destino
        turno: str
            'B' o 'N'
        es_desde_barra: bool
            Si es True, se está poniendo desde barra. Si es False, es movimiento normal.
        indice_posicion: int
            La posición de la ficha que se va a mover, para pasarla a movimiento_posible


        Raises
        ------
        PrimerCuadranteIncompletoException
            Faltan fichas en el primer cuadrante del jugador
        PosicionOcupadaException
            En la posición destino de la ficha hay 2 o más fichas contrarias
        
        Ver Tambien
        -----------
        primer_cuadrante : Verifica el primer cuadrante de un jugador y determina si todas sus fichas se encuetran en él(ignorado las fichas fuera)
        comer_ficha : Mueve una ficha contraria a la barra del otro jugador
        ficha_sacada : Suma una ficha al contador de fichas fuera del jugador
        """
        
        # Caso especial: sacar ficha del tablero (bear off)
        if indice_destino >= 24 or indice_destino < 0:
            if self.primer_cuadrante(turno):
                if self.movimiento_posible(turno, indice_posicion):
                    self.ficha_sacada(turno)
                    return
                else:
                    raise MovimientoNoPosibleException("Debes mover fichas en las posiciones de atrás")
            else:
                raise PrimerCuadranteIncompletoException("No puedes sacar fichas aún")
        
        pos_destino = self.__posiciones__[indice_destino]
        
        # Validar destino
        if len(pos_destino) >= 2 and pos_destino[0] != turno:
            raise PosicionOcupadaException("Posición bloqueada por el oponente")
        
        # Comer ficha si hay una sola enemiga
        if len(pos_destino) == 1 and pos_destino[0] != turno:
            self.comer_ficha(pos_destino, turno)
        
        # Añadir ficha al destino
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
        """Verifica el primer cuadrante de un jugador y determina si todas sus fichas se encuetran en él(ignorado las fichas fuera)
        
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

    def movimiento_posible(self, turno: str, indice_posicion: int) -> bool:
        """Verifica si un movimiento desde el ultimo cuadrante a fuera del tablero es posible
        
        Parametros
        ----------
        turno: str
            Puede ser 'B' o 'N' dependiendo del turno actual
        indice_posicion: int
            La posición de la ficha que se va a mover

        Retorna
        -------
        bool
            'True' si el movimiento es posible y 'False' si no lo es
        """

        if turno == 'B':
            pos_restantes = -(18 - indice_posicion)
            sumador = -1
        else:
            pos_restantes = 5 - indice_posicion
            sumador = 1

        if pos_restantes == 0:
            return True

        contador = sumador
        for t in range(pos_restantes):
            if len(self.__posiciones__[indice_posicion + contador]) > 0:
                return False
            contador += sumador

        return True

    def barra_vacia(self, turno: str) -> bool:
        """Verifica si hay fichas en la barra del jugador
        
        Parametros
        ----------
        turno: str
            Puede ser 'B' o 'N' dependiendo del turno actual

        Retorna
        -------
        Retorna
        -------
        bool
            'True' si no hay fichas en la barra y 'False' si hay
        """

        if turno == 'B':
            barra = self.__barra__[0]
        else:
            barra = self.__barra__[1]
        
        return (barra == 0)