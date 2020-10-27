import logging,time, requests, json, random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from urllib import request

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

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
                              '/joke - random joke\n'
                              '/start - memulai percakapan\n\n'
                              'Anda bisa mengetahui cuaca hari ini menggunankan perintah cuaca <kota>\n\n'
                              'Untuk saat ini fitur bot ini masih terbatas. Silakan menuju /contact untuk memberi kritik dan saran')


def contact(update, context):
    update.message.reply_text('Hallo saya adalah bot telegram buatan Cahyo\n'
                              'Berikut adalah kontak yang bisa anda hubungi \n\n'
                              'Github : https://github.com/cnugroho11 \n'
                              'Instagram : https://www.instagram.com/cnugroho_ \n'
                              'Telegram : https://t.me/cnugroho \n'
                              'Email : cnugroho211@gmail.com')

def joke(update, context):
    url = "https://official-joke-api.appspot.com/random_joke"
    response = request.urlopen(url)
    data = json.loads(response.read())
    update.message.reply_text('This is joke for you')
    update.message.reply_text(f"{data['setup']}")
    update.message.reply_text(f"{data['punchline']}")

def number(update, context):
    nmb = random.randint(0, 100)
    url = "http://numbersapi.com/"+str(nmb)
    response = request.urlopen(url)
    data = response.read().decode('utf-8')

    update.message.reply_text('This is fact about number '+str(nmb))
    update.message.reply_text(f"{data}")

def echo(update, context):
    get_city = update.message.text
    if "cuaca" in get_city or "Cuaca" in get_city:
        api_key = "OPEN WEATHER API"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = get_city[6:len(get_city)]
        update.message.reply_text('Mohon tunggu sebentar fitur ini masih dalam tahap BETA')
        print(city_name)
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]

            update.message.reply_text('Laporan cuaca di ' + city_name + ' adalah : \n\n'
                                      'Temperatur (kelvin) = ' + str(current_temperature) + '\n'
                                      'Tekanan atmosfer (hPa unit) = ' + str(current_pressure) + '\n'
                                      'Kelembapan (presentase) = ' + str(current_humidity) + '\n'
                                      'Deskripsi = ' + str(weather_description) + '\n\n'
                                      'Untuk saat ini bot ini masih dalam tahap pengembangan\n'
                                      'Silakan menuju /contact untuk memberi kritik & saran')
        else:
            update.message.reply_text('Maaf kota ' + city_name + ' tidak ditemukan')
    else:
        update.message.reply_text("Maaf cahyo tidak mengerti kata "+update.message.text+" silakan menuju /help untuk bantuan")

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater("TELEGRAM API", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("contact", contact))
    dp.add_handler(CommandHandler("joke", joke))
    dp.add_handler(CommandHandler("number", number))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
