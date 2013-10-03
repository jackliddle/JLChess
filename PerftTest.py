"""
    Test the Perft position from http://chessprogramming.wikispaces.com/Perft+Results
    Currently just checking the node count
"""

from PerftData import PerftData, FENs
from LegalMoves import getBoards
from Board import Board

maxdepth = 1
test_positions = range(6)

def testPosition(FEN,perftdata):
    board = Board()
    board.initFromFEN(FEN)
    print FEN
    print board
    print
    print '%12s %12s'%('Have','Need')
    for depth in range(maxdepth):
        nextboards = getBoards(board,depth+1,'WHITE')
        print '%12s %12s'%( len(nextboards),perftdata[depth].Nodes )

if __name__ == "__main__":
    for pos in test_positions:
        testPosition(FENs[pos],PerftData[pos])