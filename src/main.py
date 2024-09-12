import modes.insertion
import verification
import modes.solver as solver_mode
import modes.completion as completion_mode
import utilities.read_algorithms as readAlg

mode = 'Menu'

def main(board = [0 for _ in range(81)], note_board = [[] for _ in range(81)]):
    global mode
    while True:
        if mode == 'Menu':
            mode = menu.main(board)
        if mode == 'Insertion': 
            mode = insertion_mode.main(board, mode)
        if mode == 'Solver':
            mode = solver_mode.main(board, note_board, mode)
        if mode == 'Completion':
            mode = completion_mode.main(board, mode)

if __name__ == "__main__":
    solved_board = [0 for _ in range(81)]
    note_board = [[] for _ in range(81)]
    main(solved_board, note_board)