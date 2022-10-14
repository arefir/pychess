from array import *

class ChessBoard:

    rows, cols = (8, 8)

    board = []
    board = [[0, 0, 0, 0, 0, 0, 0, 0]for i in range(rows)]


    def __init__(self):

        board = self.board;

        print("lol")

        for i in range(8):
            board[1][i] = Pawn("black");

        for i in range(8):
            board[6][i] = Pawn("white");

        board[0][0],board[0][7] = (Rook("black"), Rook("black"));
        board[7][0],board[7][7] = (Rook("white"), Rook("white"));

        board[0][1],board[0][6] = (Knight("black"), Knight("black"));
        board[7][1],board[7][6] = (Knight("white"), Knight("white"));

        board[0][2],board[0][5] = (Bishop("black"), Bishop("black"));
        board[7][2],board[7][5] = (Bishop("white"), Bishop("white"));

        board[0][3],board[0][4] = (Queen("black"), King("black"));
        board[7][3],board[7][4] = (Queen("white"), King("white"));

    
    def printBoard(self):

        c = 8

        for i in self.board:
            print(c, end=" ");
            for j in i:
                if j == 0: print("⊡", end=" ");
                else: 
                    if j.team == "black": print(j.symbolB, end=" ");
                    else: print(j.symbolW, end=" ");
                    # print(j, end=" ");
            print();
            c -= 1;

        print("  a b c d e f g h")

class Piece:

    identifier = "piece";
    team = "";
    symbolB = "";
    symbolW = "";


class Pawn(Piece):

    def __init__(self, team):
        self.identifier = "pawn";
        self.team = team;
        self.symbolB = "♙";
        self.symbolW = "♟";

class Rook(Piece):

    def __init__(self, team):
        self.identifier = "rook";
        self.team = team;
        self.symbolB = "♖";
        self.symbolW = "♜";

class Knight(Piece):

    def __init__(self, team):
        self.identifier = "knight";
        self.team = team;
        self.symbolB = "♘";
        self.symbolW = "♞";

class Bishop(Piece):

    def __init__(self, team):
        self.identifier = "bishop";
        self.team = team;
        self.symbolB = "♗";
        self.symbolW = "♝";

class Queen(Piece):

    def __init__(self, team):
        self.identifier = "queen";
        self.team = team;
        self.symbolB = "♕";
        self.symbolW = "♛";

class King(Piece):

    def __init__(self, team):
        self.identifier = "king";
        self.team = team;
        self.symbolB = "♔";
        self.symbolW = "♚";

board1 = ChessBoard();
board1.printBoard();

while True:

    piece = input("Choose piece (eg; d2 | to exit input 'exit'): ");
    if piece == "exit": break;

    coords = list(piece);

    c = ord(coords[0]);
    r = 8 - int(coords[1]);

    if c >= 65 and c <= 90:
        c = 8 - (c - 64);
    elif c >= 97 and c <= 122:
        c = c - 97;
    else:
        print("Invalid coordinates");

    moves = "";

    if board1.board[r][c] != 0:
        move = input("Choose square to move (eg; d4): ");

    if (move) != "":
        mCoords = list(move);

        mc = ord(mCoords[0]);
        mr = 8 - int(mCoords[1]);

        if mc >= 65 and mc <= 90:
            mc = 8 - (mc - 64);
        elif mc >= 97 and mc <= 122:
            mc = mc - 97;
        else:
            print("Invalid coordinates");

        board1.board[mr][mc] = board1.board[r][c];
        board1.board[r][c] = 0;

    board1.printBoard();