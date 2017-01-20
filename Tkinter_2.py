from tkinter import *

root = Tk()
root.title('Our first GUI')

but = Button(root, text = 'This is a button', width=30, height=5, bg ='yellow', fg='blue')
lab = Label(root, text="Это метка! \n Из двух строк.", font="Arial 18")
ent = Entry(root, width=25, bd=3, font="Arial 20")
tex = Text(root,width=40,
font="Verdana 12",
wrap=WORD)

var = IntVar()
var.set(1)
'''
This is a block comment
"var"" variable is linked to Radiobuttons
'''

rad0 = Radiobutton(root, text='First', variable=var, value=0)
rad1 = Radiobutton(root, text='Second', variable=var, value=1)
rad2 = Radiobutton(root, text='Third', variable=var, value=2)

c1 = IntVar()
c2 = IntVar()

che1 = Checkbutton(root, variable=c1, onvalue=1, offvalue=0, text='First flag')
che2 = Checkbutton(root, variable=c2, onvalue=2, offvalue=0, text='Second flag')

r = ['Linux', 'Windows', 'MacOS', 'Android', 'iOS']
lis = Listbox(root, selectmode=MULTIPLE, height=4)

for i in r:
    lis.insert(END, i)



tex.pack()
lab.pack()
but.pack()
ent.pack()
rad0.pack()
rad1.pack()
rad2.pack()
che1.pack()
che2.pack()
lis.pack()



root.mainloop()