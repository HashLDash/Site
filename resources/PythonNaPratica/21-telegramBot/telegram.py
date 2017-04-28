import telepot

bot = telepot.Bot("TOKEN")

def recebendoMsg(msg):
    print(msg['text'])

bot.message_loop(recebendoMsg)

while True:
    pass
