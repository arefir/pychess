from array import *


def getTrueCoords(coords):

    if isinstance(coords[0], str):
        coords[0] = ord(coords[0]);
        coords[1] = 8 - int(coords[1]);
    
    else:
        coords[1] = 8 - coords[1];

    if coords[0] >= 65 and coords[0] <= 72:
        coords[0] = coords[0] - 65;
    elif coords[0] >= 97 and coords[0] <= 104:
        coords[0] = coords[0] - 97; 
    else:
        print("Invalid coordinates");
        return 1;
class ChessBoard:

    rows, cols = (8, 8)

    board = []
    board = [[0, 0, 0, 0, 0, 0, 0, 0]for i in range(rows)]
    count = 0;
    kingB = [4, 0];
    kingW = [4, 7];


    def __init__(self):

        board = self.board;

        for i in range(8):
            board[1][i] = Pawn("black", 1, i);

        for i in range(8):
            board[6][i] = Pawn("white", 6, i);

        board[0][0],board[0][7] = (Rook("black", 0, 0), Rook("black", 0, 7));
        board[7][0],board[7][7] = (Rook("white", 7, 0), Rook("white", 7, 7));

        board[0][1],board[0][6] = (Knight("black", 0, 1), Knight("black", 0, 6));
        board[7][1],board[7][6] = (Knight("white", 7, 1), Knight("white", 7, 6));

        board[0][2],board[0][5] = (Bishop("black", 0, 2), Bishop("black", 0, 5));
        board[7][2],board[7][5] = (Bishop("white", 7, 2), Bishop("white", 7, 5));

        board[0][3],board[0][4] = (Queen("black", 0, 3), King("black", 0, 4));
        board[7][3],board[7][4] = (Queen("white", 7, 3), King("white", 7, 4));

    
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

    def isCheck(self):

        if self.count % 2 == 0:
            team = "white";
        else:
            team = "black";

        check = False;
        for i in range(0, 8):
            for j in range(0, 8):
                piece = self.board[i][j];
                if piece != 0:
                    if piece.team != team:
                        coords = [j, i]
                        src = [piece.col + 65, 8 - piece.row]
                        # print(f"{piece.identifier} {src}")
                        if team == "white":
                            dest = [self.kingW[0] + 65, 8 - self.kingW[1]]
                            # print(dest)
                            check = piece.checkvalid(src, dest, True, coords, self.kingW);
                        if team == "black":
                            dest = [self.kingB[0] + 65, 8 - self.kingB[1]]
                            check = piece.checkvalid(src, dest, True, coords, self.kingB);
                        
        return check;

class Piece:

    identifier = "piece";
    team = "";
    symbolB = "";
    symbolW = "";
    counter = 0;
    row = 0;
    col = 0;
    srcC = [0, 0];
    destC = [0, 0];

    def __init__(self, team, row, col):
        self.team = team;
        self.row = row;
        self.col = col;

    def initCoords(self, src, dest):
        srcC = [];
        destC = [];
        if not isinstance(src, list):
            srcC = list(src);
        else:
            srcC = src;

        if not isinstance(dest, list):
            destC = list(dest);
        else:
            destC = dest;

        # print(f"init {srcC} {destC}")
        # print(srcC);
        # print(destC);
        if isinstance(srcC[0], str):
            self.srcC[0] = ord(srcC[0]);
        else:
            self.srcC[0] = srcC[0];
        self.srcC[1] = int(srcC[1]);
        if isinstance(destC[0], str):
            self.destC[0] = ord(destC[0]);
        else:
            self.destC[0] = destC[0];
        self.destC[1] = int(destC[1]);
        # print(f"init {self.srcC} {self.destC}")
        # print(self.srcC);
        # print(self.destC);

class Pawn(Piece):

    def __init__(self, team, row, col):
        Piece.__init__(self, team, row, col);
        self.identifier = "pawn";
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

        return True;
class Rook(Piece):

    def __init__(self, team, row, col):
        Piece.__init__(self, team, row, col);
        self.identifier = "rook";
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
                for i in range(c + 1, mc):
                    if board1.board[r][i] != 0:
                        return False;
            else:
                for i in range(mc + 1, c):
                    if board1.board[r][i] != 0:
                        return False;

        if (r != mr) and (abs(mr - r) > 1):
            if (mr > r):
                for i in range(r + 1, mr):
                    if board1.board[i][c] != 0:
                        return False;
            else:
                for i in range(mr + 1, r):
                    if board1.board[i][c] != 0:
                        return False;

        return True;
    

class Knight(Piece):

    def __init__(self, team, row, col):
        Piece.__init__(self, team, row, col);
        self.identifier = "knight";
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
                return True;

        if abs(destC[0] - srcC[0]) == 1:
            if abs(destC[1] - srcC[1]) == 2:
                return True; 

        return False;

class Bishop(Piece):

    def __init__(self, team, row, col):
        Piece.__init__(self, team, row, col);
        self.identifier = "bishop";
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
            # print(f"srcC: {srcC}, srcTC: {srcTC}, destC: {destC}");
            # print(f"srcCol = {srcC[0]}, srcRow = {srcC[1]}, destCol = {destC[0]}, destRow = {destC[1]}")
            # print(f"srcTCol = {srcTC[0]}, srcTRow = {srcTC[1]}")
            # print(board1.board[srcTC[1]][srcTC[0]])
            if board1.board[srcTC[1]][srcTC[0]] != 0:
                return False; 
            srcC[0] += cd; 
            srcC[1] += rd;

        return True;   

class Queen(Piece):

    def __init__(self, team, row, col):
        Piece.__init__(self, team, row, col);
        self.identifier = "queen";
        self.symbolB = "♕";
        self.symbolW = "♛";

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

            return True;
        
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

        return True;

class King(Piece):

    def __init__(self, team, row, col):
        Piece.__init__(self, team, row, col);
        self.identifier = "king";
        self.symbolB = "♔";
        self.symbolW = "♚";

    def checkvalid(self, src, dest, enemy, coords, mCoords):

        self.initCoords(src, dest);

        srcC = self.srcC;
        destC = self.destC;
        c = coords[0];
        r = coords[1];
        mc = mCoords[0];
        mr = mCoords[1];

        team = self.team;

        if (abs(destC[0] - srcC[0])) != 1 and (abs(destC[1] - srcC[1])) != 1:
            return False;

        return True;

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
            temp = board1.board[mr][mc];
            board1.board[mr][mc] = board1.board[r][c];
            board1.board[r][c] = 0;
            isCheck = board1.isCheck();
            print(isCheck);
            if isCheck:
                print("Checked");
                board1.board[r][c] = board1.board[mr][mc];
                board1.board[mr][mc] = temp;
                continue;
            board1.board[mr][mc].col = mc;
            board1.board[mr][mc].row = mr;
            board1.board[mr][mc].counter += 1;
            board1.count += 1;
        else:
            print("Invalid move")

    board1.printBoard();


