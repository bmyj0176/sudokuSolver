import interface

def main(board, mode):
    print()
    interface.print_board(board)
    print('''---------------------\nSudoku Board Complete!''')
    input("Enter to Return: ")
    return 'Insertion'