import logging
from aiogram import Bot, Dispatcher, executor, types
from db import BotDB

BotDB = BotDB('users.db')



# Объект бота
bot = Bot(token="5267221246:AAHsIYJt5-e3INE-tijJePjTkw-JnORLDhA")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# Стартовая команда
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    if(not BotDB.user_exists(message.from_user.id)):
        BotDB.add_user(message.from_user.id)

    await message.reply(" Привет!\n Напиши '/history', чтобы посмотреть свои заметки.\n\n '/task + текст заметки', чтобы добавить новую !\n\n '/delete' + текст заметки, чтобы удалить заметку ")

# Добавить заметку
@dp.message_handler(commands=['task'])
async def process_start_command(message: types.Message):
    cmd_variants = (('/task', '/t', '!task', '!t'), ('/new', '!new'))
    task = message.text 
    for i in cmd_variants:
        for j in i:
            task = task.replace(j, '').strip()
    if task:
        BotDB.add_record(message.from_user.id, task)
        await message.reply("✅ Запись успешно внесена!")
    else:
        await message.reply("Не введена заметка!")
    
    
#Посмотреть заметки
@dp.message_handler(commands = ("history", "h"), commands_prefix = "/!")
async def start(message: types.Message):
    records = BotDB.get_records(message.from_user.id)

    if(len(records)):
        answer = 'Твои заметки: \n\n'
        for i in range(len(records)):
            fix = str(i+1) + ') ' + records[i][2] + '\n'
            answer = answer + fix
        await message.reply(answer)              
    else:
        await message.reply("Записей не обнаружено!")

    

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)