Resumen de diseño general



Justificación de clases elegidas

La clase Board representará al tablero y es la conocerá las posiciones de las fichas y tendrá los métodos para moverlas. Decidí para la clase board crear el metodo mover y que este maneje la lógica de los movimientos que se pueden dar, esto lo hace llamando a otras funciones como mover_ficha y sacar_ficha

Decidí no incluir la clase Checker o Ficha para representar cada ficha, ya que en principio no lo veo necesario, vengo de hacer el Tateti y me parece que hay similitud en cuanto a lo que representa cada ficha en el tablero, dado que todas las fichas son iguales y solo cambia que sea blanca o negra, y el movimiento tampoco depende de las fichas en sí, si no de los dados

Integración continua
Para la integración continua usé una mezcla entre el archivo .yml que pasó el profesor Quinteros a Slack en el canal de la clase 09-03, y otro archivo que generosamente compartió mi compañero Joaquín Basile al canal de Backgammon el miércoles 3 de septiembre, junto con ciertas modificaciones sugeridas por la IA para que se amolde mejor a mí proyecto. El archivo de mi compañero aporta una solución a la hora de crear PR para que se actualicen los reportes del workflow además de un extra step que mergea automáticamente dichos PR.