class Accion:
    """Clase base para todas las acciones"""
    pass

class AccionLanzar(Accion):
    """El jugador quiere lanzar los dados"""
    pass

class AccionMover(Accion):
    """El jugador quiere mover una ficha del tablero"""
    def __init__(self, origen: int, dado: int):
        self.origen = origen
        self.dado = dado

class AccionPoner(Accion):
    """El jugador quiere poner una ficha desde la barra"""
    def __init__(self, dado):
        self.dado = dado

class AccionSalir(Accion):
    """El jugador quiere salir del juego"""
    pass