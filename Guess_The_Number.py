import random
def user_guess(x):
    number = random.randint(1,x)
    guessed = 0
    while(guessed!=number):
        guessed = int(input(f"Guess a mumber between 1 to {x}: "))
        if(guessed<number):
            print("Oops!too low..")
        elif(guessed>number):
            print("oops!too high...")
        else:
            print("Bingo! Correct guess..")

def computer_guess(x):
    low = 1
    high = x

    #print(com_guess)
    res=''
    while(res!='C'):
        com_guess = random.randint(low, high)
        res = input(f"Guess is : {com_guess} type C for Correct,H for High and L for Low: ")
        if(res=='H'):
            print("Oops! your guess is too high..")
            high = com_guess-1

        elif(res=='L'):
            print("Oops!Your guess is too low..")
            low = com_guess+1


    print("Correct Guess!")
            




#user_guess(25)
computer_guess(20)