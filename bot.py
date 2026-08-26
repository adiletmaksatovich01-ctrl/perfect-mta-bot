import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

# Деректер енгізілді
BOT_TOKEN = "8516274181:AAEqNxunUOnLguFquddRCa2j_X0k9p7N0-Q"
ADMIN_ID = 8235382815

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

# Түймелер (Басты мәзір)
def get_main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("🎮 Серверге кіру"), KeyboardButton("💳 Төлем жасау / Донат"))
    keyboard.add(KeyboardButton("📢 Жаңалықтар"), KeyboardButton("🆘 Көмек / Шағым"))
    return keyboard

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    welcome_text = (
        f"Ассалаумағалейкум, <b>{message.from_user.first_name}</b>!\n\n"
        f"MTA Серверінің ресми ботына кош келдіңіз!\n"
        f"Төмендегі мәзірден керекті бөлімді таңдаңыз:"
    )
    await message.answer(welcome_text, reply_markup=get_main_keyboard())

@dp.message_handler(lambda message: message.text == "🎮 Серверге кіру")
async def server_info(message: types.Message):
    text = (
        "<b>🎮 Серверге қосылу деректері:</b>\n\n"
        "<b>IP:</b> connect.yourserver.mta:22003\n"
        "<b>FPS Limit:</b> 100\n\n"
        "Жағымды ойын тілейміз!"
    )
    await message.answer(text)

@dp.message_handler(lambda message: message.text == "💳 Төлем жасау / Донат")
async def donate_info(message: types.Message):
    text = (
        "<b>💳 Донат / Төлем жасау:</b>\n\n"
        "Kaspi / Карта арқылы төлем жасаған соң, чек скриншотын осы ботқа жіберіңіз.\n"
        "Администратор тексеріп, бонусты ойынға қосып береді."
    )
    await message.answer(text)

@dp.message_handler(lambda message: message.text == "📢 Жаңалықтар")
async def news_info(message: types.Message):
    await message.answer("📢 Жаңалықтар мен жаңартуларды ресми Телеграм арнамыздан бақылап отырыңыз!")

@dp.message_handler(lambda message: message.text == "🆘 Көмек / Шағым")
async def help_info(message: types.Message):
    await message.answer("🆘 Егер проблема немесе сұрағыңыз болса, осы жерге хабарлама жазып жіберіңіз. Админ сізге жауап береді.")

# Ойыншылар жазған хабарламаны админге бағыттау
@dp.message_handler(content_types=types.ContentTypes.ANY)
async def forward_to_admin(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        await bot.forward_message(chat_id=ADMIN_ID, from_chat_id=message.chat.id, message_id=message.message_id)
        await message.reply("✅ Хабарламаңыз админге жіберілді. Жауап күтіңіз.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
