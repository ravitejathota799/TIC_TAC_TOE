theBoard={'7':'','8':'','9':'',
          '4':'','5':'','6':'',
          '1':'','2':'','3':''}
board_keys=[]
for key in theBoard:
    board_keys.append(key)
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4']+ '|' + board['5']+ '|' + board['6'])
    print('-+-+-')
    print(board['1']+ '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
def game():
    turn='x'
    count=0
    for i in range(10):
        printBoard(theBoard)
        print("Its your turn,"+turn+".move to which place?")
        move=input()
        if(theBoard[move]==''):
            theBoard[move]=turn
            count+=1
            #print(count)
        else:
            print("The place is already filled select another location")
            continue
        if(count>=5):
            if(theBoard['7']==theBoard['8']==theBoard['9']!=''):#CHECKING HORIZONTAL
                printBoard(theBoard)
                print('\nGame over')
                print("player"+" "+turn+" "+"has won the match")
                break
            elif(theBoard['4']==theBoard['5']==theBoard['6']!=''):#CHECKING HORIZONTAL
                printBoard(theBoard)
                print('\nGame over')
                print("player"+" "+turn+" "+"has won the match")
                break
            elif(theBoard['1']==theBoard['2']==theBoard['3']!=''):#CHECKING HORIZONTAL
                printBoard(theBoard)
                print('\nGame over')
                print("player"+" "+turn+" "+"has won the match")
                break
            elif(theBoard['1']==theBoard['4']==theBoard['7']!=''):#CHECKING VERTICAL
                printBoard(theBoard)
                print('\nGame over')
                print("player"+" "+turn+" "+"has won the match")
                break
            elif(theBoard['2']==theBoard['5']==theBoard['8']!=''):#CHECKING VERTICAL
                printBoard(theBoard)
                print('\nGame over')
                print("player"+" "+turn+" "+"has won the match")
                break
            elif(theBoard['3']==theBoard['6']==theBoard['9']!=''):#CHECKING VERTICAL
                printBoard(theBoard)
                print('\nGame over')
                print("player"+" "+turn+" "+"has won the match")
                break
            elif(theBoard['7']==theBoard['5']==theBoard['3']!=''):#CHECKING DIAGONAL
                printBoard(theBoard)
                print('\nGame over')
                print("player"+" "+turn+" "+"has won the match")
                break
            elif(theBoard['1']==theBoard['5']==theBoard['9']!=''):#CHECKING DIAGONAL
                printBoard(theBoard)
                print('\nGame over')
                print("player"+" "+turn+" "+"has won the match")
                break
            if(count==9):
                print("Game over\n")
        if(turn=='x'):
            turn='o'
        else:
            turn='x'
    restart=input("do u want to continue")
    if(restart=='y' or restart=='Y'):
        for key in board_keys:
            theBoard[key]=""
        game()
if __name__=="__main__":
    game()
            
