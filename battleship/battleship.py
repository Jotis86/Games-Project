import random

def play():
    print("Starting Battleship...")
    
    # Inicializar el tablero
    player_board = [[' ' for _ in range(5)] for _ in range(5)]
    computer_board = [[' ' for _ in range(5)] for _ in range(5)]
    computer_hidden_board = [[' ' for _ in range(5)] for _ in range(5)]
    
    def print_board(board):
        for row in board:
            print(' '.join(row))
    
    def place_ships(board):
        ships = 3
        while ships > 0:
            x, y = random.randint(0, 4), random.randint(0, 4)
            if board[x][y] == ' ':
                board[x][y] = 'S'
                ships -= 1
    
    def check_winner(board):
        for row in board:
            if 'S' in row:
                return False
        return True
    
    def player_move():
        while True:
            try:
                x, y = map(int, input("Enter your move (row and column): ").split())
                if 0 <= x < 5 and 0 <= y < 5:
                    return x, y
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Enter row and column separated by a space.")
    
    def computer_move():
        while True:
            x, y = random.randint(0, 4), random.randint(0, 4)
            if player_board[x][y] == ' ' or player_board[x][y] == 'S':
                return x, y
    
    place_ships(player_board)
    place_ships(computer_hidden_board)
    
    while True:
        print("Player's Board:")
        print_board(player_board)
        print("Computer's Board:")
        print_board(computer_board)
        
        # Player's turn
        x, y = player_move()
        if computer_hidden_board[x][y] == 'S':
            print("Hit!")
            computer_board[x][y] = 'X'
            computer_hidden_board[x][y] = 'X'
        else:
            print("Miss!")
            computer_board[x][y] = 'O'
        
        if check_winner(computer_hidden_board):
            print("Player wins!")
            break
        
        # Computer's turn
        x, y = computer_move()
        if player_board[x][y] == 'S':
            print("Computer hits!")
            player_board[x][y] = 'X'
        else:
            print("Computer misses!")
            if player_board[x][y] == ' ':
                player_board[x][y] = 'O'
        
        if check_winner(player_board):
            print("Computer wins!")
            break