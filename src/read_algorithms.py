def read_row(board, row):
    output_list = []
    for n in range(9):
        output_list.append(board[row*9+n])
    return output_list

def read_col(board, col):
    output_list = []
    for n in range(9):
        output_list.append(board[n*9+col])
    return output_list

def read_subgrid(board, subgrid_index):
    output_list = []
    subgrid_row = subgrid_index // 3
    subgrid_col = subgrid_index % 3
    selected_index = subgrid_row * 27 + subgrid_col * 3 # first index in subgrid
    for r0 in range(3): # each row in subgrid
        for c0 in range(3): # each column in subgrid 
            output_list.append(board[selected_index+c0+r0*9])
    return output_list

def list_row_indexes(row):
    return list(range(row*9, row*9+9))

def list_col_indexes(col):
    return [col + 9 * row for row in range(9)]

def list_subgrid_indexes(subgrid):
    output_list = []
    subgrid_row = subgrid // 3
    subgrid_col = subgrid % 3
    selected_index = subgrid_row * 27 + subgrid_col * 3
    for r0 in range(3): # each row in subgrid
        for c0 in range(3): # each column in subgrid 
            output_list.append(selected_index+c0+r0*9)
    return output_list