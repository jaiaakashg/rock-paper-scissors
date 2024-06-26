#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("You will be playing against the computer.")
    
    choices = ["rock", "paper", "scissors"]
    
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")
        
        play_again = input("Do you want to play again? (yes or no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Run the game
rock_paper_scissors()


# In[ ]:




