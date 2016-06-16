from tkinter import *
tk=Tk()
canvas=Canvas(tk,width=400,height=400)
canvas.pack()
canvas.create_poligon(10,10,10,60,50,35)

def mover(event):
	canvas.move(1,5,0)
canvas.bind_all('<KeyPress-Return>',mover)
tk.mainloop()
