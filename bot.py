from telegram import (
    Update,
    ReplyKeyboardMarkup
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = "8896501044:AAFsluRRZSMIdoGuzLCHn5ty_mmjponR55w"

# Кнопки меню
keyboard = [
    ["🔗 ССЫЛКИ", "💸 ПОКУПКА АДМИНИСТРАТОРА"]
]

reply_markup = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True
)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
👋 Привет!

Это официальный бот проекта STAR RUSSIA ⭐

Этот бот поможет тебе узнать:
• 🔗 Все ссылки проекта
• 💸 Цены на администратора
• 📜 Информацию о сервере
• 🛠 Команды и помощь
• 🎁 Новости и акции

Выбирай нужный раздел в меню ниже 👇
"""

    await update.message.reply_text(
        text,
        reply_markup=reply_markup
    )

# Обработка кнопок
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = update.message.text

    # Ссылки
    if message == "🔗 ССЫЛКИ":

        text = """
🔗 Ссылки проекта STAR RUSSIA

🌐 Форум — http://starrussia-forumm.sampproject.ru
📢 Официальный канал — https://t.me/crmp_star
💬 Чат проекта — https://t.me/Chat_StarCrmp
"""

        await update.message.reply_text(text)

    # Покупка администратора
    elif message == "💸 ПОКУПКА АДМИНИСТРАТОРА":

        text = """
💸 Покупка администратора

Здаров! Вот цены 👇

Покупка прав администрации (Навсегда)
только за Telegram звезды ⭐️

Пока действуют скидки 👍

👑 Основатель — 225 ⭐️
👑 Зам. Основателя — 200 ⭐️
🛡 Спец. Администратор — 185 ⭐️
🛡 Зам. Спец. Админа — 170 ⭐️
⭐ Команда проекта — 165 ⭐️
🔰 Главный администратор — 150 ⭐️
🔰 Зам. Гл. администратора — 125 ⭐️
💻 Тех. Специалист — 100 ⭐️
📋 Куратор администрации — 80 ⭐️
🛠 Ст. администратор — 50 ⭐️
🛠 Администратор — 25 ⭐️

🆓 Ст. модератор — Бесплатно
🆓 Модератор — Бесплатно
🆓 Мл. модератор — Бесплатно

💬 Покупка:
@uzazeb
"""

        await update.message.reply_text(text)

# Запуск бота
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, buttons))

print("Бот запущен!")

app.run_polling()
