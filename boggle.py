import random
import time
from buttons import *
def main():
        game=Boggle()
class Boggle:
    def __init__(self):
        # This is the frequency that each letter appears in boggle
        # Not ideal but it works ok
        self.tiles = 19 * ['E'] + 13 * ['T'] + 12 * ['A'] + 12 * ['R'] + 11 * ['I'] + 11 * ['N'] + 11 * ['O'] \
        + 9 * ['S'] + 6 * ['D'] + 5 * ['C'] + 5 * ['H'] + 5 * ['I'] + 4 * ['F'] + 4 * ['M'] + 4 * ['P'] + 4 * ['U'] \
        + 3 * ['G'] + 3 * ['Y'] + 2 * ['W'] + ['B'] + ['J'] + ['K'] + ['Qu'] + ['V'] + ['X'] + ['Z']
        self.endTime = time.time()+120
        self.gameOver=False
        self.player1 = ComputerPlayer(self.endTime)
        self.player2 = HumanPlayer(self.endTime)
        self.createBoard()
  
    def createBoard(self):
        '''Generates the game'''
        # Generate 4 Sets of random tiles (Each set is a row)
        self.board=[]
        for i in range(0,4):
            self.board.append(random.sample(self.tiles,4))
        # Provides the board to the player class
        self.player1.updateBoard(self.board)
        self.player2.updateBoard(self.board)
        self.player1.createWords()
        self.buttons = []
        # Prints the board in the boggle graphics window
        for row in range(4):
            for col in range(4):
                self.buttons.append(Button(row * 100, col * 100, 100, 100, self.board[row][col]))
        # Creates the submit button
        self.buttons.append(Button(150, 465, 100, 30, 'Submit'))
        self.responsetext=''
        # Creates the boggle graphics window
        self.buttonWindow = ButtonWindow("Boggle", 800, 600, self.buttons)
        self.buttonWindow.window.setMouseHandler(self.handleClick)
        self.buttonWindow.window.master.bind("<Key>",self.handleKeyPress)
        self.entry = Entry(Point(200, 450),40)
        self.entry.draw(self.buttonWindow.window)
        self.humanWordsText = Text(Point(700,400), 'Human Words: ')
        self.humanWordsText.draw(self.buttonWindow.window)
        Text(Point(200, 430),'Enter a boggle word').draw(self.buttonWindow.window) # label for the Entry
        for square in self.buttons:
            square.draw(self.buttonWindow)
        raw_input('Press Enter to Quit')

    def handleClick(self, point):
        '''Determines what happens when the human player clicks the submit button '''
        # If time is up, ends the game
        if time.time()>self.endTime:
            self.endGame()
        # Code for what happens when user clicks the 'submit' button after typing a word in the textbox
        square = self.buttonWindow.squares[-1]
        if square.pointInside(point):
            # Checks the word the human player typed into the textbox
            result = self.player2.createWord(self.entry.getText())
            # If time is up, end the game
            if result == 'END GAME':
                self.endGame()
            # Undraws text in the boggle window to make space for printing an error or 'word added' message
            self.entry.setText('')
            if self.responsetext!='':
                    self.responsetext.undraw()
            # If the word is not playable, print 'Invalid Entry, Try Aagain!' in the boggle window
            if result == False:
                self.responsetext = Text(Point(200, 530), 'Invalid entry, try again!')
                self.responsetext.draw(self.buttonWindow.window) 
            # If the word is playable add the word to the human player list and print 'Word Added' in the boggle window
            else:
                self.responsetext = Text(Point(200, 530), 'Word Added')
                self.responsetext.draw(self.buttonWindow.window) 
                self.humanWordsText.undraw()
                self.humanWordsText = Text(Point(700, 400), 'Human Words: '+ self.player2.listWords())
                self.humanWordsText.draw(self.buttonWindow.window)

    def handleKeyPress(self,key):
        '''Determines what happens when the human player presses the 'enter' button on the keyboard '''
        # If time is up, ends the game
        if time.time()>self.endTime:
            self.endGame()
        # Code for what happens when user clicks the 'enter' key after typing a word in the textbox
        if key.keysym == 'Return': #http://stackoverflow.com/questions/24671105/how-to-check-if-the-enter-key-is-pressed-python
            result = self.player2.createWord(self.entry.getText())
            # If time is up, ends the game
            if result == 'END GAME':
                self.endGame()
            # Undraws text in the boggle window to make space for printing an error or 'word added' message
            self.entry.setText('')
            if self.responsetext!='':
                self.responsetext.undraw()
            # If the word is not playable, prints 'Invalid entry, try again!' in the boggle window
            if result == False:
                self.responsetext = Text(Point(200, 530), 'Invalid entry, try again!')
                self.responsetext.draw(self.buttonWindow.window)
            # If the word is playable add the word to the human player list and print 'Word Added' in the boggle window
            else:
                self.responsetext = Text(Point(200, 530), 'Word Added')
                self.responsetext.draw(self.buttonWindow.window) 
                self.humanWordsText.undraw()
                self.humanWordsText = Text(Point(700,300), 'Human Words: '+ self.player2.listWords())
                self.humanWordsText.draw(self.buttonWindow.window)

    def endGame(self):
        '''Ends a boggle game'''
        if self.gameOver!=False:
            return False
        self.gameOver=True
        # Prints the game over text in the boggle window
        self.text = Text(Point(600, 50), 'Game Over!')
        self.text.draw(self.buttonWindow.window) 
        p1,p2,r1,r2=self.score(self.player1.getWords(),self.player2.getWords())
        # Prints a list of the words generated by the computer player in the boggle window
        self.computerWordsText = Text(Point(500, 300), 'Computer Words: '+ self.player1.listWords())
        self.computerWordsText.draw(self.buttonWindow.window)
        # Prints a list of all the words entered by the human player in the boggle window
        self.humanWordsText = Text(Point(700,300), 'Human Words: '+ self.player2.listWords())
        self.humanWordsText.draw(self.buttonWindow.window)
        # Prints the computer player score and the human score in the boggle window
        self.scoresText = Text(Point(600,100), 'Computer Score: '+ str(p1) + ' Your Score: ' + str(p2))
        self.scoresText.draw(self.buttonWindow.window)
        # Prints "You lost!" in the boggle window if the human player has a lower score than the computer player
        if p1>p2:
            self.loserText = Text(Point(600,150),'You lost!')
            textColor = color_rgb(255, 0, 0)
            self.loserText.setTextColor(textColor)
            self.loserText.setSize(36)
            self.loserText.draw(self.buttonWindow.window)
        # Prints "Congratulations, you won!" in the boggle window if the human player has a higher score than the computer player
        elif p1<p2:
            self.winnerText = Text(Point(600,150),'You won!')
            textColor = color_rgb(0, 255, 0)
            self.winnerText.setTextColor(textColor)
            self.winnerText.setSize(36)
            self.winnerText.draw(self.buttonWindow.window)
        # Prints "Tie!" in the boggle window if the human player and the computer player have an equal score
        else:
            self.tieText = Text(Point(600,150),'Tie!')
            self.tieText.setSize(36)
            self.tieText.draw(self.buttonWindow.window)

    def score(self,words1,words2):
        '''Used to score players given everyone's words'''
        # Compares the lists and gets unique values
        r1 = []
        r2 = []
        # Gets unique words that were generated by player 1 (the computer)
        for word in words1:
            if word not in words2:
                r1.append(word)
        # Gets unique words inputed by player 2 (the human player)
        for word in words2:
            if word not in words1:
                r2.append(word)        
        # Returns the score for each player and a list of unique words for each player
        return self.scoreWords(r1),self.scoreWords(r2), r1, r2        

    def scoreWords(self,words):
        '''Generates the total score for the player based on the number of unique words they have'''
        score = 0
        # Adds the score of each individual word score to generate the total score
        for word in words:
            score += self.scoreWord(word)
        return score

    def scoreWord(self,word):
        '''Generates the score of the word based on the number of letters in the word'''
        # Words with 3 letters are worth 1 point, words with 4 letters are worth 2 points, etc.
        length = len(word)-2
        #Qu counts as 2 letters
        if 'qu' in word:
                return length+1
        return length


class Player:
    '''Generates the different players of the game'''
    # Player class is inherited by human player and computer player
    def __init__(self, endTime):
        self.words = []
        self.dict = self.loadDictionary()
        self.endTime = endTime
    def updateBoard(self, board):
        self.board = board
    def getWords(self):
        '''An accessor to get a players words'''
        return self.words

    def addWord(self,word, dict=False):
        '''Adds words'''
        # If the word is playable, adds the words
        if self.validateWord(word, dict):
            self.words.append(word)
            return True
        return False

    def validateWord(self, word, dict=False):
        '''Makes sure a word is playable'''
        # dict is a variable that's true if the word is generated by the computer
        # in which case we don't need to check if it's in the dictionary (time saving)
        # we call this method first to do some initial validation
        # Ensures the word is more than 3 letters
        if len(word)<3:
            return False
        word = word.lower()
        char = word[0]
        # If the word is valid and has not already been played
        if dict!=False or (self.isWord(word) and word not in self.words):
            for row in range(4):
                for column in range(4):
                    # set the current letter
                    letter = self.board[row][column].lower()
                    if letter == char:
                        # call another function to do the rest
                        if self.validateWordRemaining(word[1:], row, column, [[row,column]]):
                                return True
        return False

    # Loads a dictionary
    # By David Liben Nowell
    def loadDictionary(self):
        words=[]
        dictfile = open("twl98.txt")
        for line in dictfile:
            word = line.strip()
            words.append(word)
        dictfile.close()
        return words

    def isWord(self,word):
        '''Checks if a word is in the dictionary'''
        # We could just go straight to binaryDictSearch but this function name makes the code much more readable    
        return self.binaryDictSearch(word)

    def binaryDictSearch(self, word):
        # A simple binary search algorithm to speed up looking through the dictionary
        left = 0
        word = word.upper()
        right = len(self.dict) - 1
        while left <= right:
            mid = (left+right)/ 2
            if word == self.dict[mid]:
                # found the word
                return True
            elif word < self.dict[mid]:
                # the max value is mid-1
                right = mid-1
            elif word > self.dict[mid]:
                # the min value is mid+1
                left = mid+1
        return False

    def validateWordRemaining(self, word, row, column, used=[]):
        '''Determines playable boggle words'''
        # Recursive formula
        # First we make sure that we're not at the edge of the board
        #   if we are then we don't look off the board
        char = word[0]
        xRange = [row-1,row,row+1]
        yRange = [column-1,column,column+1]
        # Makes sure the letters in the word are touching on the game board
        if row == 0:
            xRange = [row, row+1]
        elif row == 3:
            xRange = [row-1, row]
        if column == 0:
            yRange = [column, column+1]
        elif column == 3:
            yRange = [column-1, column]
        # We need to loop through our limited range now and see if the next letter is found in it
        for boardRow in xRange:
            for boardColumn in yRange:
                # if the characters match up
                if self.board[boardRow][boardColumn].lower() == char and [boardRow,boardColumn] not in used:
                    # add the new coordinates to the used variable so we don't go back on ourselves
                    used.append([boardRow,boardColumn])
                    if len(word)==1:
                        return True
                    #recursive!
                    if self.validateWordRemaining(word[1:],boardRow,boardColumn,used):
                        return True
        return False

    def listWords(self):
        '''Lists the words generated by the player'''
        # Creates an empty string
        str=''
        # Adds the words in a new line
        for word in self.getWords():
            str+="\n"+word
        # Returns the list of words
        return str

class ComputerPlayer(Player):
    def createWords(self):
        '''Generates playable words for Player 1 (the computer)'''
        # The computer player accesses the file of the 1000 most common words in english
        dictfile = open("common.txt")
        # Finds all the words greater than three letters from the 1000 most common words that can be played on the boggle board 
        for line in dictfile:
            word = line.strip()
            if len(word)>=3:
                self.addWord(word, True)
        dictfile.close()

class HumanPlayer(Player):
    def createWord(self,word):
        '''Allows Player 2 (the user) to play words'''
        # If time is up, ends the game
        if time.time()>self.endTime:
            return 'END GAME' #sentinel variable
        # Else, adds the word to their played words
        return self.addWord(word)


if __name__ == "__main__":
        main()
