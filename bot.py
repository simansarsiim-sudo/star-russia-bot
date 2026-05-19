from telegram import (
    Update,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    LabeledPrice
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    PreCheckoutQueryHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters
)

TOKEN = "8896501044:AAFsluRRZSMIdoGuzLCHn5ty_mmjponR55w"

# Главное меню
keyboard = [
    ["🔗 ССЫЛКИ", "💸 ПОКУПКА АДМИНИСТРАТОРА"],
    ["📢 НОВОСТИ", "🛠 ПОМОЩЬ"]
]

reply_markup = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True
)

# /start
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

Выбирай нужный раздел 👇
"""

    await update.message.reply_text(
        text,
        reply_markup=reply_markup
    )

# Кнопки
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = update.message.text

    # Ссылки
    if message == "🔗 ССЫЛКИ":

        text = """
🔗 Ссылки проекта STAR RUSSIA

🌐 Форум:
https://yourforum.com

📢 Канал:
https://t.me/yourchannel

💬 Чат:
https://t.me/yourchat
"""

        await update.message.reply_text(text)

    # Новости
    elif message == "📢 НОВОСТИ":

        await update.message.reply_text(
            "🎁 Пока новостей нет 😎"
        )

    # Помощь
    elif message == "🛠 ПОМОЩЬ":

        await update.message.reply_text(
            "💬 По всем вопросам: @uzazeb"
        )

    # Покупка
elif message == "💸 ПОКУПКА АДМИНИСТРАТОРА":

    reply_markup = InlineKeyboardMarkup([
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
        [InlineKeyboardButton("🛠 Администратор — 25⭐", callback_data="admin")]
    ])

    await update.message.reply_text(
        "💸 Покупка администрации\n\nВыберите привилегию 👇",
        reply_markup=reply_markup
    )

# Нажатия на кнопки
async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    # Администратор
    if query.data == "buy_admin":

        prices = [LabeledPrice("Администратор", 25)]

        await context.bot.send_invoice(
            chat_id=query.message.chat_id,
            title="Покупка Администратора",
            description="Права администратора навсегда",
            payload="admin_buy",
            provider_token="",
            currency="XTR",
            prices=prices
        )

    # Ст админ
    elif query.data == "buy_sadmin":

        prices = [LabeledPrice("Ст. Администратор", 50)]

        await context.bot.send_invoice(
            chat_id=query.message.chat_id,
            title="Покупка Ст. Администратора",
            description="Права Ст. Администратора навсегда",
            payload="sadmin_buy",
            provider_token="",
            currency="XTR",
            prices=prices
        )

    # Основатель
    elif query.data == "buy_owner":

        prices = [LabeledPrice("Основатель", 225)]

        await context.bot.send_invoice(
            chat_id=query.message.chat_id,
            title="Покупка Основателя",
            description="Права Основателя навсегда",
            payload="owner_buy",
            provider_token="",
            currency="XTR",
            prices=prices
        )

# Проверка оплаты
async def precheckout(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.pre_checkout_query
    await query.answer(ok=True)

# Успешная оплата
async def successful_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "✅ Оплата прошла успешно!\n\n"
        "Ожидайте выдачу прав 👑"
    )

    # Уведомление владельцу
    ADMIN_ID = 8416014400

    await context.bot.send_message(
        ADMIN_ID,
        f"💸 Новая покупка!\n\n"
        f"👤 @{update.effective_user.username}\n"
        f"💰 Купил привилегию"
    )

# Запуск
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, buttons))
app.add_handler(CallbackQueryHandler(callback))
app.add_handler(PreCheckoutQueryHandler(precheckout))
app.add_handler(
    MessageHandler(
        filters.SUCCESSFUL_PAYMENT,
        successful_payment
    )
)

print("STAR RUSSIA BOT STARTED")

app.run_polling(drop_pending_updates=True)
