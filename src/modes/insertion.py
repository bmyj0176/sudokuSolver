import interface
import note_manager as note
import utilities.calculate as calculate
import utilities.read_algorithms as readAlg

insertionHistory = []

def main(board, note_board):
    noteboardInsertion = False
    while True:
        if not noteboardInsertion:
            interface.print_board(board)
            print("[1] Switch to Note Board Editing")
            print("[2] Insert Number by Row/Col Index (eg. 2F, 3D)")
            print("[3] Quick Insert by Entire Row (eg. 8..6...1.)")
            print("[4] Save & Exit Editing")
            selection = input("Select: ")
            if selection == '1': # Switch to Note Board Editing
                noteboardInsertion = not noteboardInsertion
            elif selection == '2': # Insert Number by Row/Col Index (eg. 2F, 3D)
                errorMessage = None
                while True:  
                    print()
                    interface.print_board(board, displayAllPointers=True)
                    if errorMessage: 
                        print(f"\n{errorMessage}")
                        errorMessage = None
                    else:
                        print("\n(Example Input: 2f 3)")
                    print("[Enter] to return to editing menu")
                    inputString = input("Enter: ")
                    if inputString == '' or inputString == ' ':
                        break
                    else:
                        errorMessage, index, insertValue = process_rowcol_input(inputString)
                        if not errorMessage:
                            board[index] = insertValue
                            note.cell_scan(board, note_board, index)
            elif selection == '3': # Quick Insert by Entire Row (eg. 8..6...1.)
                errorMessage = None
                for row in range(9):
                    while True:
                        print()
                        interface.print_board(board, rowPointer=row)
                        if errorMessage: 
                            print(f"\n{errorMessage}")
                            errorMessage = None
                        else:
                            print("\n(Example Input: 8..6...1.)")
                        print("[Enter] to skip to next row")
                        inputString = input("Enter: ")
                        if inputString == '' or inputString == ' ':
                            break
                        else:
                            errorMessage, rowToBeInserted = process_row_insertion_input(inputString)
                            if not errorMessage:
                                for num in range(9):
                                    index = readAlg.list_row_indexes(row)[num]
                                    board[index] = rowToBeInserted[num]
                                    note.cell_scan(board, note_board, index)
            elif selection == '4': # Save & Exit Editing
                return 'Menu'
        else: # noteboardInsertion
            interface.print_note_board(board, note_board)
            print("[1] Switch to Board Editing")
            print("[2] Edit & Toggle Note by Cell")
            print("[3] Clean & Initialize All Notes")
            print("[4] Save & Exit Editing")
            selection = input("Select: ")
            if selection == '1': # Switch to Board Editing
                noteboardInsertion = not noteboardInsertion
            elif selection == '2': # Edit & Toggle Note by Cell
                while True:
                    pass # STOPPED OFF HERE# STOPPED OFF HERE# STOPPED OFF HERE# STOPPED OFF HERE# STOPPED OFF HERE# STOPPED OFF HERE# STOPPED OFF HERE
            elif selection == '3': # Clean & Initialize All Notes
                note.initiate_note_board(board, note_board)
            elif selection == '4': # Save & Exit Editing
                return 'Menu'

def process_rowcol_input(string):
    alphabetFilter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J']
    numFilter = list(map(str, range(1, 10)))
    alphabetList = []
    numList = []
    insertNumList = []
    spaced = False
    for char in string:
        if spaced == False:
            #print(f"elif char in numFilter:")
            #print(f"elif {char} in {numFilter}:")
            if char.upper() in alphabetFilter: # row
                alphabetList.append(char.upper())
            elif char in numFilter: # col
                numList.append(char)
            elif char == ' ' or char == ',': # spacing
                spaced = True
        else: # spaced == True 
            if char in numFilter or char == '0':
                insertNumList.append(char)
    if len(alphabetList) != 1: 
        return f"Invalid Row: \"{string}\"\n(Use A-J only, Example Input: 2f 3)", None, None
    if len(numList) != 1: 
        return f"Invalid Column: \"{string}\"\n(Use 1-9 only, Example Input: 2f 3)", None, None
    if spaced == False:
        return f"No Spacing Detected: \"{string}\"\n(Use spacing or comma only, Example Input: 2f 3 or 2f,3)", None, None
    if len(insertNumList) != 1: 
        return f"Invalid Number to be Inserted: \"{string}\"\n(Insert 1-9 or Delete using 0, Example Input: 2f 3)", None, None
    for alphabet_index in range(9):
        if alphabetList[0] == alphabetFilter[alphabet_index]:
            row = alphabet_index
        col = int(numList[0])-1
    return None, row*9+col, int(insertNumList[0]) # errorMessage, index, insertValue

def process_row_insertion_input(string):
    string = [char for char in string if char != " "] # remove spaces
    for char_index in range(len(string)):
        if string[char_index] == '.':
            string[char_index] = '0'
    filterList = list(map(str, range(0, 10)))
    for char_index in range(len(string)):
        if string[char_index] not in filterList and char_index <= 8:
            return f"Invalid Character Detected in List: \"{string}\"\n(Only use . or 0 for empty cells, Example Input: 8..6...1.)", None
        if string[char_index] in filterList and char_index >= 9:
            return f"List is too long: \"{string}\"\n(List must only be 9 characters long, Example Input: 8..6...1.)", None
    if len(string) <= 8:
        return f"List is too short: \"{string}\"\n(List has to be 9 characters long, Example Input: 8..6...1.)", None
    return None, [int(char) for char in string[:9]] # errorMessage, rowToBeInserted

board = [
    8, 0, 0, 6, 0, 0, 0, 1, 0,
    0, 2, 7, 0, 0, 0, 0, 9, 0,
    0, 0, 0, 5, 4, 0, 0, 0, 2,
    0, 0, 0, 0, 0, 5, 9, 0, 0,
    6, 0, 1, 0, 2, 0, 0, 0, 0,
    0, 4, 0, 7, 0, 0, 0, 0, 0,
    0, 0, 0, 1, 0, 0, 0, 6, 0,
    4, 0, 0, 0, 9, 0, 0, 8, 0,
    0, 0, 6, 0, 0, 0, 7, 0, 0,
]


note_board = [[] for _ in range(81)]
import note_manager
note_manager.initiate_note_board(board, note_board)
main(board, note_board)
while True: pass