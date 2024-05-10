import telepot
import time
import requests
import random


# Token del bot
TOKEN = 'Tu_token'
bot = telepot.Bot(TOKEN)
# Función que se encarga de manejar los mensajes que recibe el bot
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if content_type == 'text':
        if msg['text'].upper() == '/START':
            bot.sendMessage(chat_id, '¡Hola {} {}! Soy un bot que te ayudará a realizar tu tarea de programación. ¿En qué puedo ayudarte? Usa el comando /help para ver los demas comandos'.format(msg['from']['first_name'], msg['from']['last_name'] if 'last_name' in msg['from'] else ''))
        elif msg['text'].upper() == '/HELP':
            bot.sendMessage(chat_id, 'Comandos disponibles:\n\n/start - Inicializa el bot\n/help - Muestra los comandos disponibles\n/fake - Muestra información falsa generada de manera aleatoria\n/logo - Muestra el logo del bot\n\n¡Espero que te sea de ayuda!')
        elif msg['text'] == '/fake':
            bot.sendMessage(chat_id, 'Generando información falsa, espera un momento...')
            peticion = requests.get('https://randomuser.me/api/')
            datos = peticion.json()['results']
            bot.sendMessage(chat_id, 'Nombre: {} {}\nEmail: {}\nTelefono: {}'.format(datos[0]['name']['first'],
            datos[0]['name']['last'],
            datos[0]['email'],
            datos[0]['phone']))
        elif msg['text'].upper() == '/LOGO':
            bot.sendPhoto(chat_id, open('logo.jfif', 'rb'))

# Inicializa el bot
bot.message_loop(handle)

while True:
    time.sleep(5)