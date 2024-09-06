import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from aiogram.types import FSInputFile
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F
import aiofiles
import asyncio

# Создаём экземпляр бота
API_TOKEN = '7515340328:AAHuABhVxypqZh0wypTpJoyTFXpTIMCJJD8'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Определяем состояния
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()



# Определяем главную клавиатуру с кнопками
reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать')],
        [KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить')]
    ],
    resize_keyboard=True
)

# Создаем Inline-клавиатуру
inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
    ]
)

# Создаем Inline-клавиатуру для выбора продуктов
inline_keyboard_products = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Product1', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product2', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product3', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product4', callback_data='product_buying')]
    ]
)


# Хэндлер для команды /start
@dp.message(Command('start'))
async def start(message: Message):
    await message.answer(
        "Привет! Я помогаю вам сохранять здоровье, следя за своим питанием(рассчет калорий) и "
        "эмоциональным состоянием(поглаживание фигурок кошек). Нажмите 'Рассчитать', "
        "чтобы начать рассчет или 'Купить' для приобретения фигурки кошки.",
        reply_markup=reply_keyboard
    )
# Хэндлер для кнопки 'Рассчитать' с ReplyKeyboard
@dp.message(lambda message: message.text == 'Рассчитать')
async def main_menu(message: Message):
    await message.answer(
        "Выберите опцию:",
        reply_markup=inline_keyboard
    )


# Хэндлер для Inline-кнопки 'Формулы расчёта'
@dp.callback_query(lambda c: c.data == 'formulas')
async def get_formulas(call: CallbackQuery):
    await call.message.answer(
        "Формула Миффлина-Сан Жеора для женщин: BMR = 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) - 161\n"
        "Для мужчин: BMR = 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) + 5"
    )
    await call.answer()


# Хэндлер для Inline-кнопки 'Рассчитать норму калорий'
@dp.callback_query(lambda c: c.data == 'calories')
async def set_age(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Введите свой возраст:")
    await state.set_state(UserState.age)
    await call.answer()


# Хэндлер для ввода возраста
@dp.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await state.set_state(UserState.growth)


# Хэндлер для ввода роста
@dp.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await state.set_state(UserState.weight)


# Хэндлер для ввода веса и расчёта калорий
@dp.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    # формула Миффлина - Сан Жеора
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    calories_w = 10 * weight + 6.25 * growth - 5 * age - 161
    calories_m = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f"Дневная норма калорий: для женщин - {calories_w} ккал, для мужчин - {calories_m} ккал.")

    await state.clear()


# Хэндлер для кнопки 'Купить'
@dp.message(lambda message: message.text =='Купить')
async def get_buying_list(message: Message):
    try:
        for i in range(1, 5):
            file_path = os.path.abspath(f'files/{i}.png')
            if os.path.exists(file_path):
                 async with aiofiles.open(file_path, 'rb') as file:
                    photo = await file.read()
                    img = FSInputFile(file_path)
                    await message.answer_photo(photo=img, caption=f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100} руб.')
            else:
                await message.answer(f"Ошибка: файл {file_path} не найден.")
    except Exception as e:
        await message.answer(f"Ошибка при отправке фото: {e}")

    await message.answer(
          "Выберите продукт для покупки:",
          reply_markup=inline_keyboard_products
     )


# Хэндлер для обработки выбора продукта
@dp.callback_query(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


if __name__ == "__main__":
    dp.run_polling(bot)


