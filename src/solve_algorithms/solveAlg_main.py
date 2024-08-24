import modes.solver as solve
import utilities.read_algorithms as readAlg

import solve_algorithms.solveAlg_1 as solve1
import solve_algorithms.solveAlg_2 as solve2
import solve_algorithms.solveAlg_3 as solve3

def import_boards(board, note_board):
    solve1.import_boards(board, note_board)
    solve2.import_boards(board, note_board)
    solve3.import_boards(board, note_board)

# When there's only one note in a cell
def obvious_singles():
    solve1.obvious_singles()
    return

def obvious_pairs():
    solve1.obvious_pairs()
    return

def obvious_triples():
    solve1.obvious_triples()
    return

def hidden_singles():
    solve2.hidden_singles()
    return

def hidden_pairs():
    solve2.hidden_singles()
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
