from Board import Board
from collections import defaultdict
from itertools import chain

def boundCheckPos((row,col)):
    """
        True if the position is inside the board
    """
    r = range(8)
    return row in r and col in r

def pawnMoveGenerator(board,piece,(row,col)):
    """
        Yield possible pawn moves
        En passant not implemented
        Promotion not implemented
    """
    
    side = piece['player']
    oppo = 'BLACK' if side == 'WHITE' else 'WHITE'
    dir = -1 if side == 'WHITE' else 1
    
    starting_rank = {}
    starting_rank['WHITE'] = 6
    starting_rank['BLACK'] = 1
    
    #If we are in the starting rank we can move two spaces
    newPos = (row+2*dir,col)
    if row == starting_rank[side]:
        if board.isEmptyAt(newPos) and board.isEmptyAt((row+dir,col)):
            yield newPos

    #Move a single space, which we can always do
    newPos = (row+dir,col)
    if board.isEmptyAt(newPos):
        yield newPos

    #Taking a piece diagonally    
    for lr in [-1,1]:
        newPos = (row+dir,col+lr)
        if boundCheckPos(newPos):
            if board.siteBelongsTo(newPos,oppo):
                yield newPos

def knightMoveGenerator(board,piece,(row,col)):
    side = piece['player']
    
    def isPosValid(newPos):
        if boundCheckPos(newPos):
            if board.siteDoesNotBelongTo(newPos,side):
                return True
                
    for x in [-2,2]:
        for y in [-1,1]:
            newPos = row+x,col+y
            if isPosValid(newPos):
                yield newPos

            newPos = row+y,col+x
            if isPosValid(newPos):
                yield newPos

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
    
    def sliderMoveGenerator(board,piece,(row,col)):
        side = piece['player']
        oppo = 'BLACK' if side == 'WHITE' else 'WHITE'
        
        for vec in vecs:
            for (x,y) in vec:
                newPos = row+x,col+y
                if boundCheckPos(newPos):
                    ownsite   = board.siteBelongsTo(newPos,side)
                    theirsite = board.siteBelongsTo(newPos,oppo)
                    empty     = board.isEmptyAt(newPos) 
    
                    if ownsite:
                        break
    
                    if empty:
                        yield newPos
        
                    if theirsite:
                        yield newPos
                        break

    return sliderMoveGenerator
    
def notImplementedMoveGenerator(board,piece,(row,col)):
    print "NOT IMPLEMENTED"
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
        
    def generateMoves(self,board,colour):
        for piece,pos in board.piecesGenerator(colour):
            p =  piece['piece']
            for move in self.generators[p](board,piece,pos):
                yield pos,move

mg = MoveGenerator()

def getBoards(board,depth,side):
    oppo = 'BLACK' if side == 'WHITE' else 'WHITE'
    boards = [board.applyMove(from_pos,to_pos) for from_pos,to_pos in mg.generateMoves(board,side)]
    
    if depth == 1:
        return boards
    else:
        nextlevel = [getBoards(board,depth-1,oppo) for board in boards]
        return list(chain(*nextlevel))

def hasKing(board,side):
    for row in range(8):
        for col in range(8):
            if board.board[row][col] == side + '_KING':
                return True
    return False

def isSideInCheck(board,side):
    """
        side:  side to check if in check.  WHITE means BLACK is the attacking side
    """
    oppo = 'BLACK' if side == 'WHITE' else 'WHITE'
    boards = getBoards(board,1,oppo)
    for board in boards:
        if not hasKing(board,side):
            return True
    return False
    
if __name__ == "__main__":
    b1 = Board()
    b1.setup()
    print b1
    nextboards = getBoards(b1,3,'WHITE')   #Want 8,902
    print len(nextboards), "Positions at depth 3"
