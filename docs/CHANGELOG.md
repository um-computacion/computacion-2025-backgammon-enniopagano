# Changelog

Todos los cambios notables a este proyecto estarán en este documento.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
y este proyecto se adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.4.5] - 2025-10-30

### Added

- Clase base (Accion)
- Clases herencia (AccionLanzar, AccionMover, AccionPoner, AccionSalir)


## [0.4.4] - 2025-10-29

### Added

- Interfaz abstracta (IVistaJuego)
- Método clase backgammon (intentar_poner_ficha)

### Changed

- Ahora poner_ficha coloca del lado correspondiente

## [0.4.3] - 2025-10-28

### Added

- Método clase backgammon (intentar_mover_ficha)
- Método clase backgammon (lanzar_dados)
- Método clase backgammon (cambiar_turno)
- Método clase backgammon (saltar_turno)
- Método clase backgammon (comprobar_estado_post_movimiento)

### Changed

- Ahora mover verifica si la posición está vacía
- Get_ficha recibe el indice de la posicion

## [0.4.2] - 2025-10-27

### Added

- Clase de Estados (EstadoJuego)
- Método clase backgammon (getters)
- Método clase backgammon (lanzar_dados)
- Método clase dados (set_valores)

## [0.4.1] - 2025-10-26

### Added

- Método clase board (movimiento_posible)
- Excepción (MovimientoNoPosible)

## [0.4.0] - 2025-10-25

### Added

- Terminada la clase jugador

## [0.3.0] - 2025-10-19

### Added

- Terminada la clase Dice
- Método clase Dice (tirar)
- Método clase Dice (usar)
- Método clase Dice (dados_disponibles)
- Método clase Dice (resetear)
- Método clase Dice (fueron_dobles)

## [0.2.2] - 2025-10-18

### Added

- Clase Dice

## [0.2.1] - 2025-10-14

### Added

- Clase Backgammon

## [0.2.0] - 2025-10-13

### Added

- Terminada clase Board
- Método clase Board (poner_ficha)
- Método clase Board (ejecutar_movimiento)

### Changed

- Reemplazado el método sacar_ficha por ficha_sacada
- Reestructurado el método mover

### Removed

- Método clase Board (mover_ficha)

## [0.1.7] - 2025-09-20

### Added

- Getters para los atributos clase Board

## [0.1.6] - 2025-09-03

### Added

- Método clase Board (condicion_victoria)
- Test método clase Board (condicion_victoria)

## [0.1.5] - 2025-09-02

### Added

- Test método clase Board (mover)

## [0.1.4] - 2025-09-01

### Added

- Método clase Board (mover)
- Método clase Board (comer_ficha)
- Método clase Board (sacar_ficha)
- Test método clase Board (mover_ficha)
- Test método clase Board (comer_ficha)
- Test método clase Board (sacar_ficha)

### Fixed

- Ahora la función mover maneja toda la logica del movimiento de las fichas, y mover_ficha solo mueve de una posición a otra

## [0.1.3] - 2025-08-30

### Added

- Método clase Board (primer_cuadrante)
- Test método clase Board (primer_cuadrante)

## [0.1.2] - 2025-08-28

### Added

- Método clase Board (mover_ficha)

## [0.1.1] - 2025-08-26

### Added

- Clase Board
- Método clase Board (setup_posicion_inicial)
- Test método clase Board (setup_posicion_inicial)

## [0.1.0] - 2025-08-25

### Added

- Estructura Inicial