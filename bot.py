from aiogram import Bot, types, Dispatcher, executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
import logging, sqlite3
conn = sqlite3.connect('Xakdb.db')
cursor = conn.cursor()
API_TOKEN = '5284901920:AAH-062qW6F_Eo1xpv4W12cJW_pPZmP_v_o'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
rep_btn1 = KeyboardButton("Проверить первый датчик")
rep_btn2 = KeyboardButton("Проверить второй датчик")
rep_btn3 = KeyboardButton("Проверить третий датчик")
rep_rtrn_btn = KeyboardButton("Вернуться")
start_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(rep_btn1).add(rep_btn2).add(rep_btn3)
rtrn_from1_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(rep_btn2).add(rep_btn3).add(rep_rtrn_btn)
rtrn_from2_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(rep_btn1).add(rep_btn3).add(rep_rtrn_btn)
rtrn_from3_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(rep_btn1).add(rep_btn3).add(rep_rtrn_btn)
greet = False
@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    text = f'''Здравствуйте, {message.from_user.full_name}.
Я бот по проверке состояния оборудования. Что вы хотите узнать?'''
    await message.answer(text, reply_markup=start_kb)
@dp.message_handler(Text(equals="Вернуться"))
async def welcome(message: types.Message):
    text = f'''Здравствуйте, {message.from_user.full_name}.
Я бот по проверке состояния оборудования. Что вы хотите узнать?'''
    await message.answer(text, reply_markup=start_kb)
@dp.message_handler(Text(equals="Проверить первый датчик"))
async def first_mech(message: types.Message):
    geo1lat = float(cursor.execute(f"SELECT geo1lat FROM Xakaton WHERE DeviceID == 'device1' ORDER BY Time DESC LIMIT 1;").fetchone()[0]);
    geo1lon = float(cursor.execute(f"SELECT geo1lon FROM Xakaton WHERE DeviceID == 'device1' ORDER BY Time DESC LIMIT 1;").fetchone()[0]);
    url = f"https://www.google.com/maps/place/55%C2%B054'46.7%22N+49%C2%B017'09.2%22E/@{geo1lat},{geo1lon},17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x11b350a87beeb60b!8m2!3d55.912967!4d49.285896!5m1!1e4?hl=ru-RU"
    text = "Если геолокация не поддерживается:" + url
    await message.answer_location(geo1lat, geo1lon)
    await message.answer(text)
    if cursor.execute(f"SELECT IsWorking FROM Xakaton WHERE DeviceID == 'device1' ORDER BY Time DESC LIMIT 1;").fetchone()[0] == 'True' and cursor.execute(f"SELECT IsWatering FROM Xakaton WHERE DeviceID == 'device1' ORDER BY Time DESC;").fetchone()[0] == 'True':
        await message.answer("Устройство работает и поливает", reply_markup=rtrn_from1_kb)
    elif cursor.execute(f"SELECT IsWorking FROM Xakaton WHERE DeviceID == 'device1' ORDER BY Time DESC LIMIT 1;").fetchone()[0] == 'True':
        await message.answer("Устройство работает", reply_markup=rtrn_from1_kb)
    else:
        await message.answer("Устройство не работает!", reply_markup=rtrn_from1_kb)
@dp.message_handler(Text(equals="Проверить второй датчик"))
async def sec_mech(message: types.Message):
    geo1lat = float(cursor.execute(f"SELECT geo1lat FROM Xakaton WHERE DeviceID == 'device2'ORDER BY Time DESC LIMIT 1;").fetchone()[0]);
    geo1lon = float(cursor.execute(f"SELECT geo1lon FROM Xakaton WHERE DeviceID == 'device2' ORDER BY Time DESC LIMIT 1;").fetchone()[0]);
    url = f"https://www.google.com/maps/place/55%C2%B054'46.7%22N+49%C2%B017'09.2%22E/@{geo1lat},{geo1lon},17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x11b350a87beeb60b!8m2!3d55.912967!4d49.285896!5m1!1e4?hl=ru-RU"
    text = "Если геолокация не поддерживается:" + url
    await message.answer_location(geo1lat, geo1lon)
    await message.answer(text)
    if cursor.execute(f"SELECT IsWorking FROM Xakaton WHERE DeviceID == 'device2' ORDER BY Time DESC LIMIT 1;").fetchone()[0] == 'True' and cursor.execute(f"SELECT IsWatering FROM Xakaton WHERE DeviceID == 'device2' ORDER BY Time DESC;").fetchone()[0] == 'True':
        await message.answer("Устройство работает и поливает", reply_markup=rtrn_from2_kb)
    elif cursor.execute(f"SELECT IsWorking FROM Xakaton WHERE DeviceID == 'device2'  ORDER BY Time DESC LIMIT 1;").fetchone()[0] == 'True':
        await message.answer("Устройство работает", reply_markup=rtrn_from2_kb)
    else:
        await message.answer("Устройство не работает!", reply_markup=rtrn_from2_kb)
@dp.message_handler(Text(equals="Проверить третий датчик"))
async def third_mech(message: types.Message):
    geo1lat = float(cursor.execute(f"SELECT geo1lat FROM Xakaton WHERE DeviceID == 'device3' ORDER BY Time DESC LIMIT 1;").fetchone()[0]);
    geo1lon = float(cursor.execute(f"SELECT geo1lon FROM Xakaton WHERE DeviceID == 'device3'  ORDER BY Time DESC LIMIT 1;").fetchone()[0]);
    url = f"https://www.google.com/maps/place/55%C2%B054'46.7%22N+49%C2%B017'09.2%22E/@{geo1lat},{geo1lon},17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x11b350a87beeb60b!8m2!3d55.912967!4d49.285896!5m1!1e4?hl=ru-RU"
    text = "Если геолокация не поддерживается:" + url
    await message.answer_location(geo1lat, geo1lon)
    await message.answer(text)
    if cursor.execute(f"SELECT IsWorking FROM Xakaton WHERE DeviceID == 'device3' ORDER BY Time DESC LIMIT 1;").fetchone()[0] == 'True' and cursor.execute(f"SELECT IsWatering FROM Xakaton WHERE DeviceID == 'device3' ORDER BY Time DESC;").fetchone()[0] == 'True':
        await message.answer("Устройство работает и поливает", reply_markup=rtrn_from3_kb)
    elif cursor.execute(f"SELECT IsWorking FROM Xakaton WHERE DeviceID == 'device3' ORDER BY Time DESC LIMIT 1;").fetchone()[0] == 'True':
        await message.answer("Устройство работает", reply_markup=rtrn_from3_kb)
    else:
        await message.answer("Устройство не работает!", reply_markup=rtrn_from3_kb)
@dp.message_handler()
async def unknown(message: types.Message):
    await message.answer("Я не знаю такой команды. Для начала напишите /start")
executor.start_polling(dp)