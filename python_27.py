# Create a python program to show the question and ans to user and in last display the score
questions = ["1. Who developed Python Programming Language? \n\ta) Wick van Rossum \n\tb) Rasmus Lerdorf \n\tc) Guido van Rossum \n\td) Niene Stom","2. Which type of Programming does Python support? \n\ta) object-oriented programming \n\tb) structured programming \n\tc) functional programming \n\td) all of the mentioned","3. Is Python case sensitive when dealing with identifiers? \n\ta) no \n\tb) yes \n\tc) machine dependent \n\td) none of the mentioned"]
flsg = 0
score = 0
print(questions[0])
flag = 1
if(flag == 1):
    un = input("Enter Your Answer : ")
    if(un == 'c'):
        score=score+10
    else:
        print("You entered worng answer answer is 'c'")

print(questions[1])
flag = 2
if(flag == 2):
    un = input("Enter Your Answer : ")
    if(un == 'd'):
        score=score+10
    else:
        print("You entered worng answer answer is 'd'")
    
print(questions[2])
flag = 3
if(flag == 3):
    un = input("Enter Your Answer : ")
    if(un == 'b'):
        score=score+10
    else:
        print("You entered worng answer answer is 'b'")

print("Your Score is ",score)