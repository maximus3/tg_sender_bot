import telebot
import config
import argparse
import os

bot = telebot.TeleBot(config.TG_TOKEN)


@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        if not os.path.exists('received'):
            os.mkdir('received')

        src = os.path.join('./received/', message.document.file_name)
        with open(src, 'wb') as file:
            file.write(downloaded_file)

        bot.reply_to(message, "Файл сохранен")
    except Exception as err:
        bot.reply_to(message, str(err))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-f', '--file', type=str, help='File to send')
    parser.add_argument('-r', '--receive', action='store_true')
    args = parser.parse_args()
    if args.receive:
        print('Receiving messages')
        bot.infinity_polling()
    else:
        with open(args.file, 'rb') as f:
            for chat_id in config.SENDER_IDS:
                try:
                    bot.send_document(chat_id, f)
                except Exception as err:
                    print(err)
