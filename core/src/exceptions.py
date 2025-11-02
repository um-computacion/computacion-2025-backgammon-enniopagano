class PosicionOcupadaException(Exception):
    def __init__(self, message="Esa posición está ocupada por el rival"):
        super().__init__(message)

class PrimerCuadranteIncompletoException(Exception):
    def __init__(self, message="Te faltan fichas en el último cuadrante"):
        super().__init__(message)

class PosicionVaciaException(Exception):
    def __init__(self, message="La posición desde donde quieres mover está vacía"):
        super().__init__(message)

class MovimientoNoPosibleException(Exception):
    def __init__(self, message="Tienes fichas detrás de esa que debes mover"):
        super().__init__(message)

class TiradaInicialEmpateException(Exception):
    def __init__(self, message="Es un empate, hay que tirar de nuevo"):
        super().__init__(message)

class NoEsMomentoException(Exception):
    pass

class FichaContrariaException(Exception):
    def __init__(self, message="Esa ficha no es tuya"):
        super().__init__(message)