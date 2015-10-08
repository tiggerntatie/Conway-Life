"""
conway.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, Sprite, CircleAsset, RectangleAsset, Color

red = Color(0xff0000, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0, 1.0)
noline = LineStyle(0, black)
CELLDIAMETER = 10
CELLSWIDE = 100
CELLSHIGH = 50

class Cell(Sprite):
    """
    Cell that is either new or old.
    Pass True for new if it shall be a new color.
    """
    bluecircle = CircleAsset(4, noline, blue)
    redcircle = CircleAsset(4, noline, blue)

    def __init__(self, new, pos):
        asset = Cell.bluecircle
        if new:
            asset = Cell.redcircle
        super.__init__(asset, pos)
        self.address = (None, None)
        self.visible = False
        
    def setAddress(self, x, y):
        self.address = (x, y)
        
class ConwayGame(App):
    """
    App for implementing Conway's Game of Life
    """
    def __init__(self):
        w = CELLDIAMETER*CELLSWIDE
        h = CELLDIAMETER*CELLSHIGH
        super().__init__(w, h)
        bgasset = RectangleAsset(w, h, noline, black)
        Sprite(bgasset, (0,0))
    
    def step(self):
        pass

App = ConwayGame()
App.run()