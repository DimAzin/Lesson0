import asyncio
from aiogram import Router
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

# Создаём экземпляр бота
API_TOKEN = 'xxxxx'
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
router = Router()


# Определяем состояния
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# Создаем клавиатуру
reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать')],
        [KeyboardButton(text='Информация')]
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


# Хэндлер для команды /start
@dp.message(Command(commands=['start']))
async def start(message: Message):
    await message.answer(
        "Привет! Я помогу рассчитать вашу норму калорий. Нажмите 'Рассчитать', чтобы начать.",
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

async def main():
     dp.include_router(router)
     await dp.start_polling(bot)

# Запуск бота
if __name__ == "__main__":
     asyncio.run(main())


