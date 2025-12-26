class Jugador:
    """Clase que representa a un jugador del juego

    Atributos
    ---------
    __nombre__ : str
        El nombre del jugador
    __color__ : str
        El color de su ficha
    """

    def __init__(self, nombre: str, color: str):
        """
        Parametros
        ----------
        nombre : str
            Nombre del jugador
        color : str
            'B' para Blancas o 'N' para Negras
        """

        self.__nombre__ = nombre
        self.__color__ = color

    @property
    def nombre(self) -> str:
        """Retorna el nombre del jugador"""
        return self.__nombre__

    @property
    def color(self) -> str:
        """Retorna el color del jugador"""
        return self.__color__
