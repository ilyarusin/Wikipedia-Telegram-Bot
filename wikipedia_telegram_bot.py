

import telebot, wikipedia

# Создаем экземпляр бота
bot = telebot.TeleBot('')

# Устанавливаем русский язык в Wikipedia
wikipedia.set_lang("ru")

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])

def handle_text(message):
    s = message.text
    try:
        wikitext = wikipedia.summary(s)
        if len(wikitext) > 4096:
            for x in range(0, len(wikitext), 4096):
                bot.send_message(message.chat.id, wikitext[x:x+4096])
        else:
            bot.send_message(message.chat.id, wikitext)
    except:
        bot.send_message(message.chat.id, 'В энциклопедии нет информации об этом')

# Запускаем бота
bot.polling(none_stop=True, interval=0)