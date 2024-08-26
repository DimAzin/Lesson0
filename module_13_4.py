from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram import Router
import asyncio

# Инициализация бота и диспетчера
bot = Bot(token="xxxx")
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
router = Router()


# Определение состояний
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# Обработчик /start или "Calories"
@router.message(Command("start"))
async def set_age(message: Message, state: FSMContext):
    await message.answer("Введите 'calories' для начала:")


@router.message(lambda message: message.text.lower() == "calories")
async def set_age(message: Message, state: FSMContext):
    await message.answer("Введите свой возраст:")
    await state.set_state(UserState.age)


# Обработчик age
@router.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await state.set_state(UserState.growth)


# Обработчик growth
@router.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await state.set_state(UserState.weight)


# Обработчик weight
@router.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # формула Миффлина - Сан Жеора для расчёта калорий (для женщин)
    calories_w = 10 * weight + 6.25 * growth - 5 * age - 161
    calories_m = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f"Ваша дневная норма калорий: для женщин - {calories_w} ккал, для мужчин - {calories_m} ккал.")

    await state.clear()  # Остановка машины состояний


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
