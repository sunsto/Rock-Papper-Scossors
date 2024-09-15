'''
project workflow
1.input from user(Rock,paper,scissors)
2.Computer Choice (Computer will Choose Randomly Not Conditionally)
3.Result Print

Cases To Win User And Computer
    A-Rock
    Rock - Rock = Tie
    Rock - Paper = Paper Win
    Rock - Scissors = Rock Win

    B-Paper
    Paper - Paper = tie
    paper - Rock = Paper win
    Paper - Scissors = Scissors Win

    C-Scissors
    Scissors - Scissors = Tie
    Scissors - Rock = Rock Win
    Scissors - paper = Scissors Win

'''
import random
Items_List = ["Rock","Paper","Scissors"]

User_Choice = input("Enter Your Moves = Rock Paper Scissors = ")
Comp_Choice = random.choice(Items_List)
print(f"User Choice = {User_Choice} And Computer Choice = {Comp_Choice}")


if User_Choice == Comp_Choice:
    print("Both Choose Same: Match is Tie")

elif User_Choice == "Rock":
    if Comp_Choice == "Paper":
        print("Paper Cover Rock ! Computer Win")
    else:
        print("Rock Smashes Scissors = You Win")
    
elif User_Choice == "Paper":
    if Comp_Choice == "Rock":
        print("Paper Cover Rock = You Win")
    else:
        print("Scissors  Cuts Paper = Computer Win")

elif User_Choice =="Scissors":
    if Comp_Choice =="Paper":
        print("Scissors cut Paper = You Win")
    else:
        print("Computer Win")

