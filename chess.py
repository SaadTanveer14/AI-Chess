import numpy as np
import pandas as pd
import copy
import random

ending=False
Places=["a","b","c","d","e","f","g","h"]

locx={0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h"}
locy={0:"1",1:"2",2:"3",3:"4",4:"5",5:"6",6:"7",7:"8"}

pieces1 = {"#":"rook","$":"knight","|":"bishop","-":"queen","+":"king","^":"pawn"}
pieces2 = {"R":"rook","K":"knight","B":"bishop","Q":"queen","K":"king","P":"pawn"}

piecesW=["R","K","B","Q","k","P"]
piecesB=["#","$","|","-","+","^"]
capW=[]
capB=[]
enPassant=0
castlingW=1
castlingB=1

board=np.array([
        ["#","0","0","+","+","0","0","#"],
        ["^","^","^","^","^","^","^","^"],
        ["0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0"],
        ["P","P","P","P","P","P","P","P"],
        ["R","k","B","Q","K","B","k","R"]
        ])

newboard=np.array([
        ["#","$","|","-","+","|","$","#"],
        ["^","^","^","^","^","^","^","^"],
        ["0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0"],
        ["P","P","P","P","P","P","P","P"],
        ["R","k","B","Q","K","B","k","R"]
        ])



def Board():
    pass
def Player():
    pass
print(board)

class Player():
    def __init__(self):
        self.startx=0
        self.starty=0
        self.endx=0
        self.endy=0
def movePiece(position):
    for key,value in locx.items():
        #print(key,value)
        if(value==position[0]):
            player.startx=key
            player.starty=int(position[1])-1
        if(value==position[2]):
            player.endx=key
            player.endy=int(position[3])-1
    
    
    newboard=np.copy(board)
    print(player.startx,player.starty,player.endx,player.endy)             
    if((board[player.starty][player.startx]=="R")or(board[player.starty][player.startx]=="#")):
        if(rook(player)):
            if((board[player.starty][player.startx] in piecesW) and (board[player.endy][player.endx]  in piecesB)):
                capB.append(board[player.endy][player.endx])
                board[player.endy][player.endx]=board[player.starty][player.startx]
                board[player.starty][player.startx]="0"
                print(board[player.starty][player.startx])
                newboard=np.copy(board)
            elif((board[player.starty][player.startx] in piecesB) and (board[player.endy][player.endx]  in piecesW)):
                capW.append(board[player.endy][player.endx])
                board[player.endy][player.endx]=board[player.starty][player.startx]
                board[player.starty][player.startx]="0"
                print(board[player.starty][player.startx])
                newboard=np.copy(board)
            elif((board[player.starty][player.startx] in piecesB) and (board[player.endy][player.endx] in piecesB)):
                pass
            elif((board[player.starty][player.startx] in piecesW) and (board[player.endy][player.endx] in piecesW)):
                pass
            else:
                board[player.endy][player.endx]=board[player.starty][player.startx]
                board[player.starty][player.startx]="0"
                print(board[player.starty][player.startx])
                newboard=np.copy(board)

    elif((board[player.starty][player.startx]=="k")or(board[player.starty][player.startx]=="$")):
        if(knight(player)):
            if((board[player.starty][player.startx] in piecesW) and (board[player.endy][player.endx]  in piecesB)):
                capB.append(board[player.endy][player.endx])
                board[player.endy][player.endx]=board[player.starty][player.startx]
                board[player.starty][player.startx]="0"
                print(board[player.starty][player.startx])
                newboard=np.copy(board)
            elif((board[player.starty][player.startx] in piecesB) and (board[player.endy][player.endx]  in piecesW)):
                capW.append(board[player.endy][player.endx])
                board[player.endy][player.endx]=board[player.starty][player.startx]
                board[player.starty][player.startx]="0"
                print(board[player.starty][player.startx])
                newboard=np.copy(board)
            elif((board[player.starty][player.startx] in piecesB) and (board[player.endy][player.endx] in piecesB)):
                pass
            elif((board[player.starty][player.startx] in piecesW) and (board[player.endy][player.endx] in piecesW)):
                pass
            else:
                board[player.endy][player.endx]=board[player.starty][player.startx]
                board[player.starty][player.startx]="0"
                print(board[player.starty][player.startx])
                newboard=np.copy(board)

    elif((board[player.starty][player.startx]=="K") or (board[player.starty][player.startx]=="+")):
        if(king(player)):
            if((board[player.starty][player.startx] in piecesW) and (board[player.endy][player.endx]  in piecesB)):
                capB.append(board[player.endy][player.endx])
                board[player.endy][player.endx]=board[player.starty][player.startx]
                board[player.starty][player.startx]="0"
                print(board[player.starty][player.startx])
                newboard=np.copy(board)
            elif((board[player.starty][player.startx] in piecesB) and (board[player.endy][player.endx]  in piecesW)):
                capW.append(board[player.endy][player.endx])
                board[player.endy][player.endx]=board[player.starty][player.startx]
                board[player.starty][player.startx]="0"
                print(board[player.starty][player.startx])
                newboard=np.copy(board)
            elif((board[player.starty][player.startx] in piecesB) and (board[player.endy][player.endx] in piecesB)):
                pass
            elif((board[player.starty][player.startx] in piecesW) and (board[player.endy][player.endx] in piecesW)):
                pass
            else:
                board[player.endy][player.endx]=board[player.starty][player.startx]
                board[player.starty][player.startx]="0"
                print(board[player.starty][player.startx])
                newboard=np.copy(board)

    elif((board[player.starty][player.startx]=="Q") or (board[player.starty][player.startx]=="-")):
        if(queen(player)):
            if((board[player.starty][player.startx] in piecesW) and (board[player.endy][player.endx]  in piecesB)):
                capB.append(board[player.endy][player.endx])
                board[player.endy][player.endx]=board[player.starty][player.startx]
                board[player.starty][player.startx]="0"
                print(board[player.starty][player.startx])
                newboard=np.copy(board)
            elif((board[player.starty][player.startx] in piecesB) and (board[player.endy][player.endx]  in piecesW)):
                capW.append(board[player.endy][player.endx])
                board[player.endy][player.endx]=board[player.starty][player.startx]
                board[player.starty][player.startx]="0"
                print(board[player.starty][player.startx])
                newboard=np.copy(board)
            elif((board[player.starty][player.startx] in piecesB) and (board[player.endy][player.endx] in piecesB)):
                pass
            elif((board[player.starty][player.startx] in piecesW) and (board[player.endy][player.endx] in piecesW)):
                pass
            else:
                board[player.endy][player.endx]=board[player.starty][player.startx]
                board[player.starty][player.startx]="0"
                print(board[player.starty][player.startx])
                newboard=np.copy(board)

    elif((board[player.starty][player.startx]=="B") or (board[player.starty][player.startx]=="|")):
        if(bishop(player)):

            if((board[player.starty][player.startx] in piecesW) and (board[player.endy][player.endx]  in piecesB)):
                capB.append(board[player.endy][player.endx])
                board[player.endy][player.endx]=board[player.starty][player.startx]
                board[player.starty][player.startx]="0"
                print(board[player.starty][player.startx])
                newboard=np.copy(board)
            elif((board[player.starty][player.startx] in piecesB) and (board[player.endy][player.endx]  in piecesW)):
                capW.append(board[player.endy][player.endx])
                board[player.endy][player.endx]=board[player.starty][player.startx]
                board[player.starty][player.startx]="0"
                print(board[player.starty][player.startx])
                newboard=np.copy(board)

            elif((board[player.starty][player.startx] in piecesB) and (board[player.endy][player.endx] in piecesB)):
                pass
            elif((board[player.starty][player.startx] in piecesW) and (board[player.endy][player.endx] in piecesW)):
                pass
            else:
                board[player.endy][player.endx]=board[player.starty][player.startx]
                board[player.starty][player.startx]="0"
                print(board[player.starty][player.startx])
                newboard=np.copy(board)

            

    elif((board[player.starty][player.startx]=="P") or (board[player.starty][player.startx]=="^")):
        if(pawn(player)==2):
            if((board[player.starty][player.startx] in piecesW) and (board[player.endy][player.endx]  in piecesB)):
                capB.append(board[player.endy][player.endx])
                board[player.endy][player.endx]=board[player.starty][player.startx]
                board[player.starty][player.startx]="0"
                print(board[player.starty][player.startx])
                newboard=np.copy(board)
            elif((board[player.starty][player.startx] in piecesB) and (board[player.endy][player.endx]  in piecesW)):
                capW.append(board[player.endy][player.endx])
                board[player.endy][player.endx]=board[player.starty][player.startx]
                board[player.starty][player.startx]="0"
                print(board[player.starty][player.startx])
                newboard=np.copy(board)

        elif(pawn(player)):
            board[player.endy][player.endx]=board[player.starty][player.startx]
            board[player.starty][player.startx]="0"
            print(board[player.starty][player.startx])
            newboard=np.copy(board)

    return newboard
    # newboard=board.copy()
    # board[player.endy][player.endx]=board[player.starty][player.startx]
    # board[player.starty][player.startx]="0"
    # print(board[player.starty][player.startx])
    # print(newboard)



def knight(position):
    tempx=position.startx+2
    tempy=position.starty-1
    if((tempx==position.endx) and (tempy==position.endy)):
        return True
    tempy=position.starty+1

    if((tempx==position.endx) and (tempy==position.endy)):
        return True

    tempx=position.startx-2
    tempy=position.starty-1
    if((tempx==position.endx) and (tempy==position.endy)):
        return True

    tempy=position.starty+1
    if((tempx==position.endx) and (tempy==position.endy)):
        return True

    tempy=position.starty-2
    tempx=position.startx-1
    if((tempx==position.endx) and (tempy==position.endy)):
        return True
    tempx=position.startx+1
    if((tempx==position.endx) and (tempy==position.endy)):
        return True

    tempy=position.starty+2
    tempx=position.startx-1
    if((tempx==position.endx) and (tempy==position.endy)):
        return True
    tempx=position.startx+1
    if((tempx==position.endx) and (tempy==position.endy)):
        return True
    return False
    
def pawn(position):
    global enPassant
    if(position.endy>position.starty):
        x=position.startx+1
        y=position.starty+1
        if((position.endx==x) and (position.endy==y)):
            if(board[position.endy][position.endx]!="0"):
                return 2

        x=position.startx-1
        if((position.endx==x) and (position.endy==y)):
            if(board[position.endy][position.endx]!="0"):
                return 2

    elif(position.endy<position.starty):
        x=position.startx-1
        y=position.starty-1
        if((position.endx==x) and (position.endy==y)):
            if(board[position.endy][position.endx]!="0"):
                return 2
        x=position.startx+1
        if((position.endx==x) and (position.endy==y)):
            if(board[position.endy][position.endx]!="0"):
                return 2
    

    if(board[position.endy][position.endx]!="0"):
        return False

    if((position.starty==1) or (position.starty==6)):
        if((position.endy==3) and (board[position.starty+1][position.startx]=="0") and (board[position.starty][position.startx] in piecesB)):
            if((position.startx+1<8) and ((board[position.starty+2][position.startx+1] in piecesW) or (board[position.starty+2][position.startx-1] in piecesW))):
                
                enPassant=1
            return True
        elif((position.endy==4) and (board[position.starty-1][position.startx]=="0") and (board[position.starty][position.startx] in piecesW)):
            if((board[position.starty-2][position.startx+1] in piecesB) or (board[position.starty-2][position.startx-1] in piecesB)):
                enPassant=1
            return True


    if(board[position.starty][position.startx] in piecesW):
        if((position.startx==position.endx) and (position.starty-1==position.endy)):
            return True
    elif(board[position.starty][position.startx] in piecesB):
        if((position.startx==position.endx) and (position.starty+1==position.endy)):
            return True
    return False
    
def bishop(position):
    x=position.startx
    y=position.starty
    if((position.endx<x) and (position.endy>y)):
        while((x>=0) and (y<8)):
            if((x==position.endx)and(y==position.endy)):
                return True
            if((x!=position.startx)and(y!=position.starty)):
                if(board[y][x]!="0"):
                    return False
            x-=1
            y+=1
    
    x=position.startx
    y=position.starty
    if((position.endx>x) and (position.endy<y)):
        while((x<8) and (y>=0)):
            if((x==position.endx)and(y==position.endy)):
                return True
            if((x!=position.startx)and(y!=position.starty)):
                if(board[y][x]!="0"):
                    return False
            x+=1
            y-=1
    
    x=position.startx
    y=position.starty
    if((position.endx>x) and (position.endy>y)):
        while((x<8)or(y<8)):
            if((x==position.endx)and(y==position.endy)):
                return True
            if((x!=position.startx)and(y!=position.starty)):
                if(board[y][x]!="0"):
                    return False
            x+=1
            y+=1
    
    x=position.startx
    y=position.starty
    if((position.endx<x) and (position.endy<y)):
        while((x>=0) and (y>=0)):
            if((x==position.endx)and(y==position.endy)):
                return True
            if((x!=position.startx)and(y!=position.starty)):
                if(board[y][x]!="0"):
                    return False
            x-=1
            y-=1
    return False
    
def king(position):
    global castlingB
    global castlingW
    if((castlingB==1) and (board[position.starty][position.startx+1]=="0") and (board[position.starty][position.startx+2]=="0") and (board[position.starty][position.startx+3]=="#") and (position.endx==position.startx+2) and (position.starty==position.endy) and (position.starty==0)):
        castlingB=0
        board[position.starty][position.startx+2]=board[position.starty][position.startx]
        board[position.starty][position.startx]="0"
        board[position.starty][position.startx+1]=board[position.starty][position.startx+3]
        board[position.starty][position.startx+3]="0"

    elif((castlingB==1) and (board[position.starty][position.startx-1]=="0") and (board[position.starty][position.startx-2]=="0") and (board[position.starty][position.startx-3]=="#") and (position.endx==position.startx-2) and (position.starty==position.endy) and (position.starty==0)):
        castlingB=0
        board[position.starty][position.startx-2]=board[position.starty][position.startx]
        board[position.starty][position.startx]="0"
        board[position.starty][position.startx-1]=board[position.starty][position.startx-3]
        board[position.starty][position.startx-3]="0"

    elif((castlingW==1) and (board[position.starty][position.startx+1]=="0") and (board[position.starty][position.startx+2]=="0") and (board[position.starty][position.startx+3]=="R") and (position.endx==position.startx+2) and (position.starty==position.endy) and (position.starty==7)):
        castlingW=0
        board[position.starty][position.startx+2]=board[position.starty][position.startx]
        board[position.starty][position.startx]="0"
        board[position.starty][position.startx+1]=board[position.starty][position.startx+3]
        board[position.starty][position.startx+3]="0"

    elif((castlingW==1) and (board[position.starty][position.startx-1]=="0") and (board[position.starty][position.startx-2]=="0") and (board[position.starty][position.startx-3]=="R") and (position.endx==position.startx-2) and (position.starty==position.endy) and (position.starty==7)):
        castlingW=0
        board[position.starty][position.startx-2]=board[position.starty][position.startx]
        board[position.starty][position.startx]="0"
        board[position.starty][position.startx-1]=board[position.starty][position.startx-3]
        board[position.starty][position.startx-3]="0"

    if((position.endx==position.startx+1) and (position.endy==position.starty)):
            return True  
    if((position.endx==position.startx-1) and (position.endy==position.starty)):
            return True
    if((position.endx==position.startx) and (position.endy==position.starty-1)):
            return True  
    if((position.endx==position.startx) and (position.endy==position.starty+1)):
            return True
    if((position.endx==position.startx-1) and (position.endy==position.starty-1)):
            return True  
    if((position.endx==position.startx+1) and (position.endy==position.starty+1)):
            return True
    if((position.endx==position.startx-1) and (position.endy==position.starty+1)):
            return True  
    if((position.endx==position.startx+1) and (position.endy==position.starty-1)):
            return True
    return False
    
def queen(position):
    
    

    x=position.startx
    y=position.starty
    if((position.endx<x) and (position.endy>y)):
        while((x>=0) and (y<8)):
            if((x==position.endx)and(y==position.endy)):
                return True
            if((x!=position.startx)and(y!=position.starty)):
                if(board[y][x]!="0"):
                    return False
            x-=1
            y+=1
    
    x=position.startx
    y=position.starty
    if((position.endx>x) and (position.endy<y)):
        while((x<8) and (y>=0)):
            if((x==position.endx)and(y==position.endy)):
                return True
            if((x!=position.startx)and(y!=position.starty)):
                if(board[y][x]!="0"):
                    return False
            x+=1
            y-=1
    
    x=position.startx
    y=position.starty
    if((position.endx>x) and (position.endy>y)):
        while((x<8)or(y<8)):
            if((x==position.endx)and(y==position.endy)):
                return True
            if((x!=position.startx)and(y!=position.starty)):
                if(board[y][x]!="0"):
                    return False
            x+=1
            y+=1
    
    x=position.startx
    y=position.starty
    if((position.endx<x) and (position.endy<y)):
        while((x>=0) and (y>=0)):
            if((x==position.endx)and(y==position.endy)):
                return True
            if((x!=position.startx)and(y!=position.starty)):
                if(board[y][x]!="0"):
                    return False
            x-=1
            y-=1


    if((position.endx==position.startx) and (position.endy!=position.starty)):
        if(position.endy>position.starty):
            i=position.starty+1
            while (i<position.endy-1):
                if((board[i][position.startx]!="0")and(i!=position.endy)):
                    return False
                i+=1
        elif(position.endy<position.starty):
            
            i=position.starty-1
            while (i>position.endy-1):
                if((board[i][position.startx]!="0")and(i!=position.endy)):
                    return False
                i-=1
        return True  
    if((position.endx!=position.startx) and (position.endy==position.starty)):
        if(position.endx>position.startx):
            i=position.startx+1
            while (i<position.endx-1):
                if((board[position.starty][i]!="0")and(i!=position.endx)):
                    return False
                i+=1
        elif(position.endx<position.startx):
            i=position.startx-1
            while (i>position.endx-1):
                if((board[position.starty][i]!="0")and(i!=position.endx)):
                    return False
                i-=1
        return True

    return False

def rook(position):
    if((position.endx==position.startx) and (position.endy!=position.starty)):
        if(position.endy>position.starty):
            if(board[position.starty+1][position.startx]!=0 and board[position.starty+1][position.startx] in piecesB):
                return False

            i=position.starty+1
            while (i<position.endy-1):
                if((board[i][position.startx]!="0")and(i!=position.endy)):
                    return False
                i+=1
        elif(position.endy<position.starty):

            if(board[position.starty-1][position.startx]!=0 and board[position.starty-1][position.startx] in piecesB):
                return False
            
            i=position.starty-1
            while (i>position.endy-1):
                if((board[i][position.startx]!="0")and(i!=position.endy)):
                    return False
                i-=1
        return True  
    if((position.endx!=position.startx) and (position.endy==position.starty)):
        

        if(position.endx>position.startx):
            if(board[position.starty][position.startx+1]!=0 and board[position.starty+1][position.startx+1] in piecesB):
                return False
            i=position.startx+1
            while (i<position.endx-1):
                if((board[position.starty][i]!="0")and(i!=position.endx)):
                    return False
                i+=1
        elif(position.endx<position.startx):
            if(board[position.starty][position.startx-1]!=0 and board[position.starty+1][position.startx-1] in piecesB):
                return False

            i=position.startx-1
            while (i>position.endx-1):
                if((board[position.starty][i]!="0")and(i!=position.endx)):
                    return False
                i-=1
        return True
    
    return False


def AI_move(board):

    print()
    movements = []
    positions = []
    for x in range(board.shape[0]):
        for y in range(board.shape[1]):
            if(board[x][y]=='^' or board[x][y]=='#' or board[x][y]=='$' or board[x][y]=='|' or board[x][y]=='-' or board[x][y]=='+'):
                moves=(AI_Piece(board[x][y],x,y))
                for i in range(len(moves)):
                    movements.append(moves[i])

            if(board[x][y]=='P' or board[x][y]=='R' or board[x][y]=='k' or board[x][y]=='B' or board[x][y]=='Q' or board[x][y]=='K'):
                positions.append([x,y,board[x][y]])
    
    # print(movements)
    unique_moves=unique_rows(movements)
    # print(unique_moves)

    score = 0
    danger = []
    for i in range(len(positions)):
        for j in range(len(unique_moves)):
            if(positions[i][0]==unique_moves[j][0] and positions[i][1]==unique_moves[j][1]):
                if(score<(findScore(positions[i][2]))):
                    score = findScore(positions[i][2])
                    danger_piece = positions[i][2]
                    danger.append([positions[i][0],positions[i][1]])

    while (danger):
        index=len(danger)-1
        pos = danger[index]
        # print("Position: ",pos)
        alternates = (AI_Piece(board[pos[0]][pos[1]],pos[0],pos[1]))
        # print(alternates) 
        score = 1000
        if(alternates):
            for i in range(len(alternates)):
                ax = alternates[i][0]
                ay = alternates[i][1]
                temp_score = findScore(board[ax][ay])

                if(board[ax][ay]=='^' or board[ax][ay]=='#' or board[ax][ay]=='$' or board[ax][ay]=='|' or board[ax][ay]=='-' or board[ax][ay]=='+'):
                    temp_score = -(findScore(board[ax][ay]))

                for j in range(len(unique_moves)):
                    
                    if(alternates[i][0]==unique_moves[j][0] and alternates[i][1]==unique_moves[j][1]):
                        temp_score+=findScore(board[pos[0]][pos[1]])

                if(temp_score<score):
                    score = temp_score
                    safe = alternates[i]

            # if(score>10):
            #     return "Check Mate"

            if(score<=0):
                board[safe[0]][safe[1]] = board[pos[0]][pos[1]]
                board[pos[0]][pos[1]] = '0'
                print(board)
                return 
        danger.pop(index)
    
    possibleMoves(unique_moves)
    
    
def possibleMoves(whites):
    score=-50
    for x in range(board.shape[0]):
        for y in range(board.shape[1]):
            if(board[x][y]=='P' or board[x][y]=='R' or board[x][y]=='k' or board[x][y]=='B' or board[x][y]=='Q' or board[x][y]=='K'):
                moves=(AI_Piece(board[x][y],x,y))
                for i in range(len(moves)):
                    ax = moves[i][0]
                    ay = moves[i][1]
                    temp_score = findScore(board[ax][ay])

                    if(board[ax][ay]=='^' or board[ax][ay]=='#' or board[ax][ay]=='$' or board[ax][ay]=='|' or board[ax][ay]=='-' or board[ax][ay]=='+'):
                        temp_score = findScore(board[ax][ay])

                    for j in range(len(whites)):
                        
                        if(moves[i][0]==whites[j][0] and moves[i][1]==whites[j][1]):
                            temp_score-=findScore(board[x][y])

                    if(temp_score>score):
                        score = temp_score
                        safe = moves[i]
                        ox = x
                        oy = y
                        symbol=board[x][y]
                        # pince_score = pincer(moves[i],ox,oy)
                        # if(score<pince_score):
                        #     score = -(pince_score)

                    if(temp_score==score):
                        if(board[ox][oy]=='P' and board[x][y]=='P' and oy!=y):
                            if(y>oy and oy!=3 and oy!=4 and oy!=5):
                                score = temp_score
                                safe = moves[i]
                                ox = x
                                oy = y
                                symbol=board[x][y]

    board[ox][oy]="0"
    board[safe[0]][safe[1]]=symbol
    print(board)

def pincer(safe,ox,oy):
    temp_board = copy.deepcopy(board)
    piece_score=findScore(board[ox][oy])
    board[safe[0]][safe[1]]=board[ox][oy]
    board[ox][oy] = '0'
    greater_piece = greaterPieces(piece_score,ox,oy)

    movements = []
    for x in range(temp_board.shape[0]):
        for y in range(temp_board.shape[1]):
            if(temp_board[x][y]=='^' or temp_board[x][y]=='#' or temp_board[x][y]=='$' or temp_board[x][y]=='|' or temp_board[x][y]=='-' or temp_board[x][y]=='+'):
                moves=(AI_Piece(temp_board[x][y],x,y))
                for i in range(len(moves)):
                    movements.append(moves[i])
    
    # print(movements)
    unique_moves=unique_rows(movements)    

    for i in range(len(greater_piece)):
        for j in range(len(unique_moves)):
            if(greater_piece[i][0]==unique_moves[j][0] and greater_piece[i][1]==unique_moves[j][1]):
                return 2
    return 0


def greaterPieces(score,x,y):
    moves = []
    tempx=x
    tempy=y
    while(tempx>0 and tempy>0):
        tempx-=1
        tempy-=1
        if(board[tempx][tempy]=='#' or board[tempx][tempy]=='$' or board[tempx][tempy]=='|' or board[tempx][tempy]=='-' or board[tempx][tempy]=='+' or board[tempx][tempy]=='^'):
            break

        if(board[tempx][tempy]=='P' or board[tempx][tempy]=='R' or board[tempx][tempy]=='k' or board[tempx][tempy]=='B' or board[tempx][tempy]=='Q' or board[tempx][tempy]=='K'):
            if(score<findScore(board[tempx][tempy])):
                moves.append([tempx,tempy])
            break

        # temp.append(piece)

    tempx=x
    tempy=y
    while(tempx<7 and tempy<7):
        tempx+=1
        tempy+=1
        if(board[tempx][tempy]=='#' or board[tempx][tempy]=='$' or board[tempx][tempy]=='|' or board[tempx][tempy]=='-' or board[tempx][tempy]=='+' or board[tempx][tempy]=='^'):
            break

        if(board[tempx][tempy]=='P' or board[tempx][tempy]=='R' or board[tempx][tempy]=='k' or board[tempx][tempy]=='B' or board[tempx][tempy]=='Q' or board[tempx][tempy]=='K'):
            if(score<findScore(board[tempx][tempy])):
                moves.append([tempx,tempy])
            break


    tempx=x
    tempy=y
    while(tempx>0 and tempy<7):
        tempx-=1
        tempy+=1
        if(board[tempx][tempy]=='#' or board[tempx][tempy]=='$' or board[tempx][tempy]=='|' or board[tempx][tempy]=='-' or board[tempx][tempy]=='+' or board[tempx][tempy]=='^'):
            break
        
        if(board[tempx][tempy]=='P' or board[tempx][tempy]=='R' or board[tempx][tempy]=='k' or board[tempx][tempy]=='B' or board[tempx][tempy]=='Q' or board[tempx][tempy]=='K'):
            if(score<findScore(board[tempx][tempy])):
                moves.append([tempx,tempy])
            break
    
    tempx=x
    tempy=y
    while(tempx<7 and tempy>0):
        tempx+=1
        tempy-=1
        if(board[tempx][tempy]=='#' or board[tempx][tempy]=='$' or board[tempx][tempy]=='|' or board[tempx][tempy]=='-' or board[tempx][tempy]=='+' or board[tempx][tempy]=='^'):
            break

        if(board[tempx][tempy]=='P' or board[tempx][tempy]=='R' or board[tempx][tempy]=='k' or board[tempx][tempy]=='B' or board[tempx][tempy]=='Q' or board[tempx][tempy]=='K'):
            if(score<findScore(board[tempx][tempy])):
                moves.append([tempx,tempy])
            break

    tempx=x
    while(tempx>0):
        tempx-=1
        if(board[tempx][y]=='#' or board[tempx][y]=='$' or board[tempx][y]=='|' or board[tempx][y]=='-' or board[tempx][y]=='+' or board[tempx][y]=='^'):
            break
        
        if(board[tempx][y]=='P' or board[tempx][y]=='R' or board[tempx][y]=='k' or board[tempx][y]=='B' or board[tempx][y]=='Q' or board[tempx][y]=='K'):
            if(score<findScore(board[tempx][y])):
                moves.append([tempx,y])
            break

    tempx=x
    while(tempx<7):
        tempx+=1
        temp = []
        if(board[tempx][y]=='#' or board[tempx][y]=='$' or board[tempx][y]=='|' or board[tempx][y]=='-' or board[tempx][y]=='+' or board[tempx][y]=='^'):
            break

        if(board[tempx][y]=='P' or board[tempx][y]=='R' or board[tempx][y]=='k' or board[tempx][y]=='B' or board[tempx][y]=='Q' or board[tempx][y]=='K'):
            if(score<findScore(board[tempx][y])):
                moves.append([tempx,y])
            break

    tempy=y
    while(tempy>0):
        tempy-=1
        if(board[x][tempy]=='#' or board[x][tempy]=='$' or board[x][tempy]=='|' or board[x][tempy]=='-' or board[x][tempy]=='+' or board[x][tempy]=='^'):
            break
        
        if(board[x][tempy]=='P' or board[x][tempy]=='R' or board[x][tempy]=='k' or board[x][tempy]=='B' or board[x][tempy]=='Q' or board[x][tempy]=='K'):
            if(score<findScore(board[x][tempy])):
                moves.append([x,tempy])
            break
    
    tempy=y
    while(tempy<7):
        tempy+=1
        if(board[x][tempy]=='#' or board[x][tempy]=='$' or board[x][tempy]=='|' or board[x][tempy]=='-' or board[x][tempy]=='+' or board[x][tempy]=='^'):
            break
        
        if(board[x][tempy]=='P' or board[x][tempy]=='R' or board[x][tempy]=='k' or board[x][tempy]=='B' or board[x][tempy]=='Q' or board[x][tempy]=='K'):
            if(score<findScore(board[x][y])):
                moves.append([x,tempy])
            break

    return moves


def findScore(piece):
    if(piece == '^' or piece == 'P'):
        return 1
    elif(piece == 'R' or piece == '#'):
        return 5
    elif(piece == 'Q' or piece == '-'):
        return 9
    elif(piece == 'k' or piece == '$'):
        return 3
    elif(piece == 'B' or piece == '|'):
        return 3
    elif(piece == 'K' or piece == '+'):
        return 100
    else:
        return 0


def unique_rows(a):
    a = np.ascontiguousarray(a)
    unique_a = np.unique(a.view([('', a.dtype)]*a.shape[1]))
    return unique_a.view(a.dtype).reshape((unique_a.shape[0], a.shape[1]))

def AI_Piece(piece,x,y):
    if(piece=='#' or piece=='R'):
        moves = AI_Rook(piece,x,y)
    elif(piece=='$' or piece=='k'):
        moves = AI_Knight(piece,x,y)
    elif(piece=='|' or piece=='B'):
        moves = AI_Bishop(piece,x,y)
    elif(piece=='-' or piece=='Q'):
        moves = AI_Queen(piece,x,y)
    elif(piece=='+' or piece=='K'):
        moves = AI_King(piece,x,y)
    elif(piece=='^' or piece=='P'):
        moves = AI_Pawn(piece,x,y)

    return moves
    
def AI_Pawn(piece,x,y):
    moves = []
    
    if(piece=='^'):
        if(x<7 and y<7):
            # temp.append(piece)
            moves.append([x+1,y+1])

        if(x<7 and y>0):
            # temp.append(piece)
            moves.append([x+1,y-1])

    elif(piece=='P'):
        if(x>0 and y<7):
            if(board[x-1][y+1]=='#' or board[x-1][y+1]=='-' or board[x-1][y+1]=='+' or board[x-1][y+1]=='|' or board[x-1][y+1]=='$' or board[x-1][y+1]=='^'):
                # temp.append(piece)
                moves.append([x-1,y+1])

        if(x>0 and y>0):
            if(board[x-1][y-1]=='#' or board[x-1][y-1]=='-' or board[x-1][y-1]=='+' or board[x-1][y-1]=='|' or board[x-1][y-1]=='$' or board[x-1][y-1]=='^'):
                # temp.append(piece)
                moves.append([x-1,y-1])

        if(x>0):
            if(board[x-1][y]=='0'):
                # temp.append(piece)
                moves.append([x-1,y])
            
            if(x==6):
                if(board[x-2][y]=='0'):
                    # temp.append(piece)
                    moves.append([x-2,y])     

    # print(moves)
    return moves

def AI_Rook(piece,x,y):
    moves = []
    if(piece=='#'):
        tempx=x
        while(tempx>0):
            tempx-=1
            temp = []
            if(board[tempx][y]=='#' or board[tempx][y]=='$' or board[tempx][y]=='|' or board[tempx][y]=='-' or board[tempx][y]=='+' or board[tempx][y]=='^' or board[tempx][y]=='Q' or board[tempx][y]=='K' or board[tempx][y]=='B' or board[tempx][y]=='k' or board[tempx][y]=='R' or board[tempx][y]=='P'):
                temp.append(tempx)
                temp.append(y)
                # temp.append(piece)
                moves.append(temp)
                break

            
            temp.append(tempx)
            temp.append(y)
            # temp.append(piece)
            moves.append(temp)

        tempx=x
        while(tempx<7):
            tempx+=1
            temp = []
            if(board[tempx][y]=='#' or board[tempx][y]=='$' or board[tempx][y]=='|' or board[tempx][y]=='-' or board[tempx][y]=='+' or board[tempx][y]=='^' or board[tempx][y]=='Q' or board[tempx][y]=='K' or board[tempx][y]=='B' or board[tempx][y]=='k' or board[tempx][y]=='R' or board[tempx][y]=='P'):
                temp.append(tempx)
                temp.append(y)
                # temp.append(piece)
                moves.append(temp)
                break

            
            temp.append(tempx)
            temp.append(y)
            # temp.append(piece)
            moves.append(temp)

        tempy=y
        while(tempy>0):
            tempy-=1
            temp = []
            if(board[x][tempy]=='#' or board[x][tempy]=='$' or board[x][tempy]=='|' or board[x][tempy]=='-' or board[x][tempy]=='+' or board[x][tempy]=='^' or board[x][tempy]=='Q' or board[x][tempy]=='K' or board[x][tempy]=='B' or board[x][tempy]=='k' or board[x][tempy]=='R' or board[x][tempy]=='P'):
                temp.append(x)
                temp.append(tempy)
                # temp.append(piece)
                moves.append(temp)
                break

            
            temp.append(x)
            temp.append(tempy)
            # temp.append(piece)
            moves.append(temp)
        
        tempy=y
        while(tempy<7):
            tempy+=1
            temp = []
            if(board[x][tempy]=='#' or board[x][tempy]=='$' or board[x][tempy]=='|' or board[x][tempy]=='-' or board[x][tempy]=='+' or board[x][tempy]=='^' or board[x][tempy]=='Q' or board[x][tempy]=='K' or board[x][tempy]=='B' or board[x][tempy]=='k' or board[x][tempy]=='R' or board[x][tempy]=='P'):
                temp.append(x)
                temp.append(tempy)
                # temp.append(piece)
                moves.append(temp)
                break

            
            temp.append(x)
            temp.append(tempy)
            # temp.append(piece)
            moves.append(temp)

    elif(piece=='R'):
        tempx=x
        while(tempx>0):
            tempx-=1
            if(board[tempx][y]=='#' or board[tempx][y]=='$' or board[tempx][y]=='|' or board[tempx][y]=='-' or board[tempx][y]=='+' or board[tempx][y]=='^'):
                # temp.append(piece)
                moves.append([tempx,y])
                break
            
            if(board[tempx][y]=='P' or board[tempx][y]=='R' or board[tempx][y]=='k' or board[tempx][y]=='B' or board[tempx][y]=='Q' or board[tempx][y]=='K'):
                break

            # temp.append(piece)
            moves.append([tempx,y])

        tempx=x
        while(tempx<7):
            tempx+=1
            temp = []
            if(board[tempx][y]=='#' or board[tempx][y]=='$' or board[tempx][y]=='|' or board[tempx][y]=='-' or board[tempx][y]=='+' or board[tempx][y]=='^'):
                # temp.append(piece)
                moves.append([tempx,y])
                break

            if(board[tempx][y]=='P' or board[tempx][y]=='R' or board[tempx][y]=='k' or board[tempx][y]=='B' or board[tempx][y]=='Q' or board[tempx][y]=='K'):
                break

            # temp.append(piece)
            moves.append([tempx,y])

        tempy=y
        while(tempy>0):
            tempy-=1
            if(board[x][tempy]=='#' or board[x][tempy]=='$' or board[x][tempy]=='|' or board[x][tempy]=='-' or board[x][tempy]=='+' or board[x][tempy]=='^'):
                # temp.append(piece)
                moves.append([x,tempy])
                break
            
            if(board[x][tempy]=='P' or board[x][tempy]=='R' or board[x][tempy]=='k' or board[x][tempy]=='B' or board[x][tempy]=='Q' or board[x][tempy]=='K'):
                break

            # temp.append(piece)
            moves.append([x,tempy])
        
        tempy=y
        while(tempy<7):
            tempy+=1
            if(board[x][tempy]=='#' or board[x][tempy]=='$' or board[x][tempy]=='|' or board[x][tempy]=='-' or board[x][tempy]=='+' or board[x][tempy]=='^'):
                # temp.append(piece)
                moves.append([x,tempy])
                break
            
            if(board[x][tempy]=='P' or board[x][tempy]=='R' or board[x][tempy]=='k' or board[x][tempy]=='B' or board[x][tempy]=='Q' or board[x][tempy]=='K'):
                break

            # temp.append(piece)
            moves.append([x,tempy])

    # print(moves)
    return moves

def AI_Bishop(piece,x,y):
    moves = []
    if(piece=='|'):
        tempx=x
        tempy=y
        while(tempx>0 and tempy>0):
            tempx-=1
            tempy-=1
            temp = []
            if(board[tempx][tempy]=='#' or board[tempx][tempy]=='$' or board[tempx][tempy]=='|' or board[tempx][tempy]=='-' or board[tempx][tempy]=='+' or board[tempx][tempy]=='^' or board[tempx][tempy]=='Q' or board[tempx][tempy]=='K' or board[tempx][tempy]=='B' or board[tempx][tempy]=='k' or board[tempx][tempy]=='R' or board[tempx][tempy]=='P'):
                temp.append(tempx)
                temp.append(tempy)
                # temp.append(piece)
                moves.append(temp)
                break

            
            temp.append(tempx)
            temp.append(tempy)
            # temp.append(piece)
            moves.append(temp)

        tempx=x
        tempy=y
        while(tempx<7 and tempy<7):
            tempx+=1
            tempy+=1
            temp = []
            if(board[tempx][tempy]=='#' or board[tempx][tempy]=='$' or board[tempx][tempy]=='|' or board[tempx][tempy]=='-' or board[tempx][tempy]=='+' or board[tempx][tempy]=='^' or board[tempx][tempy]=='Q' or board[tempx][tempy]=='K' or board[tempx][tempy]=='B' or board[tempx][tempy]=='k' or board[tempx][tempy]=='R' or board[tempx][tempy]=='P'):
                temp.append(tempx)
                temp.append(tempy)
                # temp.append(piece)
                moves.append(temp)
                break

            
            temp.append(tempx)
            temp.append(tempy)
            # temp.append(piece)
            moves.append(temp)

        tempx=x
        tempy=y
        while(tempx>0 and tempy<7):
            tempx-=1
            tempy+=1
            temp = []
            if(board[tempx][tempy]=='#' or board[tempx][tempy]=='$' or board[tempx][tempy]=='|' or board[tempx][tempy]=='-' or board[tempx][tempy]=='+' or board[tempx][tempy]=='^' or board[tempx][tempy]=='Q' or board[tempx][tempy]=='K' or board[tempx][tempy]=='B' or board[tempx][tempy]=='k' or board[tempx][tempy]=='R' or board[tempx][tempy]=='P'):
                temp.append(tempx)
                temp.append(tempy)
                # temp.append(piece)
                moves.append(temp)
                break

            
            temp.append(tempx)
            temp.append(tempy)
            # temp.append(piece)
            moves.append(temp)
        
        tempx=x
        tempy=y
        while(tempx<7 and tempy>0):
            tempx+=1
            tempy-=1
            temp = []
            if(board[tempx][tempy]=='#' or board[tempx][tempy]=='$' or board[tempx][tempy]=='|' or board[tempx][tempy]=='-' or board[tempx][tempy]=='+' or board[tempx][tempy]=='^' or board[tempx][tempy]=='Q' or board[tempx][tempy]=='K' or board[tempx][tempy]=='B' or board[tempx][tempy]=='k' or board[tempx][tempy]=='R' or board[tempx][tempy]=='P'):
                temp.append(tempx)
                temp.append(tempy)
                # temp.append(piece)
                moves.append(temp)
                break

            
            temp.append(tempx)
            temp.append(tempy)
            # temp.append(piece)
            moves.append(temp)

    if(piece=='B'):
        tempx=x
        tempy=y
        while(tempx>0 and tempy>0):
            tempx-=1
            tempy-=1
            if(board[tempx][tempy]=='#' or board[tempx][tempy]=='$' or board[tempx][tempy]=='|' or board[tempx][tempy]=='-' or board[tempx][tempy]=='+' or board[tempx][tempy]=='^'):
                # temp.append(piece)
                moves.append([tempx,tempy])
                break

            if(board[tempx][tempy]=='P' or board[tempx][tempy]=='R' or board[tempx][tempy]=='k' or board[tempx][tempy]=='B' or board[tempx][tempy]=='Q' or board[tempx][tempy]=='K'):
                break

            # temp.append(piece)
            moves.append([tempx,tempy])

        tempx=x
        tempy=y
        while(tempx<7 and tempy<7):
            tempx+=1
            tempy+=1
            if(board[tempx][tempy]=='#' or board[tempx][tempy]=='$' or board[tempx][tempy]=='|' or board[tempx][tempy]=='-' or board[tempx][tempy]=='+' or board[tempx][tempy]=='^'):
                # temp.append(piece)
                moves.append([tempx,tempy])
                break

            if(board[tempx][tempy]=='P' or board[tempx][tempy]=='R' or board[tempx][tempy]=='k' or board[tempx][tempy]=='B' or board[tempx][tempy]=='Q' or board[tempx][tempy]=='K'):
                break

            # temp.append(piece)
            moves.append([tempx,tempy])

        tempx=x
        tempy=y
        while(tempx>0 and tempy<7):
            tempx-=1
            tempy+=1
            if(board[tempx][tempy]=='#' or board[tempx][tempy]=='$' or board[tempx][tempy]=='|' or board[tempx][tempy]=='-' or board[tempx][tempy]=='+' or board[tempx][tempy]=='^'):
                # temp.append(piece)
                moves.append([tempx,tempy])
                break
            
            if(board[tempx][tempy]=='P' or board[tempx][tempy]=='R' or board[tempx][tempy]=='k' or board[tempx][tempy]=='B' or board[tempx][tempy]=='Q' or board[tempx][tempy]=='K'):
                break

            # temp.append(piece)
            moves.append([tempx,tempy])
        
        tempx=x
        tempy=y
        while(tempx<7 and tempy>0):
            tempx+=1
            tempy-=1
            if(board[tempx][tempy]=='#' or board[tempx][tempy]=='$' or board[tempx][tempy]=='|' or board[tempx][tempy]=='-' or board[tempx][tempy]=='+' or board[tempx][tempy]=='^'):
                # temp.append(piece)
                moves.append([tempx,tempy])
                break

            if(board[tempx][tempy]=='P' or board[tempx][tempy]=='R' or board[tempx][tempy]=='k' or board[tempx][tempy]=='B' or board[tempx][tempy]=='Q' or board[tempx][tempy]=='K'):
                break

            # temp.append(piece)
            moves.append([tempx,tempy])

    # print(moves)
    return moves

def AI_King(piece,x,y):
    moves = []
    if(piece=='+'):

        if(x>0):
            temp = []
            temp.append(x-1)
            temp.append(y)
            # temp.append(piece)
            moves.append(temp)
        
        if(y>0):
            temp = []
            temp.append(x)
            temp.append(y-1)
            # temp.append(piece)
            moves.append(temp)

        if(x<7):
            temp = []
            temp.append(x+1)
            temp.append(y)
            # temp.append(piece)
            moves.append(temp)

        if(y<7):
            temp = []
            temp.append(x)
            temp.append(y+1)
            # temp.append(piece)
            moves.append(temp)

        if(x>0 and y>0):
            temp = []
            temp.append(x-1)
            temp.append(y-1)
            # temp.append(piece)
            moves.append(temp)

        if(x<7 and y<7):
            temp = []
            temp.append(x+1)
            temp.append(y+1)
            # temp.append(piece)
            moves.append(temp)

        if(x>0 and y<7):
            temp = []
            temp.append(x-1)
            temp.append(y+1)
            # temp.append(piece)
            moves.append(temp)

        if(x<7 and y>0):
            temp = []
            temp.append(x+1)
            temp.append(y-1)
            # temp.append(piece)
            moves.append(temp)

    elif(piece=='K'):

        if(x>0):
            if(board[x-1][y]!='P' and board[x-1][y]!='R' and board[x-1][y]!='k' and board[x-1][y]!='B' and board[x-1][y]!='Q' and board[x-1][y]!='K'):
            # temp.append(piece)
                moves.append([x-1,y])
        
        if(y>0):
           if(board[x][y-1]!='P' and board[x][y-1]!='R' and board[x][y-1]!='k' and board[x][y-1]!='B' and board[x][y-1]!='Q' and board[x][y-1]!='K'):
                # temp.append(piece)
                moves.append([x,y-1])

        if(x<7):
            if(board[x+1][y]!='P' and board[x+1][y]!='R' and board[x+1][y]!='k' and board[x+1][y]!='B' and board[x+1][y]!='Q' and board[x+1][y]!='K'):
                # temp.append(piece)
                moves.append([x+1,y])

        if(y<7):
            if(board[x][y+1]!='P' and board[x][y+1]!='R' and board[x][y+1]!='k' and board[x][y+1]!='B' and board[x][y+1]!='Q' and board[x][y+1]!='K'):
                # temp.append(piece)
                moves.append([x,y+1])

        if(x>0 and y>0):
            if(board[x-1][y-1]!='P' and board[x-1][y-1]!='R' and board[x-1][y-1]!='k' and board[x-1][y-1]!='B' and board[x-1][y-1]!='Q' and board[x-1][y-1]!='K'):
                # temp.append(piece)
                moves.append([x-1,y-1])

        if(x<7 and y<7):
            if(board[x+1][y+1]!='P' and board[x+1][y+1]!='R' and board[x+1][y+1]!='k' and board[x+1][y+1]!='B' and board[x+1][y+1]!='Q' and board[x+1][y+1]!='K'):
                # temp.append(piece)
                moves.append([x+1,y+1])

        if(x>0 and y<7):
            if(board[x-1][y+1]!='P' and board[x-1][y+1]!='R' and board[x-1][y+1]!='k' and board[x-1][y+1]!='B' and board[x-1][y+1]!='Q' and board[x-1][y+1]!='K'):
                # temp.append(piece)
                moves.append([x-1,y+1])

        if(x<7 and y>0):
            if(board[x+1][y-1]!='P' and board[x+1][y-1]!='R' and board[x+1][y-1]!='k' and board[x+1][y-1]!='B' and board[x+1][y-1]!='Q' and board[x+1][y-1]!='K'):
                # temp.append(piece)
                moves.append([x+1,y-1])


    # print(moves)
    return moves

def AI_Queen(piece,x,y):
    moves = []
    if(piece=='-'):
        tempx=x
        tempy=y
        while(tempx>0 and tempy>0):
            tempx-=1
            tempy-=1
            temp = []
            if(board[tempx][tempy]=='#' or board[tempx][tempy]=='$' or board[tempx][tempy]=='|' or board[tempx][tempy]=='-' or board[tempx][tempy]=='+' or board[tempx][tempy]=='^' or board[tempx][tempy]=='Q' or board[tempx][tempy]=='K' or board[tempx][tempy]=='B' or board[tempx][tempy]=='k' or board[tempx][tempy]=='R' or board[tempx][tempy]=='P'):
                temp.append(tempx)
                temp.append(tempy)
                # temp.append(piece)
                moves.append(temp)
                break

            
            temp.append(tempx)
            temp.append(tempy)
            # temp.append(piece)
            moves.append(temp)

        tempx=x
        tempy=y
        while(tempx<7 and tempy<7):
            tempx+=1
            tempy+=1
            temp = []
            if(board[tempx][tempy]=='#' or board[tempx][tempy]=='$' or board[tempx][tempy]=='|' or board[tempx][tempy]=='-' or board[tempx][tempy]=='+' or board[tempx][tempy]=='^' or board[tempx][tempy]=='Q' or board[tempx][tempy]=='K' or board[tempx][tempy]=='B' or board[tempx][tempy]=='k' or board[tempx][tempy]=='R' or board[tempx][tempy]=='P'):
                temp.append(tempx)
                temp.append(tempy)
                # temp.append(piece)
                moves.append(temp)
                break

            
            temp.append(tempx)
            temp.append(tempy)
            # temp.append(piece)
            moves.append(temp)

        tempx=x
        tempy=y
        while(tempx>0 and tempy<7):
            tempx-=1
            tempy+=1
            temp = []
            if(board[tempx][tempy]=='#' or board[tempx][tempy]=='$' or board[tempx][tempy]=='|' or board[tempx][tempy]=='-' or board[tempx][tempy]=='+' or board[tempx][tempy]=='^' or board[tempx][tempy]=='Q' or board[tempx][tempy]=='K' or board[tempx][tempy]=='B' or board[tempx][tempy]=='k' or board[tempx][tempy]=='R' or board[tempx][tempy]=='P'):
                temp.append(tempx)
                temp.append(tempy)
                # temp.append(piece)
                moves.append(temp)
                break

            
            temp.append(tempx)
            temp.append(tempy)
            # temp.append(piece)
            moves.append(temp)
        
        tempx=x
        tempy=y
        while(tempx<7 and tempy>0):
            tempx+=1
            tempy-=1
            temp = []
            if(board[tempx][tempy]=='#' or board[tempx][tempy]=='$' or board[tempx][tempy]=='|' or board[tempx][tempy]=='-' or board[tempx][tempy]=='+' or board[tempx][tempy]=='^' or board[tempx][tempy]=='Q' or board[tempx][tempy]=='K' or board[tempx][tempy]=='B' or board[tempx][tempy]=='k' or board[tempx][tempy]=='R' or board[tempx][tempy]=='P'):
                temp.append(tempx)
                temp.append(tempy)
                # temp.append(piece)
                moves.append(temp)
                break

            
            temp.append(tempx)
            temp.append(tempy)
            # temp.append(piece)
            moves.append(temp)

        tempx=x
        while(tempx>0):
            tempx-=1
            temp = []
            if(board[tempx][y]=='#' or board[tempx][y]=='$' or board[tempx][y]=='|' or board[tempx][y]=='-' or board[tempx][y]=='+' or board[tempx][y]=='^' or board[tempx][y]=='Q' or board[tempx][y]=='K' or board[tempx][y]=='B' or board[tempx][y]=='k' or board[tempx][y]=='R' or board[tempx][y]=='P'):
                temp.append(tempx)
                temp.append(y)
                # temp.append(piece)
                moves.append(temp)
                break

            
            temp.append(tempx)
            temp.append(y)
            # temp.append(piece)
            moves.append(temp)

        tempx=x
        while(tempx<7):
            tempx+=1
            temp = []
            if(board[tempx][y]=='#' or board[tempx][y]=='$' or board[tempx][y]=='|' or board[tempx][y]=='-' or board[tempx][y]=='+' or board[tempx][y]=='^' or board[tempx][y]=='Q' or board[tempx][y]=='K' or board[tempx][y]=='B' or board[tempx][y]=='k' or board[tempx][y]=='R' or board[tempx][y]=='P'):
                temp.append(tempx)
                temp.append(y)
                # temp.append(piece)
                moves.append(temp)
                break

            
            temp.append(tempx)
            temp.append(y)
            # temp.append(piece)
            moves.append(temp)

        tempy=y
        while(tempy>0):
            tempy-=1
            temp = []
            if(board[x][tempy]=='#' or board[x][tempy]=='$' or board[x][tempy]=='|' or board[x][tempy]=='-' or board[x][tempy]=='+' or board[x][tempy]=='^' or board[x][tempy]=='Q' or board[x][tempy]=='K' or board[x][tempy]=='B' or board[x][tempy]=='k' or board[x][tempy]=='R' or board[x][tempy]=='P'):
                temp.append(x)
                temp.append(tempy)
                # temp.append(piece)
                moves.append(temp)
                break

            
            temp.append(x)
            temp.append(tempy)
            # temp.append(piece)
            moves.append(temp)
        
        tempy=y
        while(tempy<7):
            tempy+=1
            temp = []
            if(board[x][tempy]=='#' or board[x][tempy]=='$' or board[x][tempy]=='|' or board[x][tempy]=='-' or board[x][tempy]=='+' or board[x][tempy]=='^' or board[x][tempy]=='Q' or board[x][tempy]=='K' or board[x][tempy]=='B' or board[x][tempy]=='k' or board[x][tempy]=='R' or board[x][tempy]=='P'):
                temp.append(x)
                temp.append(tempy)
                # temp.append(piece)
                moves.append(temp)
                break

            
            temp.append(x)
            temp.append(tempy)
            # temp.append(piece)
            moves.append(temp)

    elif(piece=='Q'):
        tempx=x
        tempy=y
        while(tempx>0 and tempy>0):
            tempx-=1
            tempy-=1
            if(board[tempx][tempy]=='#' or board[tempx][tempy]=='$' or board[tempx][tempy]=='|' or board[tempx][tempy]=='-' or board[tempx][tempy]=='+' or board[tempx][tempy]=='^'):
                # temp.append(piece)
                moves.append([tempx,tempy])
                break

            if(board[tempx][tempy]=='P' or board[tempx][tempy]=='R' or board[tempx][tempy]=='k' or board[tempx][tempy]=='B' or board[tempx][tempy]=='Q' or board[tempx][tempy]=='K'):
                break

            # temp.append(piece)
            moves.append([tempx,tempy])

        tempx=x
        tempy=y
        while(tempx<7 and tempy<7):
            tempx+=1
            tempy+=1
            if(board[tempx][tempy]=='#' or board[tempx][tempy]=='$' or board[tempx][tempy]=='|' or board[tempx][tempy]=='-' or board[tempx][tempy]=='+' or board[tempx][tempy]=='^'):
                # temp.append(piece)
                moves.append([tempx,tempy])
                break

            if(board[tempx][tempy]=='P' or board[tempx][tempy]=='R' or board[tempx][tempy]=='k' or board[tempx][tempy]=='B' or board[tempx][tempy]=='Q' or board[tempx][tempy]=='K'):
                break

            # temp.append(piece)
            moves.append([tempx,tempy])

        tempx=x
        tempy=y
        while(tempx>0 and tempy<7):
            tempx-=1
            tempy+=1
            if(board[tempx][tempy]=='#' or board[tempx][tempy]=='$' or board[tempx][tempy]=='|' or board[tempx][tempy]=='-' or board[tempx][tempy]=='+' or board[tempx][tempy]=='^'):
                # temp.append(piece)
                moves.append([tempx,tempy])
                break
            
            if(board[tempx][tempy]=='P' or board[tempx][tempy]=='R' or board[tempx][tempy]=='k' or board[tempx][tempy]=='B' or board[tempx][tempy]=='Q' or board[tempx][tempy]=='K'):
                break

            # temp.append(piece)
            moves.append([tempx,tempy])
        
        tempx=x
        tempy=y
        while(tempx<7 and tempy>0):
            tempx+=1
            tempy-=1
            if(board[tempx][tempy]=='#' or board[tempx][tempy]=='$' or board[tempx][tempy]=='|' or board[tempx][tempy]=='-' or board[tempx][tempy]=='+' or board[tempx][tempy]=='^'):
                # temp.append(piece)
                moves.append([tempx,tempy])
                break

            if(board[tempx][tempy]=='P' or board[tempx][tempy]=='R' or board[tempx][tempy]=='k' or board[tempx][tempy]=='B' or board[tempx][tempy]=='Q' or board[tempx][tempy]=='K'):
                break

            # temp.append(piece)
            moves.append([tempx,tempy])


        tempx=x
        while(tempx>0):
            tempx-=1
            if(board[tempx][y]=='#' or board[tempx][y]=='$' or board[tempx][y]=='|' or board[tempx][y]=='-' or board[tempx][y]=='+' or board[tempx][y]=='^'):
                # temp.append(piece)
                moves.append([tempx,y])
                break
            
            if(board[tempx][y]=='P' or board[tempx][y]=='R' or board[tempx][y]=='k' or board[tempx][y]=='B' or board[tempx][y]=='Q' or board[tempx][y]=='K'):
                break

            # temp.append(piece)
            moves.append([tempx,y])

        tempx=x
        while(tempx<7):
            tempx+=1
            temp = []
            if(board[tempx][y]=='#' or board[tempx][y]=='$' or board[tempx][y]=='|' or board[tempx][y]=='-' or board[tempx][y]=='+' or board[tempx][y]=='^'):
                # temp.append(piece)
                moves.append([tempx,y])
                break

            if(board[tempx][y]=='P' or board[tempx][y]=='R' or board[tempx][y]=='k' or board[tempx][y]=='B' or board[tempx][y]=='Q' or board[tempx][y]=='K'):
                break

            # temp.append(piece)
            moves.append([tempx,y])

        tempy=y
        while(tempy>0):
            tempy-=1
            if(board[x][tempy]=='#' or board[x][tempy]=='$' or board[x][tempy]=='|' or board[x][tempy]=='-' or board[x][tempy]=='+' or board[x][tempy]=='^'):
                # temp.append(piece)
                moves.append([x,tempy])
                break
            
            if(board[x][tempy]=='P' or board[x][tempy]=='R' or board[x][tempy]=='k' or board[x][tempy]=='B' or board[x][tempy]=='Q' or board[x][tempy]=='K'):
                break

            # temp.append(piece)
            moves.append([x,tempy])
        
        tempy=y
        while(tempy<7):
            tempy+=1
            if(board[x][tempy]=='#' or board[x][tempy]=='$' or board[x][tempy]=='|' or board[x][tempy]=='-' or board[x][tempy]=='+' or board[x][tempy]=='^'):
                # temp.append(piece)
                moves.append([x,tempy])
                break
            
            if(board[x][tempy]=='P' or board[x][tempy]=='R' or board[x][tempy]=='k' or board[x][tempy]=='B' or board[x][tempy]=='Q' or board[x][tempy]=='K'):
                break

            # temp.append(piece)
            moves.append([x,tempy])


    # print(moves)
    return moves

def AI_Knight(piece,x,y):
    moves = []
    if(piece=='$'):

        if(x>0):
            tempx=x-1
            if(tempx>0):
                if(y>0):
                    temp = []
                    temp.append(tempx-1)
                    temp.append(y-1)
                    # temp.append(piece)
                    moves.append(temp)

                if(y<7):
                    temp = []
                    temp.append(tempx-1)
                    temp.append(y+1)
                    # temp.append(piece)
                    moves.append(temp)
        
        if(x<7):
            tempx=x+1
            if(tempx<7):
                if(y>0):
                    temp = []
                    temp.append(tempx+1)
                    temp.append(y-1)
                    # temp.append(piece)
                    moves.append(temp)

                if(y<7):
                    temp = []
                    temp.append(tempx+1)
                    temp.append(y+1)
                    # temp.append(piece)
                    moves.append(temp)

            if(y<7):
                tempy=y+1
                if(tempy<7):
                    if(x>0):
                        temp = []
                        temp.append(x-1)
                        temp.append(tempy+1)
                        # temp.append(piece)
                        moves.append(temp)

                    if(x<7):
                        temp = []
                        temp.append(x+1)
                        temp.append(tempy+1)
                        # temp.append(piece)
                        moves.append(temp)

            if(y>0):
                tempy=y-1
                if(tempy>0):
                    if(x>0):
                        temp = []
                        temp.append(x-1)
                        temp.append(tempy-1)
                        # temp.append(piece)
                        moves.append(temp)

                    if(x<7):
                        temp = []
                        temp.append(x+1)
                        temp.append(tempy-1)
                        # temp.append(piece)
                        moves.append(temp)
    
    elif(piece=='k'):

        if(x>0):
            tempx=x-1
            if(tempx>0):
                tempx-=1
                if(y>0):
                    # temp.append(piece)
                    if(board[tempx][y-1]!='P' and board[tempx][y-1]!='R' and board[tempx][y-1]!='k' and board[tempx][y-1]!='B' and board[tempx][y-1]!='Q' and board[tempx][y-1]!='K'):
                        moves.append([tempx,y-1])

                if(y<7):
                    # temp.append(piece)
                    if(board[tempx][y+1]!='P' and board[tempx][y+1]!='R' and board[tempx][y+1]!='k' and board[tempx][y+1]!='B' and board[tempx][y+1]!='Q' and board[tempx][y+1]!='K'):
                        moves.append([tempx,y+1])
        
        if(x<7):
            tempx=x+1
            if(tempx<7):
                tempx+=1
                if(y>0):
                    # temp.append(piece)
                    if(board[tempx][y-1]!='P' and board[tempx][y-1]!='R' and board[tempx][y-1]!='k' and board[tempx][y-1]!='B' and board[tempx][y-1]!='Q' and board[tempx][y-1]!='K'):
                        moves.append([tempx,y-1])

                if(y<7):
                    # temp.append(piece)
                    if(board[tempx][y+1]!='P' and board[tempx][y+1]!='R' and board[tempx][y+1]!='k' and board[tempx][y+1]!='B' and board[tempx][y+1]!='Q' and board[tempx][y+1]!='K'):
                        moves.append([tempx,y+1])

        if(y<7):
            tempy=y+1
            if(tempy<7):
                tempy+=1
                if(x>0):
                    if(board[x-1][tempy]!='P' and board[x-1][tempy]!='R' and board[x-1][tempy]!='k' and board[x-1][tempy]!='B' and board[x-1][tempy]!='Q' and board[x-1][tempy]!='K'):
                        moves.append([x-1,tempy])

                if(x<7):
                    if(board[x+1][tempy]!='P' and board[x+1][tempy]!='R' and board[x+1][tempy]!='k' and board[x+1][tempy]!='B' and board[x+1][tempy]!='Q' and board[x+1][tempy]!='K'):
                        moves.append([x+1,tempy])

            if(y>0):
                tempy=y-1
                if(tempy>0):
                    tempy-=1
                    if(x>0):
                        if(board[x-1][tempy]!='P' and board[x-1][tempy]!='R' and board[x-1][tempy]!='k' and board[x-1][tempy]!='B' and board[x-1][tempy]!='Q' and board[x-1][tempy]!='K'):
                            moves.append([x-1,tempy])

                    if(x<7):
                        if(board[x+1][tempy]!='P' and board[x+1][tempy]!='R' and board[x+1][tempy]!='k' and board[x+1][tempy]!='B' and board[x+1][tempy]!='Q' and board[x+1][tempy]!='K'):
                            moves.append([x+1,tempy])
            

    # print(moves)
    return moves

def compare(board,temp):
    for x in range(board.shape[0]):
        for y in range(board.shape[1]):
            if(board[x][y]!=temp[x][y]):
                return True
    return False

def CheckMate(board):
    global ending
    player=0
    ai=0
    for x in range(8):
        for y in range(8):
            if(board[x][y]=='+'):
                player+=1

            if(board[x][y]=='K'):
                ai+=1

    if(player==0):
        print("Computer Won")
        ending=True
    elif(ai==0):
        print("Player Won")
        ending=True

def CheckPawn(board):
    for x in range(8):
        for y in range(8):
            if(board[x][y]=='^' and x==7):
                num = random.uniform(0,1)
                if(num>0.5):
                    board[x][y]='-'
                elif(num>0.25):
                    board[x][y]='|'
                else:
                    board[x][y]='#'
            
            elif(board[x][y]=='P' and x==0):
                num = random.uniform(0,1)
                if(num>0.5):
                    board[x][y]='Q'
                elif(num>0.25):
                    board[x][y]='B'
                else:
                    board[x][y]='R'






def enPess(position):
    for key,value in locx.items():
        # print(key,value)
        if(value==position[0]):
            player.startx=key
            player.starty=int(position[1])-1
        if(value==position[2]):
            player.endx=key
            player.endy=int(position[3])-1
    
    if((board[player.starty+2][player.startx+1] in piecesW) or (board[player.starty+2][player.startx-1] in piecesW)):
        if(board[player.starty+2][player.startx+1] in piecesW):
            board[player.starty+1][player.startx]=board[player.starty+2][player.startx+1]
            board[player.starty+2][player.startx+1]="0"
            board[player.starty+2][player.startx]="0"
        elif(board[player.starty+2][player.startx-1] in piecesW):
            board[player.starty+1][player.startx]=board[player.starty+2][player.startx-1]
            board[player.starty+2][player.startx-1]="0"
            board[player.starty+2][player.startx]="0"

    elif((board[player.starty-2][player.startx+1] in piecesB) or (board[player.starty-2][player.startx-1] in piecesB)):
        if(board[player.starty-2][player.startx+1] in piecesB):
            board[player.starty-1][player.startx]=board[player.starty-2][player.startx+1]
            board[player.starty-2][player.startx+1]="0"
            board[player.starty-2][player.startx]="0"
        elif(board[player.starty-2][player.startx-1] in piecesB):
            board[player.starty-1][player.startx]=board[player.starty-2][player.startx-1]
            board[player.starty-2][player.startx-1]="0"
            board[player.starty-2][player.startx]="0"



def chess():
    global ending
    while(1):

        # print ("Player One move")
        # player1=input()
        # movePiece(player1)
        global enPassant
       
        #while(np.array_equal(board,newboard)==1):
        
        enPassant=0
        temp_board=copy.deepcopy(board)
        print ("Player Two move")
        player2=input()
        movePiece(player2)

        if(compare(board,temp_board)==False):
            print("Invalid Move")
            continue

        if(enPassant==1):
            enPess(player2)
            #print(board)
            continue
        
        CheckPawn(board)
        CheckMate(board)
        if(ending==True):
            break

        #print(board)
        
        
        
        print("AI Move")
        print()
        print()
        AI_move(board)
        #print(board)
        #print(board)
        

    
player=Player()
chess()

# if("0" in piecesW):
#     print("#")
