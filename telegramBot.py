import logging,time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    update.message.reply_text('Halo!\n')
    time.sleep(0.5)
    update.message.reply_text('Nama saya Cahyo\n')
    update.message.reply_text('Anda sedang menggunakan bot buatan Cahyo!\n'
                              'Untuk saat ini hanya ada sedikit command yang bisa anda gunakan dalam bot ini\n'
                              'Untuk melihat daftar command, silakan gunakan /help')

def help(update, context):
    update.message.reply_text('Berikut adalah daftar command yang bisa anda gunakan : \n\n'
                              '/help - memunculkan bantuan\n'
                              '/contact - melihat contact\n'
                              '/start - memulai percakapan\n\n'
                              'Anda juga bisa berbicara dengan diri sendiri\n'
                              'tinggal ketik yang anda mau maka saya akan mengulang percakapan anda!')


def contact(update, context):
    update.message.reply_text('Hallo saya adalah bot telegram buatan Cahyo\n'
                              'Berikut adalah kontak yang bisa anda hubungi \n\n'
                              'Github : https://github.com/cnugroho11 \n'
                              'Instagram : https://www.instagram.com/cnugroho \n'
                              'Email : cnugroho211@gmail.com')

def echo(update, context):
    update.message.reply_text(update.message.text)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    #silakan gunakan token bot telegram
    updater = Updater("TOKEN", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("contact", contact))

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
