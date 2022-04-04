@bot.message_handler(content_types=['text']) #Срабатывание на text
def start(message): #Начало
	bot.register_next_step_handler(message, random)#"Перенаправляет" на след.функцию

def random(message):
    if message.text == '0-1':
        bot.send_message(message.chat.id, 'О-1')
    elif message.text == '0-10':
        bot.send_message(message.chat.id, 'О-10')
