import random

def get_player_choice():
    while True:
        choice = input("Foot, Nuke or Cockroach? (Quit ends): ").strip().lower()#getting player input
        if choice == "quit":
            return choice
        elif choice in ["foot", "nuke", "cockroach"]:
            print("You chose:", choice)
            return choice
        else:
            print("Incorrect selection.")

def get_computer_choice():
    return random.randint(1, 3) 

def determine_winner(player_choice, computer_choice):
    if player_choice == "nuke" and computer_choice == 1:  #todetermine the winner
        return "player"
    elif computer_choice == 3 and player_choice == "nuke": 
        return "computer"
    elif player_choice == "foot" and computer_choice == 3:  
        return "player"
    elif player_choice == "foot" and computer_choice == 2:  
        return "computer"
    elif player_choice == "cockroach" and computer_choice == 2:  
        return "player"
    elif player_choice == "cockroach" and computer_choice == 1: 
        return "computer"
    elif player_choice == "nuke" and computer_choice == 2:
        return "both_lose"
    if player_choice == "foot" and computer_choice == 1:
            return "tie"
    else:
        return "computer"

def main():
    player_score = 0
    computer_score = 0
    tie_count = 0
    total_rounds = 0

    while True:
        player_choice = get_player_choice()
        if player_choice == "quit":
            break
        total_rounds += 1
        computer_choice = get_computer_choice()
        if computer_choice == 1:
            print("Computer chose: Foot")
        elif computer_choice == 2:
            print("Computer chose: Nuke")
        elif computer_choice == 3:
            print("Computer chose: Cockroach")

        winner = determine_winner(player_choice, computer_choice)

        if winner == "player":
            player_score += 1
            print("You WIN!")
        elif winner == "computer":
            computer_score += 1
            print("You LOSE!")
        elif winner == "tie":
            tie_count += 1
            print("It is a tie!")
        elif winner == "both_lose":
            tie_count += 1
            print("Both LOSE!")

    print(f"You played {total_rounds} rounds, and won {player_score} rounds, playing tie in {tie_count} rounds.")

if __name__ == "__main__":
    main()