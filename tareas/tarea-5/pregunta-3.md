Para determinar si existe una estrategia ganadora para alguno de ls jugadores involucrados, vamos a utilizar el metodo **minmax**.

Adicionalmente, para reducir el numero de estados explorados por el algortimo, vamos a utilizar la poda alfa-beta.

Para la implementacion de este algoritmo, el jugador que maximiza es el primer jugador (que juega con `"-"`) y el jugador que minimiza es el segundo jugador (que juega con `"|"`).

El tablero de juego se representara como una lista de listas, donde cada lista representa una fila del tablero. Los valores posibles para cada celda del tablero son `"-"`, `"|"`, `"+"` y `""`.

Adicionalmente, se definen:

`possible_moves(board, player, last_move=None)`: Función que recibe el tablero de juego, el jugador que debe realizar el siguiente movimiento y el ultimo movimiento realizado. Retorna una lista con los posibles movimientos que puede realizar el jugador de acuerdo a las reglas del juego.

`make_move(board, move, player, last_move=None)`: Función que recibe el tablero de juego, el movimiento a realizar, el jugador que realiza el movimiento y el ultimo movimiento realizado. Retorna el tablero de juego con el movimiento realizado. Si el movimiento no es valido, lanza una excepcion.

`is_terminal(board)`: Función que recibe el tablero de juego y retorna `True` si el tablero es un estado terminal, es decir, ya existe un ganador. Nótese que no es posible que exista un empate en este juego pues el estado donde se tiene un tablero lleno con solo `"+"` implica que ya existe un ganador.

`eval(board, current_player)`: Función que recibe el tablero de juego y el jugador que debe realizar el siguiente movimiento. Retorna un valor numerico que representa la evaluacion del tablero de juego para el jugador que debe realizar el siguiente movimiento.

```python
def eval(board, current_player):
    """
    Retorna el valor de evaluación para el tablero actual.

    Par este juego, el valor de la heuristica es 1 si el jugador que hizo
    el ultimo movimiento gano, -1 si perdio y 0 si el juego continua.
    """

    # Si se tiene una linea de 3 "+" gano el jugador que hizo
    # el ultimo movimiento
    prev_player = MAX if current_player == MIN else MIN

    if is_terminal(board):
        return 1 if prev_player == MAX else -1

    return 0
```

Es importante mencionar que debido a que el uso de poda alfa-beta reduce el numero de estados explorados, el algoritmo minmax es capaz de explorar el arbol de estados hasta el punto de encontrar el estado terminal del juego, es por esto que la Función de evaluacion es sencilla y no requiere de una heuristica compleja.

Adicionalmente es bueno mencionar que antes de hacer la implementacion de minmax con poda alfa-beta, se probó una implementacion sin poda con una heuristica mas compleja, pero el tiempo de ejecucion era muy alto para profundidades maximas mayores a 7, por lo que se opto por la implementacion actual, que justamente es capaz de explorar el arbol de estados hasta el punto de encontrar el estado terminal del juego.

Finalmente, se implementa el algoritmo minmax con poda alfa-beta:

```python
def max_player(board, alpha, beta, last_move=None):
    """
    Algoritmo minimax para el jugador MAX.
    """

    if is_terminal(board):
        return eval(board, MAX), None, []

    moves = possible_moves(board, MAX, last_move)
    best_move = None
    best_score = float("-inf")
    best_boards = []

    for move in moves:
        new_board = make_move(board, move, MAX, last_move)
        score, min_move, min_boards = min_player(
            new_board, alpha, beta, move)

        if score > best_score:
            best_score = score
            best_move = move
            best_boards = min_boards

        alpha = max(alpha, best_score)
        if beta <= alpha:
            break

    return best_score, best_move, [make_move(board, best_move, MAX, last_move)] + best_boards


def min_player(board, alpha, beta, last_move=None):
    """
    Algoritmo minimax para el jugador MIN.
    """

    if is_terminal(board):
        return eval(board, MIN), None, []

    moves = possible_moves(board, MIN, last_move)
    best_move = None
    best_score = float("inf")
    best_boards = []

    for move in moves:
        new_board = make_move(board, move, MIN, last_move)
        score, max_move, max_boards = max_player(
            new_board, alpha, beta, move)

        if score < best_score:
            best_score = score
            best_move = move
            best_boards = max_boards

        beta = min(beta, best_score)
        if beta <= alpha:
            break

    return best_score, best_move, [make_move(board, best_move, MIN, last_move)] + best_boards


def minmax(board):
    """
    Algoritmo minimax para un tablero dado. Utilizando poda alfa-beta.
    """

    alpha = float("-inf")
    beta = float("inf")

    return max_player(board, alpha, beta, None)
```

Utilizando esta implementacion, invocamos:

```python
INITIAL_BOARD = [["", "", ""], ["", "", ""], ["", "", ""]]

score, _, _ = minmax(INITIAL_BOARD)

print(f"Score: {score}")
```

Luego de ejecutar el algoritmo (~7 segundos de tiempo de ejecución), se observa que el score máximo para el jugador que maximiza es `-1`, lo que indica que si ambos jugadores juegan de manera óptima, el jugador que minimiza siempre ganará.

Finalmente, efectivamente existe una estrategia ganadora para alguno de los jugadores involucrados. En concreto, si ambos jugadores juegan de manera óptima, el jugador que juega `"|"` siempre ganará.

Q.E.D.
