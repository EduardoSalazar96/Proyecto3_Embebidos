from tkinter import *
import subprocess
import threading
import os

deteccion_comando = 'python3 SocialDistancingDetector.py'

#Configuracion de ventana
window = Tk()
window.title("Proyecto")
window.geometry('800x700') #Tamaño de ventana (x, y)
window.resizable(0,0)
window.configure(bg='white')

#Imagen en ventana
path_imagen = 'distancia.png'
img = PhotoImage(file = path_imagen)

#Etiqueta de ventana
lbl = Label(window, text="Sistema de detección de cumplimiento del distanciamiento social", font=("Arial Bold", 18), bg='white') #etiqueta
lbl.pack() #posicion de etiqueta

imagen1 = Label(window, image=img, bg='white')
imagen1.pack(padx= 150, pady= 150)

#Botones
#Definir funciones back.end
global abrir_camara
abrir_camara = '1'

#Funcion boton 1
def iniciar_deteccion():
	print("Iniciar detección")
	deteccion = subprocess.Popen(deteccion_comando.split()) 

deteccion = None

#Funcion boton 2
#Este boton no esta configurado
def enviar_alerta():
	global deteccion
	print("Enviar alerta")
	if deteccion is not None: 
		deteccion.kill()
	if abrir_camara == '0':
		os.kill(abrir_camara)
	

#Funcion boton 3
def ver_registro():
	file = os.path.isfile('register.txt')
	if file:
		print("Ver registro")
		archivo = "gedit"
		subprocess.Popen([archivo,'register.txt'])
	
	else:
		window2 = Tk()
		window2.title("Registro")
		window2.geometry('200x200')
		no_registro = Label(window2, text="No existe el archivo", font=("Arial Bold", 12), bg='white') #etiqueta
		no_registro.place(relx = 0.5, rely = 0.5, anchor = 'center') #posicion de Etiqueta
		boton_no_registro = Button(window2, text="Salir", font=20, padx=10, pady=15, bg="white", fg="black", command= lambda: window2.destroy())
		boton_no_registro.place(relx = 0.5, rely = 0.75, anchor = 'center')
		window2.mainloop()

#Funcion boton 4
def salir():
	if deteccion is not None:
		deteccion.kill()
	exit()

window.protocol("WM_DELETE_WINDOW", salir)

#Definir botones
#Botón 1
btn1 = Button(window, text="Iniciar detección", font=20, padx=10, pady=15, bg="white", fg="black", command=iniciar_deteccion)
btn1.place(x=150, y=130)
btn1.config(state=NORMAL)

#Botón 2
btn2 = Button(window, text="Enviar alerta", font=20, padx=10, pady=15, bg="white", fg="black", command=enviar_alerta)
btn2.place(x=520, y=130)

#Botón 3
btn4 = Button(window, text="Ver registro", font=20, padx=10, pady=15, bg="white", fg="black", command= lambda : threading.Thread(target = ver_registro).start())
btn4.place(x=150, y=550)

#Botón 4
btn5 = Button(window, text="Salir", font=20, padx=10, pady=15, bg="white", fg="black", command= salir)
btn5.place(x=590, y=550)

window.mainloop()
