from copy import deepcopy

MAX = "-"
MIN = "|"
BOTH = "+"


INITIAL_BOARD = [["", "", ""], ["", "", ""], ["", "", ""]]


def print_board(board):
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


def eval(board, player, last_move=None):
    """
    Evalua un tablero para un jugador dado utilizando la heuristica de
    contar el numero de potenciales lineas ganadoras que tiene el jugador
    en el tablero.

    Para cada linea sumando:
      Caso vacio:
      - 0 si la linea esta vacia

      Caso la linea tiene una posicion jugada:
      - 0 si la linea tiene una posicion jugada y dos vacias
      - 0 si la linea tiene dos posiciones jugada y una vacia
      - 1 si la linea tiene tres posiciones jugadas

      Caso la linea tiene posiciones BOTH y vacias:
      - 1 si la linea tiene una posicion BOTH y dos vacias
      - 2 si la linea tiene dos posiciones BOTH y una vacia

      Caso la linea tiene posiciones jugadas y BOTH:
      - -2 si la linea tiene una posicion BOTH y dos posiciones jugadas del jugador
      - 2 si la linea tiene una posicion BOTH y dos posiciones jugadas del contrario
      - 12 si la linea tiene dos posiciones BOTH y una posicion jugada del contrario
      - -12 si la linea tiene dos posiciones BOTH y una posicion jugada del jugador
    """
    score = 0

    line_pos = [
        # Filas
        ((i, 0), (i, 1), (i, 2)) for i in range(3)
    ] + [
        # Columnas
        ((0, j), (1, j), (2, j)) for j in range(3)
    ] + [
        # Diagonales
        ((0, 0), (1, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0))
    ]

    for line in line_pos:
        same = 0
        other = 0
        both = 0
        empty = 0

        for pos in line:
            i, j = pos
            if board[i][j] == player:
                same += 1
            elif board[i][j] == "":
                empty += 1
            elif board[i][j] == BOTH:
                both += 1
            else:
                other += 1

        # Caso vacio
        if empty == 3:
            score += 0

        # Caso la linea tiene una posicion jugada
        if empty == 2 and both == 0:
            score += 0

        if empty == 1 and both == 0:
            score += 0

        if empty == 0 and both == 0:
            score += 1

        # Caso la linea tiene posiciones BOTH y vacias
        if empty == 2 and both == 1:
            score += 1

        if empty == 1 and both == 2:
            score += 2

        # Caso la linea tiene posiciones jugadas y BOTH
        if both == 1 and same == 2:
            score += -2

        if both == 1 and other == 2:
            score += 2

        if both == 2 and other == 1:
            score += 12

        if both == 2 and same == 1:
            score += -12

    return score if player == MAX else -score


def max_player(board, last_move=None, depth=10):
    # Si el tablero es terminal, el jugador MIN gana
    if is_terminal(board):
        return -1000, None, []

    if depth == 0:
        return eval(board, MAX, last_move), None, []

    moves = possible_moves(board, MAX, last_move)
    best_move = None
    best_score = float("-inf")
    best_boards = []

    for move in moves:
        new_board = make_move(board, move, MAX, last_move)
        score, min_move, min_boards = min_player(new_board, move, depth - 1)

        if score > best_score:
            best_score = score
            best_move = move
            best_boards = min_boards

    return best_score, best_move, [make_move(board, best_move, MAX, last_move)] + best_boards


def min_player(board, last_move=None, depth=10):
    # Si el tablero es terminal, el jugador MAX gana
    if is_terminal(board):
        return 1000, None, []

    if depth == 0:
        return eval(board, MIN, last_move), None, []

    moves = possible_moves(board, MIN, last_move)
    best_move = None
    best_score = float("inf")
    best_boards = []

    for move in moves:
        new_board = make_move(board, move, MIN, last_move)
        score, max_move, max_boards = max_player(new_board, move, depth - 1)

        if score < best_score:
            best_score = score
            best_move = move
            best_boards = max_boards

    return best_score, best_move, [make_move(board, best_move, MIN, last_move)] + best_boards


def minmax(board, depth=7):
    return max_player(board, None, depth)


TEST_BOARD = [
    ["", "+", ""],
    ["|", "-", ""],
    ["-", "", "|"]
]

score, best_move, boards = minmax(TEST_BOARD, 12)

print(f"Score: {score}")
print("Chain: ")

for b in boards:
    print_board(b)
