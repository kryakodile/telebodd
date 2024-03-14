import telebot

bot = telebot.TeleBot("7035094278:AAHSPYYBOM-o-2PFk46iVyWMkOUHi2Zej2E")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.infinity_polling()