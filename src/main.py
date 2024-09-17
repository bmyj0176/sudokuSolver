import modes.completion as completion
import modes.insertion as insertion
import modes.menu as menu
import modes.preset as preset
import modes.solver as solver

mode = 'Menu'

def main(board, note_board):
    global mode
    while True:
        if mode == 'Completion':
            mode = completion.main(board, note_board)
        if mode == 'Insertion': 
            mode = insertion.main(board, note_board)
        if mode == 'Menu':
            mode = menu.main(board, note_board)
        if mode == 'Preset':
            mode = preset.main(board, note_board)
        if mode == 'Solver':
            mode = solver.main(board, note_board)


if __name__ == "__main__":
    solved_board = [0 for _ in range(81)]
    note_board = [[] for _ in range(81)]
    main(solved_board, note_board)