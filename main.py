from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import google.generativeai as genai



GEMINI_API_KEY = "AQ.Ab8RN6JNFO-StIv755tJ6qNry4L3E7OSxPh5GkcA9sb7LOYmxQ"
BOT_TOKEN = "Your TOKEN"

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

users = {}

def handle_message(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    text = update.message.text
    if user_id not in users:
        users[user_id] = []
    users[user_id].append(f"Foydalanuvchi:{text}")
    prompt = "\n".join(users[user_id])
    response = model.generate_content(prompt)
    answer = response.text
    users[user_id].append(f"B: {answer}")
    update.message.reply_text(answer[:4049])

updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
print("Bot started")
updater.start_polling()
updater.idle()

