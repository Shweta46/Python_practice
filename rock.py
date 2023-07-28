#make a game
#use random.choice and
# choose a variable between rock, paper and scissors
#do not print it
#ask the user, what they want to choose: R, P or S
#as soon as you enter, the program will let you know who won that round
#put it inside the while loop to play 10 times, whosoever wins the game majority of the time with the most score wins the whole inning

import random
print("Welcome to the GAME of ROCK, PAPER and SCISSOR!!!")
n = 2 # n is the chances available
c = 0
i = 0
p = 0
j = 100
# i is the number you are taking
# c is the score for computer
# p is the score for player
def again1():
    global i, c, p, n
    i = 0
    c = 0
    p = 0
    n = 2
def makeit():
    global i
    i = 100

def decider(c,p,i,j):
    if c > p:
        print("You lose :'(")
        print("You lost by", c-p, "point")
        again = int(input("Want to play again?\n 1. 1 for Yes\n 2. 0 for No\n"))
        if again == 1:
            again1()
        elif again == 0:
            makeit()
            print("Thank you for playing...")

    elif c < p:
        print("You WIN!!!")
        print("You won by", p - c, "point")
        again = int(input("Want to play again?\n 1. 1 for Yes\n 2. 0 for No\n"))
        if again == 1:
            again1()
        elif again == 0:
            makeit()
            print("Thank you for playing...")

    elif c == p:
        print("Its a tie!!!")
        again = int(input("Want to play again?\n 1. 1 for Yes\n 2. 0 for No\n"))
        if again == 1:
            again1()
        elif again == 0:
            makeit()
            print("Thank you for playing...")

def chances(i):
    print("Chances left are", (n-i))

def your_score(p):
    print("Your score is", p)

while(i <= n and i != j):
        list1 = [1, 2, 3]
        d2 = {1:'Rock', 2:'Paper', 3:'Scissor'}
        comp = random.choice(list1)
        choice = int(input("What do you choose: 1= Rock, 2= Paper or 3=Scissor?\n"))
        print("The PC chose", d2.get(comp))
        if choice == 1 and comp == 1:
            print("TIE!")
            i = i + 1
            chances(i)
            your_score(p)
            if i == n:
                decider(c, p, i, j)
                if i == j:
                    break
        elif choice == 1 and comp == 2:
            print("Point goes to the computer!")
            i = i + 1
            c = c + 1
            chances(i)
            your_score(p)
            if i == n:
                decider(c, p, i, j)
                if i == j:
                    break
        elif choice == 1 and comp == 3:
            print("Point scored!")
            i = i + 1
            p = p + 1
            chances(i)
            your_score(p)
            if i == n:
                decider(c, p, i, j)
                if i == j:
                    break
        elif choice == 2 and comp == 1:
            print("Point scored!")
            p = p + 1
            i = i + 1
            chances(i)
            your_score(p)
            if i == n:
                decider(c, p, i, j)
                if i == j:
                    break
        elif choice == 2 and comp == 2:
            print("TIE!")
            i = i + 1
            chances(i)
            your_score(p)
            if i == n:
                decider(c, p, i, j)
                if i == j:
                    break
        elif choice == 2 and comp == 3:
            print("Point goes to the computer!")
            i = i + 1
            c = c + 1
            chances(i)
            your_score(p)
            if i == n:
                decider(c, p, i, j)
                if i == j:
                    break
        elif choice == 3 and comp == 1:
            print("Point goes to the computer!")
            i = i + 1
            c = c + 1
            chances(i)
            your_score(p)
            if i == n:
                decider(c, p, i, j)
                if i == j:
                    break
        elif choice == 3 and comp == 2:
            print("Point scored!")
            i = i + 1
            p = p + 1
            chances(i)
            your_score(p)
            if i == n:
                decider(c, p, i, j)
                if i == j:
                    break
        elif choice == 3 and comp == 3:
            print("TIE!")
            i = i + 1
            chances(i)
            your_score(p)
            if i == n:
                decider(c, p, i, j)
                if i == j:
                    break
    #     break
    # break





