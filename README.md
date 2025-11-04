# Backgammon

Alumno: Ennio Pagano

## Descripción

Implementación del juego de mesa Backgammon en python con interfaz por consola de comandos e interfaz gráfica por pygame.

## Ejecución

Para ejecutar el juego tanto por consola de comandos como por pygame se debe correr desde la raíz del repositorio el script main.py, este lo llevará a una interfaz de consola donde podrá elegir finalmente dónde quiere jugar

    # Correr desde consola de comandos
    python main.py

## Estructura

├── core/
│   │
│   ├── src/                   # --- MODELO ---
│   │   ├── backgammon.py      (Clase BackgammonGame, EstadoJuego)
│   │   ├── board.py           (Clase Board)
│   │   ├── dados.py           (Clase Dice)
│   │   ├── jugador.py         (Clase Jugador)
│   │   └── exceptions.py      (Excepciones)
|   |
|   ├── tests/                 # --- TESTS ---
|   │   ├── test_board.py
|   │   ├── test_backgammon.py
|   │   ├── test_dice.py
|   │   └── ...
│   │
│   ├── controlador/           # --- CONTROLADOR ---
│   │   ├── controlador.py     (Clase ControladorJuego)
│   │   ├── vista_juego.py     (Interfaz IVistaJuego)
│   │   └── acciones.py        (Accion, AccionMover, AccionPoner, etc.)
│   │
│   │── cli/                   # --- Interfaz de Consola ---
│   │   ├── cli.py             
|   |   └── test_cli_vista.py
│   │
│   └── pygame_ui/             # --- Interfaz de Pygame ---
│       └── vista_pygame.py
│
├── assets/                    # --- RECURSOS ---
│
├── main.py                    # --- RECURSOS ---
│
└── requirements.txt