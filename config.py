import telebot
import logging
import os
from decouple import config

#########################################################

# Versión del bot
VERSION = 0.1

# Obtiene el token desde el archivo de configuración
#TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN') or config('TELEGRAM_TOKEN')
#TELEGRAM_TOKEN = "1612777265:AAF310A-ULxEWyCiZyEuLiik2UoFYI35Sv0"
TELEGRAM_TOKEN = config('TELEGRAM_TOKEN')

#########################################################

# Crea el objeto bot utilizando el token
bot = telebot.TeleBot(TELEGRAM_TOKEN)    

# Determina el nivel de los mensajes que se van a mostrar (debug)
telebot.logger.setLevel(logging.INFO)

#########################################################
