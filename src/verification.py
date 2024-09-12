import utilities.read_algorithms as readAlg
import interface
import time

def main(board, write=True):
    for array in range(9):
        if readAlg.read_row(board, array) != list(set(readAlg.read_row(board, array))):
            if write: 
                interface.print_board_hinted(board, array, -1)
                print(f"Duplicate detected in Row {array+1}")
            return False
        if readAlg.read_col(board, array) != list(set(readAlg.read_col(board, array))):
            if write: 
                interface.print_board_hinted(board, -1, array)
                print(f"Duplicate detected in Column {array+1}")
            return False
        if readAlg.read_row(board, array) != list(set(readAlg.read_row(board, array))):
            if write: 
                interface.print_board(board)
                print(f"Duplicate detected in Subgrid {array+1}")
            return False
    return True

'''def main(board, mode):
    print()
    dupeRow = dupeCol = dupeSubgrid = 0
    for n in range(9):   
        if not dupeRow:     dupeRow = duplicate_check(n, readAlg.read_row(board, n))  
        if not dupeCol:     dupeCol = duplicate_check(n, readAlg.read_col(board, n))  
        if not dupeSubgrid: dupeSubgrid = duplicate_check(n, readAlg.read_subgrid(board, n))
    if dupeRow or dupeCol or dupeSubgrid:
        if dupeRow: 
            interface.print_board_hinted(board, dupeRow, -1)    
            print(f"Duplicate detected in Row {dupeRow+1}")   
        if dupeCol:   
            interface.print_board_hinted(board, -1, dupeCol)
            print(f"Duplicate detected in Column {dupeCol+1}")      
        if dupeSubgrid:
            interface.print_board(board)           
            print(f"Duplicate detected in Subgrid {dupeSubgrid+1}")            
        print("Verification Failed. Returning to Insertion Mode...\n")
        mode = 'Insertion' 
        time.sleep(1.5)
    else:
        print("Verification Success. Going to Solver Mode...\n")
        mode = 'Solver' 
        time.sleep(1.5)
    return mode

def duplicate_check(return_index, list):
    registered_items = []
    for n in range(9):
        if list[n] != 0 and list[n] in registered_items:
            print("hi")
            return return_index
        else:
            registered_items.append(list[n])
    return 0'''