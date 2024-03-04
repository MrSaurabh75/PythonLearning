# Exercise 5
# Rock-Paper-Scissors Game
import random
l1 = ["Rock","Paper","Scissors"]
com = random.choice(l1)
print("Enter Form [Rock,Paper,Scissors]")
user = input("Enter Your Choice : ")
if com == 'Scissors' and user == 'Rock':
    print(f"Computer Choice :{com}")
    print("Congratulations,You Win!")
elif com == 'Paper' and user == 'Scissors':
    print(f"Computer Choice :{com}")
    print("Congratulations,You Win!")
elif com == 'Rock' and user == 'Paper':
    print(f"Computer Choice :{com}")
    print("Congratulations,You Win!")
elif com == user:
    print("Tie")
else:
    print(f"Computer Choice :{com}")
    print("Sorry, Try Next Time")


