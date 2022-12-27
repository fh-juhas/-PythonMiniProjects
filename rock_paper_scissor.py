def rps():
    import random
    user = input("type 'R' for Rock,'P' for paper,'S' for Scissor: ").upper()
    computer = random.choice(['R','P','S'])
    print(f"you have chosen {user} and computer has chosen {computer}\n")
    if(user==computer):
        print("Tie")
        rps()
        #to Rerun the code if the result is tie

    elif((user=='R' and computer == 'S') or (user=='S' and computer == 'P') or (user=='P' and computer == 'R')):
        print("Congrates! You Win!")

    else:
        print("Oops! Computer Win!")


rps()