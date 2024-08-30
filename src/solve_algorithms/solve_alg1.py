import modes.solver as solve
import itertools
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
            return True
    return False

def naked_pairs():
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

            for combo in itertools.combinations(notes_in_array, 2): # check all combi of 3
                combined_double = list(set(itertools.chain(*combo)))  # Merge lists and remove duplicates
                if len(combined_double) == 2 and all(len(x) >= 2 for x in combo): # double detected
                    for n in range(9): # each note in array
                        if not all(notes in combined_double for notes in notes_in_array[n]): 
                            for filter_value in combined_double:
                                if filter_value in notes_in_array[n]:
                                    solve.solution_detected("Naked Pairs", filter_value, indexes_in_array[n], board, note_board)
                                    return True
    return False

def naked_triples():
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

            for combo in itertools.combinations(notes_in_array, 3): # check all combi of 3
                combined_triple = sorted(set(itertools.chain(*combo)))  # Merge lists and remove duplicates
                if len(combined_triple) == 3 and all(len(x) >= 2 for x in combo): # triple detected
                    for n in range(9): # each note in array
                        if not all(notes in combined_triple for notes in notes_in_array[n]): 
                            for filter_value in combined_triple:
                                if filter_value in notes_in_array[n]:
                                    solve.solution_detected("Naked Triples", filter_value, indexes_in_array[n], board, note_board)
                                    return True
    return False

def naked_quads(): # WIP # WIP # WIP # WIP # WIP # WIP # WIP # WIP # WIP # WIP # WIP # WIP # WIP # WIP # WIP # WIP # WIP # WIP
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
                
            for combo in itertools.combinations(notes_in_array, 4): # check all combi of 3
                combined_triple = list(set(itertools.chain(*combo)))  # Merge lists and remove duplicates
                if len(combined_triple) == 4 and all(len(x) >= 2 for x in combo): # quad detected
                    for n in range(9): # each note in array
                        if not all(notes in combined_triple for notes in notes_in_array[n]): 
                            for filter_value in combined_triple:
                                if filter_value in notes_in_array[n]:
                                    solve.solution_detected("Naked Triples", filter_value, indexes_in_array[n], board, note_board)
                                    return True
    return False