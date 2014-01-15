"""
    Test the Perft position from http://chessprogramming.wikispaces.com/Perft+Results
    Currently just checking the node count
"""

from PerftData import PerftData, FENs
from LegalMoves import getBoards,isInCheck
from Board import Board

maxdepth = 3
test_positions = [1]#range(6)#[0]



def testPosition(FEN,perftdata):
    b1 = Board()
    b1.initFromFEN(FEN)
    print FEN
    print '%3s%12s%24s%24s%24s'%('','Nodes','Captures','Checks','Castles')
    have_need = '%12s%12s'%('Have','Need')
    have_need *= 4
    print '%4s%1s'%('',have_need)
    for depth in range(maxdepth):
        
        nextboards,nextmoves = getBoards(b1,depth+1)
        Ncaps = len( filter(lambda(i): i == 'CAPTURE',nextmoves) )
        Ncast = len( filter(lambda(i): i == 'CASTLE' ,nextmoves) )
        try:
            checks = [isInCheck(board) for board in nextboards]
            checks = [check for check in checks if len(check)]
            Nchecks = len(checks)
        except:
            Nchecks = "ILLEGAL"
        print '%3s%12s%12s%12s%12s%12s%12s%12s%12s'%( depth,len(nextboards),perftdata[depth].Nodes,Ncaps,perftdata[depth].Captures,Nchecks,perftdata[depth].Checks,Ncast,perftdata[depth].Castles  )
    print


if __name__ == "__main__":
    for pos in test_positions:
        testPosition(FENs[pos],PerftData[pos])
