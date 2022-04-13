import random

def gameWin(comp, you):
    if comp == you:
        return None

    elif comp == "s":
        if you == "w":
            return False
        elif you=="g":
            return True

    elif comp == 'w':
        if you=='g':
            return False
        elif you=='s':
            return True

    elif comp == 'g':
        if you== 's':
            return False
        elif you== 'w':
            return True

print("comp turn : Snake(s)  or Water(w) or Gun(g)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you =input("your turn : Snake(s)  or Water(w) or Gun(g)?")
a = gameWin(comp, you)

print(f"comp chose {comp}")
print(f"you chose {you}")

if a== None:
    print("The Game Is Tie")
elif a:
    print("ypu won")
else:
    print("you lose")




