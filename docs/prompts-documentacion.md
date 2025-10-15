## ChatGPT GPT-5 - 30/8/2025

### Prompt: 
Estoy documentando mi proyecto con docstrings del formato NumPy/SciPy, y uno de los métodos de mi clase board (mover_ficha)llama a otros métodos de la clase board(primer_cuadrante y sacar_ficha), cómo se debería ver eso en mi docstring?

No hubo instrucciones del sistema

Resultado de la IA:

La parte en **negrita** o encerrado entre asteriscos dobles **, siempre será la salida que está presente en el código
La salida está en el codigo con modificaciones 

class Board:
    def mover_ficha(self, origen: int, destino: int, jugador: str) -> bool:
        """
        Mueve una ficha de un punto de origen a un punto de destino.

        Parameters
        ----------
        origen : int
            Índice del punto desde el cual se moverá la ficha.
        destino : int
            Índice del punto al cual se moverá la ficha.
        jugador : str
            Identificador del jugador (por ejemplo, "W" o "B").

        **Returns
        -------
        bool
            `True` si el movimiento fue válido y se realizó, `False` en caso contrario.

        See Also
        --------
        primer_cuadrante : Verifica si todas las fichas del jugador están en su primer cuadrante.
        sacar_ficha : Extrae una ficha del tablero cuando está en el cuadrante final.**
        """
        # implementación
        ...

## ChatGPT GPT-5 - 8/9/2025

### Prompt: 
Tengo que implementar integración continua que realice tests y evalúe la calidad del código al hacer push a main, esto planeaba hacerlo con github actions, tengo dos archivos que uno debe estar ya que son las pautas que se evalúan en cuanto calidad del código, ese te lo pasaré primero y después te voy a pasar un archivo .yaml que es el que usa actions para la integración continua

El primer código que le pasé fue el archivo .pylintrc tal y cómo se encuentra en el proyecto y el segundo código fue el compartido por mí compañero Joaquín Basile.

Resultado de la IA:

- **name: Run tests and generate coverage report
  run: |
    coverage run --source=core/src -m unittest discover -s core/tests
    coverage xml -o cobertura.xml
    coverage report -m > coverage_report.txt**

- **name: Run Pylint and generate report
  run: |
    pylint --rcfile=.pylintrc src tests > pylint_report.txt || true**
