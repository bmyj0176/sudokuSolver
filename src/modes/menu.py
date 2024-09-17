import main
import interface

def main(board, note_board):
    showNoteboard = False
    while True:
        interface.print_board(board)
        print(f"[1] Solve Board!")
        print(f"[2] Edit Board")
        if showNoteboard: print(f"[3] Show Board")
        else:             print(f"[3] Show Note Board")
        print(f"[4] Load Saved Presets")
        selection = input("Select: ")
        if selection == '1':
            return 'Solver'
        elif selection == '2':
            return 'Insertion'
        elif selection == '3':
            showNoteboard = not showNoteboard
        elif selection == '4':
            return 'Preset'

        