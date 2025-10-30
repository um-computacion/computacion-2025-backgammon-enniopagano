# Automated Reports
## Coverage Report
```text
Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
core/src/__init__.py         0      0   100%
core/src/backgammon.py     116      0   100%
core/src/board.py          114      1    99%   200
core/src/dados.py           31      0   100%
core/src/exceptions.py      14      0   100%
core/src/jugador.py         10      0   100%
------------------------------------------------------
TOTAL                      285      1    99%

```
## Pylint Report
```text
************* Module core.src.dados
core/src/dados.py:65:0: C0303: Trailing whitespace (trailing-whitespace)
core/src/dados.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/src/dados.py:57:8: R1703: The if statement can be replaced with 'return bool(test)' (simplifiable-if-statement)
core/src/dados.py:57:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/src/dados.py:68:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
************* Module core.src.jugador
core/src/jugador.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module core.src.board
core/src/board.py:200:0: C0301: Line too long (103/100) (line-too-long)
core/src/board.py:259:0: C0301: Line too long (101/100) (line-too-long)
core/src/board.py:388:0: C0304: Final newline missing (missing-final-newline)
core/src/board.py:388:0: C0325: Unnecessary parens after 'return' keyword (superfluous-parens)
core/src/board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/src/board.py:196:16: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/src/board.py:162:8: W0613: Unused argument 'es_desde_barra' (unused-argument)
core/src/board.py:275:8: R1703: The if statement can be replaced with 'return bool(test)' (simplifiable-if-statement)
core/src/board.py:275:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/src/board.py:295:12: R1703: The if statement can be replaced with 'return bool(test)' (simplifiable-if-statement)
core/src/board.py:295:12: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/src/board.py:300:12: R1703: The if statement can be replaced with 'return bool(test)' (simplifiable-if-statement)
core/src/board.py:300:12: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/src/board.py:360:12: W0612: Unused variable 't' (unused-variable)
core/src/board.py:7:0: C0411: standard import "typing.List" should be placed before first party import "core.src.exceptions.PosicionOcupadaException"  (wrong-import-order)
************* Module core.src.exceptions
core/src/exceptions.py:20:0: C0304: Final newline missing (missing-final-newline)
core/src/exceptions.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/src/exceptions.py:1:0: C0115: Missing class docstring (missing-class-docstring)
core/src/exceptions.py:4:0: C0115: Missing class docstring (missing-class-docstring)
core/src/exceptions.py:7:0: C0115: Missing class docstring (missing-class-docstring)
core/src/exceptions.py:10:0: C0115: Missing class docstring (missing-class-docstring)
core/src/exceptions.py:13:0: C0115: Missing class docstring (missing-class-docstring)
core/src/exceptions.py:16:0: C0115: Missing class docstring (missing-class-docstring)
core/src/exceptions.py:19:0: C0115: Missing class docstring (missing-class-docstring)
************* Module core.src.backgammon
core/src/backgammon.py:168:0: C0325: Unnecessary parens after 'not' keyword (superfluous-parens)
core/src/backgammon.py:241:0: C0301: Line too long (108/100) (line-too-long)
core/src/backgammon.py:254:0: C0301: Line too long (113/100) (line-too-long)
core/src/backgammon.py:268:0: C0305: Trailing newlines (trailing-newlines)
core/src/backgammon.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/src/backgammon.py:24:0: R0902: Too many instance attributes (8/7) (too-many-instance-attributes)
core/src/backgammon.py:113:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/src/backgammon.py:113:11: C0121: Comparison 'self.__primer_turno__ == True' should be 'self.__primer_turno__ is True' if checking for the singleton value True, or 'self.__primer_turno__' if testing for truthiness (singleton-comparison)
core/src/backgammon.py:117:12: R1720: Unnecessary "elif" after "raise", remove the leading "el" from "elif" (no-else-raise)
core/src/backgammon.py:176:12: W0719: Raising too general exception: Exception (broad-exception-raised)
core/src/backgammon.py:186:8: W0706: The except handler raises immediately (try-except-raise)
core/src/backgammon.py:219:12: W0719: Raising too general exception: Exception (broad-exception-raised)
core/src/backgammon.py:226:8: W0706: The except handler raises immediately (try-except-raise)
core/src/backgammon.py:4:0: C0411: standard import "abc.ABC" should be placed before first party imports "core.src.board.Board", "core.src.dados.Dice", "core.src.jugador.Jugador"  (wrong-import-order)
core/src/backgammon.py:5:0: C0411: standard import "enum.Enum" should be placed before first party imports "core.src.board.Board", "core.src.dados.Dice", "core.src.jugador.Jugador"  (wrong-import-order)
core/src/backgammon.py:6:0: C0411: standard import "typing.List" should be placed before first party imports "core.src.board.Board", "core.src.dados.Dice", "core.src.jugador.Jugador"  (wrong-import-order)
core/src/backgammon.py:7:0: C0411: standard import "random" should be placed before first party imports "core.src.board.Board", "core.src.dados.Dice", "core.src.jugador.Jugador"  (wrong-import-order)
core/src/backgammon.py:4:0: W0611: Unused ABC imported from abc (unused-import)
core/src/backgammon.py:4:0: W0611: Unused abstractmethod imported from abc (unused-import)
core/src/backgammon.py:8:0: W0611: Unused MovimientoNoPosibleException imported from core.src.exceptions (unused-import)
************* Module core.tests.test_jugador
core/tests/test_jugador.py:24:0: C0304: Final newline missing (missing-final-newline)
core/tests/test_jugador.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/tests/test_jugador.py:4:0: C0115: Missing class docstring (missing-class-docstring)
core/tests/test_jugador.py:6:4: C0103: Method name "test_setUp" doesn't conform to snake_case naming style (invalid-name)
************* Module core.tests.test_backgammon
core/tests/test_backgammon.py:93:0: C0301: Line too long (134/100) (line-too-long)
core/tests/test_backgammon.py:104:0: C0301: Line too long (134/100) (line-too-long)
core/tests/test_backgammon.py:317:0: C0305: Trailing newlines (trailing-newlines)
core/tests/test_backgammon.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/tests/test_backgammon.py:20:0: C0115: Missing class docstring (missing-class-docstring)
core/tests/test_backgammon.py:84:55: W0613: Unused argument 'tirada_patched' (unused-argument)
core/tests/test_backgammon.py:90:61: W0613: Unused argument 'tirada_patched' (unused-argument)
core/tests/test_backgammon.py:101:61: W0613: Unused argument 'tirada_patched' (unused-argument)
core/tests/test_backgammon.py:112:39: W0613: Unused argument 'tirada_patched' (unused-argument)
core/tests/test_backgammon.py:141:60: W0613: Unused argument 'barra_patched' (unused-argument)
core/tests/test_backgammon.py:151:50: W0613: Unused argument 'barra_patched' (unused-argument)
core/tests/test_backgammon.py:151:65: W0613: Unused argument 'ficha_patched' (unused-argument)
core/tests/test_backgammon.py:161:47: W0613: Unused argument 'barra_patched' (unused-argument)
core/tests/test_backgammon.py:161:62: W0613: Unused argument 'ficha_patched' (unused-argument)
core/tests/test_backgammon.py:174:61: W0613: Unused argument 'barra_patched' (unused-argument)
core/tests/test_backgammon.py:184:59: W0613: Unused argument 'barra_patched' (unused-argument)
core/tests/test_backgammon.py:184:74: W0613: Unused argument 'ficha_patched' (unused-argument)
core/tests/test_backgammon.py:195:8: W0613: Unused argument 'barra_patched' (unused-argument)
core/tests/test_backgammon.py:196:8: W0613: Unused argument 'ficha_patched' (unused-argument)
core/tests/test_backgammon.py:219:56: W0613: Unused argument 'barra_patched' (unused-argument)
core/tests/test_backgammon.py:250:42: W0613: Unused argument 'print_patched' (unused-argument)
core/tests/test_backgammon.py:264:42: W0613: Unused argument 'print_patched' (unused-argument)
core/tests/test_backgammon.py:283:41: W0613: Unused argument 'print_patched' (unused-argument)
core/tests/test_backgammon.py:292:41: W0613: Unused argument 'print_patched' (unused-argument)
core/tests/test_backgammon.py:301:60: W0613: Unused argument 'victoria_patched' (unused-argument)
core/tests/test_backgammon.py:310:65: W0613: Unused argument 'print_patched' (unused-argument)
core/tests/test_backgammon.py:310:80: W0613: Unused argument 'victoria_patched' (unused-argument)
core/tests/test_backgammon.py:20:0: R0904: Too many public methods (36/20) (too-many-public-methods)
core/tests/test_backgammon.py:2:0: W0611: Unused call imported from unittest.mock (unused-import)
core/tests/test_backgammon.py:10:0: W0611: Unused MovimientoNoPosibleException imported from core.src.exceptions (unused-import)
************* Module core.tests.test_dice
core/tests/test_dice.py:7:0: C0303: Trailing whitespace (trailing-whitespace)
core/tests/test_dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/tests/test_dice.py:6:0: C0115: Missing class docstring (missing-class-docstring)
core/tests/test_dice.py:11:4: C0103: Method name "test_setUp" doesn't conform to snake_case naming style (invalid-name)
core/tests/test_dice.py:57:24: W0613: Unused argument 'randint_patched' (unused-argument)
core/tests/test_dice.py:59:8: W0612: Unused variable 'tirada' (unused-variable)
core/tests/test_dice.py:80:4: C0116: Missing function or method docstring (missing-function-docstring)
core/tests/test_dice.py:81:60: W0612: Unused variable 'randint_patched' (unused-variable)
core/tests/test_dice.py:82:12: W0612: Unused variable 'tirada' (unused-variable)
************* Module core.tests.test_board
core/tests/test_board.py:287:0: C0305: Trailing newlines (trailing-newlines)
core/tests/test_board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/tests/test_board.py:9:0: C0115: Missing class docstring (missing-class-docstring)
core/tests/test_board.py:169:8: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
core/tests/test_board.py:175:8: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
core/tests/test_board.py:200:8: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
core/tests/test_board.py:206:8: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
core/tests/test_board.py:9:0: R0904: Too many public methods (21/20) (too-many-public-methods)

-----------------------------------
Your code has been rated at 8.57/10


```
