from config import bot
from time import sleep
import re 




@bot.message_handler(func=lambda message: True)
def on_fallback(message):
	bot.send_chat_action(message.chat.id, 'typing')
	sleep(1)

	bot.reply_to(
		message, 
		"\U0001F63F Ups, no entendí lo que me dijiste.")

if __name__ == '__main__':
	bot.polling(timeout=20)