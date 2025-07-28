from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

BOT_TOKEN = "7512789340:AAENZSP6nhOy0PBTda1cXKNbxPMOUJ6VII4"

def start(update, context):
    update.message.reply_text("🎵 Salom! Menga qo‘shiq nomini yozing, men sizga YouTube linkini topib beraman.")

def search(update, context):
    query = update.message.text
    youtube_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    update.message.reply_text(f"🔎 Qidiruv natijasi:\n{youtube_url}")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, search))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
