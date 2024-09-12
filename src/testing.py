import modes.preset as preset

board = [0 for _ in range(81)]
note_board = [[] for _ in range(81)]

board[47] = 7
board[13] = 1

preset.write(["Sex", board, note_board], 1)
preset.main(board, note_board)