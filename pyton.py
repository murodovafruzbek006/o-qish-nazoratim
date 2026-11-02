from datetime import datetime
from zoneinfo import ZoneInfo

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

import os 

TOKEN = os.environ.get("BOT_TOKEN")

KUNLAR = {
    0: ("dushanba", "Nazariya"),
    1: ("seshanba", "Nazariya"),
    2: ("chorshanba", "Amaliy"),
    3: ("payshanba", "Amaliy"),
    4: ("juma", "Amaliy"),   
    5: ("shanba", "Takrorlash"),
    6: ("yakshanba", "Takrorlash"),
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
   
    bugun = datetime.now(ZoneInfo("Asia/Tashkent")).weekday()
    kun_nomi, dars_turi = KUNLAR[bugun]

    if dars_turi == "dam olish":
        matn = f"Bugun {kun_nomi}, dam olish kuni. Yaxshi dam oling! 😊"
    else:
        matn = f"Bugun {kun_nomi}, {dars_turi} kuni. O'qishingizga omad tilayman! 📚"

    await update.message.reply_text(matn)


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot ishga tushdi...")
    app.run_polling()


if __name__ == "__main__":
    main()