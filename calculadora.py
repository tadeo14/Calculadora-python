import tkinter as tk
from tkinter import messagebox
import sys

def convertir (dato):
		try:
				dato = float(dato)
		except ValueError:
				dato= "error"
				messagebox.showerror(title="Error", message="No es un numero")
		return dato


def sumar ():
		ctres.delete(0,tk.END)  #de esta manera borramos el resultado
		a = cuno.get()
		a = convertir(a)		
		b= cdos.get()
		b= convertir(b)
		if a != "error" and b != "error":
				c = a + b
		else:
			c = "error"
		ctres.insert(0,c)
		
def restar ():
		ctres.delete(0,tk.END)  #de esta manera borramos el resultado
		a = cuno.get()
		a = convertir(a)		
		b= cdos.get()
		b= convertir(b)
		if a != "error" and b != "error":
				c = a - b
		else:
			c = "error"
		ctres.insert(0,c)
		
def mult ():
		ctres.delete(0,tk.END)  #de esta manera borramos el resultado
		a = cuno.get()
		a = convertir(a)		
		b= cdos.get()
		b= convertir(b)
		if a != "error" and b != "error":
				c = a * b
		else:
			c = "error"
		ctres.insert(0,c)
		
def div ():
		ctres.delete(0,tk.END)  #de esta manera borramos el resultado
		a = cuno.get()
		a = convertir(a)		
		b= cdos.get()
		b= convertir(b)
		if a != "error" and b != "error":
				try:
						c = a / b
				except ZeroDivisionError:
						messagebox.showerror(title="Error", message="No se puede dividir por 0")
		else:
			c = "error"
		ctres.insert(0,c)

def salir ():
	#True Si
	#False Si no
	r = messagebox.askokcancel(title="Salir", message="Desea Salir?")
	if r:
		sys.exit()

def informar ():
	messagebox.showinfo(title="Info", message="Calculadora 3.0 creada en python")





#########################################

ventana = tk.Tk()
ventana.config(width=300, height=300)
ventana.title("Calculadora v3")

euno = tk.Label(text="Dato uno:")
euno.place(x=20,y=20)
cuno = tk.Entry()
cuno.place(x=20, y=50)

edos = tk.Label(text="Dato dos:")
edos.place(x=160,y=20)
cdos = tk.Entry()
cdos.place(x=160, y=50)

bsuma = tk.Button(text= "+", command=sumar)
bsuma.place(x=20, y=100)

bresta = tk.Button(text= "-", command = restar)
bresta.place(x=100, y=100)

bmult = tk.Button(text= "x", command = mult)
bmult.place(x=180, y=100)

bdiv = tk.Button(text= "/", command = div)
bdiv.place(x=260, y=100)

etres = tk.Label(text="Resultado:")
etres.place(x=90,y=160)
ctres = tk.Entry()
ctres.place(x=90, y=200)


bsalir= tk.Button(text="Salir", command=salir)
bsalir.place(x=60, y=240, width=100, height=40)

binfo= tk.Button(text="Info", command=informar)
binfo.place(x=160, y=240, width=100, height=40)


ventana.mainloop()