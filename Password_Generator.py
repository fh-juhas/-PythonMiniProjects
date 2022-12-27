import random


def passgen(x):
    char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&*+'
    x=int(x)
    passw=''
    for i in range(x):

        passw+=random.choice(char)

    print(f"Your Password is {passw}")

a=int(input("How many characters would you want in your password?: "))
passgen(a)



