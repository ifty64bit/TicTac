import random

form=[
    "-","-","-",
    "-","-","-",
    "-","-","-"
    ]
def draw():
    print(form[0]+" | "+form[1]+" | "+form[2])
    print(form[3]+" | "+form[4]+" | "+form[5])
    print(form[6]+" | "+form[7]+" | "+form[8])

def winnerX():
    if (form[0]==form[1]==form[2]=='X')|(form[3]==form[4]==form[5]=='X')|(form[6]==form[7]==form[8]=='X'):
        return True
    elif (form[0]==form[3]==form[6]=='X')|(form[1]==form[4]==form[7]=='X')|(form[2]==form[5]==form[8]=='X'):
        return True
    elif (form[0]==form[4]==form[8]=='X')|(form[2]==form[4]==form[6]=='X'):
        return True
    else:
        return False

def winnerO():
    if (form[0]==form[1]==form[2]=='O')|(form[3]==form[4]==form[5]=='O')|(form[6]==form[7]==form[8]=='O'):
        return True
    elif (form[0]==form[3]==form[6]=='O')|(form[1]==form[4]==form[7]=='O')|(form[2]==form[5]==form[8]=='O'):
        return True
    elif (form[0]==form[4]==form[8]=='O')|(form[2]==form[4]==form[6]=='O'):
        return True
    else:
        return False

def Start():
    while True:
        draw()
        if winnerX():
            print("You Won")
            break
        elif winnerO():
            print("You Lost")
            break
        while True:
            x=int(input("Please Chose 1-9:\n"))
            if form[x-1]!='-':
                print("Number Already Taken, Try Another")
            else:
                form[x-1]='X'
                break
        while True:
            x=random.randint(0,8)
            if form[x]=='-':
                form[x]='O'
                break

Start()
