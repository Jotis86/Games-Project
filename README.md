# 🎮 Games Project 🎮

## Objectives and Included Games 🎯🎲

The goal of this project is to develop a collection of classic games that can be played from the command line. Each game is designed to provide a fun and challenging experience, whether you're playing against another human player or the computer. The included games are:

1. **Tic Tac Toe** ❌⭕
   - A classic strategy game for two players. The objective is to be the first to align three of your symbols (X or O) in a row, column, or diagonal.

2. **Battleship** 🚢💥
   - A strategy game where players place ships on a grid and then try to sink their opponent's ships by guessing their locations.

3. **Rock, Paper, Scissors, Lizard, Spock** ✊📄✂️🦎🖖
   - An expanded version of the classic Rock, Paper, Scissors game. In this version, two additional options are added: Lizard and Spock. The goal is to win a predetermined number of rounds to win the game.

## Development Process 🛠️

1. **Planning** 📝:
   - **Game Selection**: Deciding which games to include in the project (e.g., Tic Tac Toe, Battleship, Rock Paper Scissors Lizard Spock).
   - **Feature Definition**: Outlining the main features and rules for each game.
   - **Timeline**: Establishing a timeline for development milestones and deadlines.

2. **Design** 🎨:
   - **Project Structure**: Organizing the project into directories and files for better manageability.
   - **Game Logic**: Designing the algorithms and logic for each game's functionality.
   - **User Interface**: Planning the layout and design of the user interface for both command-line and web-based versions.

3. **Implementation** 💻:
   - **Coding**: Writing the code for each game, including game logic, user interaction, and error handling.
   - **Integration**: Combining individual game modules into a cohesive project.
   - **Version Control**: Using Git to track changes and manage different versions of the code.

4. **Testing** 🧪:
   - **Unit Testing**: Writing tests for individual functions and modules to ensure they work as expected.
   - **Integration Testing**: Testing the interaction between different modules to ensure they work together correctly.
   - **User Testing**: Gathering feedback from users to identify and fix any issues with the user experience.

5. **Documentation** 📚:
   - **User Guides**: Creating detailed guides to help users understand how to play each game.
   - **Code Comments**: Adding comments to the code to explain the purpose and functionality of different sections.
   - **README**: Writing a comprehensive README file to provide an overview of the project, installation instructions, and usage examples.

## Tools Used 🧰

- **Python** 🐍:
  - The main programming language used to develop the games.
  - Libraries such as `random` for game logic and `os` for file handling.

- **Visual Studio Code** 🖥️:
  - The integrated development environment (IDE) used to write and test the code.
  - Extensions for Python development, such as Pylint for code linting and Python Test Explorer for running tests.

- **Git** 🌳:
  - Version control system used to manage the project's source code.
  - Commands such as `git clone`, `git commit`, `git push`, and `git pull` for repository management.

- **Streamlit** 🌐:
  - Framework used to create web-based versions of the games.
  - Commands such as `streamlit run app.py` to launch the web app.

- **Markdown** ✍️:
  - Used for writing documentation, including the README file and user guides.
  - Provides a simple syntax for formatting text, creating lists, and adding links.

- **GitHub** 🐙:
  - Platform used to host the project's repository.
  - Features such as Issues for bug tracking and Pull Requests for code reviews and collaboration.

## How to Run 🚀

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/your-username/games-project.git
   cd games-project
2. Run the main.py file to start the game selection menu.
3. Select the game you want to play by entering the corresponding number in the menu.

## Project Structure 📂

- **games/**
  - **tic_tac_toe/** ❌⭕
    - `__init__.py`
    - `tic_tac_toe.py`
  - **battleship/** 🚢💥
    - `__init__.py`
    - `battleship.py`
  - **rock_paper_scissors_lizard_spock/** ✊📄✂️🦎🖖
    - `__init__.py`
    - `rpsls.py`
  - **streamlit_app/** 🌐
    - `__init__.py`
    - `app.py`
- `.gitignore` 🚫
- `main.py`
- `README.md`
- `requirements.txt`

## Streamlit App 🌐

The streamlit_app directory contains the files necessary to run a web-based version of the games using Streamlit. This allows you to play the games in a web browser with a graphical user interface.
You can try the app [here](https://games-project-hgkadwvnzyvmvwoaatvgne.streamlit.app/)

### How to Run the Streamlit App

1. Navigate to the streamlit_app directory => cd streamlit_app
2. Install the required dependencies => pip install -r ../requirements.txt
3. Run the Streamlit app => streamlit run app.py
4. Open your web browser and go to the URL provided by Streamlit to start playing the games.


## Contributions 🤝

Contributions are welcome! If you want to contribute to this project, please follow these steps:

1. Fork the repository: Click on the "Fork" button at the top right corner of the repository page to create a copy of the repository in your GitHub account.
2. Clone the repository: Clone the forked repository to your local machine.
3. git checkout -b feature/new-feature
4. git commit -m "Add new feature"
5. git push origin feature/new-feature
6. Open a Pull Request in the original repository.

## Contact 📬

If you have any questions, suggestions, or feedback, feel free to reach out:

- **Email**: jotaduranbon@gmail.com
- **LinkedIn**: www.linkedin.com/in/juan-duran-bon


We appreciate your interest and support! 🙏

Thank you for playing and contributing to this project! 🎉 


