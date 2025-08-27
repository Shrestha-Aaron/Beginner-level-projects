#This code plays rock paper scissors with the user.


import random # importing "random" library for getting random values

my_choices=["rock","paper","scissors"]

again="y" # for a rematch(used later on)

while again.lower()=="y":
    
    user_choice=input("Choose between rock paper and scissors:").lower()
    my_choice=random.choice(my_choices) # assigns my_choice a string among the list (my_choices)
    
    while user_choice not in my_choices: #to check if the user has given value with correct spelling
        user_choice=input("Please give the input with correct spelling (rock or paper or scissors)").lower()
        
    print(f"My choice is {my_choice}")
    if my_choice==user_choice:
        print("Draw")
    elif my_choice=="rock":
        if user_choice=="paper":
            print("You Won!")
        else:
            print("You lost")
    elif my_choice=="paper":
        if user_choice=="scissors":
            print("You Won!")
        else:
            print("You lost")
    elif my_choice=="scissors":
        if user_choice=="rock":
            print("You Won!")
        else:
            print("You lost")
            
    again=input("Wanna play again(y/n):") # Asking for a rematch

print("Thanks for playing! :D")
