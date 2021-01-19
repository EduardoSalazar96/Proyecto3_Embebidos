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

#Funcion 0
def log_in():
	window2 = Tk()
	window2.geometry('300x300')
	usuario = Label(window2, text = "Digite el nombre de usuario", font=("Arial Bold", 12), bg='white')
	usuario.place(relx = 0.5, rely = 0.1, anchor = 'center') #posicion de Etiqueta
	Usuario = Entry(window2)
	Usuario.place(relx = 0.5, rely = 0.2, anchor = 'center')
	ip = Label(window2, text = "Digite la dirección IP", font=("Arial Bold", 12), bg='white')
	ip.place(relx = 0.5, rely = 0.3, anchor = 'center') #posicion de Etiqueta
	IP = Entry(window2)
	IP.place(relx = 0.5, rely = 0.4, anchor = 'center')
	contrasena = Label(window2, text = "Digite la contraseña", font=("Arial Bold", 12), bg='white')
	contrasena.place(relx = 0.5, rely = 0.5, anchor = 'center')
	Contrasena = Entry(window2)
	Contrasena.place(relx = 0.5, rely = 0.6, anchor = 'center')
	def loggearse():
		cmd = "sshpass -p " + Contrasena.get()  + " ssh " + Usuario.get()+"@"+IP.get()
		print(cmd) 
		os.system(cmd)
		window2.destroy()
	boton = Button(window2, text="Log in", font=20, padx=10, pady=15, bg="white", fg="black", command=lambda: loggearse())
	boton.place(relx = 0.5, rely = 0.8, anchor = 'center')

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
	extraer_archivo = 'scp Bendicion@192.168.18:register.txt Registro.txt'
	os.system(extraer_archivo)
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

#Boton 0 
btn0 = Button(window, text="Log in", font=20, padx=10, pady=15, bg="white", fg="black", command=log_in)
btn0.place(x=380, y=130)

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
