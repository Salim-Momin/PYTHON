import random as ran

def get_choices():
    player_choice=input("Enter your choices (Rock,Paper,Scissor): ")
    options = ["Rock","Paper","Scissor"]
    computer_choice = ran.choice(options)
    choices = {"Player":player_choice,"Computer": computer_choice}
    return choices

def game(player,computer):
    print(f"Player choice: {player} and Computer choice: {computer}")
    if player=="Rock" and computer == "Paper":
        return "Player Lose :("
    elif player == "Rock" and computer == "Scissor":
        return "Player Win :)"
    elif player == "Rock" and computer == "Rock":
        return "Game is Tie play again!"
    elif player == "Paper" and computer == "Paper":
        return "Game is Tie play again!"
    elif player == "Paper" and computer == "Scissor":
        return "Player Lose :("
    elif player == "Paper" and computer == "Rock":
        return "Player Win :)"
    elif player == "Scissor" and computer == "Paper":
        return "Player Win :)"
    elif player == "Scissor" and computer == "Scissor":
        return "Game is Tie play again!"
    elif player == "Scissor" and computer == "Rock":
        return "Player Lose :("
    else:
        return "Error!"
    
choices = get_choices()
result = game(choices["Player"],choices["Computer"])
print(result)