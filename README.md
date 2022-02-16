# Battleships
This game was made with python and runs in a terminal. 
The terminal used in this project is the Code Institute moch terminal on Heroku
The aim of the game is to hit the enemy ships before the enemy hits yours

## How to play
This game is based on the classic game called Battleships, a game that dates back to to world war one. you can see more information at this link on[Wikipedia]"https://en.wikipedia.org/wiki/Battleship_(game)"

firstly the player enters their name and then there ships are automattly placed on the board shown with an @ symbol, the enemies ships are hidden so the player will have to guess where they are

if you miss the location is marked with and X and hits are maked with an * 

to win you must sink all the enemy players ships first

## Features
### Existing Features
#### Boards display
    The ship locations of the boards are randomly generated but the computers locations remain hidden

    the result of the player is displayed
    the result of the computer is displayed
    the scores are recorded and displayed

    image of the end turn info

#### Input validation
    the game will return an error if a non-numeral is entered
    also if a figure outside the scope
    lastly you cannot make the same guess twice

### Future Features
I would like to let the player set the board size and the number of ships and also to place the ships where they wish.

## Data Model
    I had to use O.O.P. so i decided to use a class model 
    each player has an instance that stores there names, the locations of their ships, their guesses
    It also had methods to populate the board print the board and take a turn

## Testing
i tested using the following:
Passed the code through a PEP8 linterwith 2 errors
Given invalid inputs: strings when numbers are expected, out of bounds inputs, same input twice
Tested in my local terminal and the Code Institute Heroku terminal

### Deployment
This project was deployed using Code Institute's mock terminal for Heroku.
Steps for deployment:
Fork or clone this repository
Create a new Heroku app o Set the buildbacks to Python and NodeJS in that order 
Link the Heroku app to the repository
Click on Deploy
### Credits
Code Institute for the deployment terminal
Wikipedia for the details of the Battleships game