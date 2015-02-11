# David Liben-Nowell
# CS 111, Carleton College
# sample.py
#
# A sample chunk of code to support some interactive buttons for projects.

from graphics import *

class Button:
    def __init__(self, x, y, width, height, letter):
        self.xRange = [x, x + width]
        self.yRange = [y, y + height]
        self.rectangle = Rectangle(Point(x, y), Point(x + width, y + height))
        self.clicks = 0
        self.letter=letter
        self.rectangle.setFill("white")
    
    def draw(self, window):
        self.rectangle.draw(window.window)
        startX=self.xRange[0]+(self.xRange[1]-self.xRange[0])/2
        startY=self.yRange[0]+(self.yRange[1]-self.yRange[0])/2
        text = Text(Point(startX, startY), self.letter)
        text.setSize(24)
        text.draw(window.window)

    def pointInside(self, point):
        return self.xRange[0] <= point.getX() <= self.xRange[1] \
            and self.yRange[0] <= point.getY() <= self.yRange[1] \


    def onRightClick(self):
        self.rectangle.setFill("red")

    
    
class ButtonWindow:
    def __init__(self, title, width, height, squares):
        self.window = GraphWin(title, width, height)
        self.window.setMouseRightHandler(self.handleRightClick)
        self.lastupdate = time.time()
        self.squares = squares

    def update(self):
        self.window.update()

    def closed(self):
        return not self.window.winfo_exists()        

    def handleClick(self, point):
        for square in self.squares:
            if square.pointInside(point):
                square.onClick()

    def handleRightClick(self, point):
        for square in self.squares:
            if square.pointInside(point):
                square.onRightClick()

def main():
    squares = []
    for row in range(4):
        for col in range(4):
            squares.append(Button(row * 200, col * 200, 200, 200))
            
    window = ButtonWindow("Game board", 800, 800, squares)
    for square in squares:
        square.draw(window)
        
    while not window.closed():
        window.update() 

if __name__ == "__main__":
    main()
