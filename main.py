from core.src.backgammon import BackgammonGame
from core.controlador.controlador import ControladorJuego
from core.cli.cli import VistaConsola
from core.pygame_ui.pygame import VistaPygame

def main():
    print("Bienvenido a Backgammon")
    print("¿Qué interfaz deseas usar?\n1: Consola\n2: Pygame")

    vista = None
    while vista == None:
        eleccion = input('Ingresa tu elección (1 o 2)\n').strip()

        if eleccion == '1':
            vista = VistaConsola()
        elif eleccion == '2':
            vista = VistaPygame()
        else:
            print(f"Elección '{eleccion}' inválida. Por favor te lo pido, ingresa 1 o 2.")

    modelo = BackgammonGame()
    
    controlador = ControladorJuego(modelo, vista)
    controlador.run()

if __name__ == "__main__":
    main()