from tkinter import *
from random import *

HEIGHT = 500
WIDTH = 500
RESOLUTION = 30
NBLOCKED = 100

class Aplication(Frame):
    xycor = []
    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.set_highway()
        self.grid()

    def xyout(self):
        print(self.xycor)

    def xyappend(self, x, y):
        self.xycor.append((x, y))

    def set_highway(self):
        side_len = HEIGHT // RESOLUTION

        self.field = Canvas(self, height=HEIGHT, width=WIDTH)

        for column in range(RESOLUTION):
            for row in range(RESOLUTION):
                self.field.create_rectangle(side_len * (row + 1) - side_len//2, side_len * (column + 1) - side_len//2,  side_len * (row + 1) + side_len//2, side_len * (column + 1) + side_len//2, fill="GREEN")

        for i in range(NBLOCKED):
            x = randrange(RESOLUTION) + 1
            y = randrange(RESOLUTION) + 1
            self.xyappend(x, y)
            self.field.create_rectangle(side_len * (x) - side_len // 2, side_len * (y) - side_len // 2,
                                        side_len * (x) + side_len // 2, side_len * (y) + side_len // 2,
                                        fill="YELLOW")
        xstart = randrange(RESOLUTION)+1
        ystart = randrange(RESOLUTION)+1
        self.field.create_rectangle(side_len * (xstart) - side_len // 2, side_len * (ystart) - side_len // 2,
                                    side_len * (xstart) + side_len // 2, side_len * (ystart) + side_len // 2,
                                    fill="RED")
        xfinish = randrange(RESOLUTION)+1
        yfinish = randrange(RESOLUTION)+1
        self.field.create_rectangle(side_len * (xfinish) - side_len // 2, side_len * (yfinish) - side_len // 2,
                                    side_len * (xfinish) + side_len // 2, side_len * (yfinish) + side_len // 2,
                                    fill="WHITE")

        self.field.grid()
        deltax = xstart-xfinish;  deltay = ystart-yfinish


        if deltax>=0:
            if deltay >= 0:
                vect = "SE"
            else:
                vect = "NE"
        else:
            if deltay >= 0:
                vect = "SW"
            else:
                vect = "NW"

        print(vect)


'''
deltax >0, deltay >0 direct = SE
......

'''


root = Tk()
root.geometry("{}x{}".format(HEIGHT,WIDTH))
app = Aplication(root)

root.mainloop()