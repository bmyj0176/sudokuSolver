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
            print("[4] Clear Board")
            print("[5] Save & Exit Editing")
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
                        errorMessage, index, insertValue = process_rowcol_insert_input(inputString)
                        if not errorMessage:
                            board[index] = insertValue
                            note.cell_scan(board, note_board, index)
            elif selection == '3': # Quick Insert by Entire Row (eg. 8..6...1.)
                errorMessage = None
                row = 0
                while row < 9:
                    while True:
                        print()
                        interface.print_board(board, rowPointer=row)
                        if errorMessage: 
                            print(f"\n{errorMessage}")
                            errorMessage = None
                        else:
                            print("\n(Example Input: 8..6...1.)")
                        print("[/] Previous row [Enter] Next row")
                        inputString = input("Enter: ")
                        if inputString == '/':
                            row -= 1
                            if row == -1: row = 0
                        elif inputString == '' or inputString == ' ':
                            break
                        else:
                            errorMessage, rowToBeInserted = process_row_insertion_input(inputString)
                            if not errorMessage:
                                for num in range(9):
                                    index = readAlg.list_row_indexes(row)[num]
                                    board[index] = rowToBeInserted[num]
                                    note.cell_scan(board, note_board, index)
                                break
                    row += 1
            elif selection == '4': # Clear Board
                while True:
                    confirmation = input("Are you sure you want to clear your board?\n[Enter] to Proceed, [0] to Return\nSelect: ")
                    if confirmation == '' or confirmation == ' ':
                        board.clear()
                        board.extend([0 for _ in range(81)])
                        note_board.clear()
                        note_board.extend([[] for _ in range(81)])
                        break
                    elif confirmation == "0":
                        break
            elif selection == '5': # Save & Exit Editing
                if all(not notes_in_cell for notes_in_cell in note_board): # completely empty note board
                    note.initiate_note_board(board, note_board)
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
                errorMessage = None
                while True:  
                    print()
                    interface.print_note_board(board, note_board, displayAllPointers=True)
                    if errorMessage: 
                        print(f"\n{errorMessage}")
                        errorMessage = None
                    else:
                        print("\n(Select a cell. Example: 2F, 5D)")
                    print("[Enter] to return to editing menu")
                    inputString = input("Enter: ")
                    if inputString == '' or inputString == ' ':
                        break
                    else:
                        errorMessage, index = process_rowcol_input(inputString)
                        if not errorMessage:
                            print("Cell Selected.")
                            responseMessage = None
                            while True:
                                interface.print_note_board(board, note_board, calculate.index_to_row(index), calculate.index_to_col(index))
                                print("\n[Enter] to return to editing menu")
                                if responseMessage:
                                    print(f"{responseMessage}")
                                    responseMessage = None
                                else:
                                    print("Insert value between 1-9 to toggle note.")
                                inputValue = input("Enter: ")
                                if inputValue == '' or inputValue == ' ':
                                    break
                                else:
                                    try:
                                        inputValue = int(inputValue)
                                    except ValueError:
                                        responseMessage = f"Invalid Input: \"{inputValue}\"\nYou have to insert value between 1-9 to toggle note."
                                    if not responseMessage:
                                        if 1 <= inputValue <= 9:
                                            responseMessage = f"Successfully Toggled.\nInsert value between 1-9 to toggle note."
                                            if inputValue in note_board[index]:
                                                note.remove_note(note_board, index, inputValue)
                                            else:
                                                note.insert_note(note_board, index, inputValue)
                                        elif inputValue < 1:
                                            responseMessage = f"Value too small: \"{inputValue}\"\nYou have to insert value between 1-9 to toggle note."
                                        elif inputValue > 9:
                                            responseMessage = f"Value too large: \"{inputValue}\"\nYou have to insert value between 1-9 to toggle note."

            elif selection == '3': # Clean & Initialize All Notes
                note.initiate_note_board(board, note_board)
            elif selection == '4': # Save & Exit Editing
                if all(not notes_in_cell for notes_in_cell in note_board): # completely empty note board
                    note.initiate_note_board(board, note_board)
                return 'Menu'

def process_rowcol_insert_input(string):
    alphabetFilter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J']
    numFilter = list(map(str, range(1, 10)))
    alphabetList = []
    numList = []
    insertNumList = []
    spaced = False
    for char in string:
        if spaced == False:
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
        for _ in range(9-len(string)):
            string.append(0)
    return None, [int(char) for char in string[:9]] # errorMessage, rowToBeInserted

def process_rowcol_input(string):
    alphabetFilter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J']
    numFilter = list(map(str, range(1, 10)))
    alphabetList = []
    numList = []
    for char in string:
        if char.upper() in alphabetFilter: # row
            alphabetList.append(char.upper())
        elif char in numFilter: # col
            numList.append(char)
    if len(alphabetList) != 1: 
        return f"Invalid Row: \"{string}\"\n(Use A-J only, Example: 2F, 5D)", None
    if len(numList) != 1: 
        return f"Invalid Column: \"{string}\"\n(Use 1-9 only, Example: 2F, 5D)", None
    for alphabet_index in range(9):
        if alphabetList[0] == alphabetFilter[alphabet_index]:
            row = alphabet_index
        col = int(numList[0])-1
    return None, row*9+col # errorMessage, index

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