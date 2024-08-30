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
    return solve1.naked_singles()

def naked_pairs():
    return solve1.naked_pairs()

def naked_triples():
    return solve1.naked_triples()

def naked_quads():
    return solve1.naked_quads()

def hidden_singles():
    return solve2.hidden_singles()

def hidden_pairs():
    return solve2.hidden_pairs()

def hidden_triples():
    return solve2.hidden_triples()

def pointing_pairs_triples():
    return solve2.pointing_pairs_triples()

def x_wing():
    return solve3.x_wing()

def xy_wing():
    return solve3.xy_wing()

def swordfish():
    return solve3.swordfish()
