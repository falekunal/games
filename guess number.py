import random

cnum = random.randint(1, 100)

print(cnum)
unum = None
guesses = 0

while (unum != cnum):
    unum = int(input("please enter a number between 1 to 100\n"))
    guesses += 1
    if (cnum == unum):
        print('you guessed the correct value')

    elif (cnum < unum):
        print(f'the guessed number is too high, please enter smaller number')


    elif (cnum > unum):
        print(f'the guessed number is too low, please enter larger number')

print(f'you used {guesses} guesses to reach the correct value ')


with open('his.txt') as f:
    h= f.readline()
    hisco = int(f.readline())



if (guesses < hisco):
    print('you made a hiscore!')
    with open('his.txt', 'w') as f:
        hisco=f.write(f'''you made a Hiscore       
 {str(guesses)}''')


