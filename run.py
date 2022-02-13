from random import randint

# Write your code to expect a terminal of 80 characters wide and 24 rows high
class Board:
    """
     
    """
    def __init__(self, cptn, player_type):
        self.cptn = cptn
        self.player_type = player_type
        self.loc_ships = []
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

def new_game():
    """
    this is a doc string
    """
    print("Welcome to Battleships")
    cptn_name = input("What is your name: ")
    print(f"Welcome Captian {cptn_name}.")

    computer_board = Board("enemy", "computer")
    player_board = Board(cptn_name, "player")

new_game()