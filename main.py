def show_menu():
    print("Select a game:")
    print("1. Tic Tac Toe")
    print("2. Battleship")
    print("3. Rock, Paper, Scissors, Lizard, Spock")
    print("4. Exit")

def main():
    while True:
        show_menu()
        option = input("Enter the number of the game you want to play: ")
        
        if option == '1':
            from tic_tac_toe import tic_tac_toe
            tic_tac_toe.play()
        elif option == '2':
            from battleship import battleship
            battleship.play()
        elif option == '3':
            from rock_paper_scissors_lizard_spock import rpsls
            rpsls.play()
        elif option == '4':
            print("Thanks for playing. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()