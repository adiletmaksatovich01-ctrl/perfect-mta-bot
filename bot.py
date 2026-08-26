import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "8516274181:AAEqNxunUOnLguFquddRCa2j_X0k9p7N0-Q"
ADMIN_ID = 8235382815

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

user_state = {}

def get_main_menu():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text="🛒 Товар сатып алу", callback_data="buy_goods"),
        InlineKeyboardButton(text="✍️ Шағым жазу", callback_data="write_claim"),
        InlineKeyboardButton(text="❓ Сервер бойынша сұрақтар", callback_data="server_faq"),
        InlineKeyboardButton(text="📢 Пост салу", callback_data="send_post")
    )
    return keyboard

def get_goods_menu():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text="💎 Вип - 1000 тенге", callback_data="item_vip"),
        InlineKeyboardButton(text="🛡 Простой Админ - 2000 тенге", callback_data="item_admin"),
        InlineKeyboardButton(text="⭐ Зам Админ - 3000 тенге", callback_data="item_zam"),
        InlineKeyboardButton(text="👑 Главный Админ - 6000 тенге", callback_data="item_head_admin"),
        InlineKeyboardButton(text="⚡ Главный Босс - 10000 тенге", callback_data="item_boss"),
        InlineKeyboardButton(text="⬅️ Басты менюге қайту", callback_data="back_to_main")
    )
    return keyboard

def get_buy_action_keyboard(item_name):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text="💳 Сатып алу", callback_data=f"pay_{item_name}"),
        InlineKeyboardButton(text="⬅️ Товарларға қайту", callback_data="buy_goods")
    )
    return keyboard

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    user_state[message.from_user.id] = None
    await message.answer("Сәлеметсіз бе! Сізге не көмектесе аламын?", reply_markup=get_main_menu())

@dp.callback_query_handler(lambda c: True)
async def process_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    code = callback_query.data

    if code == "buy_goods":
        user_state[user_id] = None
        await callback_query.message.edit_text("🛒 Товар тізімі:\n\nӨзіңізге қажетті шенді таңдаңыз:", reply_markup=get_goods_menu())

    elif code == "write_claim":
        user_state[user_id] = "waiting_claim"
        await callback_query.message.edit_text("✍️ Шағым жазу бөлімі\n\nКімге шағым жазасыз (Ник) және себебін (Причина) толық жазып жіберіңіз:")

    elif code == "server_faq":
        user_state[user_id] = "waiting_faq"
        await callback_query.message.edit_text("❓ Сервер бойынша сұрақ қою бөлімі\n\nСерверге немесе ойынға байланысты сұрағыңызды жазыңыз:")

    elif code == "send_post":
        user_state[user_id] = "waiting_post"
        await callback_query.message.edit_text("📢 Пост салу бөлімі\n\nСкриншотты жүктеп, астына өз никіңізді жазып жіберіңіз:")

    elif code == "back_to_main":
        user_state[user_id] = None
        await callback_query.message.edit_text("Сәлеметсіз бе! Сізге не көмектесе аламын?", reply_markup=get_main_menu())

    elif code == "item_vip":
        info = ("Вип - [Вип] 👤\n\n"
                "Мәңгілік - яғни сервер жұмысын тоқтатқанша. ✅\n"
                "Сатып алынғаннан кейін ақша қайтарылмайды❗️\n\n"
                "Хп, броня, мылтықтар, навыктар, джетпак, басы жоқ, елес, супермен, скин-1, скин-2, вип машина, вип мото, жарылмау, көрінбеу, секіру, ұшу, жүзу, кемпірқосақ")
        await callback_query.message.edit_text(info, reply_markup=get_buy_action_keyboard("Вип"))

    elif code == "item_admin":
        info = ("Простой Админ - [Простой Админ] 👤\n\n"
                "Мәңгілік - яғни сервер жұмысын тоқтатқанша. ✅\n"
                "Сатып алынғаннан кейін ақша қайтарылмайды❗️\n\n"
                "Мут, Фриз, Слап, Өмір, Броня, Мылтық, Джетпак, Ойыншыға ТП жасау, Ойыншыны ТП алу, Көлікті жөндеу, Көлікті кетіру.")
        await callback_query.message.edit_text(info, reply_markup=get_buy_action_keyboard("Простой Админ"))

    elif code == "item_zam":
        info = ("Зам Админ - [Зам Админ] 👤\n\n"
                "Мәңгілік - яғни сервер жұмысын тоқтатқанша. ✅\n"
                "Сатып алынғаннан кейін ақша қайтарылмайды❗️\n\n"
                "Мут, Фриз, Слап, Өмір, Броня, Мылтық, Ақша, Джетпак, Ойыншыға ТП жасау, Ойыншыны ТП алу, Көлікті жөндеу, Көлікті кетіру.")
        await callback_query.message.edit_text(info, reply_markup=get_buy_action_keyboard("Зам Админ"))

    elif code == "item_head_admin":
        info = ("Главный Админ - [Главный Админ] 👤\n\n"
                "Мәңгілік - яғни сервер жұмысын тоқтатқанша. ✅\n"
                "Сатып алынғаннан кейін ақша қайтарылмайды❗️\n\n"
                "Кик, Мут, Фриз, Слап, Өмір, Броня, Мылтық, Ақша, Джетпак, Ойыншыға ТП жасау, Ойыншыны ТП алу, Көлікті жөндеу, Көлікті кетіру.")
        await callback_query.message.edit_text(info, reply_markup=get_buy_action_keyboard("Главный Админ"))

    elif code == "item_boss":
        info = ("Главный Босс - [Главный BOSS] 👤\n\n"
                "Мәңгілік - яғни сервер жұмысын тоқтатқанша. ✅\n"
                "Сатып алынғаннан кейін ақша қайтарылмайды❗️\n\n"
                "Кик, Мут, Фриз, Слап, Өмір, Броня, Мылтық, Ақша, Джетпак, Ойыншыға ТП жасау, Ойыншыны ТП алу, Көлікті жөндеу, Көлікті кетіру, Интерьерге ТП бару, БАН беру.")
        await callback_query.message.edit_text(info, reply_markup=get_buy_action_keyboard("Главный Босс"))

    elif code.startswith("pay_"):
        item_name = code.split("pay_")[1]
        user_state[user_id] = "waiting_receipt"
        pay_info = (f"💳 {item_name} товар сатылым деректері:\n\n"
                    "Kaspi: 4400430344137697\n"
                    "Әділет М.\n\n"
                    "Сообщение получателю деген жерге логин + ник жаз\n"
                    "Чек обезательно!\n\n"
                    "Ақшаны аударып, осы чатқа чектің суретін жіберіңіз:")
        await callback_query.message.edit_text(pay_info, reply_markup=get_main_menu())

    await callback_query.answer()

@dp.message_handler(content_types=[types.ContentType.TEXT, types.ContentType.PHOTO])
async def handle_user_messages(message: types.Message):
    user_id = message.from_user.id
    state = user_state.get(user_id)

    if message.from_user.id == ADMIN_ID and message.reply_to_message:
        try:
            orig_text = message.reply_to_message.text or message.reply_to_message.caption
            if orig_text and "ID:" in orig_text:
                target_user_id = int(orig_text.split("ID:")[1].split()[0])
                await bot.send_message(target_user_id, f"🔔 Админнен жауап:\n\n{message.text}")
                await message.reply("✅ Жауабыңыз пайдаланушыға жіберілді!")
                return
        except Exception:
            await message.reply("❌ Жауапты жіберу мүмкін болмады.")
            return

    if state == "waiting_claim":
        text = f"📩 ЖАҢА ШАҒЫМ!\n\nПайдаланушы: @{message.from_user.username} (ID:{user_id})\nШағым: {message.text}"
        await bot.send_message(ADMIN_ID, text)
        await message.answer("✅ Шағымыңыз админге жіберілді!", reply_markup=get_main_menu())
        user_state[user_id] = None

    elif state == "waiting_faq":
        text = f"❓ ЖАҢА СҰРАҚ!\n\nПайдаланушы: @{message.from_user.username} (ID:{user_id})\nСұрақ: {message.text}"
        await bot.send_message(ADMIN_ID, text)
        await message.answer("✅ Сұрағыңыз қабылданды!", reply_markup=get_main_menu())
        user_state[user_id] = None

    elif state == "waiting_post":
        caption = f"📢 ПОСТҚА ӨТІНІШ!\n\nПайдаланушы: @{message.from_user.username} (ID:{user_id})\nНик/Ақпарат: {message.caption or message.text}"
        if message.photo:
            await bot.send_photo(ADMIN_ID, message.photo[-1].file_id, caption=caption)
        else:
            await bot.send_message(ADMIN_ID, caption)
        await message.answer("Сіздің скриныз тексеріліп, ұнаса міндетті түрде пост шығады!", reply_markup=get_main_menu())
        user_state[user_id] = None

    elif state == "waiting_receipt":
        caption = f"🧾 ЖАҢА ТӨЛЕМ ЧЕГІ!\n\nПайдаланушы: @{message.from_user.username} (ID:{user_id})\nДеректер: {message.caption or message.text}"
        if message.photo:
            await bot.send_photo(ADMIN_ID, message.photo[-1].file_id, caption=caption)
        else:
            await bot.send_message(ADMIN_ID, caption)
        await message.answer("✅ Чек қабылданды! Админ тексеріп, шенді береді.", reply_markup=get_main_menu())
        user_state[user_id] = None

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
