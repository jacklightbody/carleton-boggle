readme.txt
CS 111, Fall 2014

Program Description:
This program generates the popular word game boggle in a graphics window. The user plays against the computer, which generates it's own  list of words from the boggle board. The user can enter words into a box in the grahics window using their keyboard.The user can submit a word by hitting the enter key or pressing the 'submit' button with their mouse. Every time the user submits a word, it will be added to a running list of the user's words in the graphics window. At the end of the game (after 2 minutes), the game will end automatically, each player's scores and a list of their unique words appears in the graphics window, and text appears in the graphics window telling the user if they have won or lost the game.

Program Construction:
This program is made of four different classes. The Boggle class generates the board and the game itself and includes functions for generating the letters and boogle board, creating the graphics window (with the boggle board, textbox for entering words, and submit button), ending the game, and keeping score. The player class allows the players to generate playable words. The human player class and the computer player class inherit the player class to prevent code duplication. The player class stores all the words that both players have, and the boggle class stores the current board and when the game should end. 
 
Program's Current Status:
It works!
To improve the game, we could:
1) Make the tiles buttons so that the user can enter a word by clicking on the tiles with their mouse
2) Make the timer show up on the screen
3) Have a 'play again' button appear at the end of the game
4) Let player choose between different difficulty levels
 
Running the Program:
1) Go to the project directory. Make sure that the directory contains the files buttons.py, graphics.py, twl98.txt, common.txt, and boggle.py
2) In the python terminal, run boggle.py, a boggle board will appear in the graphics window, and the timer will automatically start for 2 minutes. 
3) To input a playable word, type the playable word using the keyboard into the textbox beneath the gameboard and hit either the 'enter' button on the keyboard or press the 'submit' button
4) When the game ends, close the window
5) To play again, run boggle.py in the python terminal.