from Chatbot import Chatbot
import pyttsx

en = pyttsx.init()
en.setProperty('voice',b'brazil')

class BotFalante(Chatbot):
    def fala(self,frase):
        en.say(frase)
        en.runAndWait()
        self.historico.append(frase)

Bot = BotFalante('Felipe')
while True:
    frase = Bot.escuta()
    resp = Bot.pensa(frase)
    Bot.fala(resp)
    if resp == 'tchau':
        break
