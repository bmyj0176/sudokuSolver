import noter
import solve_algorithms as solve
import interface
import calculate

def main(board, note_board, mode):
    global skipNotesMode
    global quickSolveMode
    skipNotesMode = False
    quickSolveMode = False
    inputValue = -1
    while inputValue in [-1, '1', '2']:
        print(f"\n→ Enter 1 to toggle note-related solves. Currently {skipNotesMode}")
        print(f"→ Enter 2 to toggle straight to the final solution. Currently {quickSolveMode}")
        inputValue = input("Continue? ")
        if inputValue == '1': skipNotesMode = not skipNotesMode
        if inputValue == '2': quickSolveMode = not quickSolveMode

    fill_empty_cells_w_all_notes(board, note_board) # completely fill all non-empty cells with notes
    for index in range(81):
        noter.cell_scan(board, note_board, index) # cleans up all cells' notes
    
    while(0 in board):
        solve.obvious_singles(board, note_board)
    
    mode = 'Completion'
    return mode

def solution_detected(technique, number, index, board, note_board):
    noteRemovalTechniques = []
    # numberInsertionTechniques = ["Obvious Singles"]
    if technique in noteRemovalTechniques: 
        if not skipNotesMode and not quickSolveMode:
            print()
            interface.print_note_board(note_board, calculate.index_to_row(index), calculate.index_to_col(index))
            input(f"({technique}) Remove note {number} from this cell. ")
        noter.remove_note(note_board, index, number)
        if not skipNotesMode and not quickSolveMode:
            print()
            interface.print_note_board(note_board, calculate.index_to_row(index), calculate.index_to_col(index))
            input(f"Your notes should look like this afterwards. ")
    else: # numberInsertionTechniques
        if not quickSolveMode:
            print()
            interface.print_board_hinted(board, calculate.index_to_row(index), calculate.index_to_col(index))
            input(f"({technique}) Insert {number} into this cell. Then, remove notes accordingly. ")
        board[index] = number
        noter.cell_scan(board, note_board, index)
        if not quickSolveMode:
            print()
            interface.print_board_hinted(board, calculate.index_to_row(index), calculate.index_to_col(index))
            input(f"Your board should look like this afterwards. ")
            
        
def fill_empty_cells_w_all_notes(board, note_board):
    for index in range(81):
        if not board[index]: # if 0
            note_board[index] = list(range(1, 10))