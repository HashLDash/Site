import telepot
from Chatbot import Chatbot

telegram = telepot.Bot("378167546:AAGCfaDvlj9HY6qstSEKm4uL6qn_oOII4Is")

bot = Chatbot("HashLDash")

def recebendoMsg(msg):
    frase = bot.escuta(frase=msg['text'])
    resp = bot.pensa(frase)
    bot.fala(resp)
    #chatID = msg['chat']['id']
    tipoMsg, tipoChat, chatID = telepot.glance(msg)
    telegram.sendMessage(chatID,resp)

telegram.message_loop(recebendoMsg)

while True:
    pass
