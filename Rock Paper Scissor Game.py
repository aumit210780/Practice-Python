import random
#Rock Paper Scissor
#1 for Rock, 2 for Paper and 3 for Scissor
Rounds = int(input("Enter the number of rounds: "))
Data = ["Rock","Paper","Scissor"]
i = 1
while i <= Rounds:
    userchoice = int(input("USER : "))
    if userchoice>=1 and userchoice<=3:
        computerchoice = random.randint(1,3)
        if userchoice == computerchoice:
            print("Tie")
        elif userchoice == 1 and computerchoice == 2:
            print("Computer wins")
        elif userchoice == 2 and computerchoice == 1:
            print("User wins")
        elif userchoice == 2 and computerchoice == 3:
            print("Computer wins")
        elif userchoice == 3 and computerchoice == 2:
            print("User wins")
        elif userchoice == 1 and computerchoice == 3:
            print("User wins")
        elif userchoice == 3 and computerchoice == 1:
            print("Computer wins")
        else:
            print("Something went wrong")
    print("User : {} Computer : {}".format(Data[userchoice-1],Data[computerchoice-1]))
    i=i+1