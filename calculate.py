def rowcol_to_index(row, col): # from row 0-8, column 0-8
    return (row)*9 + col

def index_to_row(index):
    return index // 9

def index_to_col(index):
    return index % 9

def index_to_subgrid(index):
    row = index_to_row(index)
    col = index_to_col(index)
    return row // 3 * 3 + col // 3