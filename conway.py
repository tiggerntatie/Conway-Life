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
        self.livingcells = {}
        # set three living cells
        self.livingcells[(10,10)] = 0
        self.livingcells[(10,11)] = 0
        self.livingcells[(10,12)] = 0
    
    def population(self, addr):
        if addr in self.livingcells:
            return 1
        else:
            return 0
    
    def neighboraddresses(self, addr):
        return [(addr[0]+1, addr[1]+1),
                (addr[0], addr[1]+1),
                (addr[0]-1, addr[1]+1),
                (addr[0]-1, addr[1]),
                (addr[0]+1, addr[1]),
                (addr[0]+1, addr[1]-1),
                (addr[0], addr[1]-1),
                (addr[0]-1, addr[1]-1)]
                
    
    def countneighbors(self, addr):
        count = 0
        for naddr in self.neighboraddresses(addr):
            count += population(naddr)
        return count

    def birthnew(self, nextgen, addr):
        if addr not in self.livingcells:
            if self.countneighbors(addr) == 3:
                nextgen[addr] = 0

    def step(self):
        nextgen = {}
        for addr in self.livingcells:
            n = self.countneighbors(addr)
            if n in (2, 3):
                nextgen[addr] = self.livingcells[addr]+1
            for naddr in self.neighboraddresses(addr):
                self.birthnew(nextgen, naddr)
        for s in self.getSpritesbyClass(Cell):
            s.destroy()
            self.spritelist.remove(s)
        self.livingcells = nextgen
        for c in self.livingcells:
            isnew = self.livingcells[c] == 0
            Cell(isnew, (c.x*CELLDIAMETER, c.y*CELLDIAMETER))
            

App = ConwayGame()
App.run()