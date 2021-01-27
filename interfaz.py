from tkinter import *
import subprocess
import threading
import os
#import paramiko

#from aplicacion_mensajeria import saludo
from aplicacion_mensajeria import archivo

deteccion_comando ='python3 ejecucion.py'

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
#Funcion boton 1
def iniciar_deteccion():
	
	print("Iniciar detección")
	cmd = "sshpass -p " + "Bendicion7"  + " ssh " + "Bendicion"+"@"+"192.168.18.18"
	print(cmd)
	os.system(cmd)
	
deteccion = None

#Funcion boton 2
def enviar_alerta():
	print("Enviar alerta")
	saludo()
	

#Funcion boton 3
def ver_registro():
	extraer_archivo = "sshpass -p " + "Bendicion7" + " scp " + "Bendicion"+"@"+"192.168.18.18"+":register.txt register.txt"
	os.system(extraer_archivo)
	file = os.path.isfile('register.txt')
	
	if file:
		print("Ver registro")
		archivo1 = "gedit"
		subprocess.Popen([archivo1,'register.txt'])
		archivo()
	
	else:
		window2 = Tk()
		window2.title("Registro")
		window2.geometry('200x200')
		no_registro = Label(window2, text="No existe el archivo", font=("Arial Bold", 12), bg='white') #etiqueta
		no_registro.place(relx = 0.5, rely = 0.5, anchor = 'center') #posicion de etiqueta
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
btn1 = Button(window, text="Iniciar detección", font=20, padx=10, pady=15, bg="white", fg="black", command=  lambda : threading.Thread(target =  iniciar_deteccion).start())
btn1.place(x=150, y=130)
btn1.config(state=NORMAL)

#Botón 2
btn2 = Button(window, text="Enviar alerta", font=20, padx=10, pady=15, bg="white", fg="black", command=enviar_alerta)
btn2.place(x=520, y=130)

#Botón 3
btn3 = Button(window, text="Ver registro", font=20, padx=10, pady=15, bg="white", fg="black", command= lambda : threading.Thread(target = ver_registro()).start())
btn3.place(x=150, y=550)

#Botón 4
btn4 = Button(window, text="Salir", font=20, padx=10, pady=15, bg="white", fg="black", command=salir)
btn4.place(x=590, y=550)

window.mainloop()
