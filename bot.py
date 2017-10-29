import time
import sys
import thread
import paho.mqtt.client as mqtt

global client
import telegram
import logging
from telegram.ext import CommandHandler, CallbackQueryHandler, Updater, Filters, MessageHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = '408131912:AAEkgOLg0uJn2vZEKm4Qb_7Fu-s0fiyDmtk'

bot = telegram.Bot(token=TOKEN)

print(bot.get_me())

################################
################################
###########Thread 1#############
def startMQTTLoop():
	global client
	client.loop_forever()
################################
################################
###########Thread 1#############	

####Start Command####
def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="Welcome")
#####################

#####################
######MQTT Setup#####
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("SenState")
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    bot.sendMessage(chat_id='@OmniBotChannel', text='Proximity Alert')
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("qjetscfh", "0M49osqO3srw")
client.connect("m10.cloudmqtt.com", 12670)
#client.loop_forever()
#Starting thread1
try:
	thread.start_new_thread(startMQTTLoop, ())
except:
	print "Error: unable to start MQTT Thread"
#####################
######MQTT Setup#####


####Error Handler####	
def error(bot, update, error):
    logging.warning('Update "%s" caused error "%s"' % (update, error))
####################
# Create the Updater and pass it your bot's token.
updater = Updater(token=TOKEN)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
dispatcher = updater.dispatcher

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_error_handler(error)

# Start the Bot
updater.start_polling()


# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT
updater.idle()
