import interface
import calculate

insertionHistory = []

def main(board, mode):
    selectedRow, selectedCol = -1, -1
    while mode == 'Insertion':
        print()
        interface.print_board_hinted(board, selectedRow, selectedCol)
        if selectedRow == selectedCol == -1: # INSERT ROW
            print("[. to enter verify & start solving]")
            print("[/ to undo] Enter row number: ", end="")
            my_input = input_mode()
            if my_input == '/': 
                if insertionHistory: # if theres history to undo
                    extractedHistory = insertionHistory.pop() # [my_input, selectedRow, selectedCol]
                    board[calculate.rowcol_to_index(extractedHistory[1], extractedHistory[2])] = 0
                else:  
                    print("No history to undo.")
            elif my_input == '.':   mode = 'Verification'
            else:               selectedRow = int(my_input)
        elif selectedCol == -1: # INSERT COL
            print("[/ to undo] Enter col number: ", end="")
            my_input = input_mode()
            if my_input == '/': selectedRow = -1
            elif my_input == '.':   print("Invalid Input!")
            else:               selectedCol = int(my_input)
        else: # INSERT NUMBER
            print("[/ to undo] Insert number: ", end="")
            my_input = input_mode()
            if my_input == '/': selectedCol = -1
            elif my_input == '.':   print("Invalid Input!")
            else:               
                board[calculate.rowcol_to_index(selectedRow, selectedCol)] = int(my_input) + 1
                insertionHistory.append([my_input, selectedRow, selectedCol])
                selectedRow, selectedCol = -1, -1
    return mode

def input_mode():
    while True:
        my_input = input()
        if my_input.isdigit() and 0 <= int(my_input) <= 9:
            my_input = str(int(my_input)-1)
            break
        elif my_input in ('/', '.'):
            break
        else:
            print("Invalid Input: ", end="")
    return str(my_input)