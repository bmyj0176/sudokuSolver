import json
import interface

board = [0 for _ in range(81)]
note_board = [[] for _ in range(81)]

board[47] = 7
board[13] = 1

data = ["Test", board, note_board]
with open('preset_data.json', 'w') as file:
        json.dump(data, file, indent=4)

def main(board, note_board):
    page = 1
    maxPage = 10 # temporary
    showNoteboard = False
    invalidInput = False
    while True:
        if showNoteboard: interface.print_note_board(note_board)
        else:             interface.print_board(board)
        print(f"[{page} / x] {read()[page-1]["Preset"]}")
        print(f"[1] < Previous || Next > [2]")
        if showNoteboard: print(f"[3] Show Note Board")
        else:             print(f"[3] Show Board")
        print(f"[4] Load Preset")
        print(f"[5] Rename Preset")
        print(f"[6] Delete Preset")
        print(f"[7] Save Current Board as New Preset")
        print(f"[8] Return to Menu")
        if invalidInput: print("[Invalid Input!] ", end="")
        selection = input("Select: ")
        if selection == '1': # Previous
            page -= 1
            if page == 0: page = maxPage
        if selection == '2': # Next
            page += 1
            if page == maxPage+1: page = 1
        if selection == '3': # 
            showNoteboard = not showNoteboard
        if selection == '4':
            board = read[page-1]["board"]
            note_board = read[page-1]["note_board"]
        if selection == '5':
            write(input("Rename to: "), page, "Preset")
        if selection == '6':
            read().pop(page-1)
        if selection == '7':
            interface.print_board(board)
            presetName = input("Insert New Preset Name: ")
            entry = [presetName, board, note_board]
            write(entry, maxPage+1)
        if selection == '8':
            return "Menu"

def read():
    with open('preset_data.json', 'r') as file:
        return json.load(file)

def write(newValue, page=-1, key=-1):
    if page == -1:
        data = newValue
    elif page >= 0:
        pass
    else:
        data = read()
        if key == -1: 
            data[page] = newValue
        else:
            data[page][key] = newValue
    with open('preset_data.json', 'w') as file:
        json.dump(data, file)