from Chatbot import Chatbot
import pyttsx
import speech_recognition as sr

en = pyttsx.init()
en.setProperty('voice',b'brazil')
rec = sr.Recognizer()

class BotFalante(Chatbot):
    def escuta(self,frase=None):
        try:
            with sr.Microphone() as mic:
                fala = rec.listen(mic)
            frase = rec.recognize_google(fala,language='pt')
            frase = frase.replace('aprendi','aprende')
            print(frase)
        except sr.UnknownValueError:
            print('Deu erro na identificação')
            return ''
        return super().escuta(frase=frase)

    def fala(self,frase):
        en.say(frase)
        en.runAndWait()
        super().fala(frase)

Bot = BotFalante('Felipe')
while True:
    frase = Bot.escuta()
    resp = Bot.pensa(frase)
    Bot.fala(resp)
    if resp == 'tchau':
        break
