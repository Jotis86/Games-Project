import random

def play():
    print("Starting Tic Tac Toe...")
    
    # Inicializar el tablero
    board = [' ' for _ in range(9)]
    
    def print_board():
        print(f"{board[0]} | {board[1]} | {board[2]}")
        print("--+---+--")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print("--+---+--")
        print(f"{board[6]} | {board[7]} | {board[8]}")
    
    def check_winner(player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontales
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Verticales
            [0, 4, 8], [2, 4, 6]              # Diagonales
        ]
        for condition in win_conditions:
            if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
                return True
        return False
    
    def check_draw():
        return ' ' not in board
    
    def computer_move_easy():
        available_moves = [i for i, spot in enumerate(board) if spot == ' ']
        return random.choice(available_moves)
    
    def computer_move_hard():
        # Intentar bloquear al jugador
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                if check_winner('X'):
                    board[i] = 'O'
                    return i
                board[i] = ' '
        # Si no hay necesidad de bloquear, hacer un movimiento aleatorio
        return computer_move_easy()
    
    def select_difficulty():
        while True:
            difficulty = input("Select difficulty (easy/hard): ").lower()
            if difficulty in ['easy', 'hard']:
                return difficulty
            print("Invalid choice. Please select 'easy' or 'hard'.")
    
    difficulty = select_difficulty()
    current_player = 'X'
    
    while True:
        print_board()
        
        if current_player == 'X':
            move = int(input("Player X, enter your move (1-9): ")) - 1
        else:
            if difficulty == 'easy':
                move = computer_move_easy()
            else:
                move = computer_move_hard()
            print(f"Computer (O) chooses position {move + 1}")
        
        if board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        
        board[move] = current_player
        
        if check_winner(current_player):
            print_board()
            if current_player == 'X':
                print("Player wins!")
            else:
                print("Computer wins!")
            break
        
        if check_draw():
            print_board()
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

