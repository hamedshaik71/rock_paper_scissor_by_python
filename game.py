import random

def get_choices():
    player_choice=input("Enter the choice (rock,paper,scissor):")
    options=["rock","paper","scissor"]
    computer_choice=random.choice(options)
    choices = {"player":player_choice,"computer":computer_choice}
    return choices
    
def check_win(player,computer):
    print(f"You chose {player} ,computer chose {computer}" )
    if player == computer:
       return "It's a Tie!"
    elif player == "rock":
        if computer == "scissor":
           return "Rock smashes scissors! You win!"
        else:
           return "Paper covers rock! You lose"
    elif player == "paper":
        if computer == "rock":
           return "Paper covers rock! You win!"
        else:
           return "Scissors cuts paper! You lose"
    elif player == "scissor":
        if computer == "paper":
           return "Scissors cuts paper! You win!"
        else:
           return "Rock smashes paper! You lose"
    
choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)
    
    
    
    
