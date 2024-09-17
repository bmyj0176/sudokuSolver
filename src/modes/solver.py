import note_manager as note
import solve_algorithms.solve_alg_main as solve
import interface
import utilities.calculate as calculate
import sys

def main(board, note_board, mode):
    global skipNotesMode
    global quickSolveMode
    skipNotesMode = False
    quickSolveMode = False
    inputValue = -1
    while inputValue in [-1, '1', '2']:
        print(f"\n→ Enter 1 to toggle hide note-related solves. Currently {skipNotesMode}")
        print(f"→ Enter 2 to toggle skip straight to the final solution. Currently {quickSolveMode}")
        inputValue = input("Continue? ")
        if inputValue == '1': skipNotesMode = not skipNotesMode
        if inputValue == '2': quickSolveMode = not quickSolveMode
    
    solve.import_boards(board, note_board)
    global check_fail
    while(0 in board):
        solved = False
        check_fail = True
        if not solved: solved = solve.naked_singles()
        if not solved: solved = solve.naked_pairs()
        if not solved: solved = solve.naked_triples()
        if not solved: solved = solve.naked_quads()
        if not solved: solved = solve.hidden_singles()
        if not solved: solved = solve.hidden_pairs()
        if check_fail:
            print()
            interface.print_board(board)
            print("sudokuSolver has failed to find any further solutions.")
            while True:
                print("1 - Display Board")
                print("2 - Display Notes")
                print("3 - Exit to Insertion Mode")
                selectionInput = input("Input: ")
                if selectionInput == "1": interface.print_board(board)
                elif selectionInput == "2": interface.print_note_board(note_board, -1, -1)
                elif selectionInput == "3": 
                    mode = 'Insertion'
                    return mode
                else: print("Invalid Input!")
    mode = 'Completion'
    return mode

def solution_detected(technique, number, index, board, note_board):
    global check_fail
    check_fail = False
    noteRemovalTechniques = ["Naked Pairs", "Naked Triples", "Naked Quads", "Naked Quintuples", "Hidden Pairs"]
    # numberInsertionTechniques = ["Naked Singles", "Hidden Singles"]
    if technique in noteRemovalTechniques: 
        if not skipNotesMode and not quickSolveMode:
            print()
            interface.print_note_board(note_board, calculate.index_to_row(index), calculate.index_to_col(index))
            input(f"({technique}) Remove note {number} from this cell. ")
        note.remove_note(note_board, index, number)
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
        note.cell_scan(board, note_board, index)
        if not quickSolveMode:
            print()
            interface.print_board_hinted(board, calculate.index_to_row(index), calculate.index_to_col(index))
            input(f"Your board should look like this afterwards. ")
    return