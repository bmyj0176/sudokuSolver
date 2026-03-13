import utilities.read_algorithms as helper
import utilities.calculate as calculate
import interface

def main(board, write=True):
    if board.count(0) == 81:
        if write: 
            print(f"Your board is completely empty!")
        return False
    for array_index in range(9):
        row = helper.read_row(board, array_index)
        row = [n for n in row if n != 0] # remove zeros
        if len(row) != len(set(row)):
            if write: 
                interface.print_board(board, rowPointer=array_index)
                print(f"Duplicate detected in Row {array_index+1}")
            return False
        col = helper.read_col(board, array_index)
        col = [n for n in col if n != 0] # remove zeros
        if len(col) != len(set(col)):
            if write: 
                interface.print_board(board, colPointer=array_index)
                print(f"Duplicate detected in Column {array_index+1}")
            return False
        subgrid = helper.read_subgrid(board, array_index)
        subgrid = [n for n in subgrid if n != 0] # remove zeros
        if len(subgrid) != len(set(subgrid)):
            if write: 
                rowPointer = (array_index//3)*3+1
                colPointer = (array_index%3)*3+1
                interface.print_board(board, rowPointer=rowPointer, colPointer=colPointer)
                print(f"Duplicate detected in Subgrid {array_index+1}")
            return False
    return True

'''def main(board, mode):
    print()
    dupeRow = dupeCol = dupeSubgrid = 0
    for n in range(9):   
        if not dupeRow:     dupeRow = duplicate_check(n, helper.read_row(board, n))  
        if not dupeCol:     dupeCol = duplicate_check(n, helper.read_col(board, n))  
        if not dupeSubgrid: dupeSubgrid = duplicate_check(n, helper.read_subgrid(board, n))
    if dupeRow or dupeCol or dupeSubgrid:
        if dupeRow: 
            interface.print_board(board, dupeRow, -1)    
            print(f"Duplicate detected in Row {dupeRow+1}")   
        if dupeCol:   
            interface.print_board(board, -1, dupeCol)
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