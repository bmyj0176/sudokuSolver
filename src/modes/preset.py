import json
import interface
from pathlib import Path

# $env:PYTHONPATH="c:\Users\bryon\OneDrive\Homework\Projects\sudokuSolver\src"

board = [0 for _ in range(81)]
note_board = [[] for _ in range(81)]

def main(board, note_board):
    page = 1
    showNoteboard = False
    extraMessage = None
    while True:
        if showNoteboard: interface.print_note_board(read()[page-1]["note_board"], -1, -1)
        else:             interface.print_board(read()[page-1]["board"])
        print(f"<{page} / {len(read())}> {read()[page-1]["preset"]}")
        print(f"[1] < Previous || Next > [2]")
        if showNoteboard: print(f"[3] Show Board")
        else:             print(f"[3] Show Note Board")
        print(f"[4] Load Preset")
        print(f"[5] Rename Preset")
        print(f"[6] Delete Preset")
        print(f"[7] Save Current Board as New Preset")
        print(f"[8] Return to Menu")
        if extraMessage: print(f"({extraMessage}) ", end="")
        selection = input("Select: ")
        extraMessage = None
        if selection == '1': # Previous
            page -= 1
            if page == 0: page = len(read())
        elif selection == '2': # Next
            page += 1
            if page == len(read())+1: page = 1
        elif selection == '3': # Show Noteboard
            showNoteboard = not showNoteboard
        elif selection == '4': # Load Preset
            board = read()[page-1]["board"]
            note_board = read()[page-1]["note_board"]
            extraMessage = f"Loaded Preset {read()[page-1]['preset']}"
        elif selection == '5': # Rename Preset
            newName = input("Rename to: ")
            write(newName, page, "preset")
            extraMessage = f"Renamed Preset to {newName}"
        elif selection == '6': # Delete Preset
            extraMessage = f"Deleted Preset {read()[page-1]['preset']}"
            list = read()
            list.pop(page-1)
            write(list)
        elif selection == '7': # Save Current Board as New Preset
            interface.print_board(board)
            presetName = input("Insert New Preset Name: ")
            entry = {"preset": presetName, "board": board, "note_board": note_board}
            write(entry, len(read())+1)
            extraMessage = f"Saved Preset {presetName}"
        elif selection == '8': # Return to Menu
            return "Menu"
        else: 
            extraMessage = "Invalid Selection"

def read():
    with open(Path(__file__).parent / 'preset_data.json', 'r') as file:
        return json.load(file)

def write(newValue, page=-1, key=-1):
    if page == -1:
        data = newValue
    else:
        data = read()
        if page > len(data):
            data.append(newValue)
        else:
            if key == -1: 
                data[page-1] = newValue
            else:
                data[page-1][key] = newValue
    with open(Path(__file__).parent / 'preset_data.json', 'w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    note_board = [[] for _ in range(81)]

    

    main(board, note_board)