from abc import  ABC, abstractmethod

class IVistaJuego(ABC):
    """Interfaz abstracta para cualquier vista de Backgammon"""
    
    @abstractmethod
    def inicializar(self):
        """
        Prepara la vista para empezar
        Abre la ventana para Pygame
        Limpia la consola para el cli
        """
        pass

    @abstractmethod
    def dibujar_tablero(self, tablero, dados, jugador_actual):
        """Muestra el estado completo del tablero"""
        pass
    
    @abstractmethod
    def obtener_entrada(self):
        """
        Espera o comprueba la acción del usuario
        Debe devolver un objeto de Accion
        """
        pass

    @abstractmethod
    def mostrar_mensaje(self, mensaje: str):
        """Muestra un mensaje informativo al usuario"""
        pass

    @abstractmethod
    def mostrar_error(self, error: str):
        """Muestra un mensaje de error al usuario"""
        pass

    @abstractmethod
    def cerrar(self):
        """Cierra la vista y limpia los recursos"""
        pass
