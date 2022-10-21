from array import *


def getTrueCoords(coords):

    if isinstance(coords[0], str):
        coords[0] = ord(coords[0]);
        coords[1] = 8 - int(coords[1]);
    
    else:
        coords[1] = 8 - coords[1];

    if coords[0] >= 65 and coords[0] <= 72:
        coords[0] = 8 - (coords[0] - 64);
    elif coords[0] >= 97 and coords[0] <= 104:
        coords[0] = coords[0] - 97; 
    else:
        print("Invalid coordinates");
        return 1;

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
    counter = 0;
    srcC = [0, 0];
    destC = [0, 0];

    def initCoords(self, src, dest):
        srcC = list(src);
        destC = list(dest);
        # print(srcC);
        # print(destC);
        self.srcC[0] = ord(srcC[0]);
        self.srcC[1] = int(srcC[1]);
        self.destC[0] = ord(destC[0]);
        self.destC[1] = int(destC[1]);
        # print(self.srcC);
        # print(self.destC);

class Pawn(Piece):

    def __init__(self, team):
        self.identifier = "pawn";
        self.team = team;
        self.symbolB = "♙";
        self.symbolW = "♟";

    def checkvalid(self, src, dest, enemy, coords, mCoords):

        self.initCoords(src, dest);

        srcC = self.srcC;
        destC = self.destC;

        team = self.team;
        
        if team == "white":
            if self.counter > 0:
                if (destC[1] - srcC[1]) != 1:
                    return False;
            elif (destC[1] - srcC[1]) > 2 or (destC[1] - srcC[1]) < 1:
                    return False;

        if team == "black":
            if self.counter > 0:
                if (destC[1] - srcC[1]) != -1:
                    return False;
            elif (destC[1] - srcC[1]) < -2 or (destC[1] - srcC[1]) > -1:
                    return False;

        if srcC[0] != destC[0]:
            if abs(destC[0] - srcC[0]) != 1 or abs(destC[1] - srcC[1]) != 1:
                return False;
            elif enemy == False:
                return False;
        elif enemy:
            return False;

        self.counter += 1;
        return True;
class Rook(Piece):

    def __init__(self, team):
        self.identifier = "rook";
        self.team = team;
        self.symbolB = "♖";
        self.symbolW = "♜";

    def checkvalid(self, src, dest, enemy, coords, mCoords):

        self.initCoords(src, dest);

        srcC = self.srcC;
        destC = self.destC;
        c = coords[0];
        r = coords[1];
        mc = mCoords[0];
        mr = mCoords[1];

        team = self.team;

        if (srcC[0] != destC[0]) and (srcC[1] != destC[1]):
            return False;
        
        if (c != mc) and (abs(mc - c) > 1):
            if (mc > c):
                for i in range(c + 1, mc - 1):
                    if board1.board[r][i] != 0:
                        return False;
            else:
                for i in range(mc + 1, c - 1):
                    if board1.board[r][i] != 0:
                        return False;

        if (r != mr) and (abs(mr - r) > 1):
            if (mr > r):
                for i in range(r + 1, mr - 1):
                    if board1.board[i][c] != 0:
                        return False;
            else:
                for i in range(mr + 1, r - 1):
                    if board1.board[i][c] != 0:
                        return False;

        self.counter += 1;
        return True;
    

class Knight(Piece):

    def __init__(self, team):
        self.identifier = "knight";
        self.team = team;
        self.symbolB = "♘";
        self.symbolW = "♞";

    def checkvalid(self, src, dest, enemy, coords, mCoords):

        self.initCoords(src, dest);

        srcC = self.srcC;
        destC = self.destC;
        c = coords[0];
        r = coords[1];
        mc = mCoords[0];
        mr = mCoords[1];

        team = self.team;

        if abs(destC[0] - srcC[0]) == 2:
            if abs(destC[1] - srcC[1]) == 1:
                self.counter += 1;
                return True;

        if abs(destC[0] - srcC[0]) == 1:
            if abs(destC[1] - srcC[1]) == 2:
                self.counter += 1;
                return True; 

        return False;

class Bishop(Piece):

    def __init__(self, team):
        self.identifier = "bishop";
        self.team = team;
        self.symbolB = "♗";
        self.symbolW = "♝";

    def checkvalid(self, src, dest, enemy, coords, mCoords):

        self.initCoords(src, dest);

        srcC = self.srcC;
        destC = self.destC;

        c = coords[0];
        r = coords[1];
        mc = mCoords[0];
        mr = mCoords[1];

        team = self.team;

        if abs(destC[0] - srcC[0]) != abs(destC[1] - srcC[1]):
            return False;
        
        cd = 0;
        rd = 0;

        if destC[0] > srcC[0]:
            cd = 1;
        else:
            cd = -1;

        if destC[1] > srcC[1]:
            rd = 1;
        else:
            rd = -1;
        
        srcC[0] += cd;
        srcC[1] += rd;

        while (srcC[0] != destC[0]):
            srcTC = srcC.copy();
            getTrueCoords(srcTC);
            # print(f"srcCol = {srcC[0]}, srcRow = {srcC[1]}, destCol = {destC[0]}, destRow = {destC[1]}")
            # print(f"srcTCol = {srcTC[0]}, srcTRow = {srcTC[1]}")
            # print(board1.board[srcTC[1]][srcTC[0]])
            if board1.board[srcTC[1]][srcTC[0]] != 0:
                return False; 
            srcC[0] += cd; 
            srcC[1] += rd;

        self.counter += 1;
        return True;   

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

###########################################################################

board1 = ChessBoard();
board1.printBoard();

while True:

    piece = input("Choose piece (eg; d2 | to exit input 'exit'): ");
    if piece == "exit": break;

    coords = list(piece);

    abort = getTrueCoords(coords);

    if abort == 1:
        print("Invalid input");
        continue;

    c = coords[0];
    r = coords[1];

    # c = ord(coords[0]);
    # r = 8 - int(coords[1]);

    # if c >= 65 and c <= 72:
    #     c = 8 - (c - 64);
    # elif c >= 97 and c <= 104:
    #     c = c - 97;
    # else:
    #     print("Invalid coordinates");

    move = "";

    if board1.board[r][c] != 0:
        move = input("Choose square to move (eg; d4): ");
    else:
        print("No piece in selected square");
        continue;

    if (move) != "":
        mCoords = list(move);

        abort = getTrueCoords(mCoords);

        if abort == 1:
            print("Invalid input");
            continue;

        mc = mCoords[0];
        mr = mCoords[1];

        pc = board1.board[r][c];

        enemy = False;
        if board1.board[mr][mc] != 0:
            if board1.board[mr][mc].team != pc.team:
                enemy = True;
            else:
                print("Destination Square Occupied");
                continue;

        valid = pc.checkvalid(piece, move, enemy, coords, mCoords);

        if valid:
            board1.board[mr][mc] = board1.board[r][c];
            board1.board[r][c] = 0;
        else:
            print("Invalid move")

    board1.printBoard();


