from tkinter import *
from random import randrange

HEIGHT = 500
WIDTH = 500
RESOLUTION = 30

class Application(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.set_highway()
		self.grid()

	def set_highway(self):
		side_len = HEIGHT // RESOLUTION

		self.field = Canvas(self, height=HEIGHT, width=WIDTH)

		for column in range(RESOLUTION):
			for row in range(RESOLUTION):
				self.field.create_rectangle(side_len * (row + 1) - side_len//2, side_len * (column + 1) - side_len//2, side_len * (row + 1) + side_len//2, side_len * (column + 1) + side_len//2, fill="GREEN")

		self.field.grid()

root = Tk()
root.geometry("{}x{}".format(HEIGHT, WIDTH))
app = Application(root)
root.mainloop()