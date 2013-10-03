from Board import Board
from UnicodeDefs import pieces_s
from sys import exit
from itertools import count
inv_pieces = {v:k for k, v in pieces_s.items()}


def boardToFEN(board):
    row_strs = []
    for row in range(0,8):
        row = board.board[row]
    
        counter = 0
        row_str = ""
        for cell in row:
            if cell:
                if counter == 0:
                    row_str += pieces_s[cell]
                else:
                    row_str += "%d%s"%(counter,pieces_s[cell])        
                counter = 0
            else:
                counter += 1

        if counter:
            row_str += str(counter)
            
        row_strs.append(row_str)
        
    return "/".join(row_strs)
    

if __name__ == "__main__":
    #Perft initial positions from http://chessprogramming.wikispaces.com/Perft+Results
    FENs = []
    FENs.append('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1 ')
    FENs.append('r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq -')
    FENs.append('8/2p5/3p4/KP5r/1R3p1k/8/4P1P1/8 w - -')
    FENs.append('r3k2r/Pppp1ppp/1b3nbN/nP6/BBP1P3/q4N2/Pp1P2PP/R2Q1RK1 w kq - 0 1')
    FENs.append('rnbqkb1r/pp1p1ppp/2p5/4P3/2B5/8/PPP1NnPP/RNBQK2R w KQkq - 0 6')
    FENs.append('r4rk1/1pp1qppp/p1np1n2/2b1p1B1/2B1P1b1/P1NP1N2/1PP1QPPP/R4RK1 w - - 0 10')
    
    
    for FEN in FENs:
        board = Board()
        board.initFromFEN(FEN)
        #print FEN.split(' ')[0]
        #print board.toFEN()
        assert FEN.split(' ')[0] == board.toFEN(),"Failed to serialise to FEN"

            