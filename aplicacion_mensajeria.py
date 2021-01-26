import telebot
import os
#from pynput import keyboard as kb

bot=telebot.TeleBot("1537448177:AAGonc8AbdFggfMEM8QyDPMqV4VacsMA9LM", parse_mode=None)
global chat

@bot.message_handler(commands=['inicio'])
def send_welcome(message):
	chat=message.chat.id
	bot.reply_to(message, "Saludos")
	archivo=os.path.isfile('register.txt')
	if(archivo):
		bot.send_document(chat, open('register.txt', 'rb') )	
	else:
		bot.reply_to(message, "No hay registro de actividades")
		
@bot.message_handler(commands=['saludo'])
def send_welcome1(message):
	chat=message.chat.id
	bot.reply_to(message, "En espera")
	variable=input("Esperando")
	print("Texto1")
	bot.reply_to(message, "Puede revisar")

@bot.message_handler(commands=['registro'])
def send_welcome2(message):
	chat=message.chat.id
	identificador=str(chat)
	bot.reply_to(message, "En espera")
	#print(chat)
	registro=open("registro.txt", "w")
	registro.write(identificador)
	registro.close()
	print("Registrado")
	bot.reply_to(message, "Puede revisar")	

def saludo():
	#chat=message.chat.id
	#bot.reply_to(message, "En espera")
	print("Saludo")
	registro=open("registro.txt","r")
	identificador=registro.read()
	registro.close()
	#registro=str(registro)
	#identificador=int(registro)
	#bot.reply_to(message, "Puede revisar")
	bot.send_message(identificador, "Saludo")

	
def archivo():
	#chat=message.chat.id
	#bot.reply_to(message, "En espera")
	registro=open("registro.txt","r")
	identificador=registro.read()
	registro.close()
	print("Archivo:")
	#bot.reply_to(message, "Puede revisar")
	bot.send_message(identificador, "Archivo:")
	bot.send_document(identificador, open('register.txt', 'rb') )
	
bot.polling()


#@bot.message_handler(commands=['registro'])
#	
	
#@bot.message_handler(func=lambda m: True)
#def echo_all(message):
#	bot.reply_to(message, message.text)



