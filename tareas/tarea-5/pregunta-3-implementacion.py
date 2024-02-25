from copy import deepcopy

MAX = "-"
MIN = "|"
BOTH = "+"


INITIAL_BOARD = [["", "", ""], ["", "", ""], ["", "", ""]]


def print_board(board):
    """
    Imprime el tablero en consola
    """

    for i in range(3):
        row = ""

        for j in range(3):
            if board[i][j] == "":
                row += " . "
            else:
                row += f" {board[i][j]} "

        print(row)
    print()


def possible_moves(board, player, last_move=None):
    """
    Retorna una lista con los posibles movimientos que puede hacer el jugador
    tomando en cuenta el estado actual del tablero y el ultimo movimiento
    realizado.
    """

    moves = []

    for i in range(3):
        for j in range(3):
            if last_move:
                if (i, j) == last_move:
                    continue

            if board[i][j] == "":
                moves.append((i, j))

            if player == MAX:
                if board[i][j] == MIN:
                    moves.append((i, j))

            if player == MIN:
                if board[i][j] == MAX:
                    moves.append((i, j))

    return moves


def make_move(board, move, player, last_move=None):
    """
    Retorna un nuevo tablero con el movimiento realizado por el jugador.

    Si el movimiento es invalido, se lanza una excepcion.
    """

    i, j = move
    new_board = deepcopy(board)

    if last_move:
        if (i, j) == last_move:
            raise Exception(f"Invalid move {move} for player {player}")

    if board[i][j] == "":
        new_board[i][j] = player
        return new_board

    if player == MAX:
        if board[i][j] == MIN:
            new_board[i][j] = BOTH
            return new_board

    if player == MIN:
        if board[i][j] == MAX:
            new_board[i][j] = BOTH
            return new_board

    raise Exception(f"Invalid move {move} for player {player}")


def is_terminal(board):
    """
    Retorna True si el tablero es un estado terminal, es decir, ya existe un
    ganador.

    Notese que no es posible que exista un empate en este juego pues
    el estado donde se tiene un tablero lleno con solo "+" implica que
    ya existe un ganador.
    """

    # Ganar por filas
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == BOTH:
            return True

    # Ganar por columnas
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == BOTH:
            return True

    # Ganar por diagonales
    if board[0][0] == board[1][1] == board[2][2] == BOTH:
        return True

    if board[0][2] == board[1][1] == board[2][0] == BOTH:
        return True

    return False


def eval(board, current_player):
    """
    Retorna el valor de la heuristica para el tablero actual.

    Par este juego, el valor de la heuristica es 1 si el jugador que hizo
    el ultimo movimiento gano, -1 si perdio y 0 si el juego continua.
    """

    # Si se tiene una linea de 3 "+" gano el jugador que hizo
    # el ultimo movimiento
    prev_player = MAX if current_player == MIN else MIN

    if is_terminal(board):
        return 1 if prev_player == MAX else -1

    return 0


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


score, best_move, boards = minmax(INITIAL_BOARD)

print(f"Score: {score}")
print("Chain: ")

for b in boards:
    print_board(b)
