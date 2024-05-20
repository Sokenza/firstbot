from aiogram import Bot, Dispatcher, types, executor
from config import  TELEGRAM_TOKEN

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command= '/start', description= 'Команда для того чтобы запустить бота'),
        types.BotCommand(command='/help', description='Команда для того, чтобы узнать с чем может помочь бот'),
        types.BotCommand(command='/gg', description='Команда для того, чтобы что'),
        types.BotCommand(command='/info', description='Команда для того, чтобы узнать информацию о боте'),
        types.BotCommand(command='/leave', description='Команда для того, чтобы выйти с бота')
    ]

    await bot.set_my_commands(commands)


@dp.message_handler(commands= 'start')
async def start(message: types.message):
    await message.answer('Привет, давай начнем работу')

@dp.message_handler(commands='info')
async def info(message: types.message):
    await message.answer('Информация: Создатель- Shadw Cntry. Дата создания-20.05.2024')

@dp.message_handler(commands='gg')
async def gg(message: types.message):
    await message.answer('Просто да')

@dp.message_handler(commands='leave')
async def leave(message: types.message):
    await message.answer('Прощай')

@dp.message_handler(commands= 'help')
async def help(message: types.message):
    await message.reply('Я готов помочь тебе с ...')

@dp.message_handler()
async def echo(message: types.message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)
