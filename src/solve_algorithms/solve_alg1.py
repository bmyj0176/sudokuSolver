import modes.solver as solve
import utilities.read_algorithms as readAlg

def import_boards(imported_board, imported_note_board):
    global board
    board = imported_board
    global note_board
    note_board = imported_note_board

# 1. Obvious Singles
#    When there's only one note in a cell
# 2. Obvious Pairs
#    When there's two identical pairs of notes
# 3. Obvious Triples
#    When there's three pairs that consists of two occurrences of each note [1, 2] [2, 3] [1, 3]

def naked_singles():
    for index in range(81):
        if len(note_board[index]) == 1:
            solve.solution_detected("Naked Singles", note_board[index][0], index, board, note_board)
    return

def naked_pairs():
    for array_type in range(3): # 0=row, 1=col, 2=subgrid
        for array in range(9): # for every array
            saved_cell, saved_index = [], -1
            if array_type == 0:
                notes_in_array = readAlg.read_row(note_board, array) 
                indexes_in_array = readAlg.list_row_indexes(array) 
            elif array_type == 1:
                notes_in_array = readAlg.read_col(note_board, array) 
                indexes_in_array = readAlg.list_col_indexes(array) 
            else: # array_type == 2
                notes_in_array = readAlg.read_subgrid(note_board, array) 
                indexes_in_array = readAlg.list_subgrid_indexes(array) 
            for n in range(9): # for every cell in an array
                if len(notes_in_array[n]) == 2:
                    if not saved_cell:
                        saved_cell = notes_in_array[n]
                        saved_index = indexes_in_array[n]  
                    else:
                        if set(notes_in_array[n]) == set(saved_cell) and indexes_in_array[n] != saved_index: # pair found
                            for filter_value in saved_cell:
                                for n in range(9): # for every cell in a array
                                    if filter_value in notes_in_array[n] and set(notes_in_array[n]) != set(saved_cell):
                                        solve.solution_detected("Naked Pairs", filter_value, indexes_in_array[n], board, note_board)
                            saved_cell, saved_index = [], -1
    return

def naked_triples():
    for array_type in range(3): # 0=row, 1=col, 2=subgrid
        for array in range(9): # for every array
            saved_cell1, saved_index1 = [], -1
            saved_cell2, saved_index2 = [], -1
            saved_index3 = -1
            if array_type == 0:
                notes_in_array = readAlg.read_row(note_board, array) 
                indexes_in_array = readAlg.list_row_indexes(array) 
            elif array_type == 1:
                notes_in_array = readAlg.read_col(note_board, array) 
                indexes_in_array = readAlg.list_col_indexes(array) 
            else: # array_type == 2
                notes_in_array = readAlg.read_subgrid(note_board, array) 
                indexes_in_array = readAlg.list_subgrid_indexes(array) 
            for n in range(9): # for every cell in an array
                if len(notes_in_array[n]) == 2:
                    if not saved_cell1: # first pair
                        saved_cell1 = notes_in_array[n]
                        saved_index1 = indexes_in_array[n]
                    elif saved_cell1 and not saved_cell2: # 2nd pair
                        if indexes_in_array[n] != saved_index1 and set(notes_in_array[n]) != set(saved_cell1): # checks if different cell and not obvious pairs
                            if saved_cell1[0] in notes_in_array[n] or saved_cell1[1] in notes_in_array[n]: # checks if it contains one of the notes in saved_cell1
                                saved_cell2 = notes_in_array[n]
                                saved_index2 = indexes_in_array[n]
                    elif saved_cell2: # 3rd pair
                        thirdpair_template = list(set(saved_cell1+saved_cell2))
                        thirdpair_template.remove(readAlg.find_duplicates(saved_cell1+saved_cell2)[0])
                        thirdpair_template.sort()
                        if notes_in_array[n] == thirdpair_template: # 3rd pair is found
                            saved_index3 = indexes_in_array[n]
                            for filter_value in list(set(saved_cell1+saved_cell2)):
                                for n in range(9):
                                    if filter_value in notes_in_array[n] and indexes_in_array[n] not in [saved_index1, saved_index2, saved_index3]:
                                        solve.solution_detected("Naked Triples", filter_value, indexes_in_array[n], board, note_board)
                            saved_cell1, saved_index1 = [], -1
                            saved_cell2, saved_index2 = [], -1
                            saved_index3 = -1
    return