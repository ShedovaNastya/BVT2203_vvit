import telebot
from telebot import types
import psycopg2
import datetime
import math

def timetable_day(week,day):
    days = ['ПОНЕДЕЛЬНИК', 'ВТОРНИК', 'СРЕДА', 'ЧЕТВЕРГ', 'ПЯТНИЦА', 'СУББОТА']
    time = ['9.30 - 11.05', '11.20 - 12.55', '13.10 - 14.45', '15.25 - 17.00', '17.15 - 18.50']
    cursor.execute('''
        SELECT num_of_pair, title,lec_lab_prac, room_numb, name  FROM subject 
        join timetable on (subject.id = timetable.subject_id_fk)
        join preps on (subject.id = preps.subject_id_fk) 
        WHERE day = %s AND num_of_week = %s''', 
        (str(day), str(week)))
    records = list(cursor.fetchall())

    ans=''
    ans = days[day-1]  +  '\n\n'
    for pair in range(1,6):
        flag = 0
        for elems in range(len(records)):
            if records[elems][0] == pair:
                flag = 1
                elem_pair = records[elems]
        if flag==0:
            ans+= str(pair) + '.  ' + time[pair-1] + '\n    < Нет пары >  \n\n'
        else:
            ans += str(pair) + '.  ' + time[pair - 1] + '\n    ' + elem_pair[1] + '\n    ' + elem_pair[4] + '\n    '  + elem_pair[2] + ' в ' + elem_pair[3] + '\n\n'
    

    return ans

def timetable_week(week):
    ans = ''
    for i in range(1, 7):
        ans += timetable_day(week, i) + '\n----------------------------------------------------------\n\n'
    return ans


conn = psycopg2.connect(database = 'lab_7',
                        user = 'postgres', password = '95299392',
                        host = 'localhost', port ='5432')
cursor = conn.cursor()

token = "6042343821:AAFphHqMeLjIBcuAudYCD0zNufOXQ6dCmKs"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Понедельник", "Вторник")
    keyboard.row('Среда','Четверг')
    keyboard.row('Пятница','Суббота')
    keyboard.row('Расписание на текущую неделю')
    keyboard.row('Расписание на следующую неделю')
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    msg = ''
    msg += 'Здравствуйте. С помощью данного бота вы можете узнать'
    msg += ' расписание группы БВТ2203 за 2 семестр этого года. Для того, '
    msg += 'чтобы бот выдал вам расписание, необходимо нажать на одну из кнопок\n\n'
    msg += 'Бот имеет следующие команды\n'
    msg += '/week - расписание на эту неделю\n'
    msg += '/mtuci - сайт университета.\n\n'
    msg += 'Приятного использования.'
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands=['mtuci'])
def start_message(message):
    bot.send_message(message.chat.id, 'https://mtuci.ru/')

@bot.message_handler(commands=['week'])
def week(message):
    first_date = datetime.datetime.now()
    second_date = datetime.datetime(2023,1,29)
    delta =  first_date - second_date
    week = math.ceil(delta.days/7) % 2
    if week == 0:
        bot.send_message(message.chat.id, 'Сейчас чётная неделя')
    else:
        bot.send_message(message.chat.id, 'Сейчас нечётная неделя')

@bot.message_handler(content_types=['text'])
def answer(message):
    first_date = datetime.datetime.now()
    second_date = datetime.datetime(2023,1,29)
    delta =  first_date - second_date
    week = math.ceil(delta.days/7) % 2
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда - https://mtuci.ru/')
    elif message.text.lower() == 'понедельник':
        bot.send_message(message.chat.id, timetable_day(week,1) )
    elif message.text.lower() == 'вторник':
        bot.send_message(message.chat.id, timetable_day(week,2))
    elif message.text.lower() == 'среда':
        bot.send_message(message.chat.id, timetable_day(week,3))
    elif message.text.lower() == 'четверг':
        bot.send_message(message.chat.id, timetable_day(week,4))
    elif message.text.lower() == 'пятница':
        bot.send_message(message.chat.id, timetable_day(week,5))
    elif message.text.lower() == 'суббота':
        bot.send_message(message.chat.id, timetable_day(week,6))
    elif message.text.lower() == 'расписание на текущую неделю':
        bot.send_message(message.chat.id, timetable_week(week))
    elif message.text.lower() == 'расписание на следующую неделю':
        bot.send_message(message.chat.id, timetable_week((week+1)%2))
    else:
        bot.send_message(message.chat.id, "Извините, я вас не понимаю")


bot.infinity_polling()
