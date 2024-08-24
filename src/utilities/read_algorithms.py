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

def find_duplicates(input_list):
    checked = set()
    duplicate = set()
    for item in input_list:
        if isinstance(item, list): item = tuple(sorted(item))  # sort list and convert to tuple
        if item in checked:
            duplicate.add(item)
        else:
            checked.add(item)
    if duplicate:
        if isinstance(next(iter(duplicate)), tuple): 
            return [list(d) for d in duplicate]  # convert tuples back to lists
        else: 
            return list(duplicate)
    
def find_duplicates_w_count(input_list):
    checked = {}
    duplicates = []
    duplicate_count = []
    
    for item in input_list:
        # Sort lists and convert to tuples if necessary
        if isinstance(item, list): 
            item = tuple(sorted(item))
        
        # Track occurrences of each item
        if item in checked:
            checked[item] += 1
        else:
            checked[item] = 1
    
    # Identify duplicates and their counts
    for item, count in checked.items():
        if count > 1:
            duplicates.append(item)
            duplicate_count.append(count)
    
    # Convert tuples back to lists if necessary
    if duplicates and isinstance(duplicates[0], tuple):
        duplicates = [list(d) for d in duplicates]
    
    return duplicates, duplicate_count


