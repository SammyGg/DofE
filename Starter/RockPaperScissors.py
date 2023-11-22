import random
computerchoice = random.choice (["rock", "paper", "scissors"])
person = input("rock, paper or scissors?\n")
if computerchoice == person:
    print("Tie")
elif person == "rock" and computerchoice == "scissors":
    print(f"Player WINS. Computer Chose {computerchoice}.")
elif person == "scissors" and computerchoice == "paper":
    print(f"Player WINS. Computer Chose {computerchoice}.")
elif person == "paper" and computerchoice == "rock":
    print(f"Player WINS. Computer Chose {computerchoice}.")
else:
    print(f"Computer WINS. Computer chose {computerchoice}.")