import random

def play():
    print("Starting Rock, Paper, Scissors, Lizard, Spock...")
    
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    
    def get_winner(player, computer):
        winning_combinations = {
            "rock": ["scissors", "lizard"],
            "paper": ["rock", "spock"],
            "scissors": ["paper", "lizard"],
            "lizard": ["spock", "paper"],
            "spock": ["scissors", "rock"]
        }
        if player == computer:
            return "draw"
        elif computer in winning_combinations[player]:
            return "player"
        else:
            return "computer"
    
    def select_number_of_wins():
        while True:
            try:
                wins = int(input("Enter the number of wins needed to win the match: "))
                if wins > 0:
                    return wins
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    number_of_wins = select_number_of_wins()
    player_wins = 0
    computer_wins = 0
    
    while player_wins < number_of_wins and computer_wins < number_of_wins:
        print("Choices: rock, paper, scissors, lizard, spock")
        player_choice = input("Enter your choice: ").lower()
        
        if player_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        winner = get_winner(player_choice, computer_choice)
        
        if winner == "draw":
            print("It's a draw!")
        elif winner == "player":
            print("Player wins this round!")
            player_wins += 1
        else:
            print("Computer wins this round!")
            computer_wins += 1
        
        print(f"Score: Player {player_wins} - Computer {computer_wins}")
        
        if player_wins == number_of_wins:
            print("Player wins the match!")
        elif computer_wins == number_of_wins:
            print("Computer wins the match!")