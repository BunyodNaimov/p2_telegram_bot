from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

register_inl_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Ro'yxatdan o'tish", callback_data="/register")]
])

get_phone_btn = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="telefon raqamni jo'natish", request_contact=True),
    ]
], resize_keyboard=True)

add_product_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Mahsulot qo'shish", callback_data="/add_product")],
], resize_keyboard=True)

