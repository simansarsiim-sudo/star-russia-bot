from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters
)

TOKEN = "ТВОЙ_ТОКЕН_БОТА"

# СТАРТ
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [KeyboardButton("🔗 ССЫЛКИ"), KeyboardButton("💸 ПОКУПКА АДМИНИСТРАТОРА")],
        [KeyboardButton("📢 НОВОСТИ"), KeyboardButton("🛠 ПОМОЩЬ")]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "👋 Добро пожаловать в STAR RUSSIA",
        reply_markup=reply_markup
    )


# СООБЩЕНИЯ
async def messages(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = update.message.text

    # ПОКУПКА АДМИНКИ
    if message == "💸 ПОКУПКА АДМИНИСТРАТОРА":

        keyboard = [
            [InlineKeyboardButton("👑 Основатель — 225⭐", callback_data="founder")],
            [InlineKeyboardButton("👑 Зам. Основателя — 200⭐", callback_data="zam_founder")],
            [InlineKeyboardButton("🛡 Спец. Администратор — 185⭐", callback_data="spec_admin")],
            [InlineKeyboardButton("🛡 Зам. Спец. Админа — 170⭐", callback_data="zam_spec")],
            [InlineKeyboardButton("⭐ Команда проекта — 165⭐", callback_data="team")],
            [InlineKeyboardButton("🔰 Главный администратор — 150⭐", callback_data="gl_admin")],
            [InlineKeyboardButton("🔰 Зам. Гл. администратора — 125⭐", callback_data="zam_gl")],
            [InlineKeyboardButton("💻 Тех. Специалист — 100⭐", callback_data="tech")],
            [InlineKeyboardButton("📋 Куратор администрации — 80⭐", callback_data="curator")],
            [InlineKeyboardButton("🛠 Ст. администратор — 50⭐", callback_data="st_admin")],
            [InlineKeyboardButton("🛠 Администратор — 25⭐", callback_data="admin")],
            [InlineKeyboardButton("🆓 Ст. модератор — 10⭐", callback_data="st_moder")],
            [InlineKeyboardButton("🆓 Модератор — 5⭐", callback_data="moder")],
            [InlineKeyboardButton("🆓 Мл. модератор — 3⭐", callback_data="ml_moder")]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            "💸 Покупка администрации\n\nВыберите привилегию 👇",
            reply_markup=reply_markup
        )

    # ССЫЛКИ
    elif message == "🔗 ССЫЛКИ":
        await update.message.reply_text(
            "🔗 Наши ссылки:\n\nTelegram: @uzazeb"
        )

    # НОВОСТИ
    elif message == "📢 НОВОСТИ":
        await update.message.reply_text(
            "📢 Пока новостей нет."
        )

    # ПОМОЩЬ
    elif message == "🛠 ПОМОЩЬ":
        await update.message.reply_text(
            "🛠 По вопросам: @uzazeb"
        )


# КНОПКИ
async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    texts = {
        "founder": "👑 Основатель — 225⭐",
        "zam_founder": "👑 Зам. Основателя — 200⭐",
        "spec_admin": "🛡 Спец. Администратор — 185⭐",
        "zam_spec": "🛡 Зам. Спец. Админа — 170⭐",
        "team": "⭐ Команда проекта — 165⭐",
        "gl_admin": "🔰 Главный администратор — 150⭐",
        "zam_gl": "🔰 Зам. Гл. администратора — 125⭐",
        "tech": "💻 Тех. Специалист — 100⭐",
        "curator": "📋 Куратор администрации — 80⭐",
        "st_admin": "🛠 Ст. администратор — 50⭐",
        "admin": "🛠 Администратор — 25⭐",
        "st_moder": "🆓 Ст. модератор — 10⭐",
        "moder": "🆓 Модератор — 5⭐",
        "ml_moder": "🆓 Мл. модератор — 3⭐"
    }

    text = texts.get(query.data, "Неизвестная привилегия")

    await query.message.reply_text(
        f"✅ Вы выбрали:\n\n{text}\n\n💬 Для покупки: @uzazeb"
    )


# ЗАПУСК
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, messages))
app.add_handler(CallbackQueryHandler(callback))

print("Бот запущен!")

app.run_polling()
