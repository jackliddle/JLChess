from Board import Board
from collections import defaultdict
from itertools import chain
import pdb

opposition = lambda(side): 'BLACK' if side == 'WHITE' else 'WHITE'

def boundCheckPos((row,col)):
    """
        True if the position is inside the board
    """
    r = range(8)
    return row in r and col in r

def pawnMoveGenerator(board,(row,col)):
    """
        Yield possible pawn moves
        En passant not implemented
        Promotion not implemented
    """
    
    #side = piece['player']
    side = board.toplay
    oppo = opposition(side)
    dir = -1 if side == 'WHITE' else 1
    
    starting_rank = {}
    starting_rank['WHITE'] = 6
    starting_rank['BLACK'] = 1
    
    #If we are in the starting rank we can move two spaces
    newPos = (row+2*dir,col)
    if row == starting_rank[side]:
        if board.siteOwner(newPos) == 'EMPTY' and board.siteOwner((row+dir,col))  == 'EMPTY':
            yield newPos,"MOVE"

    #Move a single space, which we can always do
    newPos = (row+dir,col)
    if board.siteOwner(newPos) == 'EMPTY':
        yield newPos,"MOVE"

    #Taking a piece diagonally    
    for lr in [-1,1]:
        newPos = (row+dir,col+lr)
        if boundCheckPos(newPos):
            if board.siteOwner(newPos) == oppo:
                yield newPos,"CAPTURE"

def knightMoveGenerator(board,(row,col)):
    side = board.toplay
    oppo = opposition(side)
    
    def isPosValid(newPos):
        if boundCheckPos(newPos):
            if not board.siteOwner(newPos) == side:
                return True
                
    for x in [-2,2]:
        for y in [-1,1]:
            newPos = row+x,col+y
            if isPosValid(newPos):
                movetype = "CAPTURE" if board.siteOwner(newPos) == oppo else "MOVE"
                yield newPos,movetype

            newPos = row+y,col+x
            if isPosValid(newPos):
                movetype = "CAPTURE" if board.siteOwner(newPos) == oppo else "MOVE"
                yield newPos,movetype

king_vecs = [ [( 0, 1)],
              [( 0,-1)],
              [( 1, 0)],
              [(-1, 0)],
              [( 1, 1)],
              [( 1,-1)],
              [(-1, 1)],
              [(-1,-1)] ]

rook_vecs = [[( 0, i) for i in range(1,8)], 
             [( 0,-i) for i in range(1,8)], 
             [( i, 0) for i in range(1,8)],
             [(-i, 0) for i in range(1,8)]]

bishop_vecs = [[( i, i) for i in range(1,8)],
               [( i,-i) for i in range(1,8)],
               [(-i, i) for i in range(1,8)],
               [(-i,-i) for i in range(1,8)]]

def sliderMoveFactory(vecs):
    def sliderMoveGenerator(board,(row,col)):
        side = board.toplay
        oppo = opposition(side)
        
        for vec in vecs:
            for (x,y) in vec:
                newPos = row+x,col+y
                if boundCheckPos(newPos):
                    siteowner = board.siteOwner(newPos)
                    if siteowner == side:
                        break
    
                    if siteowner == "EMPTY":
                        yield newPos,"MOVE"
        
                    if siteowner == oppo:
                        yield newPos,"CAPTURE"
                        break

    return sliderMoveGenerator
    
    
def notImplementedMoveGenerator(board,(row,col)):
    return
    yield
    
class MoveGenerator:
    def __init__(self):
        self.generators = defaultdict(lambda: notImplementedMoveGenerator)
        self.generators['PAWN']   = pawnMoveGenerator
        self.generators['KNIGHT'] = knightMoveGenerator
        self.generators['KING']   = sliderMoveFactory(king_vecs)
        self.generators['ROOK']   = sliderMoveFactory(rook_vecs)
        self.generators['BISHOP'] = sliderMoveFactory(bishop_vecs)
        self.generators['QUEEN']  = sliderMoveFactory(bishop_vecs+rook_vecs)
        
    def generateMoves(self,board):
        for piece,pos in board.piecesGenerator(board.toplay):
            p =  piece['piece']
            for move,movetype in self.generators[p](board,pos):
                yield pos,move,movetype

class ThreatGenerator:
    def __init__(self):
        self.generators = defaultdict(lambda: notImplementedMoveGenerator)
        self.movegenerators = [sliderMoveFactory(bishop_vecs), sliderMoveFactory(rook_vecs)]
        self.validtargets   = [('QUEEN','BISHOP'),('QUEEN','ROOK')]
        
    def findThreats(self,board,pos):

        movegenerator = self.movegenerators[0]
        validtargets = self.validtargets[0]

        blocks_list  = []
        blocks = []
        
        for move,movetype in movegenerator(board,pos):
            if movetype == "MOVE":
                blocks.append(move)
            if movetype == "CAPTURE":
                if board.pieceAt(move)['piece'] in validtargets:
                    blocks.append(move)
                    blocks_list.append(blocks)
                    blocks = []
                else:
                    blocks = []

        return blocks_list


def isInCheck(board):
    for piece,pos in board.piecesGenerator(board.toplay):
        if piece['piece'] == 'KING':
            kingpos = pos
    return tg.findThreats(board,kingpos)

mg = MoveGenerator()
tg = ThreatGenerator()

def getBoards(board,depth):
    boards,movetypes = zip( *[( board.applyMove(from_pos,to_pos),movetype) for from_pos,to_pos,movetype in mg.generateMoves(board)] )
#    boards = [ board.applyMove(from_pos,to_pos) for from_pos,to_pos in mg.generateMoves(board)]
    #print type(movetypes),len(movetypes)
    if depth == 1:
        return boards,movetypes
    else:
        
        #This is quite complicated at this depth
        nextboards,nextmoves = zip( *[getBoards(board,depth-1) for board in boards] ) 
        nextboards = list(chain(*nextboards))
        nextmoves  = list(chain(*nextmoves))
        return nextboards,nextmoves
        #nextlevel = [getBoards(board,depth-1) for board in boards]
        #pdb.set_trace()
        #return list(chain(*nextlevel))

