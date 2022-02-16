from random import randint

class Board:

    """
    This is the main object of the program.
    It sets the players name and if they are the computer
    It stores the location of the ships, scores and guesses made
    """
    def __init__(self, cptn, player_type):
        self.cptn = cptn
        self.player_type = player_type
        self.loc_ships = []
        self.loc_guesses = []
        self.score = 0
        # these are the printable boards,
        # their values are updated as as the game plays
        self.your_board = [
            ['. ', '. ', '. ', '. '],
            ['. ', '. ', '. ', '. '],
            ['. ', '. ', '. ', '. '],
            ['. ', '. ', '. ', '. ']]
        # this board is printed to hide the location of the enemy ships
        self.your_hidden_board = [
            ['. ', '. ', '. ', '. '],
            ['. ', '. ', '. ', '. '],
            ['. ', '. ', '. ', '. '],
            ['. ', '. ', '. ', '. ']]

    def pop_board(self):
        """
        this function populates the board
        It tests that it doesnt place a ship in the same location twice
        It updates the 'printable boards' and the .loc_ships list
        """
        while len(self.loc_ships) < 4:
            list = []
            while len(list) < 2:
                point = randint(0, 3)
                list.append(point)
            if list not in self.loc_ships:
                self.loc_ships.append(list)
                coord_x = list[0]
                coord_y = list[1]
                self.your_board[coord_x][coord_y] = "@ "

    def print_board(self):
        """
        This function based on what player it is
        prints the correct board
        """
        if(self.player_type == "player"):
            print(f"This is Captian {self.cptn}'s board")
            print(*self.your_board[0],)
            print(*self.your_board[1],)
            print(*self.your_board[2],)
            print(*self.your_board[3],)
        else:
            print("This is the computers board")
            print(*self.your_hidden_board[0],)
            print(*self.your_hidden_board[1],)
            print(*self.your_hidden_board[2],)
            print(*self.your_hidden_board[3],)

    def loc_validator(self):
        """
        this function fistly checks if it is the player or computer
        Then either checks the player values or
        gives the computer random values
        It also checks if the same place was guessed twice
        """
        if self.player_type == "player":
            while True:
                target = []
                target.append(row_validator())
                target.append(column_validator())
                if target not in self.loc_guesses:
                    self.loc_guesses.append(target)
                    return target
                    break
                else:
                    print("You cant guess the same place twice")
        else:
            while True:
                target = []
                target.append(randint(0, 3))
                target.append(randint(0, 3))
                if target not in self.loc_guesses:
                    self.loc_guesses.append(target)
                    return target
                    break

    def take_turn(self):
        """
        This function firstly checks if it is the player or the computer
        if it is the player:
            it lets the player know that their coordinates have been acepted
        if it is the computer:
            tells the player that the computer is taking its turn
        then it checks if it was a hit or a miss
        updates the correct boards
        prints the results of the targeted locations
        in the case of a hit, increments the score

        """
        turn_guess = self.loc_validator()
        if self.player_type == "player":
            print("Firing!")
            if computer_board.your_board[turn_guess[0]][turn_guess[1]] == "@ ":
                computer_board.your_hidden_board[turn_guess[0]][turn_guess[1]] = "*"
                print(f"Captian {self.cptn} has hit!")
                self.score += 1
            else:
                computer_board.your_hidden_board[turn_guess[0]][turn_guess[1]] = "X "
                print(f"Captian {self.cptn} has missed!")
        else:
            print("The Computer is firing!")
            if player_board.your_board[turn_guess[0]][turn_guess[1]] == "@ ":
                player_board.your_board[turn_guess[0]][turn_guess[1]] = "* "
                print("The Computer has hit!")
                self.score += 1
            else:
                player_board.your_board[turn_guess[0]][turn_guess[1]] = "X "
                print("The computer has missed!")
        if self.player_type == "computer":
            player_board.print_board()
            computer_board.print_board()

def row_validator():
    """
    This function simply asks the player for a row to target
    checks two condtions:
        validates that it is a number
        and if the number is between 0 and 3
    if both parameters are not met it returns and error and asks again
    """
    while True:
        try:
            guess_y = int(input("select a row: "))
        except ValueError:
            print("not a number")
        else:
            if 0 <= guess_y <= 3:
                return guess_y
                break
            else:
                print("Please choose a number between 0 and 3")

def column_validator():
    """
    This function simply asks the player for a column to target
    checks two condtions:
        validates that it is a number
        and if the number is between 0 and 3
    if both parameters are not met it returns and error and asks again
    """
    while True:
        try:
            guess_x = int(input("select a column: "))
        except ValueError:
            print("not a number")
        else:
            if 0 <= guess_x <= 3:
                return guess_x
                break
            else:
                print("Please choose a number between 0 and 3")

def play_game():
    """
    This function starts the game
    prints the score every turn
    checks if a player has won
    """
    while player_board.score <= 3 or computer_board.score <= 3:
        print(f"Captian {player_board.cptn}'s score is: {player_board.score}")
        print(f"Computers score is: {computer_board.score}")
        input("Press enter to continue ")
        player_board.take_turn()
        if player_board.score == 4:
            print(f"Captian {player_board.cptn} wins!")
            break
        computer_board.take_turn()
        if computer_board.score == 4:
            print(f"{computer_board.cptn} wins!")
            break

def game_setup():
    """
    this function sets up the boards by
    populating them and
    printing the boards before the turn begins
    """
    computer_board.pop_board()
    player_board.pop_board()

    player_board.print_board()
    computer_board.print_board()

print("Welcome to Battleships")
cptn_name = input("What is your name: ")
print(f"Welcome Captian {cptn_name}.")
print("The boards use Zero-based numbering")
print("Only values 0, 1, 2, 3 will be accepted")

# I had to declare these outside of a function to make them globally accessible
computer_board = Board("The Computer", "computer")
player_board = Board(cptn_name, "player")

game_setup()
play_game()
