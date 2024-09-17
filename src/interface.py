'''
4 3 5 | 2 6 9 | 7 8 1 
6 8 2 | 5 7 1 | 4 9 3
1 9 . | 8 3 4 | 5 6 2
------+-------+------
8 2 6 | 1 9 5 | 3 4 7
3 7 4 | 6 8 2 | 9 1 5
9 5 1 | 7 4 3 | 6 2 8
------+-------+------
5 1 9 | 3 2 6 | 8 7 4
2 4 8 | 9 . 7 | 1 3 6
7 6 3 | 4 1 8 | 2 5 9
'''
def print_board(board, rowPointer=None, colPointer=None, displayAllPointers=False):
    index = 0
    index_to_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J']
    for big_row in range(3):
        for small_row in range(3):
            for big_col in range(3):
                for small_col in range(3):
                    printItem = str(board[index])
                    if printItem == '0': printItem = '.'
                    print(f"{printItem} ", end='')
                    index += 1
                if big_col < 2: print('| ', end='')
            if big_col == 2: 
                if rowPointer == big_row*3+small_row: print("←-")
                elif displayAllPointers: print(f"←- {index_to_alphabet[big_row*3+small_row]}")
                else:                          print()
        if big_row < 2: print('------+-------+------')
    if colPointer:
        for _ in range(colPointer + colPointer // 3): print('  ', end='')
        print('↑')
    if displayAllPointers:
        print('↑ ↑ ↑   ↑ ↑ ↑   ↑ ↑ ↑\n1 2 3   4 5 6   7 8 9')

'''
 (  8  )    __3_5___9   __345___9 |  (  6  )    __3___7__   _23___7_9 | __345____    (  1  )    __345_7__
1_3_5____    (  2  )     (  7  )  | __3____8_   1_3____8_   1_3____8_ | __3456_8_    (  9  )    __3456_8_
1_3_____9   1_3__6__9   __3_____9 |  (  5  )     (  4  )    1_3___789 | __3__6_8_   __3___7__    (  2  )
----------------------------------+-----------------------------------+----------------------------------
_23___7__   __3___78_   _23____8_ | __34___8_   1_3__6_8_    (  5  )  |  (  9  )    _234__7__   1_34_678_
 (  6  )    __3_5_789    (  1  )  | __34___89    (  2  )    __34___89 | __345__8_   __345_7__   __345_78_
_23_5___9    (  4  )    _23_5__89 |  (  7  )    1_3__6_8_   1_3__6_89 | 123_56_8_   _23_5____   1_3_56_8_
----------------------------------+-----------------------------------+----------------------------------
_23_5_7_9   __3_5_789   _23_5__89 |  (  1  )    __3_5_78_   _234__78_ | _2345____    (  6  )    __345___9
 (  4  )    1_3_5_7__   _23_5____ | _23______    (  9  )    _23__67__ | 123_5____    (  8  )    1_3_5____
123_5___9   1_3_5__89    (  6  )  | _234___8_   __3_5__8_   _234___8_ |  (  7  )    _2345____   1_345___9
'''
def print_note_board(board, note_board, rowPointer=None, colPointer=None, displayAllPointers=False):
    index_to_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J']
    for big_row in range(3):
        for small_row in range(3):
            for big_col in range(3):
                for small_col in range(3):
                    if note_board[(small_col+big_col*3)+(small_row+big_row*3)*9]: # contains value
                        for note in range(9):
                            if (note+1) in note_board[(small_col+big_col*3)+(small_row+big_row*3)*9]: # 1-9
                                print(note+1, end='')
                            else: print(end='_')
                    else:
                        print(end=f' (  {board[(small_col+big_col*3)+(small_row+big_row*3)*9]}  ) ')
                    if small_col < 2: print(end="   ")
                if big_col < 2: print(end=' | ')
                else:
                    if (big_row*3+small_row) == rowPointer: print(end=' ←--')
                    elif displayAllPointers: print(end=f" ←-- {index_to_alphabet[big_row*3+small_row]}")
            print() # newline
        if big_row < 2: print('----------------------------------+-----------------------------------+----------------------------------') # newline
        elif colPointer:
            for _ in range(colPointer): print(end='            ')
            print(' ↑↑↑↑↑↑↑ ')
    if displayAllPointers:
        print(' ↑↑↑↑↑↑↑     ↑↑↑↑↑↑↑     ↑↑↑↑↑↑↑     ↑↑↑↑↑↑↑     ↑↑↑↑↑↑↑     ↑↑↑↑↑↑↑     ↑↑↑↑↑↑↑     ↑↑↑↑↑↑↑     ↑↑↑↑↑↑↑\n    1           2           3           4           5           6           7           8           9')

board = [ # missing a few only
    4, 3, 5, 2, 6, 9, 7, 8, 1,
    6, 8, 2, 5, 7, 1, 4, 9, 3,
    1, 9, 0, 8, 3, 4, 5, 6, 2,
    8, 2, 6, 1, 9, 5, 3, 4, 7,
    3, 7, 4, 6, 8, 2, 9, 1, 5,
    9, 5, 1, 7, 4, 3, 6, 2, 8,
    5, 1, 9, 3, 2, 6, 8, 7, 4,
    2, 4, 8, 9, 0, 7, 1, 3, 6,
    7, 6, 3, 4, 1, 8, 2, 5, 9
]