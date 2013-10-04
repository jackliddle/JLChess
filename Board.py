from UnicodeDefs import *
import re
from copy import deepcopy
from itertools import count

piece_reg = '(?P<player>WHITE|BLACK)_(?P<piece>PAWN|ROOK|KNIGHT|BISHOP|QUEEN|KING)'
piece_re = re.compile(piece_reg)

"""
    Pieces are layed out in a list of lists.
        Board.board[row][col]
    Pieces are designated as <player>_<piece>, or None if empty
"""

class Board:
    def __init__(self):
        self.board = [[None for i in range(8)] for j in range(8)]
        self.toplay = None
        
        # Flags for Castling, set to False if one of the castling is now forever impossible, e.g. Rook or King have moved.
        self.WHITE_QUEENSIDE_CASTLE = True
        self.WHITE_KINGSIDE_CASTLE  = True
        self.BLACK_QUEENSIDE_CASTLE = True
        self.BLACK_KINGSIDE_CASTLE  = True

    def setup(self):
        """
            Layout the board in starting position.
        """
        piece_order = ['ROOK','KNIGHT','BISHOP','QUEEN','KING','BISHOP','KNIGHT','ROOK']
        for row,colour in zip([0,7],['BLACK','WHITE']):
            for col,piece in enumerate(piece_order):
                self.board[row][col] = colour + '_' + piece
                
        for row,colour in zip([1,6],['BLACK','WHITE']):
            for i in range(8):
                self.board[row][i] = colour + '_' + 'PAWN'
                
        self.toplay = 'WHITE'
        
    def initFromFEN(self,FENstring):
        """
            Initialise board from FEN string
            http://chessprogramming.wikispaces.com/Forsyth-Edwards+Notation
        """
        inv_pieces_s = {v:k for k, v in pieces_s.items()}

        FENstring = FENstring.strip()
        #print FENstring.split(' ')[0:4]
        try:
            pieces,toplay,castling,enpassant = FENstring.split(' ')[0:4]
        except ValueError:
            pieces,toplay = FENstring.split(' ')[0:2]
            

        piece_rows = pieces.split('/')
        for row_string,row in zip(piece_rows,count()):
            col=0
            for char in row_string:
                if inv_pieces_s.has_key(char):
                    self.board[row][col] = inv_pieces_s[char]
                    col += 1
                if char.isdigit():
                    col += int(char)
        self.toplay = "WHITE" if toplay == "w" else "BLACK"
                    
    def toFEN(self):
        """
            Serialise board to FEN string
            http://chessprogramming.wikispaces.com/Forsyth-Edwards+Notation
        """
        row_strs = []
        for row in range(0,8):
            row = self.board[row]
        
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
            
        toplay = "w" if self.toplay == "WHITE" else "b"
        boardrep = "/".join(row_strs) 
        return "%s %s"%(boardrep,toplay)
    

    def applyMove(self, (from_row,from_col), (to_row,to_col)):
        """
            Apply move giving a new Board object
        """
        newboard = deepcopy(self)
        piece = newboard.board[from_row][from_col]
        newboard.board[from_row][from_col] = None
        newboard.board[to_row][to_col] = piece
        newboard.toplay = 'BLACK' if self.toplay == 'WHITE' else 'WHITE'
        return newboard

    def pieceAt(self,(row,col)):
        return piece_re.match( self.board[row][col] ).groupdict()

    def piecesGenerator(self,player):
        """
            Yield all the pieces in the board belonging to 
        """
        for row in range(8):
            for col in range(8):
                if self.board[row][col] != None:
                    piece,pos = self.pieceAt((row,col)) ,((row,col))
                    if piece['player'] == player:
                        yield piece,pos 
                        
    
    
    def siteOwner(self,(row,col)):
        if self.board[row][col] == None:
            return "EMPTY"
        else:
            return self.pieceAt((row,col))['player']
    
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
        rep += "%s to play"%self.toplay
        rep += "\n"
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
    b1 = Board()

    b1.setup()
    b2 = b1.applyMove( (6,0), (4,0))
    b3 = b2.applyMove( (1,0), (3,0))

    print b1
    print b2
    print b3