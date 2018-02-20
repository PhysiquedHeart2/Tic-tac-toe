import random#this allows me to use the random functions
win="yes"#this is useless(kinda anyway)
List=["?","?","?","?","?","?","?","?","?"]#this is this is the list(which is the table)
def board():#this creates the board function
    print("""
                """,List[0],"|",List[1],"|",List[2],"""
	     -----------------
	        """,List[3],"|",List[4],"|",List[5],"""
	     -----------------
	        """,List[6],"|",List[7],"|",List[8],"""
	        """)#this is the game board
board()#this prints out the board  
input1=0
turn=["x","o"]#this decides what the symbol will change to 
def Player1():
    input1=int(input("please type the position you want : "))
    input1=input1 - 1
    double_check()
    List[input1]="x"#this allows the user to input there number and then allocate the possition
    print(List[input1])
    board()#this prints the board
    
def Player2():  
    input1=random.randint(0,8)
    check()#this prints the checl thing
    List[input1]="O"
    print(input1)
    board()
turn=0
def opp(objects):
    List_Return = objects
    turn=0
    while turn <=1:
        turn=turn+1
        if List_Return == "x":
            print("You won")
            win=True
            break
        elif List_Return == "o":
            print("You lost")
        break
def double_check():
    if input1 == 1:
        print("that slot is taken try again")
        Player1()
def check():
    if List[0] == List[1] and List[1] == List[2]:
        opp(List[0])
    if List[3] == List[4] and List[4] == List[5]:
        opp(List[3])
    if List[6] == List[7] and List[7] == List[8]:
        opp(List[6])
    if List[0] == List[3] and List[3] == List[6]:
        opp(List[0])
    if List[1] == List[4] and List[4] == List[7]:
        opp(List[1])
    if List[2] == List[5] and List[5] == List[8]:
        opp(List[2])
    if List[0] == List[4] and List[4] == List[8]:
        opp(List[0])
    if List[2] == List[4] and List[4] == List[6]:
        opp(List[2])

while True:
    if win != True:
        double_check()
        Player1()
        check()
        Player2()
    else:
        break

    
    
    
