import streamlit as st
import random
import time
from PIL import Image
import base64

# Set page configuration and styling
st.set_page_config(page_title="Arcade Games Hub", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for better styling
def local_css():
    st.markdown("""
    <style>
        .main-header {
            font-size: 3rem !important;
            color: #1E88E5;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            margin-bottom: 1rem;
        }
        .game-header {
            color: #1976D2;
            text-align: center;
            padding: 0.5rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid #1976D2;
        }
        .game-board {
            margin: 2rem auto;
            max-width: 600px;
        }
        .cell-btn {
            width: 100%;
            height: 100px;
            font-size: 2rem;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .score-display {
            padding: 1rem;
            background-color: #f0f2f6;
            border-radius: 10px;
            margin: 1rem 0;
            text-align: center;
        }
        .result-text {
            font-size: 1.5rem;
            font-weight: bold;
            text-align: center;
            margin: 1rem 0;
        }
        .win-text {
            color: #4CAF50;
            font-size: 1.75rem;
            font-weight: bold;
            text-align: center;
            margin: 1rem 0;
            animation: pulse 1.5s infinite;
        }
        .lose-text {
            color: #F44336;
            font-size: 1.75rem;
            font-weight: bold;
            text-align: center;
            margin: 1rem 0;
        }
        .draw-text {
            color: #FF9800;
            font-size: 1.75rem;
            font-weight: bold;
            text-align: center;
            margin: 1rem 0;
        }
        .rules-container {
            background-color: #f0f2f6;
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 1rem;
        }
        .ship-cell {
            background-color: #2196F3;
            color: white;
            border-radius: 5px;
        }
        .hit-cell {
            background-color: #F44336;
            color: white;
            border-radius: 5px;
        }
        .miss-cell {
            background-color: #78909C;
            color: white;
            border-radius: 5px;
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
    </style>
    """, unsafe_allow_html=True)

def main():
    local_css()
    
    # App header with animation
    st.markdown('<h1 class="main-header">🎮 Arcade Games Hub</h1>', unsafe_allow_html=True)
    
    # Sidebar navigation
    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2257/2257820.png", width=100)
    st.sidebar.title("Game Selection")
    
    game = st.sidebar.selectbox(
        "Choose a game to play", 
        ["Battleship", "Tic Tac Toe", "Rock Paper Scissors Lizard Spock"]
    )
    
    # Game-specific content
    if game == "Battleship":
        display_rules("battleship")
        play_battleship()
    elif game == "Tic Tac Toe":
        display_rules("tictactoe")
        difficulty = st.sidebar.radio("Select Difficulty", ["Easy", "Medium", "Hard"])
        play_tic_tac_toe(difficulty)
    else:  # RPSLS
        display_rules("rpsls")
        play_rpsls()

def display_rules(game_type):
    """Display game rules in a collapsible section"""
    with st.sidebar.expander("Game Rules", expanded=False):
        if game_type == "battleship":
            st.markdown("""
            ### Battleship Rules
            1. You'll play on a 5x5 grid against the computer
            2. Place your 3 ships on the grid
            3. Take turns guessing locations of opponent's ships
            4. First to sink all opponent's ships wins!
            """)
        elif game_type == "tictactoe":
            st.markdown("""
            ### Tic Tac Toe Rules
            1. Play on a 3x3 grid (you're X, computer is O)
            2. Take turns placing your symbol
            3. Get three in a row (horizontally, vertically, or diagonally) to win
            4. If the board fills up with no winner, it's a draw
            """)
        else:  # RPSLS
            st.markdown("""
            ### Rock Paper Scissors Lizard Spock Rules
            - Rock crushes Scissors and Lizard
            - Paper covers Rock and disproves Spock
            - Scissors cuts Paper and decapitates Lizard
            - Lizard eats Paper and poisons Spock
            - Spock vaporizes Rock and smashes Scissors
            
            First to score 3 points wins the match!
            """)

# ROCK PAPER SCISSORS LIZARD SPOCK IMPLEMENTATION
def play_rpsls():
    st.markdown('<h2 class="game-header">Rock Paper Scissors Lizard Spock ✊✋✌️🦎🖖</h2>', unsafe_allow_html=True)
    
    # Initialize session state
    if 'player_score' not in st.session_state:
        st.session_state.player_score = 0
    if 'computer_score' not in st.session_state:
        st.session_state.computer_score = 0
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False
    if 'game_history' not in st.session_state:
        st.session_state.game_history = []
    
    # Display scores in a visually appealing way
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="score-display">
            <h3>Your Score</h3>
            <h2>{st.session_state.player_score}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="score-display">
            <h3>Computer Score</h3>
            <h2>{st.session_state.computer_score}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    # Game elements
    choices = {
        "Rock": "✊", 
        "Paper": "✋", 
        "Scissors": "✌️", 
        "Lizard": "🦎", 
        "Spock": "🖖"
    }
    
    # Display choices as buttons in a row
    st.markdown("<h3 style='text-align: center;'>Make your choice:</h3>", unsafe_allow_html=True)
    
    # Create buttons for each choice
    cols = st.columns(len(choices))
    player_choice = None
    
    for idx, (choice, emoji) in enumerate(choices.items()):
        if cols[idx].button(f"{emoji} {choice}", key=f"choice_{choice}", disabled=st.session_state.game_over):
            player_choice = choice
    
    # Process game logic when a choice is made
    if player_choice:
        computer_choice = random.choice(list(choices.keys()))
        
        # Show the choices with animation
        choice_display_col1, choice_display_col2 = st.columns(2)
        
        with choice_display_col1:
            st.markdown(f"""
            <div style='text-align: center;'>
                <h4>Your choice</h4>
                <div style='font-size: 4rem;'>{choices[player_choice]}</div>
                <p>{player_choice}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with choice_display_col2:
            st.markdown(f"""
            <div style='text-align: center;'>
                <h4>Computer's choice</h4>
                <div style='font-size: 4rem;'>{choices[computer_choice]}</div>
                <p>{computer_choice}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Determine winner with visual feedback
        result = determine_winner(player_choice, computer_choice)
        
        if result == "You win!":
            st.markdown(f"<div class='win-text'>{result}</div>", unsafe_allow_html=True)
        elif result == "You lose!":
            st.markdown(f"<div class='lose-text'>{result}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='draw-text'>{result}</div>", unsafe_allow_html=True)
        
        # Update score and check for game over
        update_score(result)
        
        # Add to game history
        st.session_state.game_history.append({
            "player_choice": player_choice,
            "computer_choice": computer_choice,
            "result": result
        })
    
    # Game history section
    if st.session_state.game_history:
        with st.expander("Game History", expanded=False):
            for idx, round_data in enumerate(st.session_state.game_history):
                st.write(f"Round {idx+1}: You chose {round_data['player_choice']}, "
                         f"Computer chose {round_data['computer_choice']} - {round_data['result']}")
    
    # Game over state
    if st.session_state.game_over:
        if st.session_state.player_score > st.session_state.computer_score:
            st.markdown("<div class='win-text'>🎉 CONGRATULATIONS! YOU WON THE MATCH! 🎉</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='lose-text'>💔 You lost the match. Better luck next time! 💔</div>", unsafe_allow_html=True)
        
        if st.button("Play Again", key="rpsls_play_again"):
            reset_rpsls()

def determine_winner(player, computer):
    """Determine the winner of RPSLS"""
    if player == computer:
        return "It's a draw!"
    
    winning_combinations = {
        "Rock": ["Scissors", "Lizard"],
        "Paper": ["Rock", "Spock"],
        "Scissors": ["Paper", "Lizard"],
        "Lizard": ["Paper", "Spock"],
        "Spock": ["Rock", "Scissors"]
    }
    
    if computer in winning_combinations[player]:
        return "You win!"
    else:
        return "You lose!"

def update_score(result):
    """Update scores based on game result"""
    if result == "You win!":
        st.session_state.player_score += 1
    elif result == "You lose!":
        st.session_state.computer_score += 1

    # Check for game over
    if st.session_state.player_score >= 3 or st.session_state.computer_score >= 3:
        st.session_state.game_over = True

def reset_rpsls():
    """Reset RPSLS game state"""
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.game_over = False
    st.session_state.game_history = []

# BATTLESHIP IMPLEMENTATION
def play_battleship():
    st.markdown('<h2 class="game-header">Battleship 🚢💥</h2>', unsafe_allow_html=True)
    
    # Initialize battleship session state
    if 'player_board' not in st.session_state:
        reset_game_battleship()
    
    # Display game status
    if not st.session_state.ships_placed:
        st.markdown("<h3>Phase 1: Place Your Ships</h3>", unsafe_allow_html=True)
        st.write(f"Ships placed: {st.session_state.player_ships}/3")
    else:
        st.markdown("<h3>Phase 2: Battle!</h3>", unsafe_allow_html=True)
    
    # Create visual grid for player's board
    st.markdown("<h4>Your Fleet:</h4>", unsafe_allow_html=True)
    display_interactive_board(
        "player", 
        st.session_state.player_board, 
        clickable=not st.session_state.ships_placed,
        show_ships=True
    )
    
    # Display computer's board only after ships are placed
    if st.session_state.ships_placed:
        st.markdown("<h4>Enemy Waters:</h4>", unsafe_allow_html=True)
        display_interactive_board(
            "computer", 
            st.session_state.computer_board, 
            clickable=st.session_state.game_started,
            show_ships=False
        )
    
    # Game status and messages
    status_container = st.empty()
    message_container = st.empty()
    
    # Phase 1: Ship placement
    if not st.session_state.ships_placed:
        message_container.info("Click on the grid to place your ships (3 required)")
        
        # Option to place ships randomly
        if st.button("Place Ships Randomly"):
            place_ships_randomly(st.session_state.player_board)
            st.session_state.player_ships = 3
            st.session_state.ships_placed = True
            place_ships_randomly(st.session_state.computer_hidden_board)
            st.session_state.game_started = True
            message_container.success("Ships placed! The battle begins!")
            st.rerun()
    
    # Phase 2: Battle phase
    elif st.session_state.game_started:
        # Check for game over
        if check_winner(st.session_state.computer_hidden_board):
            message_container.markdown("<div class='win-text'>🎉 VICTORY! You sank all enemy ships! 🎉</div>", unsafe_allow_html=True)
            st.session_state.game_started = False
            if st.button("Play Again", key="battleship_play_again"):
                reset_game_battleship()
                st.experimental_rerun()
        elif check_winner(st.session_state.player_board):
            message_container.markdown("<div class='lose-text'>💔 DEFEAT! Your fleet has been destroyed! 💔</div>", unsafe_allow_html=True)
            st.session_state.game_started = False
            if st.button("Play Again", key="battleship_play_again2"):
                reset_game_battleship()
                st.rerun()
        else:
            status_container.info("Click on enemy waters to launch an attack!")

def display_interactive_board(board_type, board, clickable=True, show_ships=True):
    """Display an interactive board with clickable cells"""
    columns = st.columns(6)
    # Column headers (A-E)
    for i in range(5):
        columns[i+1].markdown(f"<div style='text-align:center; font-weight:bold;'>{chr(65+i)}</div>", unsafe_allow_html=True)
    
    for row in range(5):
        columns = st.columns(6)
        # Row headers (1-5)
        columns[0].markdown(f"<div style='text-align:center; font-weight:bold;'>{row+1}</div>", unsafe_allow_html=True)
        
        for col in range(5):
            cell_value = board[row][col]
            cell_style = ""
            
            # Apply appropriate styling based on cell content
            if cell_value == '🚢' and show_ships:
                cell_style = "ship-cell"
            elif cell_value == '💥':
                cell_style = "hit-cell"
            elif cell_value == '❌':
                cell_style = "miss-cell"
            
            # Create clickable buttons for empty cells if the board is clickable
            if clickable and (cell_value == ' ' or (board_type == "computer" and cell_value != '💥' and cell_value != '❌')):
                if columns[col+1].button(" ", key=f"{board_type}_{row}_{col}"):
                    handle_board_click(board_type, row, col)
            else:
                # Display non-clickable cells with appropriate styling
                columns[col+1].markdown(
                    f"<div style='height:40px; display:flex; justify-content:center; align-items:center; "
                    f"border:1px solid #ddd; border-radius:4px;' class='{cell_style}'>{cell_value if cell_value != ' ' else ''}</div>",
                    unsafe_allow_html=True
                )

def handle_board_click(board_type, row, col):
    """Handle clicks on the game boards"""
    if board_type == "player" and not st.session_state.ships_placed:
        # Place ship on player's board
        if st.session_state.player_board[row][col] == ' ':
            st.session_state.player_board[row][col] = '🚢'
            st.session_state.player_ships += 1
            
            # Check if all ships are placed
            if st.session_state.player_ships == 3:
                st.session_state.ships_placed = True
                place_ships_randomly(st.session_state.computer_hidden_board)
                st.session_state.game_started = True
    
    elif board_type == "computer" and st.session_state.game_started:
        # Player attacks computer's board
        if (row, col) not in st.session_state.player_moves:
            st.session_state.player_moves.add((row, col))
            
            # Check hit or miss
            if st.session_state.computer_hidden_board[row][col] == '🚢':
                st.session_state.computer_board[row][col] = '💥'
                st.session_state.computer_hidden_board[row][col] = '💥'
            else:
                st.session_state.computer_board[row][col] = '❌'
            
            # Computer's turn
            if not check_winner(st.session_state.computer_hidden_board):
                computer_turn()

def computer_turn():
    """Computer makes a move"""
    while True:
        row, col = random.randint(0, 4), random.randint(0, 4)
        if (row, col) not in st.session_state.computer_moves:
            st.session_state.computer_moves.add((row, col))
            
            # Check hit or miss
            if st.session_state.player_board[row][col] == '🚢':
                st.session_state.player_board[row][col] = '💥'
            elif st.session_state.player_board[row][col] == ' ':
                st.session_state.player_board[row][col] = '❌'
            
            break

def place_ships_randomly(board):
    """Place ships randomly on a board"""
    ships = 3
    while ships > 0:
        x, y = random.randint(0, 4), random.randint(0, 4)
        if board[x][y] == ' ':
            board[x][y] = '🚢'
            ships -= 1

def check_winner(board):
    """Check if there are any ships left on the board"""
    for row in board:
        if '🚢' in row:
            return False
    return True

def reset_game_battleship():
    """Reset the battleship game state"""
    st.session_state.player_board = [[' ' for _ in range(5)] for _ in range(5)]
    st.session_state.computer_board = [[' ' for _ in range(5)] for _ in range(5)]
    st.session_state.computer_hidden_board = [[' ' for _ in range(5)] for _ in range(5)]
    st.session_state.ships_placed = False
    st.session_state.player_ships = 0
    st.session_state.game_started = False
    st.session_state.player_moves = set()
    st.session_state.computer_moves = set()

# TIC TAC TOE IMPLEMENTATION
def play_tic_tac_toe(difficulty):
    st.markdown('<h2 class="game-header">Tic Tac Toe ❌⭕</h2>', unsafe_allow_html=True)
    
    # Initialize session state
    if 'tic_tac_toe_board' not in st.session_state:
        reset_tic_tac_toe()
    
    # Get current game state
    board = st.session_state.tic_tac_toe_board
    current_player = st.session_state.tic_tac_toe_current_player
    
    # Display current player's turn
    if not st.session_state.tic_tac_toe_game_over:
        st.markdown(f"""
        <div style='text-align:center; margin-bottom:1rem;'>
            <h3>Current Player: {current_player}</h3>
        </div>
        """, unsafe_allow_html=True)
    
    # Display the game board with interactive buttons
    display_tic_tac_toe_board(board)
    
    # Game over state
    if st.session_state.tic_tac_toe_game_over:
        if st.session_state.tic_tac_toe_winner == "Draw":
            st.markdown("<div class='draw-text'>It's a draw!</div>", unsafe_allow_html=True)
        elif st.session_state.tic_tac_toe_winner == "X":
            st.markdown("<div class='win-text'>🎉 You win! 🎉</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='lose-text'>💔 Computer wins! 💔</div>", unsafe_allow_html=True)
        
        if st.button("Play Again", key="ttt_play_again"):
            reset_tic_tac_toe()
            st.rerun()

def display_tic_tac_toe_board(board):
    """Display interactive Tic Tac Toe board"""
    board_container = st.container()
    
    with board_container:
        # Create a 3x3 grid of buttons
        for i in range(3):
            cols = st.columns(3)
            for j in range(3):
                index = i * 3 + j
                if board[index] == ' ' and not st.session_state.tic_tac_toe_game_over:
                    # Empty cell - create clickable button
                    if cols[j].button(" ", key=f"ttt_cell_{index}", 
                                     help="Click to place your X",
                                     on_click=make_move, args=(index,)):
                        pass
                else:
                    # Show X or O with appropriate styling
                    symbol = board[index]
                    if symbol == 'X':
                        cols[j].markdown("""
                        <div style='height:80px; display:flex; justify-content:center; 
                        align-items:center; font-size:2rem; color:#2196F3;'>❌</div>
                        """, unsafe_allow_html=True)
                    elif symbol == 'O':
                        cols[j].markdown("""
                        <div style='height:80px; display:flex; justify-content:center; 
                        align-items:center; font-size:2rem; color:#F44336;'>⭕</div>
                        """, unsafe_allow_html=True)
                    else:
                        cols[j].markdown("""
                        <div style='height:80px; display:flex; justify-content:center; 
                        align-items:center; border:1px solid #ddd;'></div>
                        """, unsafe_allow_html=True)

def make_move(index):
    """Process a player's move in Tic Tac Toe"""
    board = st.session_state.tic_tac_toe_board
    current_player = st.session_state.tic_tac_toe_current_player
    
    if board[index] == ' ':
        # Update the board with player's move
        board[index] = current_player
        
        # Check for win or draw
        if check_tic_tac_toe_winner(board, current_player):
            st.session_state.tic_tac_toe_game_over = True
            st.session_state.tic_tac_toe_winner = current_player
        elif check_tic_tac_toe_draw(board):
            st.session_state.tic_tac_toe_game_over = True
            st.session_state.tic_tac_toe_winner = "Draw"
        else:
            # Switch player
            st.session_state.tic_tac_toe_current_player = 'O' if current_player == 'X' else 'X'
            
            # If it's computer's turn, make a move
            if st.session_state.tic_tac_toe_current_player == 'O':
                computer_move(st.session_state.tic_tac_toe_difficulty)

def computer_move(difficulty):
    """Computer makes a move in Tic Tac Toe"""
    board = st.session_state.tic_tac_toe_board
    
    # Choose move based on difficulty
    if difficulty == "Easy":
        move = computer_move_easy(board)
    elif difficulty == "Medium":
        # 50% chance of using hard strategy
        if random.random() < 0.5:
            move = computer_move_hard(board, 'O')
        else:
            move = computer_move_easy(board)
    else:  # Hard
        move = computer_move_hard(board, 'O')
    
    # Make the move
    board[move] = 'O'
    
    # Check for win or draw
    if check_tic_tac_toe_winner(board, 'O'):
        st.session_state.tic_tac_toe_game_over = True
        st.session_state.tic_tac_toe_winner = 'O'
    elif check_tic_tac_toe_draw(board):
        st.session_state.tic_tac_toe_game_over = True
        st.session_state.tic_tac_toe_winner = "Draw"
    else:
        st.session_state.tic_tac_toe_current_player = 'X'

def computer_move_easy(board):
    """Easy difficulty: random moves"""
    available_moves = [i for i, spot in enumerate(board) if spot == ' ']
    return random.choice(available_moves)

def computer_move_hard(board, player):
    """Hard difficulty: strategic moves (minimax simplified)"""
    opponent = 'X' if player == 'O' else 'O'
    
    # First, check for winning move
    for move in range(9):
        if board[move] == ' ':
            board[move] = player
            if check_tic_tac_toe_winner(board, player):
                board[move] = ' '  # Reset for testing other moves
                return move
            board[move] = ' '  # Reset for testing other moves
    
    # Second, block opponent's winning move
    for move in range(9):
        if board[move] == ' ':
            board[move] = opponent
            if check_tic_tac_toe_winner(board, opponent):
                board[move] = ' '  # Reset
                return move
            board[move] = ' '  # Reset
    
    # Third, prefer center
    if board[4] == ' ':
        return 4
    
    # Fourth, prefer corners
    corners = [0, 2, 6, 8]
    available_corners = [corner for corner in corners if board[corner] == ' ']
    if available_corners:
        return random.choice(available_corners)
    
    # Last, choose sides
    sides = [1, 3, 5, 7]
    available_sides = [side for side in sides if board[side] == ' ']
    if available_sides:
        return random.choice(available_sides)
    
    # Fallback (should not reach here if board has empty spaces)
    return random.choice([i for i, spot in enumerate(board) if spot == ' '])

def check_tic_tac_toe_winner(board, player):
    """Check if a player has won"""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_tic_tac_toe_draw(board):
    """Check if the game is a draw"""
    return ' ' not in board

def reset_tic_tac_toe():
    """Reset the Tic Tac Toe game state"""
    st.session_state.tic_tac_toe_board = [' ' for _ in range(9)]
    st.session_state.tic_tac_toe_current_player = 'X'
    st.session_state.tic_tac_toe_game_over = False
    st.session_state.tic_tac_toe_winner = None
    st.session_state.tic_tac_toe_difficulty = "Medium"  # Default difficulty

if __name__ == "__main__":
    main()

