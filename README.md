# Battleships
This game was made with python and runs in a terminal. 
The terminal used in this project is the Code Institute mock terminal on Heroku
The aim of the game is to hit the enemy ships before the enemy hits yours

[Link to deployed project](https://joes-battleships.herokuapp.com/)
<br>![Various device breakpoints for responsive design](assets/images/amiresponsive.png)

## How to play
This game is based on the classic game called Battleships, a game that dates back to to world war one. you can see more information at this link on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)).

After the player enters their name there board is randomly populated with four ships, each ship is represented by the @ symbol. The enemies ships are hidden so the player will have to guess where they are.

Every turn the player will have to choose two locations between 0 - 3
After the player takes their turn the computer will take their turn and both scores and boards will be updated.
### The guide is as follows:
    Open sea: .
    Location of ally ship: @
    Location missed: X
    Enemy/Ally ship hit: *
<br>![Guide](assets/images/guide.png)

To win you must sink all the enemy ships before they sink yours

## Features
### Existing Features
- Entering your Name
<br>![Enter your name in the app](assets/images/enteryourname.png)
- Random ship locations
<br>![Example Board](assets/images/randomshiploc.png)
- Enemy ships are hidden
<br>![Example of the enemy board](assets/images/hiddenships.png)
- Play against the computer
<br>![The Computer taking their turn](assets/images/complaying.png)
- Choose firing location
<br>![Player taking there turn](assets/images/chooseloc.png)
- Score area
<br>![Example Score](assets/images/score.png)


#### Input validation
- You must guess a Number
<br>![Example of entering the wrong number](assets/images/notanumber.png)
- The Number must be between 0 - 3
<br>![Example of entering a number greater than the board size](assets/images/scope.png)
- You cant guess the same location twice
<br>![Example of guessing the same location twice](assets/images/sameloctwice.png)

### Future Features
- Allow for a player to play vs another player
- Choose your own ship locations
- Choose the size of the board

## Data Model
I had to use O.O.P. so i decided to use a class model
Each player has an instance that stores there:
- Their name
- Their guesses
<br>![instance guesses and name](assets/images/nameandscore.png)
- The locations of their ships
<br>![Code for the location of the ships](assets/images/locationofships.png)

It also had methods to:
- Populate the board
<br>![code for populating the board](assets/images/popboard.png)
- Print the board 
<br>![code for printing the board](assets/images/printboard.png)
- Take a turn
<br>![code for taking a turn](assets/images/taketurn.png)

## Testing
I tested using the following:
Passed the code through a PEP8 with two errors
I also added the incorrect inputs to test if the program would sucessfully atempt to resolve the error.<br>
These errors were:
- Strings were numbers could only be inputed
<br>![Example of entering the wrong number](assets/images/notanumber.png)
- Values outside the scope
<br>![Example of entering a number greater than the board size](assets/images/scope.png)
- Targeting the same location more than once
<br>![Example of guessing the same location twice](assets/images/sameloctwice.png)<br>
I ran the code in my local terminal and the Code Institute Heroku terminal in chrome browser on my Windows PC, I also ran it on chrome browser on my Adroid mobile device and it worked without error.
### Bugs
Solved Bugs
- I had to declare the instances outside of a function to make them globally accessible
<br>![Fixed Bug](assets/images/bug.png)

There are no known remaining Bugs
### Validator Testing
- PEP8
    * Passed the code through a PEP8 with two errors. These errors were that two lines were too long but I did not know how to shorten these lines
    <br>![PEP8 Result](assets/images/pep8.png)

## Deployment 
This project was deployed using the Code Institute mock terminal on Heroku.
The steps for deployment are as follows:
- Fork or clone this repository
<br>![fork button](assets/images/fork.png)
- Create a new Heroku app
<br>![New app button](assets/images/new.png)
- Set the buildbacks to Python and NodeJS in that order
<br>![buildback layout](assets/images/build.png)
- Link the Heroku app to the repository
<br>![Linking the repo](assets/images/repo.png)
- Click on Deploy
<br>![Deployment button](assets/images/deploy.png)
## Credits 
- Code Institute for the deployment terminal
- Wikipedia for the details of the Battleships game