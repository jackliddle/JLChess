WHITE_KING   = u'\u2654'
WHITE_QUEEN  = u'\u2655'
WHITE_ROOK   = u'\u2656'
WHITE_BISHOP = u'\u2657'
WHITE_KNIGHT = u'\u2658'
WHITE_PAWN   = u'\u2659'

BLACK_KING   = u'\u265A'
BLACK_QUEEN  = u'\u265B'
BLACK_ROOK   = u'\u265C'
BLACK_BISHOP = u'\u265D'
BLACK_KNIGHT = u'\u265E'
BLACK_PAWN   = u'\u265F'

pieces_u = {}

pieces_u['WHITE_KING']   = u'\u2654'
pieces_u['WHITE_QUEEN']  = u'\u2655'
pieces_u['WHITE_ROOK']   = u'\u2656'
pieces_u['WHITE_BISHOP'] = u'\u2657'
pieces_u['WHITE_KNIGHT'] = u'\u2658'
pieces_u['WHITE_PAWN']   = u'\u2659'

pieces_u['BLACK_KING']   = u'\u265A'
pieces_u['BLACK_QUEEN']  = u'\u265B'
pieces_u['BLACK_ROOK']   = u'\u265C'
pieces_u['BLACK_BISHOP'] = u'\u265D'
pieces_u['BLACK_KNIGHT'] = u'\u265E'
pieces_u['BLACK_PAWN']   = u'\u265F'

pieces_s = {}

pieces_s['WHITE_KING']   = 'K'
pieces_s['WHITE_QUEEN']  = 'Q'
pieces_s['WHITE_ROOK']   = 'R'
pieces_s['WHITE_BISHOP'] = 'B'
pieces_s['WHITE_KNIGHT'] = 'N'
pieces_s['WHITE_PAWN']   = 'P'

pieces_s['BLACK_KING']   = 'k'
pieces_s['BLACK_QUEEN']  = 'q'
pieces_s['BLACK_ROOK']   = 'r'
pieces_s['BLACK_BISHOP'] = 'b'
pieces_s['BLACK_KNIGHT'] = 'n'
pieces_s['BLACK_PAWN']   = 'p'


if __name__ == "__main__":
#    print WHITE_KING,WHITE_QUEEN,WHITE_ROOK,WHITE_BISHOP,WHITE_KNIGHT,WHITE_PAWN
#    print WHITE_KING,BLACK_QUEEN,BLACK_ROOK,BLACK_BISHOP,BLACK_KNIGHT,BLACK_PAWN

    for name,code in pieces.iteritems():
        print name,code