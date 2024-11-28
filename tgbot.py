import telebot
import openpyxl
import re
import os
# Токен вашего бота
TOKEN = "8131352638:AAExNoR73lyaT-CTvjnWTMw2hmemS96tNAw"

bot = telebot.TeleBot(TOKEN)

# Путь к файлу Excel
FILE_PATH = "TOP100_yandex_music_chart.xlsx"

def get_song_data(row):
    try:
        track_number = row[0].value
        song_title = row[1].value
        artist = row[2].value
        return f"{track_number}. {song_title} - {artist}"
    except IndexError:
        return "Ошибка: Недостаточно данных в строке"

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("ДА", callback_data='yes'))
    markup.add(telebot.types.InlineKeyboardButton("НЕТ", callback_data='no'))
    bot.send_message(message.chat.id, "Привет, хочешь узнать топ 100 песен в Яндекс Музыке на сегодняшний момент?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'yes':
        workbook = None
        try:
            workbook = openpyxl.load_workbook(FILE_PATH)
            sheet = workbook.active
            song_list = []

            for row in sheet.iter_rows(min_row=2):
                song_list.append(get_song_data(row))

            if not song_list:
                bot.answer_callback_query(call.id, "Список песен пуст или не найден.")
                return

            msg = ""
            for song in song_list:
                msg += f"{song}\n"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=msg)

        except FileNotFoundError:
            bot.answer_callback_query(call.id, f"Ошибка: файл '{FILE_PATH}' не найден.")
        except Exception as e:
            bot.answer_callback_query(call.id, f"Ошибка: {e}")
        finally:
            if workbook:
                workbook.close()
    elif call.data == 'no':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="До новых встреч!")

bot.polling()