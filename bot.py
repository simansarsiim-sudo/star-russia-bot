from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    LabeledPrice
)

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    PreCheckoutQueryHandler,
    ContextTypes,
    filters
)

TOKEN = "8896501044:AAFsluRRZSMIdoGuzLCHn5ty_mmjponR55w"
OWNER_ID = 8416014400

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

    text = """
👋 Привет!

Это официальный бот проекта STAR RUSSIA ⭐

Этот бот поможет тебе узнать:
• 🔗 Все ссылки проекта
• 💸 Цены на администратора
• 📜 Информацию о сервере
• 🛠 Команды и помощь
• 🎁 Новости и акции

Выбирай нужный раздел 👇
"""

    await update.message.reply_text(
        text,
        reply_markup=reply_markup
    )

# СООБЩЕНИЯ
async def messages(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = update.message.text

    # ПОКУПКА
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
            [InlineKeyboardButton("🆕 Мл. модератор — 3⭐", callback_data="ml_moder")]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            "💸 Покупка администрации\n\nВыберите привилегию 👇",
            reply_markup=reply_markup
        )

    # ССЫЛКИ
    elif message == "🔗 ССЫЛКИ":

        await update.message.reply_text(
            "🔗 Ссылки проекта:\n\n"
            "🌐 Форум: https://yourforum.com\n"
            "📢 Канал: https://t.me/yourchannel\n"
            "💬 Чат: https://t.me/yourchat"
        )

    # НОВОСТИ
    elif message == "📢 НОВОСТИ":

        await update.message.reply_text(
            "📢 Пока новостей нет 😎"
        )

    # ПОМОЩЬ
    elif message == "🛠 ПОМОЩЬ":

        await update.message.reply_text(
            "🛠 По вопросам: @uzazeb"
        )

# КНОПКИ ПОКУПКИ
async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    prices = {
        "founder": ("👑 Основатель", 225),
        "zam_founder": ("👑 Зам. Основателя", 200),
        "spec_admin": ("🛡 Спец. Администратор", 185),
        "zam_spec": ("🛡 Зам. Спец. Админа", 170),
        "team": ("⭐ Команда проекта", 165),
        "gl_admin": ("🔰 Главный администратор", 150),
        "zam_gl": ("🔰 Зам. Гл. администратора", 125),
        "tech": ("💻 Тех. Специалист", 100),
        "curator": ("📋 Куратор администрации", 80),
        "st_admin": ("🛠 Ст. администратор", 50),
        "admin": ("🛠 Администратор", 25),
        "st_moder": ("🆓 Ст. модератор", 10),
        "moder": ("🆓 Модератор", 5),"ml_moder": ("🆕 Мл. модератор", 3)
    }

    title, stars = prices[query.data]

    await context.bot.send_invoice(
        chat_id=query.message.chat_id,
        title=title,
        description=f"Покупка привилегии {title}",
        payload=query.data,
        provider_token="",
        currency="XTR",
        prices=[LabeledPrice(title, stars)]
    )

# ПРОВЕРКА ОПЛАТЫ
async def pre_checkout_query(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.pre_checkout_query
    await query.answer(ok=True)

# УСПЕШНАЯ ОПЛАТА
async def successful_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user
    payload = update.message.successful_payment.invoice_payload

    names = {
        "founder": "👑 Основатель",
        "zam_founder": "👑 Зам. Основателя",
        "spec_admin": "🛡 Спец. Администратор",
        "zam_spec": "🛡 Зам. Спец. Админа",
        "team": "⭐ Команда проекта",
        "gl_admin": "🔰 Главный администратор",
        "zam_gl": "🔰 Зам. Гл. администратора",
        "tech": "💻 Тех. Специалист",
        "curator": "📋 Куратор администрации",
        "st_admin": "🛠 Ст. администратор",
        "admin": "🛠 Администратор",
        "st_moder": "🆓 Ст. модератор",
        "moder": "🆓 Модератор",
        "ml_moder": "🆕 Мл. модератор"
    }

    privilege = names.get(payload, payload)

    # СООБЩЕНИЕ ВЛАДЕЛЬЦУ
    await context.bot.send_message(
        chat_id=OWNER_ID,
        text=(
            f"💸 Новая покупка!\n\n"
            f"👤 Ник: @{user.username}\n"
            f"🆔 ID: {user.id}\n"
            f"🎖 Привилегия: {privilege}"
        )
    )

    # СООБЩЕНИЕ ПОКУПАТЕЛЮ
    await update.message.reply_text(
        "✅ Оплата прошла успешно!\n\n"
        "Ожидайте выдачу привилегии 👑"
    )

# ЗАПУСК
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, messages))
app.add_handler(CallbackQueryHandler(callback))
app.add_handler(PreCheckoutQueryHandler(pre_checkout_query))
app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment))

print("STAR RUSSIA BOT STARTED")

app.run_polling(drop_pending_updates=True)
