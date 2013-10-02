from UnicodeDefs import *
import re
from copy import deepcopy

piece_reg = '(?P<player>WHITE|BLACK)_(?P<piece>PAWN|ROOK|KNIGHT|BISHOP|QUEEN|KING)'
piece_re = re.compile(piece_reg)

class Board:
    def __init__(self):
        self.board = [[None for i in range(8)] for j in range(8)]

    def setup(self):
        """
            Layout the board in starting position
        """
        piece_order = ['ROOK','KNIGHT','BISHOP','QUEEN','KING','BISHOP','KNIGHT','ROOK']
        for row,colour in zip([0,7],['BLACK','WHITE']):
            for col,piece in enumerate(piece_order):
                self.board[row][col] = colour + '_' + piece
                
        for row,colour in zip([1,6],['BLACK','WHITE']):
            for i in range(8):
                self.board[row][i] = colour + '_' + 'PAWN'

    def applyMove(self, (from_row,from_col), (to_row,to_col)):
        """
            Apply move giving a new Board object
        """
        newboard = deepcopy(self)
        piece = newboard.board[from_row][from_col]
        newboard.board[from_row][from_col] = None
        newboard.board[to_row][to_col] = piece
        return newboard

    def pieceAt(self,(row,col)):
        return piece_re.match( self.board[row][col] ).groupdict()

    def piecesGenerator(self,colour):
        for row in range(8):
            for col in range(8):
                if self.board[row][col] != None:
                    piece,pos = self.pieceAt((row,col)),((row,col))
                    if piece['player'] == colour:
                        yield piece,pos 
    
    def isEmptyAt(self,(row,col)):
        if self.board[row][col] == None:
            return True
        else:
            return False

    def siteBelongsTo(self,newPos,oppo):
        if self.isEmptyAt(newPos):
            return False
        else:
            return self.pieceAt(newPos)['player'] == oppo

    def siteDoesNotBelongTo(self,newPos,side):
        if self.isEmptyAt(newPos):
            return True
        else:
            return self.pieceAt(newPos)['player'] != side
        
    
    def __str__(self):
        rep = ""
        
        def tagToStr(tag):
            if tag == None:
                return ' '
            else:
                return pieces_s[tag]
        rep += '  ' + ' '.join([str(i) for i in range(8)]) + '\n'
        for i,row in enumerate(self.board):
            rep += str(i) + ' ' + ' '.join(tagToStr(tag) for tag in row) + '\n'
        return rep
        
    def unicoderep(self):
        rep = '  '+u'\u2009\u2009'+u'\u0020'.join( [chr(i) for i in range(ord('a'),ord('h')+1)] ) #All manner of unicode hacks adjust for the chess piece column width
        rep += '\n'
        def tagToUnicode(tag):
            try:
                return pieces_u[tag]
            except KeyError:
                return '  '

        for i,row in enumerate(self.board):
            rep +=  str(i) + ' ' + ''.join([tagToUnicode(tag) for tag in row]) + '\n'
            
        return rep.encode('utf-8')
    
    
if __name__ == "__main__":
    print "Testing"
    b1 = Board()
    b1.setup()

    newb = b1.applyMove((1,0),(4,4))
    print "New board"
    print newb
    print "Old board"
    print b1

