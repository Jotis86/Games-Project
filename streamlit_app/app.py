import streamlit as st
import random
import time
import base64
from PIL import Image, ImageDraw, ImageFont
import io

# Set page configuration
st.set_page_config(page_title="Arcade Games Hub", layout="wide", initial_sidebar_state="expanded")

# Update the CSS with this completely new sidebar design
def load_css():
    st.markdown("""
    <style>
    /* Main app styling */
    .header-container {
        background: linear-gradient(135deg, #6e8efb, #a777e3);
        padding: 1.8rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
        color: white;
    }
    
    .header-container h1 {
        font-size: 3rem;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .header-container p {
        font-size: 1.2rem;
        opacity: 0.9;
    }
    
    /* COMPLETELY NEW SIDEBAR DESIGN */
    [data-testid="stSidebar"] {
        background-color: #f8f9fa;
        border-right: none;
    }
    
    .sidebar-container {
        padding: 1.5rem;
        margin: -1rem -1rem 0 -1rem;
        background: linear-gradient(135deg, #6e8efb, #a777e3);
        color: white;
        border-radius: 0 0 20px 20px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    
    .sidebar-container h2 {
        font-size: 1.8rem;
        margin-bottom: 0.5rem;
        color: white;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
    }
    
    .sidebar-container p {
        font-size: 1rem;
        color: white;
        opacity: 0.9;
    }
    
    .game-option {
        margin: 0.8rem 0;
        padding: 0.8rem;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        transition: all 0.3s;
        font-weight: 500;
        text-align: center;
        color: #555;
        border-left: 4px solid transparent;
    }
    
    .game-option:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        border-left: 4px solid #6e8efb;
    }
    
    .game-option.active {
        background-color: #f0f4ff;
        border-left: 4px solid #6e8efb;
        color: #3a5bb8;
        font-weight: 600;
    }
    
    .sidebar-separator {
        margin: 1.5rem 0;
        height: 1px;
        background: linear-gradient(to right, transparent, rgba(0,0,0,0.1), transparent);
        border: none;
    }
    
    .sidebar-footer {
        margin-top: 2rem;
        padding: 1rem;
        background: linear-gradient(135deg, #a777e3, #6e8efb);
        border-radius: 10px;
        color: white;
        text-align: center;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    
    .github-link {
        margin: 1.5rem auto;
        padding: 0.8rem;
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.3s;
        color: #333;
        text-decoration: none;
    }
    
    .github-link:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    
    .github-link img {
        width: 24px;
        margin-right: 8px;
    }
    
    /* Game container styling */
    .game-container {
        background-color: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
        border: 1px solid #f0f2f6;
    }
    
    .game-title {
        color: #6e8efb;
        text-align: center;
        margin-bottom: 1.5rem;
        font-size: 2.2rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    /* FIXED SCOREBOARD with better contrast */
    .score-card {
        background-color: white;
        padding: 1.2rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        border: 1px solid #e9ecef;
    }
    
    .score-card h3 {
        color: #555;
        margin-bottom: 0.5rem;
        font-size: 1.2rem;
    }
    
    .score-value {
        font-size: 3rem;
        font-weight: bold;
        margin: 0.5rem 0;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    .player-score { color: #3a5bb8; }
    .computer-score { color: #c62828; }
    
    /* Enhanced win/lose messages */
    .game-result {
        text-align: center;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1.5rem 0;
        font-weight: bold;
        font-size: 1.5rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% {
            transform: scale(1);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        50% {
            transform: scale(1.03);
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        }
        100% {
            transform: scale(1);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
    }
    
    .result-win { 
        background: linear-gradient(to right, rgba(76, 175, 80, 0.2), rgba(76, 175, 80, 0.1)); 
        color: #2e7d32; 
        border-left: 5px solid #2e7d32;
    }
    
    .result-lose { 
        background: linear-gradient(to right, rgba(244, 67, 54, 0.2), rgba(244, 67, 54, 0.1)); 
        color: #c62828; 
        border-left: 5px solid #c62828;
    }
    
    .result-draw { 
        background: linear-gradient(to right, rgba(255, 152, 0, 0.2), rgba(255, 152, 0, 0.1)); 
        color: #ef6c00; 
        border-left: 5px solid #ef6c00;
    }
    
    /* Tic Tac Toe styling */
    .ttt-cell {
        height: 110px;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: #f8f9fa;
        border-radius: 10px;
        font-size: 2.8rem;
        font-weight: bold;
        cursor: pointer;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        transition: all 0.2s;
        margin: 6px;
    }
    
    .ttt-cell:hover {
        background-color: #e9ecef;
        transform: scale(1.03);
    }
    
    .ttt-x { color: #6e8efb; }
    .ttt-o { color: #f44336; }
    
    /* Battleship styling */
    .ship-cell { 
        background: linear-gradient(to bottom, #bbdefb, #90caf9);
        border: 1px solid #64b5f6;
    }
    .hit-cell { 
        background: linear-gradient(to bottom, #ffcdd2, #ef9a9a);
        border: 1px solid #ef5350;
    }
    .miss-cell { 
        background: linear-gradient(to bottom, #e0e0e0, #bdbdbd);
        border: 1px solid #9e9e9e;
    }
    </style>
    """, unsafe_allow_html=True)

# And replace your sidebar code with this completely redesigned version:
def main():
    load_css()
    
    # Main app header
    st.markdown("""
    <div class="header-container">
        <h1>Arcade Games Hub</h1>
        <p>Classic games with a modern twist - Fun for everyone!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # COMPLETELY REDESIGNED SIDEBAR
    with st.sidebar:
        # Custom sidebar header
        st.markdown("""
        <div class="sidebar-container">
            <h2>Game Selection</h2>
            <p>Choose your favorite game to play</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Create game selector
        games = [
            "Battleship",
            "Tic Tac Toe",
            "Rock Paper Scissors Lizard Spock"
        ]
        
        # Store selected game in session state
        if 'selected_game' not in st.session_state:
            st.session_state.selected_game = "Battleship"
        
        # Display game options with better styling
        st.markdown("<div style='padding: 1rem 0;'>", unsafe_allow_html=True)
        for game_name in games:
            is_selected = st.session_state.selected_game == game_name
            active_class = "active" if is_selected else ""
            
            st.markdown(f"""
            <div class="game-option {active_class}" id="btn_{game_name}" 
                 onclick="document.getElementById('btn_{game_name}_hidden').click()">
                {game_name}
            </div>
            """, unsafe_allow_html=True)
            
            # Hidden button to handle the click
            if st.button(game_name, key=f"btn_{game_name}_hidden", label_visibility="collapsed"):
                st.session_state.selected_game = game_name
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<hr class='sidebar-separator'>", unsafe_allow_html=True)
        
        # Show difficulty settings for Tic Tac Toe
        if st.session_state.selected_game == "Tic Tac Toe":
            st.markdown("<div style='padding: 0 0.5rem;'>", unsafe_allow_html=True)
            difficulty = st.radio("Difficulty:", ["Easy", "Hard"])
            st.markdown("</div>", unsafe_allow_html=True)
        
        # GitHub link with better styling
        st.markdown("""
        <a href="https://github.com/Jotis86/Games-Project" target="_blank" class="github-link">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png">
            View on GitHub
        </a>
        """, unsafe_allow_html=True)
        
        # Footer
        st.markdown("""
        <div class="sidebar-footer">
            <p>Made with ❤️ and Streamlit</p>
            <p style="font-size: 0.8rem; opacity: 0.7;">© 2023 Arcade Games Hub</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Game section based on selection
    selected_game = st.session_state.selected_game
    
    if selected_game == "Battleship":
        display_rules("battleship")
        play_battleship()
    elif selected_game == "Tic Tac Toe":
        display_rules("tictactoe")
        play_tic_tac_toe(difficulty)
    else:  # Rock Paper Scissors Lizard Spock
        display_rules("rpsls")
        play_rpsls()

def display_rules(game_type):
    with st.expander("Game Rules", expanded=False):
        if game_type == "battleship":
            st.markdown("""
            ### 🚢 Battleship Rules
            - Play on a 5×5 grid against the computer
            - Place your 3 ships on the grid
            - Take turns firing at opponent's grid
            - First to sink all opponent's ships wins
            """)
        elif game_type == "tictactoe":
            st.markdown("""
            ### ❌⭕ Tic Tac Toe Rules
            - You play as X, computer plays as O
            - Take turns placing marks on the 3×3 grid
            - First to get 3 in a row wins
            - If all squares are filled with no winner, it's a draw
            """)
        else:  # RPSLS
            st.markdown("""
            ### ✊✋✌️🦎🖖 Rock Paper Scissors Lizard Spock Rules
            - Rock crushes Scissors and crushes Lizard
            - Paper covers Rock and disproves Spock
            - Scissors cuts Paper and decapitates Lizard
            - Lizard eats Paper and poisons Spock
            - Spock smashes Scissors and vaporizes Rock
            - First to score 3 points wins
            """)

# Replace the score display in the Rock Paper Scissors function
def play_rpsls():
    st.markdown('<div class="game-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="game-title">Rock Paper Scissors Lizard Spock ✊✋✌️🦎🖖</h2>', unsafe_allow_html=True)
    
    # Initialize session state
    if 'player_score' not in st.session_state:
        st.session_state.player_score = 0
    if 'computer_score' not in st.session_state:
        st.session_state.computer_score = 0
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False
    if 'round_result' not in st.session_state:
        st.session_state.round_result = None
    if 'player_choice' not in st.session_state:
        st.session_state.player_choice = None
    if 'computer_choice' not in st.session_state:
        st.session_state.computer_choice = None
    
    # Display scores with enhanced styling for better visibility
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="score-card">
            <h3>Your Score</h3>
            <div class="score-value player-score">{st.session_state.player_score}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="score-card">
            <h3>Computer's Score</h3>
            <div class="score-value computer-score">{st.session_state.computer_score}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Game result display
    if st.session_state.round_result:
        result_class = ""
        if st.session_state.round_result == "You win!":
            result_class = "result-win"
        elif st.session_state.round_result == "You lose!":
            result_class = "result-lose"
        else:
            result_class = "result-draw"
        
        st.markdown(f'<div class="game-result {result_class}">{st.session_state.round_result}</div>', unsafe_allow_html=True)
    
    # Display choices if made
    if st.session_state.player_choice and st.session_state.computer_choice:
        choice_col1, choice_col2 = st.columns(2)
        with choice_col1:
            st.markdown(f"""
            <div style="text-align: center;">
                <h4>You chose</h4>
                <div style="font-size: 3rem;">{get_rpsls_emoji(st.session_state.player_choice)}</div>
                <p>{st.session_state.player_choice}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with choice_col2:
            st.markdown(f"""
            <div style="text-align: center;">
                <h4>Computer chose</h4>
                <div style="font-size: 3rem;">{get_rpsls_emoji(st.session_state.computer_choice)}</div>
                <p>{st.session_state.computer_choice}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Button choices - now with all 5 options
    if not st.session_state.game_over:
        st.markdown("<h3 style='text-align: center;'>Make your choice:</h3>", unsafe_allow_html=True)
        
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            if st.button("✊ Rock", use_container_width=True):
                play_rpsls_round("Rock")
        with col2:
            if st.button("✋ Paper", use_container_width=True):
                play_rpsls_round("Paper")
        with col3:
            if st.button("✌️ Scissors", use_container_width=True):
                play_rpsls_round("Scissors")
        with col4:
            if st.button("🦎 Lizard", use_container_width=True):
                play_rpsls_round("Lizard")
        with col5:
            if st.button("🖖 Spock", use_container_width=True):
                play_rpsls_round("Spock")
    
    # Game over state
    if st.session_state.game_over:
        if st.session_state.player_score > st.session_state.computer_score:
            st.success("🎉 Congratulations! You won the game! 🎉")
        else:
            st.error("💔 Game over! The computer won! 💔")
        
        if st.button("Play Again"):
            reset_rpsls()
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def get_rpsls_emoji(choice):
    emojis = {
        "Rock": "✊",
        "Paper": "✋",
        "Scissors": "✌️",
        "Lizard": "🦎",
        "Spock": "🖖"
    }
    return emojis.get(choice, "")

def play_rpsls_round(player_choice):
    choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    computer_choice = random.choice(choices)
    
    # Save choices
    st.session_state.player_choice = player_choice
    st.session_state.computer_choice = computer_choice
    
    # Determine winner
    result = determine_rpsls_winner(player_choice, computer_choice)
    st.session_state.round_result = result
    
    # Update scores
    if result == "You win!":
        st.session_state.player_score += 1
    elif result == "You lose!":
        st.session_state.computer_score += 1
    
    # Check for game over
    if st.session_state.player_score >= 3 or st.session_state.computer_score >= 3:
        st.session_state.game_over = True
    
    # Force UI update
    st.rerun()

def determine_rpsls_winner(player, computer):
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

def reset_rpsls():
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.game_over = False
    st.session_state.round_result = None
    st.session_state.player_choice = None
    st.session_state.computer_choice = None

# TIC TAC TOE IMPLEMENTATION
def play_tic_tac_toe(difficulty):
    st.markdown('<div class="game-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="game-title">Tic Tac Toe ❌⭕</h2>', unsafe_allow_html=True)
    
    # Initialize session state
    if 'ttt_board' not in st.session_state:
        reset_tic_tac_toe()
    
    # Get current game state
    board = st.session_state.ttt_board
    current_player = st.session_state.ttt_current_player
    
    # Display current player
    if not st.session_state.ttt_game_over:
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 1rem;">
            <h3>Current Player: {current_player}</h3>
        </div>
        """, unsafe_allow_html=True)
    
    # Create the game board with better spacing
    st.markdown('<div style="max-width: 450px; margin: 0 auto; padding: 10px;">', unsafe_allow_html=True)
    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            index = i * 3 + j
            with cols[j]:
                if board[index] == ' ' and not st.session_state.ttt_game_over:
                    if st.button(" ", key=f"ttt_{index}", use_container_width=True, 
                               help="Click to place your mark"):
                        make_ttt_move(index, difficulty)
                        st.rerun()
                else:
                    symbol_class = "ttt-x" if board[index] == "X" else "ttt-o" if board[index] == "O" else ""
                    symbol = "❌" if board[index] == "X" else "⭕" if board[index] == "O" else " "
                    st.markdown(f'<div class="ttt-cell {symbol_class}">{symbol}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Game over state
    if st.session_state.ttt_game_over:
        result_message = ""
        result_class = ""
        
        if st.session_state.ttt_winner == "Draw":
            result_message = "It's a draw!"
            result_class = "result-draw"
        elif st.session_state.ttt_winner == "X":
            result_message = "🎉 You win! 🎉"
            result_class = "result-win"
        else:
            result_message = "💔 Computer wins! 💔"
            result_class = "result-lose"
        
        st.markdown(f'<div class="game-result {result_class}">{result_message}</div>', unsafe_allow_html=True)
        
        if st.button("Play Again", key="ttt_play_again"):
            reset_tic_tac_toe()
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def make_ttt_move(index, difficulty):
    board = st.session_state.ttt_board
    current_player = st.session_state.ttt_current_player
    
    if board[index] == ' ':
        # Update the board with player's move
        board[index] = current_player
        
        # Check for win or draw
        if check_ttt_winner(board, current_player):
            st.session_state.ttt_game_over = True
            st.session_state.ttt_winner = current_player
        elif check_ttt_draw(board):
            st.session_state.ttt_game_over = True
            st.session_state.ttt_winner = "Draw"
        else:
            # Switch player
            st.session_state.ttt_current_player = 'O' if current_player == 'X' else 'X'
            
            # Computer's turn
            if st.session_state.ttt_current_player == 'O' and not st.session_state.ttt_game_over:
                time.sleep(0.5)  # Slight delay for better UX
                if difficulty == "Easy":
                    computer_move = get_easy_move(board)
                else:
                    computer_move = get_hard_move(board)
                
                board[computer_move] = 'O'
                
                if check_ttt_winner(board, 'O'):
                    st.session_state.ttt_game_over = True
                    st.session_state.ttt_winner = 'O'
                elif check_ttt_draw(board):
                    st.session_state.ttt_game_over = True
                    st.session_state.ttt_winner = "Draw"
                else:
                    st.session_state.ttt_current_player = 'X'

def get_easy_move(board):
    available_moves = [i for i, spot in enumerate(board) if spot == ' ']
    return random.choice(available_moves)

def get_hard_move(board):
    # Check for winning move
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if check_ttt_winner(board, 'O'):
                board[i] = ' '
                return i
            board[i] = ' '
    
    # Block player's winning move
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if check_ttt_winner(board, 'X'):
                board[i] = ' '
                return i
            board[i] = ' '
    
    # Take center if available
    if board[4] == ' ':
        return 4
    
    # Take a corner
    corners = [0, 2, 6, 8]
    available_corners = [c for c in corners if board[c] == ' ']
    if available_corners:
        return random.choice(available_corners)
    
    # Take any available space
    available_moves = [i for i, spot in enumerate(board) if spot == ' ']
    return random.choice(available_moves)

def check_ttt_winner(board, player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for pattern in win_patterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] == player:
            return True
    return False

def check_ttt_draw(board):
    return ' ' not in board

def reset_tic_tac_toe():
    st.session_state.ttt_board = [' ' for _ in range(9)]
    st.session_state.ttt_current_player = 'X'
    st.session_state.ttt_game_over = False
    st.session_state.ttt_winner = None

# BATTLESHIP IMPLEMENTATION
def play_battleship():
    st.markdown('<div class="game-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="game-title">Battleship 🚢</h2>', unsafe_allow_html=True)
    
    # Initialize battleship state
    if 'bs_player_board' not in st.session_state:
        reset_battleship()
    
    # Phase indicator
    if not st.session_state.bs_ships_placed:
        st.subheader("Phase 1: Place your ships")
        st.write(f"Ships placed: {st.session_state.bs_player_ships}/3")
        
        # Option to place ships randomly
        if st.button("Place Ships Randomly"):
            place_ships_randomly(st.session_state.bs_player_board)
            st.session_state.bs_player_ships = 3
            st.session_state.bs_ships_placed = True
            place_ships_randomly(st.session_state.bs_computer_hidden_board)
            st.session_state.bs_game_started = True
            st.rerun()
    else:
        st.subheader("Phase 2: Battle!")
    
    # Display player's board
    st.write("Your Board:")
    display_battleship_board("player", st.session_state.bs_player_board, 
                           clickable=not st.session_state.bs_ships_placed, 
                           show_ships=True)
    
    # Display computer's board after ships are placed
    if st.session_state.bs_ships_placed:
        st.write("Enemy Board:")
        display_battleship_board("computer", st.session_state.bs_computer_board, 
                               clickable=st.session_state.bs_game_started, 
                               show_ships=False)
    
    # Game over states - Fixed the conditional display
    if st.session_state.bs_ships_placed:
        if check_battleship_winner(st.session_state.bs_computer_hidden_board):
            st.markdown('<div class="game-result result-win">🎉 VICTORY! You sank all enemy ships! 🎉</div>', unsafe_allow_html=True)
            st.session_state.bs_game_started = False
            
            if st.button("Play Again", key="bs_play_again1"):
                reset_battleship()
                st.rerun()
                
        elif check_battleship_winner(st.session_state.bs_player_board):
            st.markdown('<div class="game-result result-lose">💔 DEFEAT! Your fleet has been destroyed! 💔</div>', unsafe_allow_html=True)
            st.session_state.bs_game_started = False
            
            if st.button("Play Again", key="bs_play_again2"):
                reset_battleship()
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def display_battleship_board(board_type, board, clickable=True, show_ships=True):
    # Create coordinate labels
    cols = st.columns([0.5] + [1]*5)
    cols[0].write("")
    for i in range(5):
        cols[i+1].write(chr(65+i), help="Column")
    
    # Create board
    for row in range(5):
        cols = st.columns([0.5] + [1]*5)
        cols[0].write(str(row+1), help="Row")
        
        for col in range(5):
            cell_value = board[row][col]
            cell_class = ""
            
            # Determine cell display
            display_value = " "
            if cell_value == '🚢' and show_ships:
                cell_class = "ship-cell"
                display_value = "🚢"
            elif cell_value == '💥':
                cell_class = "hit-cell"
                display_value = "💥"
            elif cell_value == '❌':
                cell_class = "miss-cell"
                display_value = "❌"
            
            # Create button or display cell
            if clickable and cell_value == ' ':
                if cols[col+1].button(" ", key=f"{board_type}_{row}_{col}"):
                    handle_battleship_click(board_type, row, col)
                    st.rerun()
            else:
                cols[col+1].markdown(
                    f'<div style="height:40px; text-align:center; border-radius:4px;" class="{cell_class}">{display_value}</div>',
                    unsafe_allow_html=True
                )

def handle_battleship_click(board_type, row, col):
    if board_type == "player" and not st.session_state.bs_ships_placed:
        # Place ship on player board
        if st.session_state.bs_player_board[row][col] == ' ':
            st.session_state.bs_player_board[row][col] = '🚢'
            st.session_state.bs_player_ships += 1
            
            # Check if all ships placed
            if st.session_state.bs_player_ships == 3:
                st.session_state.bs_ships_placed = True
                place_ships_randomly(st.session_state.bs_computer_hidden_board)
                st.session_state.bs_game_started = True
    
    elif board_type == "computer" and st.session_state.bs_game_started:
        # Player attacks computer
        if (row, col) not in st.session_state.bs_player_moves:
            st.session_state.bs_player_moves.add((row, col))
            
            # Hit or miss
            if st.session_state.bs_computer_hidden_board[row][col] == '🚢':
                st.session_state.bs_computer_board[row][col] = '💥'
                st.session_state.bs_computer_hidden_board[row][col] = '💥'
            else:
                st.session_state.bs_computer_board[row][col] = '❌'
            
            # Check if player won
            if check_battleship_winner(st.session_state.bs_computer_hidden_board):
                st.session_state.bs_game_started = False
                return
            
            # Computer's turn
            computer_battleship_turn()
            
            # Check if computer won
            if check_battleship_winner(st.session_state.bs_player_board):
                st.session_state.bs_game_started = False

def computer_battleship_turn():
    while True:
        row, col = random.randint(0, 4), random.randint(0, 4)
        if (row, col) not in st.session_state.bs_computer_moves:
            st.session_state.bs_computer_moves.add((row, col))
            
            # Check hit or miss
            if st.session_state.bs_player_board[row][col] == '🚢':
                st.session_state.bs_player_board[row][col] = '💥'
            elif st.session_state.bs_player_board[row][col] == ' ':
                st.session_state.bs_player_board[row][col] = '❌'
            
            break

def place_ships_randomly(board):
    ships = 3
    while ships > 0:
        x, y = random.randint(0, 4), random.randint(0, 4)
        if board[x][y] == ' ':
            board[x][y] = '🚢'
            ships -= 1

def check_battleship_winner(board):
    for row in board:
        if '🚢' in row:
            return False
    return True

def reset_battleship():
    st.session_state.bs_player_board = [[' ' for _ in range(5)] for _ in range(5)]
    st.session_state.bs_computer_board = [[' ' for _ in range(5)] for _ in range(5)]
    st.session_state.bs_computer_hidden_board = [[' ' for _ in range(5)] for _ in range(5)]
    st.session_state.bs_ships_placed = False
    st.session_state.bs_player_ships = 0
    st.session_state.bs_game_started = True  # This is set initially to avoid errors
    st.session_state.bs_player_moves = set()
    st.session_state.bs_computer_moves = set()

if __name__ == "__main__":
    main()
