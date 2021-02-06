from config import bot, VERSION
from time import sleep
import config
import re 
import logic
import database.db as db


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)

@bot.message_handler(commands=['start'])
def on_command_start(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, logic.get_welcome_message(bot.get_me()), parse_mode="Markdown")
    bot.send_message(message.chat.id, logic.get_help_message(), parse_mode="Markdown")
    logic.register_account(message.from_user.id)


@bot.message_handler(commands=['help'])
def on_command_help(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, logic.get_help_message(), parse_mode="Markdown")


@bot.message_handler(commands=['about'])
def on_command_about(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message( message.chat.id, logic.get_about_this(config.VERSION), parse_mode="Markdown")


@bot.message_handler(regexp=r"^(obtener saldo|s)$")
def on_get_balance(message):
    bot.send_chat_action(message.chat.id, 'typing')
    balance = logic.get_balance(message.from_user.id)
    text = "\U0000274C Aún no tienes una cuenta asociada, ejecuta /start para arreglarlo."
    if balance != None:
        text = f"Tu saldo actual es ${balance}"
    bot.reply_to(message, text)

@bot.message_handler(regexp=r"^(gane|gané|g) ([+-]?([0-9]*[.])?[0-9]+)$")
def on_earn_money(message):
    bot.send_chat_action(message.chat.id, 'typing')
    parts = re.match(r"^(gane|gané|g) ([+-]?([0-9]*[.])?[0-9]+)$", message.text)
    # print (parts.groups())
    amount = float(parts[2])
    control = logic.earn_money(message.from_user.id, amount)
    bot.reply_to(
        message, 
        f"\U0001F4B0 ¡Dinero ganado!: {amount}" if control == True 
        else "\U0001F4A9 Tuve problemas registrando la transacción, ejecuta/start y vuelve a intentarlo")

@bot.message_handler(regexp=r"^(gane|gané|g) ([+-]?([0-9]*[.])?[0-9]+)$")
def on_earn_money(message):
    pass


@bot.message_handler(regexp=r"^(gaste|gasté|gg) ([+-]?([0-9]*[.])?[0-9]+)$")
def on_spend_money(message):
    pass


@bot.message_handler(regexp=r"^(listar ganancias|lg) en ([0-9]{1,2}) de ([0-9]{4})$")
def on_list_earnings(message):
    pass


@bot.message_handler(regexp=r"^(listar gastos|lgg) en ([0-9]{1,2}) de ([0-9]{4})$")
def on_list_spendings(message):
    pass


@bot.message_handler(regexp=r"^(remover|r) (ganancia|g|gasto|gg) ([0-9]+)$")
def on_remove_record(message):
    pass

@bot.message_handler(func=lambda message: True)
def on_fallback(message):
    pass


if __name__ == '__main__':
    bot.polling(timeout=20)


# @bot.message_handler(regexp=r"^sumar ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$")
# def on_add(message):
# 	bot.send_chat_action(message.chat.id, 'typing')
# 	sleep(1)
# 	parts = re.match(
# 	r"^sumar ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$",
# 	message.text)
# 	# print (parts.groups())
# 	oper1 = float(parts[1])
# 	oper2 = float(parts[3])
# 	result = oper1 + oper2
# 	bot.reply_to(message, f"\U0001F522 Resultado: {result}")

# @bot.message_handler(regexp=r"^dividir ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$")
# def on_divide(message):
# 	bot.send_chat_action(message.chat.id, 'typing')
# 	sleep(1)
# 	parts = re.match(r"^dividir ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$", message.text)
# 	# print (parts.groups())
# 	oper1 = float(parts[1])
# 	oper2 = float(parts[3])
# 	if (oper2 == 0):
# 		bot.reply_to(message, f"\U0001F522 Operacion indeterminada")
# 		return 
		
# 	result = oper1 / oper2
# 	bot.reply_to(message, f"\U0001F522 Resultado: {result}")


# @bot.message_handler(func=lambda message: True)
# def on_fallback(message):
# 	bot.send_chat_action(message.chat.id, 'typing')
# 	sleep(1)

# 	bot.reply_to(
# 		message, 
# 		"\U0001F63F Ups, no entendí lo que me dijiste.")

