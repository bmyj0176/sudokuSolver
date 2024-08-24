import modes.solver as solve
import utilities.read_algorithms as readAlg

def import_boards(imported_board, imported_note_board):
    global board
    board = imported_board
    global note_board
    note_board = imported_note_board

# 4. Hidden Singles
#    When there is only a single occurrence in note of a number in a row/col/subgrid
# 5. Hidden Pairs
#    ?
# 6. Hidden Triples
#    ?
# 7. Pointing Pairs/Triples
#    ?

def hidden_singles():
    for array_type in range(3): # 0=row, 1=col, 2=subgrid
        for array in range(9): # for every array
            if array_type == 0:
                notes_in_array = readAlg.read_row(note_board, array)  
                indexes_in_array = readAlg.list_row_indexes(array) 
            elif array_type == 1:
                notes_in_array = readAlg.read_col(note_board, array) 
                indexes_in_array = readAlg.list_col_indexes(array) 
            else: # array_type == 2
                notes_in_array = readAlg.read_subgrid(note_board, array)
                indexes_in_array = readAlg.list_subgrid_indexes(array) 
            digit_counts = [0] * 9
            for notes_in_cell in notes_in_array:
                for note in notes_in_cell:
                    digit_counts[note-1] += 1
            for digit in range(9):
                if digit_counts[digit] == 1:
                    for n in range(9): # find index of singular digit
                        if digit+1 in notes_in_array[n]: digit_index = indexes_in_array[n]
                    solve.solution_detected("Hidden Singles", digit+1, digit_index, board, note_board)
    return

def hidden_pairs():
    return

def hidden_triples():
    return

def pointing_pairs_triples():
    return