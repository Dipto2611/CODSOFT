"""TASK 4"""

#Rock-Paper-Scissors Game using Cmd line:

import random

print("-----------------ROCK PAPER SCISSORS GAME -----------------")

while True:
    
    choices = ["R", "P", "S"]
    
    #rounds
    total_rounds = 3
    current_round = 1

    #scores
    user_score = 0
    comp_score = 0

    while current_round <= total_rounds:
        
        print(f"\nROUND: {current_round}")
        
        #to ensure that user choice is valid:
        while True:
            user = input("Choose: Rock, Paper, Scissors or R/P/S: ").capitalize()  #user choice
            
            if user in choices:
                break
            else:
                print("Invalid input! Please choose from 'R','P', or 'S'")
                print("")
        
        comp = random.choice(choices).capitalize()  #computer choice
        print(f"You chose: {user}")
        print(f"Computer chose: {comp}")

        # rules for the game (winning conditions)
        #NOTE: go thr' all the blocks to check who won (T/F case in general)

        rule = {
            "R": "S", #rock beats sci
            "P": "R", #paper beats rock
            "S": "P"  #sci beats paper
        } 
        
        if user == comp:
            print("Tie")
        elif rule.get(user) == comp:
            print("User won")
            user_score += 1 
        elif rule.get(comp) == user:
            print("Computer won")
            comp_score += 1 
        
        current_round += 1

    # After all rounds, print the final score

    print("\n-----------FINAL SCORE-----------")
    print("")
    print(f"User: {user_score} || Computer: {comp_score}")

    # To determine the winner
    if user_score > comp_score:
        print("User wins the game!")
    elif user_score < comp_score:
        print("Computer wins the game!")
    else:
        print("It's a tie!")
    print("")

    #if the user want a rematch
    again = input("Do you want to play another session? (yes/no):").lower()
    if again == 'yes':
        print("")
        continue
    else:
        print("\nGoodbye!")
        break