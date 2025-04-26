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
        /* Main banner styling */
        .main-banner {
            background: linear-gradient(to right, #1a237e, #4a148c);
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
            text-align: center;
        }
        
        .main-banner h1 {
            font-size: 3.5rem !important;
            font-weight: 800;
            color: white;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
            margin: 0;
            letter-spacing: 1px;
        }
        
        .main-banner p {
            color: rgba(255,255,255,0.8);
            font-size: 1.2rem;
            margin-top: 10px;
        }
        
        /* Sidebar styling */
        .sidebar-banner {
            background: linear-gradient(to bottom, #303f9f, #7b1fa2);
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 25px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        
        .sidebar-banner h2 {
            color: white;
            font-size: 1.8rem;
            margin: 0;
            font-weight: 700;
        }
        
        /* Game cards styling */
        .game-card {
            background: white;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 6px 12px rgba(0,0,0,0.1);
            margin-bottom: 25px;
            transition: transform 0.3s ease;
        }
        
        .game-card:hover {
            transform: translateY(-5px);
        }
        
        .game-header {
            color: #1976D2;
            text-align: center;
            padding: 10px 15px;
            margin-bottom: 20px;
            border-radius: 8px;
            background: #f0f7ff;
            font-weight: 700;
            font-size: 2rem;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        
        /* Score display styling */
        .score-display {
            padding: 15px;
            background: linear-gradient(to right, #2196F3, #4CAF50);
            border-radius: 10px;
            margin: 15px 0;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        
        .score-display h3 {
            color: white;
            margin: 0;
            font-size: 1.3rem;
            font-weight: 600;
        }
        
        .score-display h2 {
            color: white;
            margin: 5px 0 0 0;
            font-size: 2.5rem;
            font-weight: 800;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }
        
        /* Tic Tac Toe board styling */
        .ttt-board {
            max-width: 400px;
            margin: 0 auto;
            background: #f8f9fa;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        
        .ttt-cell {
            height: 100px;
            background: white;
            border: 2px solid #dee2e6;
            border-radius: 8px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 3rem;
            margin: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            transition: all 0.2s ease;
        }
        
        .ttt-cell:hover {
            background: #f0f2f6;
            transform: scale(1.03);
        }
        
        .ttt-x {
            color: #007bff;
            font-weight: bold;
        }
        
        .ttt-o {
            color: #dc3545;
            font-weight: bold;
        }
        
        /* GitHub link button */
        .github-button {
            background: #333;
            color: white;
            padding: 10px 15px;
            border-radius: 8px;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            margin-top: 10px;
            transition: all 0.2s ease;
        }
        
        .github-button:hover {
            background: #555;
            transform: translateY(-2px);
        }
        
        .github-button img {
            width: 24px;
            height: 24px;
        }
        
        /* Responsive cell sizes for smaller screens */
        @media (max-width: 768px) {
            .ttt-cell {
                height: 80px;
            }
        }
        
        /* Other existing styles */
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
            background-color: #2196F3 !important;
            color: white;
            border-radius: 5px;
        }
        
        .hit-cell {
            background-color: #F44336 !important;
            color: white;
            border-radius: 5px;
        }
        
        .miss-cell {
            background-color: #78909C !important;
            color: white;
            border-radius: 5px;
        }
        
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        
        /* Battleship grid styling */
        .bs-grid {
            max-width: 500px;
            margin: 0 auto;
            background: #f8f9fa;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        
        .bs-cell {
            height: 50px;
            background: white;
            border: 2px solid #dee2e6;
            border-radius: 8px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 1.5rem;
            margin: 3px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            transition: all 0.2s ease;
        }
        
        .bs-cell:hover {
            background: #e9ecef;
            transform: scale(1.05);
        }
        
        /* RPSLS choice buttons */
        .choice-btn {
            background: white;
            border: 2px solid #dee2e6;
            border-radius: 50%;
            width: 80px;
            height: 80px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            margin: 0 auto;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: all 0.2s ease;
        }
        
        .choice-btn:hover {
            transform: scale(1.1);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
            border-color: #007bff;
        }
        
        .choice-emoji {
            font-size: 2rem;
            margin-bottom: 5px;
        }
        
        .choice-name {
            font-size: 0.8rem;
            color: #495057;
        }
    </style>
    """, unsafe_allow_html=True)

def main():
    local_css()
    
    # App header with custom banner
    st.markdown("""
    <div class="main-banner">
        <h1>🎮 Arcade Games Hub</h1>
        <p>Classic games reimagined for your entertainment!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Customize sidebar
    with st.sidebar:
        st.markdown("""
        <div class="sidebar-banner">
            <h2>🎲 Game Selection</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Add a nice game selection image
        st.image("https://cdn-icons-png.flaticon.com/512/2257/2257820.png", width=120)
        
        # Game selection
        game = st.selectbox(
            "Choose a game to play", 
            ["Battleship", "Tic Tac Toe", "Rock Paper Scissors Lizard Spock"]
        )
        
        # GitHub Link
        st.markdown("""
        <a href="https://github.com/yourusername/games-project" class="github-button" target="_blank">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png">
            View on GitHub
        </a>
        """, unsafe_allow_html=True)
    
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
            ### 🚢 Battleship Rules
            1. You'll play on a 5x5 grid against the computer
            2. Place your 3 ships on the grid
            3. Take turns guessing locations of opponent's ships
            4. First to sink all opponent's ships wins!
            """)
        elif game_type == "tictactoe":
            st.markdown("""
            ### ⭕❌ Tic Tac Toe Rules
            1. Play on a 3x3 grid (you're X, computer is O)
            2. Take turns placing your symbol
            3. Get three in a row (horizontally, vertically, or diagonally) to win
            4. If the board fills up with no winner, it's a draw
            """)
        else:  # RPSLS
            st.markdown("""
            ### ✊✋✌️🦎🖖 Rock Paper Scissors Lizard Spock Rules
            - Rock crushes Scissors and Lizard
            - Paper covers Rock and disproves Spock
            - Scissors cuts Paper and decapitates Lizard
            - Lizard eats Paper and poisons Spock
            - Spock vaporizes Rock and smashes Scissors
            
            First to score 3 points wins the match!
            """)

# ROCK PAPER SCISSORS LIZARD SPOCK IMPLEMENTATION
def play_rpsls():
    with st.container():
        st.markdown('<div class="game-card">', unsafe_allow_html=True)
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
        st.markdown("<h3 style='text-align: center; margin-top: 20px;'>Make your choice:</h3>", unsafe_allow_html=True)
        
        # Create buttons for each choice
        cols = st.columns(len(choices))
        player_choice = None
        
        for idx, (choice, emoji) in enumerate(choices.items()):
            with cols[idx]:
                st.markdown(f"""
                <div style="text-align: center;">
                    <button class="choice-btn" onclick="document.getElementById('choice_{choice}').click()">
                        <span class="choice-emoji">{emoji}</span>
                        <span class="choice-name">{choice}</span>
                    </button>
                </div>
                """, unsafe_allow_html=True)
                
                # Hidden button to handle the click
                if st.button(f"{choice}", key=f"choice_{choice}", 
                           help=f"Choose {choice}", 
                           on_click=None, 
                           disabled=st.session_state.game_over):
                    player_choice = choice
        
        # Process game logic when a choice is made
        if player_choice:
            computer_choice = random.choice(list(choices.keys()))
            
            # Show the choices with animation
            choice_display_col1, choice_display_col2 = st.columns(2)
            
            with choice_display_col1:
                st.markdown(f"""
                <div style='text-align: center; background: #f8f9fa; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
                    <h4 style="margin-bottom: 15px;">Your choice</h4>
                    <div style='font-size: 4rem; margin-bottom: 10px;'>{choices[player_choice]}</div>
                    <p style="font-weight: bold; color: #007bff;">{player_choice}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with choice_display_col2:
                st.markdown(f"""
                <div style='text-align: center; background: #f8f9fa; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
                    <h4 style="margin-bottom: 15px;">Computer's choice</h4>
                    <div style='font-size: 4rem; margin-bottom: 10px;'>{choices[computer_choice]}</div>
                    <p style="font-weight: bold; color: #dc3545;">{computer_choice}</p>
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
                    st.markdown(f"""
                    <div style="padding: 10px; border-bottom: 1px solid #eee; margin-bottom: 5px;">
                        <b>Round {idx+1}:</b> You chose {round_data['player_choice']} {choices[round_data['player_choice']]}, 
                        Computer chose {round_data['computer_choice']} {choices[round_data['computer_choice']]} - 
                        <span style="color: {'#4CAF50' if round_data['result'] == 'You win!' else '#F44336' if round_data['result'] == 'You lose!' else '#FF9800'}">
                            {round_data['result']}
                        </span>
                    </div>
                    """, unsafe_allow_html=True)
        
        # Game over state
        if st.session_state.game_over:
            if st.session_state.player_score > st.session_state.computer_score:
                st.markdown("""
                <div class='win-text' style="padding: 20px; background: rgba(76, 175, 80, 0.1); border-radius: 10px;">
                    🎉 CONGRATULATIONS! YOU WON THE MATCH! 🎉
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class='lose-text' style="padding: 20px; background: rgba(244, 67, 54, 0.1); border-radius: 10px;">
                    💔 You lost the match. Better luck next time! 💔
                </div>
                """, unsafe_allow_html=True)
            
            if st.button("Play Again", key="rpsls_play_again"):
                reset_rpsls()
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

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
    with st.container():
        st.markdown('<div class="game-card">', unsafe_allow_html=True)
        st.markdown('<h2 class="game-header">Battleship 🚢💥</h2>', unsafe_allow_html=True)
        
        # Initialize battleship session state
        if 'player_board' not in st.session_state:
            reset_game_battleship()
        
        # Display game status
        if not st.session_state.ships_placed:
            st.markdown("""
            <div style="text-align: center; padding: 10px; background: #e3f2fd; border-radius: 10px; margin-bottom: 20px;">
                <h3 style="color: #1976D2;">Phase 1: Place Your Ships</h3>
                <p>Click on the grid to place your ships - 3 ships required</p>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.markdown(f"""
                <div style="text-align: center; font-size: 1.5rem; font-weight: bold; 
                    color: {'#4CAF50' if st.session_state.player_ships == 3 else '#1976D2'};">
                    Ships placed: {st.session_state.player_ships}/3
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="text-align: center; padding: 10px; background: #fff3e0; border-radius: 10px; margin-bottom: 20px;">
                <h3 style="color: #FF9800;">Phase 2: Battle!</h3>
                <p>Click on enemy waters to launch your attack</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Create visual grid for player's board
        st.markdown("<h4 style='text-align: center; margin-bottom: 15px;'>Your Fleet:</h4>", unsafe_allow_html=True)
        
        # Display the battleship board with a nicer UI
        display_battleship_board(
            "player", 
            st.session_state.player_board, 
            clickable=not st.session_state.ships_placed,
            show_ships=True
        )
        
        # Display computer's board only after ships are placed
        if st.session_state.ships_placed:
            st.markdown("<h4 style='text-align: center; margin: 30px 0 15px 0;'>Enemy Waters:</h4>", unsafe_allow_html=True)
            display_battleship_board(
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
            # Option to place ships randomly
            if st.button("Place Ships Randomly", key="random_ships"):
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
                message_container.markdown("""
                <div class='win-text' style='padding: 20px; background: rgba(76, 175, 80, 0.1); border-radius: 10px;'>
                    🎉 VICTORY! You sank all enemy ships! 🎉
                </div>
                """, unsafe_allow_html=True)
                st.session_state.game_started = False
                if st.button("Play Again", key="battleship_play_again"):
                    reset_game_battleship()
                    st.rerun()
            elif check_winner(st.session_state.player_board):
                message_container.markdown("""
                <div class='lose-text' style='padding: 20px; background: rgba(244, 67, 54, 0.1); border-radius: 10px;'>
                    💔 DEFEAT! Your fleet has been destroyed! 💔
                </div>
                """, unsafe_allow_html=True)
                st.session_state.game_started = False
                if st.button("Play Again", key="battleship_play_again2"):
                    reset_game_battleship()
                    st.rerun()
            else:
                status_container.info("Click on enemy waters to launch an attack!")
        
        st.markdown('</div>', unsafe_allow_html=True)

def display_battleship_board(board_type, board, clickable=True, show_ships=True):
    """Display a more visually appealing battleship board"""
    # Create a CSS grid for the battleship board
    st.markdown("""
    <div class="bs-grid">
        <div style="display: grid; grid-template-columns: 30px repeat(5, 1fr); gap: 5px; margin-bottom: 10px;">
            <div></div>
            <div style="text-align: center; font-weight: bold;">A</div>
            <div style="text-align: center; font-weight: bold;">B</div>
            <div style="text-align: center; font-weight: bold;">C</div>
            <div style="text-align: center; font-weight: bold;">D</div>
            <div style="text-align: center; font-weight: bold;">E</div>
    """, unsafe_allow_html=True)
    
    # Create grid rows
    for row in range(5):
        st.markdown(f"""
        <div style="display: grid; grid-template-columns: 30px repeat(5, 1fr); gap: 5px; margin-bottom: 5px;">
            <div style="display: flex; justify-content: center; align-items: center; font-weight: bold;">{row+1}</div>
        """, unsafe_allow_html=True)
        
        # Create cells for this row
        for col in range(5):
            cell_value = board[row][col]
            cell_class = ""
            cell_content = ""
            
            # Style based on cell content
            if cell_value == '🚢' and show_ships:
                cell_class = "ship-cell"
                cell_content = "🚢"
            elif cell_value == '💥':
                cell_class = "hit-cell"
                cell_content = "💥"
            elif cell_value == '❌':
                cell_class = "miss-cell"
                cell_content = "❌"
            
            # Create the cell
            btn_id = f"{board_type}_cell_{row}_{col}"
            
            if clickable and (cell_value == ' ' or (board_type == "computer" and cell_value != '💥' and cell_value != '❌')):
                st.markdown(f"""
                <div class="bs-cell" onclick="document.getElementById('{btn_id}').click()"></div>
                """, unsafe_allow_html=True)
                
                # Hidden button to handle click
                if st.button("", key=btn_id, help=f"Cell {chr(65+col)}{row+1}", on_click=None):
                    handle_battleship_click(board_type, row, col)
                    st.rerun()
            else:
                st.markdown(f"""
                <div class="bs-cell {cell_class}">{cell_content}</div>
                """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def handle_battleship_click(board_type, row, col):
    """Handle clicks on the battleship board"""
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
                st.session_state.last_result = "hit"
            else:
                st.session_state.computer_board[row][col] = '❌'
                st.session_state.last_result = "miss"
            
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
    st.session_state.last_result = None

# TIC TAC TOE IMPLEMENTATION
def play_tic_tac_toe(difficulty):
    with st.container():
        st.markdown('<div class="game-card">', unsafe_allow_html=True)
        st.markdown('<h2 class="game-header">Tic Tac Toe ❌⭕</h2>', unsafe_allow_html=True)
        
        # Initialize session state
        if 'tic_tac_toe_board' not in st.session_state:
            reset_tic_tac_toe()
            st.session_state.tic_tac_toe_difficulty = difficulty
        
        # Get current game state
        board = st.session_state.tic_tac_toe_board
        current_player = st.session_state.tic_tac_toe_current_player
        
        # Display current player's turn
        if not st.session_state.tic_tac_toe_game_over:
            player_color = "#007bff" if current_player == "X" else "#dc3545"
            player_symbol = "❌" if current_player == "X" else "⭕"
            
            st.markdown(f"""
            <div style='text-align:center; margin-bottom:1rem; padding: 10px; 
                 background: rgba({0, 123, 255, 0.1 if current_player == "X" else 220, 53, 69, 0.1});
                 border-radius: 10px;'>
                <h3 style='color: {player_color}'>Current Player: {player_symbol} {current_player}</h3>
            </div>
            """, unsafe_allow_html=True)
        
        # Create the enhanced Tic Tac Toe board
        display_enhanced_ttt_board(board)
        
        # Game over state
        if st.session_state.tic_tac_toe_game_over:
            if st.session_state.tic_tac_toe_winner == "Draw":
                st.markdown("""
                <div class='draw-text' style='padding: 20px; background: rgba(255, 152, 0, 0.1); border-radius: 10px;'>
                    🤝 IT'S A DRAW! 🤝
                </div>
                """, unsafe_allow_html=True)
            elif st.session_state.tic_tac_toe_winner == "X":
                st.markdown("""
                <div class='win-text' style='padding: 20px; background: rgba(76, 175, 80, 0.1); border-radius: 10px;'>
                    🎉 YOU WIN! 🎉
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class='lose-text' style='padding: 20px; background: rgba(244, 67, 54, 0.1); border-radius: 10px;'>
                    💔 COMPUTER WINS! 💔
                </div>
                """, unsafe_allow_html=True)
            
            if st.button("Play Again", key="ttt_play_again"):
                reset_tic_tac_toe()
                st.session_state.tic_tac_toe_difficulty = difficulty
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

def display_enhanced_ttt_board(board):
    """Display enhanced Tic Tac Toe board with better styling"""
    st.markdown('<div class="ttt-board">', unsafe_allow_html=True)
    
    # Create 3x3 grid
    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            index = i * 3 + j
            with cols[j]:
                cell_value = board[index]
                cell_class = "ttt-x" if cell_value == "X" else "ttt-o" if cell_value == "O" else ""
                btn_id = f"ttt_btn_{index}"
                
                if cell_value == ' ' and not st.session_state.tic_tac_toe_game_over:
                    # Empty cell - create clickable button
                    st.markdown(f"""
                    <div class="ttt-cell" onclick="document.getElementById('{btn_id}').click()"></div>
                    """, unsafe_allow_html=True)
                    
                    # Hidden button to handle the click
                    if st.button("", key=btn_id, help="Place your X here", on_click=None):
                        make_ttt_move(index)
                        st.rerun()
                else:
                    # Show X or O with appropriate styling
                    symbol = "❌" if cell_value == "X" else "⭕" if cell_value == "O" else ""
                    st.markdown(f"""
                    <div class="ttt-cell {cell_class}">{symbol}</div>
                    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def make_ttt_move(index):
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
                # Add a slight delay for better UX
                time.sleep(0.5)
                make_computer_move(st.session_state.tic_tac_toe_difficulty)

def make_computer_move(difficulty):
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

if __name__ == "__main__":
    main()
