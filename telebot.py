import telebot		# Библиотека не работает без VPN

bot = telebot.TeleBot('896186290:AAEIYOZ-TdIyxNpQGkOZsDW-qwpOr3OkKBI')			# Токен нашего бота

keyboard1 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)		    # Создаем кнопку на клавиатуре, которая сразу исчезнет после нажатия
keyboard1.row('Elementary','Pre-Intermediate','Intermediate')													    # Надпись на кнопке

keyboard2 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)		    # Создаем кнопку на клавиатуре, которая сразу исчезнет после нажатия
keyboard2.row('Тайна Коко','Что-то другое','Выбор уровня')	

keyboard3 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard3.row('Продолжить')

keyboard4 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard4.row('научиться шить обувь', 'быть проклятым (кем-то)', 'благодарить судьбу')

keyboard5 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard5.row('быть музыкантом', 'играть для всего мира', 'иметь проблемы с памятью')

keyboard6 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard6.row('иметь проблемы с памятью', 'играть для всего мира', 'иметь мечту')

keyboard7 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard7.row('научиться шить обувь', 'скрывать умения', 'разрешить')

keyboard8 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard8.row('иметь проблемы с памятью', 'иметь веру в мечту', 'иметь мечту')

keyboard9 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard9.row('следовать семейным традициям', 'быть непохожим на остальных членов своей семьи', 'быть уничтоженным огромным колоколом')

keyboard10 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard10.row('иметь мечту', 'скрывать умения', 'научиться шить обувь')

keyboard11 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard11.row('иметь проблемы с памятью', 'не упускать свой шанс', 'разрешить')
#
keyboard12 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard12.row('иметь проблемы с памятью', 'иметь силу менять сердца', 'разрешить')

keyboard13 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard13.row('не упускать свой шанс', 'иметь веру в мечту', 'играть для всего мира')

keyboard14 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard14.row('Продолжить', 'Пройти тест заново')

keyboard15 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard15.row('True', 'False')

keyboard16 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard16.row('Следующая часть фильма', 'Пройти тест заново', 'Выбор фильма', 'Выбор уровня')

keyboard17 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard17.row('Miguel', 'Hector', 'Imelda', 'De la Cruz', 'Coco')

keyboard18 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard18.row('Выбор фильма', 'Выбор уровня')

keyboard19 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard19.row('Вернуться на главную', 'Вернуться к выбору фильма')

keyboard20 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard20.row('Вернуться на главную')
score = 0

@bot.message_handler(commands=['start'])										# Функция обработки команды /start
def start_message(message): 
     bot.send_message(message.chat.id, 'Выберите уровень', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])									# Функция обработки текста
def level_selection(message):
    if message.text.lower() == 'pre-intermediate':
        bot.send_message(message.chat.id, 'Раздел в разработке', reply_markup=keyboard20)
        bot.register_next_step_handler(message, err_click)
    elif message.text.lower() == 'intermediate':
        bot.send_message(message.chat.id, 'Раздел в разработке', reply_markup=keyboard20)
        bot.register_next_step_handler(message, err_click)
    elif message.text.lower() == 'elementary':
        bot.send_message(message.chat.id, 'Выберите фильм', reply_markup=keyboard2)
        bot.register_next_step_handler(message, movie_selection)

def movie_selection(message):
    if message.text.lower() == 'тайна коко':
        bot.send_message(message.chat.id, 'The Day of the Dead is a famous mexican holiday. It’s a day where most Mexican families gather together to remember their dead relatives and pray for their souls. They also set altars to remember and pray for them. This altar is decorated with photos of our relatives, skulls of sugar that represent the dead, candles that represent life, Marigold flowers, the statue of a dog, Xoloitzcuintli, who is a guide to heaven, the favorite objects of the person and the Dead’s Bread, which is a cake that is prepared on that day and set as a gift to the dead. Traditionally, people gather at the graves of deceased relatives, put them in order, decorate them with flowers and spend all night singing songs and telling stories about their ancestors who died. Продолжить?',reply_markup=keyboard3)
        bot.register_next_step_handler(message, first_task)
    elif message.text.lower() == 'что-то другое':
        bot.send_message(message.chat.id, 'Раздел в разработке', reply_markup=keyboard19)
        bot.register_next_step_handler(message, err_click)
    else:
        bot.send_message(message.chat.id, 'Выберите уровень', reply_markup=keyboard1)
        bot.register_next_step_handler(message, level_selection)

def first_task(message):
    global score
    if message.text.lower() == 'продолжить':
        score = 0
        bot.send_message(message.chat.id, 'Part 0: Connect words with their translates. №1 to be cursed by', reply_markup = keyboard4)
        bot.register_next_step_handler(message, second_task)

def second_task(message):
    if message.text.lower() == 'быть проклятым (кем-то)':
        global score
        score = score + 1
        bot.send_message(message.chat.id, 'Right. №2 to be a musician', reply_markup = keyboard5)
        bot.register_next_step_handler(message, third_task)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №2 to be a musician', reply_markup = keyboard5)
        bot.register_next_step_handler(message, third_task)

def third_task(message):
    if message.text.lower() == 'быть музыкантом':
        global score
        score = score + 1
        bot.send_message(message.chat.id, 'Right. №3 to have a dream', reply_markup = keyboard6)
        bot.register_next_step_handler(message, fourth_task)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №3 to have a dream', reply_markup = keyboard6)
        bot.register_next_step_handler(message, fourth_task)

def fourth_task(message):
    if message.text.lower() == 'иметь мечту':
        global score
        score = score + 1
        bot.send_message(message.chat.id, 'Right. №4 to learn to make shoes', reply_markup = keyboard7)
        bot.register_next_step_handler(message, fifth_task)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №4 to learn to make shoes', reply_markup = keyboard7)
        bot.register_next_step_handler(message, fifth_task)

def fifth_task(message):
    if message.text.lower() == 'научиться шить обувь':
        global score
        score = score + 1
        bot.send_message(message.chat.id, 'Right. №5 to have trouble remembering things', reply_markup = keyboard8)
        bot.register_next_step_handler(message, sixth_task)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №5 to have trouble remembering things', reply_markup = keyboard8)
        bot.register_next_step_handler(message, sixth_task)

def sixth_task(message):
    if message.text.lower() == 'иметь проблемы с памятью':
        global score
        score = score + 1
        bot.send_message(message.chat.id, 'Right. №6 to be crushed by a giant bell', reply_markup = keyboard9)
        bot.register_next_step_handler(message, seventh_task)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №6 to be crushed by a giant bell', reply_markup = keyboard9)
        bot.register_next_step_handler(message, seventh_task)

def seventh_task(message):
    if message.text.lower() == 'быть уничтоженным огромным колоколом':
        global score
        score = score + 1
        bot.send_message(message.chat.id, 'Right. №7 to hide skills', reply_markup = keyboard10)
        bot.register_next_step_handler(message, eighth_task)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №7 to hide skills', reply_markup = keyboard10)
        bot.register_next_step_handler(message, eighth_task)

def eighth_task(message):
    if message.text.lower() == 'скрывать умения':
        global score
        score = score + 1
        bot.send_message(message.chat.id, 'Right. №8 to seize your moment', reply_markup = keyboard11)
        bot.register_next_step_handler(message, ninth_task)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №8 to seize your moment', reply_markup = keyboard11)
        bot.register_next_step_handler(message, ninth_task)

def ninth_task(message):
    if message.text.lower() == 'не упускать свой шанс':
        global score
        score = score + 1
        bot.send_message(message.chat.id, 'Right. №9 to give smb’s permission', reply_markup = keyboard12)
        bot.register_next_step_handler(message, tenth_task)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №9 to give smb’s permission', reply_markup = keyboard12)
        bot.register_next_step_handler(message, tenth_task)

def tenth_task(message):
    if message.text.lower() == 'разрешить':
        global score
        score = score + 1
        bot.send_message(message.chat.id, 'Right. №10 to have faith in smb’s dream', reply_markup = keyboard13)
        bot.register_next_step_handler(message, final_before)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №10 to have faith in smb’s dream', reply_markup = keyboard13)
        bot.register_next_step_handler(message, final_before)

def final_before(message):
    global score
    if message.text.lower() == 'иметь веру в мечту':
        score = score + 1
        if score >= 9:
            mark = 5
        elif score < 9 and score > 6:
            mark = 4
        elif score <= 6 and score > 4:
            mark = 3
        elif score <= 4:
            mark = 2
        bot.send_message(message.chat.id, 'Right. Ваш результат: '+ str(score) + '/ 10. Оценка: '+ str(mark) +'. Повторить тест или приступим к фильму?', reply_markup = keyboard14)
        bot.register_next_step_handler(message, final_before2)
    else: 
        if score >= 9:
            mark = 5
        elif score < 9 and score > 6:
            mark = 4
        elif score <= 6 and score > 4:
            mark = 3
        elif score <= 4:
            mark = 2
        bot.send_message(message.chat.id, 'Wrong. Ваш результат: '+ str(score) + '/ 10. Оценка: '+ str(mark) +'. Повторить тест или приступим к фильму?', reply_markup = keyboard14)
        bot.register_next_step_handler(message, final_before2)

def final_before2(message):
    if message.text.lower() == 'пройти тест заново':
        bot.send_message(message.chat.id, 'Продолжить?', reply_markup = keyboard3)
        bot.register_next_step_handler(message, first_task)
    elif message.text.lower() == 'продолжить':
        bot.send_message(message.chat.id, 'Ссылка на фильм: https://film-smile.ru/load/multfilmy/coco_tajna_koko_2017/6-1-0-156. Посмотрите до 22 минут 46 секунд. Если посмотрели, то жмите "Продолжить"', reply_markup = keyboard3)
        bot.register_next_step_handler(message, first_first)

def first_first(message):
    if message.text.lower() == 'продолжить':
        global score1
        score1 = 0
        bot.send_message(message.chat.id, 'Part 1: True/False №1: The main character of the cartoon is Miguel who loves his family very much and wants to carry on the family traditions.', reply_markup = keyboard15)
        bot.register_next_step_handler(message, second_first)

def second_first(message):
    global score1
    if message.text.lower() == 'false':
        score1 = score1 + 1
        bot.send_message(message.chat.id, 'Right. №2: Once upon a time, a great-great grandmother Imelda opened a shoe workshop to provide her daughter.', reply_markup = keyboard15)
        bot.register_next_step_handler(message, third_first)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №2: Once upon a time, a great-great grandmother Imelda opened a shoe workshop to provide her daughter.', reply_markup = keyboard15)
        bot.register_next_step_handler(message, third_first)

def third_first(message):
    global score1
    if message.text.lower() == 'true':
        score1 = score1 + 1
        bot.send_message(message.chat.id, 'Right. №3: Miguel isn’t like the rest of his family because he has a dream to become a musician.', reply_markup = keyboard15)
        bot.register_next_step_handler(message, fourth_first)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №3: Miguel isn’t like the rest of his family because he has a dream to become a musician.', reply_markup = keyboard15)
        bot.register_next_step_handler(message, fourth_first)

def fourth_first(message):
    global score1
    if message.text.lower() == 'true':
        score1 = score1 + 1
        bot.send_message(message.chat.id, 'Right. №4: Secretly from everyone, Miguel listens to the songs of his beloved musician Ernesto de la Cruz.', reply_markup = keyboard15)
        bot.register_next_step_handler(message, fifth_first)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №4: Secretly from everyone, Miguel listen to the songs of his beloved musician Ernesto de la Cruz.', reply_markup = keyboard15)
        bot.register_next_step_handler(message, fifth_first)
        # тут
def fifth_first(message):
    global score1
    if message.text.lower() == 'true':
        score1 = score1 + 1
        bot.send_message(message.chat.id, 'Right. №5: Coco has a trouble remembering things so her relatives are very annoyed.', reply_markup = keyboard15)
        bot.register_next_step_handler(message, sixth_first)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №5: Coco has a trouble remembering things so her relatives are very annoyed.', reply_markup = keyboard15)
        bot.register_next_step_handler(message, sixth_first)

def sixth_first(message):
    global score1
    if message.text.lower() == 'true':
        score1 = score1 + 1
        bot.send_message(message.chat.id, 'Right. №6: Miguel’s family banish all music from their lives.', reply_markup = keyboard15)
        bot.register_next_step_handler(message, seventh_first)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №6: Miguel’s family banish all music from their lives.', reply_markup = keyboard15)
        bot.register_next_step_handler(message, seventh_first)

def seventh_first(message):
    global score1
    if message.text.lower() == 'true':
        score1 = score1 + 1
        bot.send_message(message.chat.id, 'Right. №7: Granny Abuelita runs the house and everybody listens to her.', reply_markup = keyboard15)
        bot.register_next_step_handler(message, eighth_first)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №7: Granny Abuelita runs the house and everybody listens to her.', reply_markup = keyboard15)
        bot.register_next_step_handler(message, eighth_first)

def eighth_first(message):
    global score1
    if message.text.lower() == 'true':
        score1 = score1 + 1
        bot.send_message(message.chat.id, 'Right. №8: One day a man who Miguel is cleaning the shoes gives an advice to stop hiding his desire of being a musician and tell his family.', reply_markup = keyboard15)
        bot.register_next_step_handler(message, ninth_first)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №8: One day a man who Miguel is cleaning the shoes gives an advice to stop hiding his desire of being a musician and tell his family.', reply_markup = keyboard15)
        bot.register_next_step_handler(message, ninth_first)

def ninth_first(message):
    global score1
    if message.text.lower() == 'false':
        score1 = score1 + 1
        bot.send_message(message.chat.id, 'Right. №9: Miguel thinks that his great- great grandfather is  Ernesto de la Cruz so he runs to his crypt to borrow the guitar.', reply_markup = keyboard15)
        bot.register_next_step_handler(message, tenth_first)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №9: Miguel thinks that his great- great grandfather is  Ernesto de la Cruz so he runs to his crypt to borrow the guitar.', reply_markup = keyboard15)
        bot.register_next_step_handler(message, tenth_first)

def tenth_first(message):
    global score1
    if message.text.lower() == 'true':
        score1 = score1 + 1
        bot.send_message(message.chat.id, 'Right. №10: The statue of Ernesto de la Cruz is in the middle of the square and the crypt is located under it.', reply_markup = keyboard15)
        bot.register_next_step_handler(message, final_first_coco)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №10: The statue of Ernesto de la Cruz is in the middle of the square and the crypt is located under it.', reply_markup = keyboard15)
        bot.register_next_step_handler(message, final_first_coco)

def final_first_coco(message):
    global score1
    if message.text.lower() == 'true':
        score1 = score1 + 1
        if score1 >= 9:
            mark = 5
        elif score1 < 9 and score1 > 6:
            mark = 4
        elif score1 <= 6 and score1 > 4:
            mark = 3
        elif score1 <= 4:
            mark = 2
        bot.send_message(message.chat.id, 'Right. Ваш результат: '+ str(score1) + '/10. Ваша оценка: ' + str(mark) + '. Продолжить работу с фильмом, повторить тест, вернуться к выбору фильма или к выбору уровня?', reply_markup = keyboard16)
        bot.register_next_step_handler(message, final_task_coco)
    else: 
        if score1 >= 9:
            mark = 5
        elif score1 < 9 and score1 > 6:
            mark = 4
        elif score1 <= 6 and score1 > 4:
            mark = 3
        elif score1 <= 4:
            mark = 2
        bot.send_message(message.chat.id, 'Wrong. Ваш результат: '+ str(score1) + '/10. Ваша оценка: ' + str(mark) + '. Продолжить работу с фильмом, повторить тест, вернуться к выбору фильма или к выбору уровня?', reply_markup = keyboard16)
        bot.register_next_step_handler(message, final_task_coco)

def final_task_coco(message):
    if message.text.lower() == 'пройти тест заново':
        bot.send_message(message.chat.id, 'Продолжить?', reply_markup = keyboard3)
        bot.register_next_step_handler(message, first_first)
    elif message.text.lower() == 'выбор фильма':
        bot.send_message(message.chat.id, 'Выберите фильм', reply_markup = keyboard2)
        bot.register_next_step_handler(message, movie_selection)
    elif message.text.lower() == 'выбор уровня':
        bot.send_message(message.chat.id, 'Выберите уровень', reply_markup=keyboard1)
        bot.register_next_step_handler(message, level_selection)
    elif message.text.lower() == 'следующая часть фильма':
        bot.send_message(message.chat.id, 'Ссылка на фильм: https://film-smile.ru/load/multfilmy/coco_tajna_koko_2017/6-1-0-156. Посмотрите до 41 минуты 15 секунд. Если посмотрели, то жмите "Продолжить"', reply_markup=keyboard3)
        bot.register_next_step_handler(message, first_second)

def final_task_coco2(message):
    if message.text.lower() == 'пройти тест заново':
        bot.send_message(message.chat.id, 'Продолжить?', reply_markup = keyboard3)
        bot.register_next_step_handler(message, first_second)
    elif message.text.lower() == 'выбор фильма':
        bot.send_message(message.chat.id, 'Выберите фильм', reply_markup = keyboard2)
        bot.register_next_step_handler(message, movie_selection)
    elif message.text.lower() == 'выбор уровня':
        bot.send_message(message.chat.id, 'Выберите уровень', reply_markup=keyboard1)
        bot.register_next_step_handler(message, level_selection)
    elif message.text.lower() == 'следующая часть фильма':
        bot.send_message(message.chat.id, 'Ссылка на фильм: https://film-smile.ru/load/multfilmy/coco_tajna_koko_2017/6-1-0-156. Посмотрите до 1 часа 11 минут 30 секунд. Если посмотрели, то жмите "Продолжить"', reply_markup=keyboard3)
        bot.register_next_step_handler(message, first_third)

def final_task_coco3(message):
    if message.text.lower() == 'пройти тест заново':
        bot.send_message(message.chat.id, 'Продолжить?', reply_markup = keyboard3)
        bot.register_next_step_handler(message, first_third)
    elif message.text.lower() == 'выбор фильма':
        bot.send_message(message.chat.id, 'Выберите фильм', reply_markup = keyboard2)
        bot.register_next_step_handler(message, movie_selection)
    elif message.text.lower() == 'выбор уровня':
        bot.send_message(message.chat.id, 'Выберите уровень', reply_markup=keyboard1)
        bot.register_next_step_handler(message, level_selection)
    elif message.text.lower() == 'следующая часть фильма':
        bot.send_message(message.chat.id, 'Ссылка на фильм: https://film-smile.ru/load/multfilmy/coco_tajna_koko_2017/6-1-0-156. Посмотрите до конца. Если посмотрели, то жмите "Продолжить"', reply_markup=keyboard3)
        bot.register_next_step_handler(message, first_fourth)

def first_second(message):
    if message.text.lower() == 'продолжить':
        global score2
        score2 = 0
        bot.send_message(message.chat.id, 'Part 2: Connect beginnings (numbers) and endings (letters) of sentences. Write letters in correct order without spaces.')
        bot.send_message(message.chat.id, 'Beginnings:\n1. Striking the strings, Miguel...\n2. The boy is very scared but calms down...\n3. They take him to the World of the Dead...\n4. There Miguel meets Imelda...\n5. She isn’t able to do that...\n6. Imelda makes up her mind...\n7. But the boy must give up the idea...\n8. He comes back home...\n9. Nobody from his family except Imelda...\n10. So Miguel runs away and...')
        bot.send_message(message.chat.id, 'Endings:\nA) to be a musician\nB) when he meets his dead ancestors\nC) meets skeleton Hector\nD) wants to help him to return home again\nE) but breaks the promise not to take the guitar anymore\nF) because Miguel removes her photo from the family altar\nG) begins to see spirits\nH) who can’t get into the Living World\nI) to send the boy back home with her blessing\nJ) over the Flower Bridge.')
        bot.register_next_step_handler(message, final_second_coco)

def final_second_coco(message):
    global score2
    if message.text.lower() == 'gbjhfiaedc':
        score2 = score2 + 5

        bot.send_message(message.chat.id, 'Right. Продолжить работу с фильмом, повторить задание, вернуться к выбору фильма или к выбору уровня?', reply_markup = keyboard16)
        bot.register_next_step_handler(message, final_task_coco2)
    else: 
        bot.send_message(message.chat.id, 'Wrong. Продолжить работу с фильмом, повторить задание, вернуться к выбору фильма или к выбору уровня?', reply_markup = keyboard16)
        bot.register_next_step_handler(message, final_task_coco2)

def first_third(message):
    if message.text.lower() == 'продолжить':
        global score3
        score3 = 0
        bot.send_message(message.chat.id, 'Part 3: Paste words in correct places. Write sequence of numbers without spaces.')
        bot.send_message(message.chat.id, 'Miguel _____ that he needs the blessing of his grandfather - Ernesto de la Cruz. The boy goes to _____ with Hector, and at this time his relatives are looking for him. On the way to de la Cruz, Hector takes _____ from a dying old man, and for the first time Miguel sees death in _____. Then Miguel and Hector fall into the musical competition, and there Miguel first performs in front of _____. But at the competition the boy is found by _____. Miguel escapes from the scene, quarrels with Hector and lonely gets to the de la Cruz party. There he _____ the artist and spends a wonderful evening with him, and then _____. However, the boy finds Hector. He understands that it was de la Cruz who killed him in order to appropriate _____. The artist orders to put them both in _____. ')
        bot.send_message(message.chat.id, '1) a guitar\n2) the public\n3) understands\n4) the World of the Dead\n5) his party\n6) prison\n7) his relatives\n8) asks for blessings\n9) meets\n10) Hector`s songs')
        bot.register_next_step_handler(message, final_third_coco)
def final_third_coco(message):
    global score3
    if message.text.lower() == '35142798106':
        score3 = score3 + 5

        bot.send_message(message.chat.id, 'Right. Продолжить работу с фильмом, повторить задание, вернуться к выбору фильма или к выбору уровня?', reply_markup = keyboard16)
        bot.register_next_step_handler(message, final_task_coco3)
    else: 
        bot.send_message(message.chat.id, 'Wrong. Продолжить работу с фильмом, повторить задание, вернуться к выбору фильма или к выбору уровня?', reply_markup = keyboard16)
        bot.register_next_step_handler(message, final_task_coco3)

def first_fourth(message):
    if message.text.lower() == 'продолжить':
        global score4
        score4 = 0
        bot.send_message(message.chat.id, 'Part 4: Who asked? №1: - Hector! You were right. I should have gone back to family.', reply_markup = keyboard17)
        bot.register_next_step_handler(message, second_fourth)

def second_fourth(message):
    global score4
    if message.text.lower() == 'miguel':
        score4 = score4 + 1
        bot.send_message(message.chat.id, 'Right. №2: - I spent decades protecting my family from your mistakes.', reply_markup = keyboard17)
        bot.register_next_step_handler(message, third_fourth)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №2: - I spent decades protecting my family from your mistakes.', reply_markup = keyboard17)
        bot.register_next_step_handler(message, third_fourth)

def third_fourth(message):
    global score4
    if message.text.lower() == 'imelda':
        score4 = score4 + 1
        bot.send_message(message.chat.id, 'Right. №3: - Papa was a musician.', reply_markup = keyboard17)
        bot.register_next_step_handler(message, fourth_fourth)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №3: - Papa was a musician.', reply_markup = keyboard17)
        bot.register_next_step_handler(message, fourth_fourth)

def fourth_fourth(message):
    global score4
    if message.text.lower() == 'coco':
        score4 = score4 + 1
        bot.send_message(message.chat.id, 'Right. №4: - Nothing`s more important than family.', reply_markup = keyboard17)
        bot.register_next_step_handler(message, fifth_fourth)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №4: - Nothing`s more important than family.', reply_markup = keyboard17)
        bot.register_next_step_handler(message, fifth_fourth)

def fifth_fourth(message):
    global score4
    if message.text.lower() == 'miguel':
        score4 = score4 + 1
        bot.send_message(message.chat.id, 'Right. №5: - I am trying to save your life!', reply_markup = keyboard17)
        bot.register_next_step_handler(message, sixth_fourth)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №5: - I am trying to save your life!', reply_markup = keyboard17)
        bot.register_next_step_handler(message, sixth_fourth)

def sixth_fourth(message):
    global score4
    if message.text.lower() == 'imelda':
        score4 = score4 + 1
        bot.send_message(message.chat.id, 'Right. №6: - Hey musician to musician... I need a favor.', reply_markup = keyboard17)
        bot.register_next_step_handler(message, seventh_fourth)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №6: - Hey musician to musician... I need a favor.', reply_markup = keyboard17)
        bot.register_next_step_handler(message, seventh_fourth)

def seventh_fourth(message):
    global score4
    if message.text.lower() == 'miguel':
        score4 = score4 + 1
        bot.send_message(message.chat.id, 'Right. №7: - You have to be willing to do whatever it takes to seize your moment.', reply_markup = keyboard17)
        bot.register_next_step_handler(message, eighth_fourth)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №7: - You have to be willing to do whatever it takes to seize your moment.', reply_markup = keyboard17)
        bot.register_next_step_handler(message, eighth_fourth)

def eighth_fourth(message):
    global score4
    if message.text.lower() == 'de la cruz':
        score4 = score4 + 1
        bot.send_message(message.chat.id, 'Right. №8: - I didn`t choke, okey? I got food poisoning which is a big difference.', reply_markup = keyboard17)
        bot.register_next_step_handler(message, ninth_fourth)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №8: - I didn`t choke, okey? I got food poisoning which is a big difference.', reply_markup = keyboard17)
        bot.register_next_step_handler(message, ninth_fourth)

def ninth_fourth(message):
    global score4
    if message.text.lower() == 'hector':
        score4 = score4 + 1
        bot.send_message(message.chat.id, 'Right. №9: - We`re both out of time, mijo.', reply_markup = keyboard17)
        bot.register_next_step_handler(message, tenth_fourth)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №9: - We`re both out of time, mijo.', reply_markup = keyboard17)
        bot.register_next_step_handler(message, tenth_fourth)

def tenth_fourth(message):
    global score4
    if message.text.lower() == 'hector':
        score4 = score4 + 1
        bot.send_message(message.chat.id, 'Right. №10: - He will listen to music.', reply_markup = keyboard17)
        bot.register_next_step_handler(message, final_fourth_coco)
    else: 
        bot.send_message(message.chat.id, 'Wrong. №10: - He will listen to music.', reply_markup = keyboard17)
        bot.register_next_step_handler(message, final_fourth_coco)

def final_fourth_coco(message):
    global score4
    if message.text.lower() == 'de la cruz':
        score4 = score4 + 1
        if score4 >= 9:
            mark = 5
        elif score4 < 9 and score4 > 6:
            mark = 4
        elif score4 <= 6 and score4 > 4:
            mark = 3
        elif score4 <= 4:
            mark = 2
        bot.send_message(message.chat.id, 'Right. Ваш результат: '+ str(score4) + '/10. Ваша оценка: ' + str(mark) + '. Продолжить или повторить тест?', reply_markup = keyboard14)
        bot.register_next_step_handler(message, final_fourth_coco2)
    else: 
        if score4 >= 9:
            mark = 5
        elif score4 < 9 and score4 > 6:
            mark = 4
        elif score4 <= 6 and score4 > 4:
            mark = 3
        elif score4 <= 4:
            mark = 2
        bot.send_message(message.chat.id, 'Wrong. Ваш результат: '+ str(score4) + '/10. Ваша оценка: ' + str(mark) + '. Продолжить или повторить тест?', reply_markup = keyboard14)
        bot.register_next_step_handler(message, final_fourth_coco2)

def final_fourth_coco2(message):
    if message.text.lower() == 'продолжить':
        global score1
        global score2
        global score3
        global score4
        sum = score1 + score2 + score3 + score4
        if sum >= 27:
            mark = 5
        elif score4 < 27 and score4 > 20:
            mark = 4
        elif score4 <= 20 and score4 > 14:
            mark = 3
        elif score4 <= 14:
            mark = 2
        bot.send_message(message.chat.id, 'Ваш результат по всему фильму: '+ str(sum) + '/40. Ваша оценка: ' + str(mark) + '. Вернуться к выбору фильма или к выбору уровня?', reply_markup = keyboard18)
        bot.register_next_step_handler(message, final_task_coco4)
    else:
        bot.send_message(message.chat.id, 'Продолжить?', reply_markup = keyboard3)
        bot.register_next_step_handler(message, first_fourth)

def final_task_coco4(message):
    if message.text.lower() == 'выбор фильма':
        bot.send_message(message.chat.id, 'Выберите фильм', reply_markup = keyboard2)
        bot.register_next_step_handler(message, movie_selection)
    elif message.text.lower() == 'выбор уровня':
        bot.send_message(message.chat.id, 'Выберите уровень', reply_markup=keyboard1)
        bot.register_next_step_handler(message, level_selection)

def err_click(message):
    if message.text.lower() == 'вернуться на главную':
        bot.send_message(message.chat.id, 'Выберите уровень', reply_markup=keyboard1)
        bot.register_next_step_handler(message, level_selection)
    elif message.text.lower() == 'вернуться к выбору фильма':
        bot.send_message(message.chat.id, 'Выберите фильм', reply_markup = keyboard2)
        bot.register_next_step_handler(message, movie_selection)

bot.polling(none_stop=True, interval=0)																	#Это нужно для того, чтобы бот не выключился сразу, а работал и проверял, нет ли на сервере нового сообщения
