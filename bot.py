import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from models import User
from database import SessionLocal
from sqlalchemy.exc import IntegrityError

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    user = User(chat_id=chat.id, username=chat.username)

    session = SessionLocal()
    try:
        session.add(user)
        session.commit()
        await update.message.reply_text("Hey, I am your simple bot!")
    except IntegrityError:
        session.rollback()
        await update.message.reply_text("Hey, you already started a conversation!")
    finally:
        session.close()

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot is running!")
    app.run_polling()

if __name__ == "__main__":
    main()