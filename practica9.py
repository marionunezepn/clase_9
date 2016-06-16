from Tkinter import *
tk=Tk()
canvas=Canvas(tk,width=800,height=800)
canvas.pack()

my_image=PhotoImage(file="ball.gif")
canvas.create_image(0,0,anchor=NW,Image=my_image)
tk.mainloop()
