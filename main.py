import os
from flask import Flask
from threading import Thread
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")

# --- TOMAR SOB LINK EK JAYGAY ---
BOT_LINK = "https://t.me/Asifstore786954_bot"
FEEDBACK_LINK = "https://t.me/Suvosk786951"
UPDATE_PANEL_LINK = "https://t.me/Asifstore786952"
HOWTOUSE_LINK = "https://t.me/Asifstore786953"

# --- 24 GHONTA ONLINE ---
app_flask = Flask('')
@app_flask.route('/')
def home(): return "ASIF STORE BOT 24/7 LIVE"
def run_flask(): app_flask.run(host='0.0.0.0', port=8080)
def keep_alive():
    t = Thread(target=run_flask)
    t.start()

def get_caption():
    return """Aslamualaikum Welcome to ASIF STORE 👑

💰 Your Balance: ₹0.00
💳 Trusted Store Since 2023
🔒 2nd ID Always 100% Safe ✅
⚠️ Never Use On Main ID!"""

async def show_language_menu(msg_obj):
    kb = [[InlineKeyboardButton("English 🇬🇧", callback_data="lang_en")],[InlineKeyboardButton("বাংলা 🇧🇩", callback_data="lang_bn")],[InlineKeyboardButton("हिन्दी 🇮🇳", callback_data="lang_hi")]]
    await msg_obj.reply_text("🌐 Please select your language:", reply_markup=InlineKeyboardMarkup(kb))

async def show_main_menu(msg_obj):
    caption = get_caption()
    kb = [
  
        [InlineKeyboardButton ("🛒 Store and Products", url=UPDATE_PANEL_LINK)],
        [InlineKeyboardButton("📖 How To Use Panel", url=HOWTOUSE_LINK)],
        [InlineKeyboardButton("⭐ Feedback", url=FEEDBACK_LINK)],
        [InlineKeyboardButton("🌐 Language", callback_data="change_lang")],
    ]
    try:
        await msg_obj.reply_photo(photo=open("photo.jpg", "rb"), caption=caption, reply_markup=InlineKeyboardMarkup(kb))
    except:
        await msg_obj.reply_text(caption, reply_markup=InlineKeyboardMarkup(kb))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await show_language_menu(update.message)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data.startswith("lang_"):
        await show_main_menu(query.message)
    elif query.data == "change_lang":
        await show_language_menu(query.message)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

keep_alive()
print("Bot Running 24/7")
app.run_polling()
