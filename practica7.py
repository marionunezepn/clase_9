import turtle
t=turtle.Pen()
l=(int(input("Numero de lados:")))

def mipoligono(size,l):	
	for x in range(1,l):
		t.forward(size)
		t.left(360/l)
	

mipoligono(size,l)
turtle.getscreen()._root.mainloop()