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
            digit_appearances = [[] for _ in range(9)] # each list for each digit, containing 0-8 being array index
            for n in range(9):
                notes_in_cell = notes_in_array[n]
                for note in notes_in_cell:
                    digit_counts[note-1] += 1
                    digit_appearances[note-1].append(n)
            dupe_appearances_list, dupe_appearances_count = readAlg.find_duplicates_w_count(digit_appearances)
            if dupe_appearances_list: # dupes found

                for dupe_index in range(len(dupe_appearances_list)): # for each dupe occurrence [1,2] then [1,3,4]...
                    masked_digits = []
                    if len(dupe_appearances_list[dupe_index]) == 2 and dupe_appearances_count[dupe_index] == 2: # if only hidden pairs
                        for n in range(9): # for every digit
                            if dupe_appearances_list[dupe_index] == digit_appearances[n]: # if dupe in (non-dupe) list
                                masked_digits.append(n+1)
                        for n in dupe_appearances_list[dupe_index]: # for every cell containing hidden pair
                            for note in list(notes_in_array[n]): # list() makes copy so modification wont cause note skipping so its systematic
                                if note not in masked_digits:
                                    solve.solution_detected("Hidden Pairs", note, indexes_in_array[n], board, note_board)
                

                    
    return

def hidden_triples():
    return

def pointing_pairs_triples():
    return