import os 
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

load_dotenv(dotenv_path='D:\py\src\.env')

TOKEN = os.getenv('TELEGRAM_TOKEN')

if TOKEN is None:
    print("Переменная TOKEN не установлена! Проверьте файл .env.")
    exit(1)
else:
    print("TOKEN успешно загружен:")
    
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Вопросы? Не ко мне')
    context.user_data['message_count'] = 0

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    count = context.user_data.get('message_count', 0)
    count += 1
    context.user_data['message_count'] = count

    if count == 1:
        await update.message.reply_text('Привет-привет, так уж и быть. Как жень прошел?')
    elif count == 2:
        await update.message.reply_text('Да, не очень интересно, но тоже неплохо, рад за тебя, ты молодец, у тебя все получится и бла-бла-бла')
    elif count == 3:
        await update.message.reply_text('Что-то еще надо? Неужели тебе так хочется со мной общаться? Иди своей дорогой, путник')
    elif count == 4:
        await update.message.reply_text('Все, хватит спамить, мне пора')
    else:
        await update.message.reply_text('-игнор-')

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    app.run_polling()

if __name__ == '__main__':
    main()