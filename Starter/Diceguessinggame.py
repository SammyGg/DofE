import random
roll=random.randint(1,6)
guess = (int(input("Take a guess what the computer has rolled \n")))
if guess == roll:
    print("You are right the roll is" +" "+ str(roll))
elif guess != roll:
    print("You are wrong the roll is " + str(roll))