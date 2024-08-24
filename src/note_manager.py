import utilities.calculate as calculate
import utilities.read_algorithms as readAlg

def insert_note(note_board, index, note): # adds a single note at index
    if not note in note_board[index]:
        note_board[index].append(note)

def remove_note(note_board, index, note): # removes a single note at index
    if not note: # is 0
        note_board[index].clear()
    else:
        if note in note_board[index]:
            note_board[index].remove(note)

def clear_cell_notes(note_board, index):
    remove_note(note_board, index, 0)

def cell_scan(board, note_board, index): # checks for cell value, then scans its row, col, subgrid to clean notes
    value_at_index = board[index]
    if value_at_index: # between 1-9 ONLY, deny 0
        note_board[index] = [] # clears notes in occupied slot 
        for rowSlot in readAlg.list_row_indexes(calculate.index_to_row(index)): # for every slot in same row
            if value_at_index in note_board[rowSlot]:
                note_board[rowSlot].remove(value_at_index) # clean note
        for colSlot in readAlg.list_col_indexes(calculate.index_to_col(index)): # for every slot in same col
            if value_at_index in note_board[colSlot]:
                note_board[colSlot].remove(value_at_index) # clean note
        for subgridSlot in readAlg.list_subgrid_indexes(calculate.index_to_subgrid(index)): # for every slot in same subgrid
            if value_at_index in note_board[subgridSlot]:
                note_board[subgridSlot].remove(value_at_index) # clean note
    return