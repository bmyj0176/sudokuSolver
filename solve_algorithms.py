import mode.solver as solve

# When there's only one note in a cell
def obvious_singles(board, note_board):
    for index in range(81):
        if len(note_board[index]) == 1:
            solve.solution_detected("Obvious Singles", note_board[index][0], index, board, note_board)
    return