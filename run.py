from random import randint

class Board:
    """
    gg
    """
    def __init__(self, cptn, player_type):
        self.cptn = cptn
        self.player_type = player_type
        self.loc_ships = []
        self.loc_guesses = []
        self.score = 0
        self.your_board = [
            ['. ', '. ', '. ', '. '],
            ['. ', '. ', '. ', '. '],
            ['. ', '. ', '. ', '. '],
            ['. ', '. ', '. ', '. ']]
        self.your_hidden_board = [
            ['. ', '. ', '. ', '. '],
            ['. ', '. ', '. ', '. '],
            ['. ', '. ', '. ', '. '],
            ['. ', '. ', '. ', '. ']]

    def pop_board(self):
        """
        this is a doc string
        """
        while len(self.loc_ships) < 4:
            list = []
            while len(list) < 2:
                point = randint(0,3)
                list.append(point)
            if list not in self.loc_ships: 
                self.loc_ships.append(list)
                coord_x = list[0]
                coord_y = list[1]
                self.your_board[coord_x][coord_y] = "@ "

    def print_board(self):
        """
        this is a doc string
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
        .git/
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
                target.append(randint(0,3))
                target.append(randint(0,3))
                if target not in self.loc_guesses:
                    self.loc_guesses.append(target)
                    return target
                    break

    def take_turn(self):
        """
        .git/
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

def column_validator():
    """
    .git/
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

def row_validator():
    """
    .git/
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


def play_game():
    """
    .git/
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


    

def new_game():
    """
    this is a doc string
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

computer_board = Board("The Computer", "computer")
player_board = Board(cptn_name, "player")

new_game()
play_game()
