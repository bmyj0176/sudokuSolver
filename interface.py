'''
5 3 . | . . . | . . . 
6 . . | . . . | . . . 
. . . | . . . | . . . 
---------------------
. . . | . . . | . . . 
. . . | . 7 . | . . . 
. . . | . . . | . . . 
---------------------
. . . | . . . | . . . 
. . . | . . . | . . 9 
. . . | . . . | . . . 

1234_6789   1234_6789   1234_6789 | 123456789   123_5678_   123456789   1234_6789   1234_678_   1234_6789
1234_6789   1234_6789   1234_6789 | 1234_6789   123__678_   1234_6789   _________   1234_678_   1234_6789
1234_6789   _________   1234_6789 | 1234_6789   123__678_   1234_6789   1234_6789   1234_678_   1234_6789
----------------------------------+-----------------------------------+----------------------------------
123456789   1234_6789   123456789   123_56789   123_5678_   123_56789   1234_6789   12345678_   123456789
123456789   1234_6789   123456789   123_56789   123_5678_   123_56789   1234_6789   12345678_   123456789
123_56789   123__6789   123_56789   123_56789   _________   123_56789   123__6789   123_5678_   123_56789
---------------------------------------------------------------------------------------------------------
12345678_   1234_678_   12345678_   12345678_   _________   12345678_   1234_678_   12345678_   12345678_
12345678_   1234_678_   12345678_   12345678_   123_5678_   12345678_   1234_678_   _________   12345678_   
123456789   1234_6789   123456789   12345678_   123_5678_   12345678_   1234_678_   12345678_   12345678_
'''

def print_board(board):
    print_board_hinted(board, -2, -2)

def print_board_hinted(board, row, col): # 
    index = 0
    for l0 in range(3): # big rows + horizontal line
        for l1 in range(3): # small rows in big row
            for l2 in range(3): # each section in small row + vert line
                for l3 in range(3): # each element of small row section
                    printItem = str(board[index])
                    if printItem == '0':
                        printItem = '.'
                    print(printItem, end=' ')
                    index += 1
                if l2 < 2: print('|', end=' ')
            if row == l0*3+l1:  print("←-",end=' ')
            elif row == -1:      print("←- " + str(l0*3+l1+1), end=' ')    
            print() # newline
        if l0 < 2: print('------+-------+------')
    if col >= 0 and col <= 8:
        for spacing in range(col + col // 3): print(end='  ') # spacing before arrow
        print('↑')
    elif row != -1 and col == -1:
        print('↑ ↑ ↑   ↑ ↑ ↑   ↑ ↑ ↑\n1 2 3   4 5 6   7 8 9')

def print_note_board(note_board, row, col):
    for big_row in range(3):
        for small_row in range(3):
            for big_col in range(3):
                for small_col in range(3):
                    for note in range(9):
                        if (note+1) in note_board[(small_col+big_col*3)+(small_row+big_row*3)*9]: # 1-9
                            print(note+1, end='')
                        else: print(end='_')
                    if small_col < 2: print(end="   ")
                if big_col < 2: print(end=' | ')
                elif (big_row*3+small_row) == row: print(end=' ←--')
            print() # newline
        if big_row < 2: print('----------------------------------+-----------------------------------+----------------------------------') # newline
        else:
            for spacing in range(col): print(end='            ')
            print('↑↑↑↑↑↑↑↑↑')