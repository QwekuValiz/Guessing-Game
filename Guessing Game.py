import random 
number = 5
name = input("Hello,What is your name?")
print("Well, " + name + " I am thinking of a number")
guessCorrect = False
while guessCorrect == False:
    guess = int(input("Take a guess "))
    if guess == number:
        print ("Hooray!!!. You are correct.") 
        guessCorrect = True
    elif guess < number: 
        print ("Oops, try again.Choose a higher number")
    else:
        print ("Oops, try again.Choose a lower number")