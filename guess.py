import random

def guess(x):
    random_number = random.randint(1,x) #limporting function from random library, so that computer can have a number
    guess=0 #initialising guess
    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x} "))
        if guess < random_number :
            print("sorry guess again. too low")
        if guess> random_number :
            print("sorry, too high")
    print(f"u have guessed the number {random_number}")
    
guess(10)
        