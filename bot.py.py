from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Я твій бот!")

app = ApplicationBuilder().token("8452226570:AAHjrpEYZrmz7EO8aZLdqZonKTFzH7R1J9Y").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
