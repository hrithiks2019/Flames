import random
import pyautogui
import time

pscore, cscore = 0, 0


def genran():
    print('Move Your Mouse For Better Results and randomity')
    sx, sy = pyautogui.position()
    rn = random.seed((sx + sy))
    return rn


def p1():
    p(pscore)
    c(cscore)


def c1():
    c(cscore)
    p(pscore)


def toss(ch):
    genran()
    fp = (random.choice([1, 2, 3, 4, 5, 6]))
    if fp % 2 == 0:
        if ch == 'even':
            print('Player Wins the toss \n')
            decision()
        else:
            print('Computer Wins the toss and chooses bowling \n')
            p1()
    else:
        if ch == 'odd':
            print('Player Wins the toss \n')
            decision()
        else:
            print('Computer Wins the toss and chooses bowling \n')
            p1()


def decision():
    d = str(input('Choose your Option Bating or Bowling \n '))
    if d == 'bowling':
        c1()
    else:
        p1()


def p(pscore):
    X = True
    print('player is now batting \n')
    time.sleep(0.5)
    print('Good Luck Player \n')
    while X:
        time.sleep(0.5)
        genran()
        PR = int(input('Enter the Batting Run \n'))
        CR = random.choice([1, 2, 3, 4, 5, 6])
        if PR == CR:
            X = False
            print(name, 'OUT \n Better Luck Next Time \n')
            print('you scored ', pscore, 'runs')

        else:
            pscore += PR


def c(cscore):
    Y = True
    print('Computer is now batting \n')
    time.sleep(0.5)
    print('Good Luck Player \n')
    while Y:
        genran()
        time.sleep(0.5)
        PR = int(input('Enter the Bowling Run \n'))
        CR = random.choice([1, 2, 3, 4, 5, 6])
        if CR == PR:
            Y = False
            print('Computer OUT \n Samugam Periya Pudingi tha pola')
            print('computer scored ', cscore, 'runs')

        else:
            cscore += CR


print('Welcome to hand cricket simulator \n')
time.sleep(0.5)
name = str(input('Enter your name \n'))
time.sleep(0.5)
choice = str(input('Choose your Side ODD or EVEN'))
toss(choice)

if pscore > cscore:
    print('Match has Ended')
    time.sleep(0.5)
    print('The Winner is ', name)
elif pscore == cscore:
    print('Match has Ended')
    time.sleep(0.5)
    print('The Match is an Draw')

else:
    print('Match has Ended')
    time.sleep(0.5)
    print('The Winner is Computer')
time.sleep(0.5)
print('thanks for using this programs , play again')
