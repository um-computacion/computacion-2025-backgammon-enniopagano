Resumen de diseño general



Justificación de clases elegidas

La clase Board representará al tablero y es la que conocerá las posiciones de las fichas y tendrá los métodos para moverlas. Los atributos de la clase board son simples, un atributo posiciones, que es una lista de listas, siendo cada lista elemento una posición del tablero, un atributo barra y un atributo fuera, cada uno es una lista de dos elementos que indica la cantidad de fichas ya sea en la barra o fuera de ambos jugadores. Decidí para la clase board crear el metodo mover para encargarse de los movimientos normales de una ficha que se encuentra en el tablero, y el método poner_ficha para los movimientos que implican incorporar una ficha desde la barra, ambas funciones llaman eventualmente a ejecutar_movimiento, que termina de poner la ficha en la posicion correspondiente o fuera del tablero, y actua llamando al resto de métodos según las situaciones que se den, como pueden ser sacar una ficha del tablero, comer una ficha o que un movimiento no se pueda realizar.

Decidí no incluir la clase Checker o Ficha para representar cada ficha, ya que en principio no lo veo necesario, vengo de hacer el Tateti y me parece que hay similitud en cuanto a lo que representa cada ficha en el tablero, dado que todas las fichas son iguales y solo cambia que sea blanca o negra, y el movimiento tampoco depende de las fichas en sí, si no de los dados.

La clase dados representa los dados, y decidí que cuente con un único atributo llamado valores, que incluya la cantidad de dados disponibles para usar, y que a través del método tirar, defina si son 2 o 4 valores, y estos valores a medida que se usen los dados se irán quitando de la lista de valores con el método usar.

La clase jugador representa a un jugodor que participa en la partida y esta es muy simple, ya que solo cuenta con el nombre del jugador y el color de su ficha, y los únicos métodos que tiene son los getters.

Integración continua
Para la integración continua usé una mezcla entre el archivo .yml que pasó el profesor Quinteros a Slack en el canal de la clase 09-03, y otro archivo que generosamente compartió mi compañero Joaquín Basile al canal de Backgammon el miércoles 3 de septiembre, junto con ciertas modificaciones sugeridas por la IA para que se amolde mejor a mí proyecto. El archivo de mi compañero aporta una solución a la hora de crear PR para que se actualicen los reportes del workflow además de un extra step que mergea automáticamente dichos PR.

Excepciones
Las primeras excepciones son las que pertenecen al tablero, y son:
PosicionOcupada: para cuando se quiera realizar un movimiento sobre una posición con 2 o más fichas contrarias,
PrimerCuadranteIncompleto: para cuando se quiera sacar una ficha del tablero sin tener todas las fichas restantes en home, también me dí cuenta de que primer cuadrante es más bien incorrecto ya que sería el último cuadrante del jugador que saca la ficha, es algo que cambiaré si tengo tiempo ya que no me parece un error catastrófico.
PosicionVaciaException: para cuando en la posicion que se le pasa a mover no se encuentra ninguna ficha.
MovimientoNoPosible: para cuando se intente sacar una ficha del tablero mientras se encuentran otras fichas detrás que se deberían mover primero

Testing y covertura
En todas las clases se viene testeando el 100% del código ya que es algo que me deja más seguro y se me ha generado la costumbre de ir testeando el código a medida que lo voy haciendo.

Referencias a SOLID
Todas las clases tienen métodos que se centran en respetar el principio de Single-Responsibility