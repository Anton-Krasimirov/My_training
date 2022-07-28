'''стойностите за ляв и десен диагонал , които се получават от (row - col) и (row + col) не са
ясни как работят , но така са ми подадени и работят'''
def print_board(board):
    for row in board:
        print(' '.join(row))
    print()


def can_place_queen(row, col, rows, cols, left_diag, right_diag):
    if row in rows:
        return False
    if col in cols:
        return False
    if (row - col) in left_diag:
        return False
    if (row + col) in right_diag:
        return False
    return True


def set_queen(row, col, board, rows, cols, left_diag, right_diag):
    board[row][col] = '*'
    rows.add(row)
    cols.add(col)
    left_diag.add(row - col)
    right_diag.add((row + col))


def remove_queen(row, col, board, rows, cols, left_diag, right_diag):
    board[row][col] = '-'
    rows.remove(row)
    cols.remove(col)
    left_diag.remove(row - col)
    right_diag.remove((row + col))


def put_queen(row, board, rows, cols, left_diag, right_diag):
    if row == 8:
        print_board(board)
        return
    for col in range(8):
        if can_place_queen(row, col, rows, cols, left_diag, right_diag):
            set_queen(row, col, board, rows, cols, left_diag, right_diag)
            put_queen(row + 1, board, rows, cols, left_diag, right_diag)
            remove_queen(row, col, board, rows, cols, left_diag, right_diag)


n = 8
board = []
[board.append(['-'] * n) for _ in range(8)]# добавяне на 8 листа от по 8 тирета на дъската

put_queen(0, board, set(), set(), set(), set())