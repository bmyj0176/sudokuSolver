import modes.insertion as insertion_mode
import modes.verification as verification_mode
import modes.solver as solver_mode
import modes.completion as completion_mode
import utilities.read_algorithms as readAlg

mode = 'Insertion'

def main(solved_board, note_board):
    global mode
    while True:
        if mode == 'Insertion': 
            print("[sudokuSolver] Entered Insertion Mode")
            mode = insertion_mode.main(solved_board, mode)
        if mode == 'Verification':
            print("[sudokuSolver] Entered Verification Mode")
            mode = verification_mode.main(solved_board, mode)
        if mode == 'Solver':
            print("[sudokuSolver] Entered Solver Mode")
            mode = solver_mode.main(solved_board, note_board, mode)
        if mode == 'Completion':
            mode = completion_mode.main(solved_board, mode)

if __name__ == "__main__":
    solved_board = [0 for _ in range(81)]
    note_board = [[] for _ in range(81)]
    main(solved_board, note_board)