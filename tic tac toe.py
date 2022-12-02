import random
print("Welcome To Tic Tac Toe")
print("-------------------------")
possibleNumbers=[1,2,3,4,5,6,7,8]
gameBoard=[[1,2,3], [4,5,6], [7,8,9]]
rows=3
cols=3
def printGameBoard():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|",end="")
        for y in range(cols):
            print("", gameBoard[x][y], end="|")
    print("\n+---+---+---+")
printGameBoard()
def modifyArray(num,turn):
    num-=1
    if (num==0):
        gameBoard[0][0]=turn
    elif(num==1):
        gameBoard[0][1]=turn
    elif(num==2):
        gameBoard[0][2]=turn
    elif(num==3):
        gameBoard[1][0]=turn
    elif(num==4):
        gameBoard[1][1]=turn
    elif(num==5):
        gameBoard[1][2]=turn
    elif(num==6):
        gameBoard[2][0]=turn
    elif(num==7):
        gameBoard[2][1]=turn
    elif(num==8):
        gameBoard[2][2]=turn
def checkForWinner(gameBoard):
    if(gameBoard[0][0]=='X' and gameBoard[0][1]=='X' and gameBoard[0][2]=='X'):
        print("X has won!")
        return "X"
    elif(gameBoard[0][0]=='O' and gameBoard[0][1]=='O' and gameBoard[0][2]=='O'):
        print("O has won!")
        return "O"
    elif(gameBoard[0][0]=='X' and gameBoard[1][0]=='X' and gameBoard[2][0]=='X'):
        print("X has won!")
        return "X"
    elif(gameBoard[0][0]=='O' and gameBoard[1][0]=='O' and gameBoard[2][0]=='O'):
        print("O has won!")
        return "O"
    elif(gameBoard[0][0]=='X' and gameBoard[1][1]=='X' and gameBoard[2][2]=='X'):
        print("X has won!")
        return "X"
    elif(gameBoard[0][0]=='O' and gameBoard[1][1]=='O' and gameBoard[2][2]=='O'):
        print("O has won!")
        return "O"


        
    
    leaveloop=False
    
    turncounter=0
    while(leaveloop==False):
        if(turnCounter%2==1):
            printGameBoard()
            numberpicked=int(input("\nChoose a number [1-9]"))
            if(numberpicked>=1 or numberpicked<=9):
                modifyArray(numberpicked,'X')
                possibleNumbers.remove(numberpicked)
            else:
                print("Invalid.Please Try Again")
                turncounter+=1
        else:
            while(True):
                cpuchoice=random.choice(possibleNumbers)
                print("\nCpu Choice:",cpuchoice)
                if(cpuchoice in possiblenumbers):
                    modifyArray(cpuchoice,'O')
                    possiblenumbers.remove(cpuchoice)
                    turncounter+=1
                    break
                 
        
            
            
        