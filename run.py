from random import randint

# Write your code to expect a terminal of 80 characters wide and 24 rows high
class Board:
    """
    gg
    """
    def __init__(self, cptn, player_type):
        self.cptn = cptn
        self.player_type = player_type
        self.loc_ships = []
        self.loc_guesses = []
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
            print("This is your board")
            print(*self.your_board[0],)
            print(*self.your_board[1],) 
            print(*self.your_board[2],) 
            print(*self.your_board[3],) 
        else:
            print("This is the enemy board")
            print(*self.your_hidden_board[0],)
            print(*self.your_hidden_board[1],) 
            print(*self.your_hidden_board[2],) 
            print(*self.your_hidden_board[3],)

    def loc_validator(self):
        """
        .git/
        """
        while True:
            target = []
            target.append(column_validator())
            target.append(row_validator())
            if target not in self.loc_guesses:
                return target
                break
            else:
                print("You cant guess the same place twice")

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

def new_game():
    """
    this is a doc string
    """
    print("Welcome to Battleships")
    cptn_name = input("What is your name: ")
    print(f"Welcome Captian {cptn_name}.")

    computer_board = Board("enemy", "computer")
    player_board = Board(cptn_name, "player")

    computer_board.pop_board()
    player_board.pop_board()

    player_board.print_board()
    computer_board.print_board()

    player_board.loc_validator()
    computer_board.loc_validator()

new_game()
