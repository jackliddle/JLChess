# Perft data from http://chessprogramming.wikispaces.com/Perft+Results
# Used as input for testing move generation

from collections import namedtuple

PerftResults = namedtuple('PerftResults',['Nodes','Captures','EP','Castles','Promotions','Checks','Checkmates'])

#Position 1
Position1 = []
#Position1.append( PerftResults(                  1,      0,   0,   0,   0,    0,     0) )  #0
Position1.append( PerftResults(                 20,      0,   0,   0,   0,    0,     0) )  #1
Position1.append( PerftResults(                400,      0,   0,   0,   0,    0,     0) )  #2
Position1.append( PerftResults(               8902,     34,   0,   0,   0,    12,    0) )  #3
Position1.append( PerftResults(             197281,   1576,   0,   0,   0,   469,    8) )  #4
Position1.append( PerftResults(            4865609,  82719,   0,   0,   0, 27351,  347) )  #5
Position1.append( PerftResults(          119060324,2812008,5248,   0,   0,809099,10828) )  #6
Position1.append( PerftResults(         3195901860,   None,None,None,None,  None, None) )  #7
Position1.append( PerftResults(        84998978956,   None,None,None,None,  None, None) )  #8
Position1.append( PerftResults(     24395302341670,   None,None,None,None,  None, None) )  #9
Position1.append( PerftResults(     69352859712417,   None,None,None,None,  None, None) )  #10
Position1.append( PerftResults(   2097651003696806,   None,None,None,None,  None, None) )  #11
Position1.append( PerftResults(  62854969236701747,   None,None,None,None,  None, None) )  #12
Position1.append( PerftResults(1981066775000396239,   None,None,None,None,  None, None) )  #13  #Probably wont test this far!

#Position 2
Position2 = []
Position2.append( PerftResults(       48,       8,    0,      2,    0,      0,    0))
Position2.append( PerftResults(     2039,     351,    1,     91,    0,      3,    0))
Position2.append( PerftResults(    97862,   17102,   45,   3162,    0,    993,    1))
Position2.append( PerftResults(  4085603,  757163, 1929, 128013,15172,  25523,   43))
Position2.append( PerftResults(193690690,35043416,73365,4993637, 8392,3309887,30171))

#Position 3
Position3 = []
Position3.append( PerftResults(       14,       1,     0,0,     0,       2,   0))
Position3.append( PerftResults(      191,      14,     0,0,     0,      10,   0))
Position3.append( PerftResults(     2812,     209,     2,0,     0,     267,   0))
Position3.append( PerftResults(  43238,    3348,   123,0,     0,    1680,  17))
Position3.append( PerftResults(   674624,   52051,  1165,0,     0,   52950,   0))
Position3.append( PerftResults( 11030083,  940350, 33325,0,  7552,  452473,2733))
Position3.append( PerftResults(178633661,14519036,294874,0,140024,12797406,  87))

#Position 4, White King is in check from black Bishop.  
Position4 = []
Position4.append( PerftResults(        6,        0,   0,       0,       0,       0,    0))
Position4.append( PerftResults(      264,       87,   0,       6,      48,      10,    0))
Position4.append( PerftResults(     9467,     1021,   4,       0,     120,      38,   22))
Position4.append( PerftResults(   422333,   131393,   0,    7795,   60032,   15492,    5))
Position4.append( PerftResults( 15833292,  2046173,6512,       0,  329464,  200568,50562))
Position4.append( PerftResults(706045033,210369132, 212,10882006,81102984,26973664,81076))

#Position 5
Position5 = []
Position5.append( PerftResults(   42,None,None,None,None,None,None))
Position5.append( PerftResults( 1352,None,None,None,None,None,None))
Position5.append( PerftResults(53392,None,None,None,None,None,None))

#Position 6
Position6 = []
Position6.append( PerftResults(              46,None,None,None,None,None,None))
Position6.append( PerftResults(            2079,None,None,None,None,None,None))
Position6.append( PerftResults(           89890,None,None,None,None,None,None))
Position6.append( PerftResults(         3894594,None,None,None,None,None,None))
Position6.append( PerftResults(       164075551,None,None,None,None,None,None))
Position6.append( PerftResults(      6923051137,None,None,None,None,None,None))
Position6.append( PerftResults(    287188994746,None,None,None,None,None,None))
Position6.append( PerftResults(  11923589843526,None,None,None,None,None,None))
Position6.append( PerftResults( 490154852788714,None,None,None,None,None,None))

PerftData = [Position1,Position2,Position3,Position4,Position5,Position6]

FENs = []
FENs.append('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1 ')
FENs.append('r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq -')
FENs.append('8/2p5/3p4/KP5r/1R3p1k/8/4P1P1/8 w - -')
FENs.append('r3k2r/Pppp1ppp/1b3nbN/nP6/BBP1P3/q4N2/Pp1P2PP/R2Q1RK1 w kq - 0 1')
FENs.append('rnbqkb1r/pp1p1ppp/2p5/4P3/2B5/8/PPP1NnPP/RNBQK2R w KQkq - 0 6')
FENs.append('r4rk1/1pp1qppp/p1np1n2/2b1p1B1/2B1P1b1/P1NP1N2/1PP1QPPP/R4RK1 w - - 0 10')

if __name__ == "__main__":
    from Board import Board
    
    print len(PerftData), "Perft data sets found"
    print
    for FEN in FENs:
        board = Board()
        board.initFromFEN(FEN)
        print FEN
        print board