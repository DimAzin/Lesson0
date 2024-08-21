

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = 'XXXXXX'
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет! Я бот помогающий твоему здоровью.")
    print("Привет! Я бот, помогающий твоему здоровью.")


@dp.message()
async def all_messages(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")
    print("Введите команду /start, чтобы начать общение.")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())