import streamlit as st
import random

def main():
    st.title("Games Project 🎮")
    st.sidebar.title("Select a Game")
    game = st.sidebar.selectbox("Choose a game", ["Battleship", "Tic Tac Toe", "Rock Paper Scissors Lizard Spock"])

    if game == "Battleship":
        st.sidebar.write("**Battleship Rules:**")
        st.sidebar.write("1. The game is played on a 5x5 grid.")
        st.sidebar.write("2. Each player places 3 ships on their grid.")
        st.sidebar.write("3. Players take turns to guess the location of the opponent's ships.")
        st.sidebar.write("4. The first player to sink all of the opponent's ships wins.")
        play_battleship()
    elif game == "Tic Tac Toe":
        st.sidebar.write("**Tic Tac Toe Rules:**")
        st.sidebar.write("1. The game is played on a 3x3 grid.")
        st.sidebar.write("2. Players take turns to place their symbol (X or O) in an empty cell.")
        st.sidebar.write("3. The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins.")
        st.sidebar.write("4. If all cells are filled and no player has three in a row, the game is a draw.")
        difficulty = st.sidebar.radio("Select Difficulty", ["Easy", "Hard"])
        play_tic_tac_toe(difficulty)
    elif game == "Rock Paper Scissors Lizard Spock":
        st.sidebar.write("**Rock Paper Scissors Lizard Spock Rules:**")
        st.sidebar.write("1. Rock crushes Scissors.")
        st.sidebar.write("2. Scissors cuts Paper.")
        st.sidebar.write("3. Paper covers Rock.")
        st.sidebar.write("4. Rock crushes Lizard.")
        st.sidebar.write("5. Lizard poisons Spock.")
        st.sidebar.write("6. Spock smashes Scissors.")
        st.sidebar.write("7. Scissors decapitates Lizard.")
        st.sidebar.write("8. Lizard eats Paper.")
        st.sidebar.write("9. Paper disproves Spock.")
        st.sidebar.write("10. Spock vaporizes Rock.")
        play_rpsls()

def play_rpsls():
    st.header("Rock Paper Scissors Lizard Spock ✊✋✌️🦎🖖")
    
    if 'player_score' not in st.session_state:
        st.session_state.player_score = 0
    if 'computer_score' not in st.session_state:
        st.session_state.computer_score = 0
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False

    choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    player_choice = st.selectbox("Choose your move", choices)
    if st.button("Play"):
        computer_choice = random.choice(choices)
        st.write(f"Computer chose: {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        st.write(result)
        update_score(result)

    st.write(f"Player Score: {st.session_state.player_score}")
    st.write(f"Computer Score: {st.session_state.computer_score}")

    if st.session_state.game_over:
        if st.button("Play Again"):
            reset_rpsls()

def determine_winner(player, computer):
    if player == computer:
        return "It's a draw!"
    elif (player == "Rock" and (computer == "Scissors" or computer == "Lizard")) or \
         (player == "Paper" and (computer == "Rock" or computer == "Spock")) or \
         (player == "Scissors" and (computer == "Paper" or computer == "Lizard")) or \
         (player == "Lizard" and (computer == "Spock" or computer == "Paper")) or \
         (player == "Spock" and (computer == "Scissors" or computer == "Rock")):
        return "You win!"
    else:
        return "You lose!"

def update_score(result):
    if result == "You win!":
        st.session_state.player_score += 1
    elif result == "You lose!":
        st.session_state.computer_score += 1

    if st.session_state.player_score == 3:
        st.write("Congratulations! You won the game!")
        st.session_state.game_over = True
    elif st.session_state.computer_score == 3:
        st.write("Sorry! The computer won the game!")
        st.session_state.game_over = True

def reset_rpsls():
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.game_over = False
    st.session_state.play_again = False

def play_battleship():
    st.header("Battleship 🚢💥")
    
    if 'player_board' not in st.session_state:
        reset_game_battleship()

    def display_board(board):
        display = ""
        for row in board:
            display += " | ".join(row) + "\n"
        return display
    
    def place_ships_randomly(board):
        ships = 3
        while ships > 0:
            x, y = random.randint(0, 4), random.randint(0, 4)
            if board[x][y] == ' ':
                board[x][y] = '🚢'
                ships -= 1

    def check_winner(board):
        for row in board:
            if '🚢' in row:
                return False
        return True
    
    def player_move():
        x = st.number_input("Enter row (0-4):", min_value=0, max_value=4, step=1, key='player_row_move')
        y = st.number_input("Enter column (0-4):", min_value=0, max_value=4, step=1, key='player_col_move')
        return x, y
    
    def computer_move():
        while True:
            x, y = random.randint(0, 4), random.randint(0, 4)
            if (x, y) not in st.session_state.computer_moves:
                st.session_state.computer_moves.add((x, y))
                return x, y

    if not st.session_state.ships_placed:
        st.write("Place your ships:")
        x = st.number_input("Enter row for ship (0-4):", min_value=0, max_value=4, step=1, key='ship_row')
        y = st.number_input("Enter column for ship (0-4):", min_value=0, max_value=4, step=1, key='ship_col')
        if st.button("Place Ship"):
            if st.session_state.player_board[x][y] == ' ':
                st.session_state.player_board[x][y] = '🚢'
                st.session_state.player_ships += 1
                if st.session_state.player_ships == 3:
                    st.session_state.ships_placed = True
                    place_ships_randomly(st.session_state.computer_hidden_board)
                    st.write("All ships placed! The game begins!")
                    st.session_state.game_started = True
            else:
                st.write("Invalid position. Try again.")
        st.write("Player's Board:")
        st.text(display_board(st.session_state.player_board))

    elif st.session_state.game_started:
        st.write("Make your move:")
        x, y = player_move()
        if st.button("Attack"):
            if (x, y) in st.session_state.player_moves:
                st.write("Invalid move. You already attacked this position. Try again.")
            else:
                st.session_state.player_moves.add((x, y))
                if st.session_state.computer_hidden_board[x][y] == '🚢':
                    st.write("Hit!")
                    st.session_state.computer_board[x][y] = '💥'
                    st.session_state.computer_hidden_board[x][y] = '💥'
                else:
                    st.write("Miss!")
                    st.session_state.computer_board[x][y] = '❌'
                
                if check_winner(st.session_state.computer_hidden_board):
                    st.write("Player wins!")
                    st.session_state.game_started = False
                else:
                    x, y = computer_move()
                    if st.session_state.player_board[x][y] == '🚢':
                        st.write("Computer hits!")
                        st.session_state.player_board[x][y] = '💥'
                    else:
                        st.write("Computer misses!")
                        if st.session_state.player_board[x][y] == ' ':
                            st.session_state.player_board[x][y] = '❌'
                    
                    if check_winner(st.session_state.player_board):
                        st.write("Computer wins!")
                        st.session_state.game_started = False
        
        st.write("Player's Board:")
        st.text(display_board(st.session_state.player_board))
        st.write("Computer's Board:")
        st.text(display_board(st.session_state.computer_board))

    if not st.session_state.game_started and st.session_state.ships_placed:
        if st.button("Play Again"):
            reset_game_battleship()

def reset_game_battleship():
    st.session_state.player_board = [[' ' for _ in range(5)] for _ in range(5)]
    st.session_state.computer_board = [[' ' for _ in range(5)] for _ in range(5)]
    st.session_state.computer_hidden_board = [[' ' for _ in range(5)] for _ in range(5)]
    st.session_state.ships_placed = False
    st.session_state.player_ships = 0
    st.session_state.game_started = False
    st.session_state.player_moves = set()
    st.session_state.computer_moves = set()

def play_tic_tac_toe(difficulty):
    st.header("Tic Tac Toe ❌⭕")
    
    if 'tic_tac_toe_board' not in st.session_state:
        reset_tic_tac_toe()

    def display_tic_tac_toe_board(board):
        for i in range(3):
            cols = st.columns(3)
            for j in range(3):
                index = i * 3 + j
                if board[index] == ' ':
                    if cols[j].button(" ", key=f"cell_{index}"):
                        make_move(index)
                else:
                    cols[j].write(board[index])

    def check_tic_tac_toe_winner(board, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontales
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Verticales
            [0, 4, 8], [2, 4, 6]              # Diagonales
        ]
        for condition in win_conditions:
            if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
                return True
        return False
    
    def check_tic_tac_toe_draw(board):
        return ' ' not in board

    def computer_move_easy(board):
        available_moves = [i for i, spot in enumerate(board) if spot == ' ']
        return random.choice(available_moves)

    def computer_move_hard(board, player):
        opponent = 'X' if player == 'O' else 'O'
        for move in range(9):
            if board[move] == ' ':
                board[move] = player
                if check_tic_tac_toe_winner(board, player):
                    return move
                board[move] = ' '
        for move in range(9):
            if board[move] == ' ':
                board[move] = opponent
                if check_tic_tac_toe_winner(board, opponent):
                    return move
                board[move] = ' '
        return random.choice([i for i, spot in enumerate(board) if spot == ' '])

    def make_move(index):
        board = st.session_state.tic_tac_toe_board
        current_player = st.session_state.tic_tac_toe_current_player

        if board[index] == ' ':
            board[index] = current_player
            if check_tic_tac_toe_winner(board, current_player):
                st.session_state.tic_tac_toe_game_over = True
                st.session_state.tic_tac_toe_winner = current_player
            elif check_tic_tac_toe_draw(board):
                st.session_state.tic_tac_toe_game_over = True
                st.session_state.tic_tac_toe_winner = "Draw"
            else:
                st.session_state.tic_tac_toe_current_player = 'O' if current_player == 'X' else 'X'
                if st.session_state.tic_tac_toe_current_player == 'O':
                    computer_move()

    def computer_move():
        board = st.session_state.tic_tac_toe_board
        if difficulty == "Easy":
            move = computer_move_easy(board)
        else:
            move = computer_move_hard(board, 'O')
        board[move] = 'O'
        if check_tic_tac_toe_winner(board, 'O'):
            st.session_state.tic_tac_toe_game_over = True
            st.session_state.tic_tac_toe_winner = 'O'
        elif check_tic_tac_toe_draw(board):
            st.session_state.tic_tac_toe_game_over = True
            st.session_state.tic_tac_toe_winner = "Draw"
        else:
            st.session_state.tic_tac_toe_current_player = 'X'

    board = st.session_state.tic_tac_toe_board
    current_player = st.session_state.tic_tac_toe_current_player

    st.write("Current Player: " + current_player)
    display_tic_tac_toe_board(board)

    if st.session_state.tic_tac_toe_game_over:
        if st.session_state.tic_tac_toe_winner == "Draw":
            st.write("It's a draw!")
        else:
            st.write(f"Player {st.session_state.tic_tac_toe_winner} wins!")
        if st.button("Play Again"):
            reset_tic_tac_toe()

def reset_tic_tac_toe():
    st.session_state.tic_tac_toe_board = [' ' for _ in range(9)]
    st.session_state.tic_tac_toe_current_player = 'X'
    st.session_state.tic_tac_toe_game_over = False
    st.session_state.tic_tac_toe_winner = None

if __name__ == "__main__":
    main()

