import telebot
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

rpc_user = 'kzcashrpc'
rpc_password = '121'
rpc_connection = AuthServiceProxy(f'http://{rpc_user}:{rpc_password}@127.0.0.1:8276')
bot = telebot.TeleBot("7035094278:AAHSPYYBOM-o-2PFk46iVyWMkOUHi2Zej2E")

@bot.message_handler(commands=['getbalance'])
def get_balance(message):
    balance = float(rpc_connection.getbalance())
    bot.reply_to(message, f"Ваш баланс: {balance}")

@bot.message_handler(commands=['getnewaddress'])
def get_new_address(message):
    new_address = rpc_connection.getnewaddress()
    bot.reply_to(message, f"Новый адрес: {new_address}")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.infinity_polling()