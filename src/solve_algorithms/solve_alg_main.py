import modes.solver as solve
import utilities.read_algorithms as readAlg

import solve_algorithms.solve_alg1 as solve1
import solve_algorithms.solve_alg2 as solve2
import solve_algorithms.solve_alg3 as solve3

def import_boards(board, note_board):
    solve1.import_boards(board, note_board)
    solve2.import_boards(board, note_board)
    solve3.import_boards(board, note_board)

# When there's only one note in a cell
def naked_singles():
    solve1.naked_singles()
    return

def naked_multiples():
    solve1.naked_multiples()
    return

def hidden_singles():
    solve2.hidden_singles()
    return

def hidden_pairs():
    solve2.hidden_pairs()
    return

def hidden_triples():
    solve2.hidden_triples()
    return

def pointing_pairs_triples():
    solve2.pointing_pairs_triples()
    return

def x_wing():
    solve3.x_wing()
    return

def xy_wing():
    solve3.xy_wing()
    return

def swordfish():
    solve3.swordfish()
    return
