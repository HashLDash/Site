import json
import subprocess as s

try:
    FileNotFoundError
except NameError:
    import sys
    if sys.version_info < (3, 0):
        reload(sys)
        sys.setdefaultencoding('utf-8')
    FileNotFoundError = IOError

class Chatbot():
    def __init__(self, nome):
        try:
            memoria = open(nome+'.json','r')
        except FileNotFoundError:
            with open(nome+'.json','w') as memoria:
                memoria.write('[["Will","Alfredo"],{"hi": "Hello, what is your name?","bye":"Bye bye!"}]')
            memoria = open(nome+'.json','r')
        self.nome = nome
        self.conhecidos, self.frases = json.load(memoria)
        memoria.close()
        self.historico = [None,]

    def escuta(self,frase=None):
        if frase == None:
            frase = input('>: ')
        frase = str(frase)
        if 'execute ' in frase:
            return frase
        frase = frase.lower()
        frase = frase.replace('é','eh')
        return frase

    def pensa(self,frase):
        if frase in self.frases:
            return self.frases[frase]
        if frase == 'learn':
            return 'Tell the phrase: '

        # Responde frases que dependem do historico
        ultimaFrase = self.historico[-1]
        if ultimaFrase == 'Hello, what is your name?':
            nome = self.pegaNome(frase)
            frase = self.respondeNome(nome)
            return frase
        if ultimaFrase == 'Tell the phrase: ':
            self.chave = frase
            return 'Tell the answer: '
        if ultimaFrase == 'Tell the answer: ':
            resp = frase
            self.frases[self.chave] = resp
            self.gravaMemoria()
            return 'Got it!'
        try:
            resp = str(eval(frase))
            return resp
        except:
            pass
        return 'I did not understand'
            
    def pegaNome(self,nome):
        if 'my name is ' in nome:
            nome = nome[14:]

        nome = nome.title()
        return nome

    def respondeNome(self,nome):
        if nome in self.conhecidos:
            frase = 'Yow '
        else:
            frase = 'Nice to meet you '
            self.conhecidos.append(nome)
            self.gravaMemoria()
        return frase+nome

    def gravaMemoria(self):
        memoria = open(self.nome+'.json','w')
        json.dump([self.conhecidos,self.frases],memoria)
        memoria.close()

    def fala(self,frase):
        if 'execute ' in frase:
            comando = frase.replace('execute ','')
            try:
                s.Popen(comando.lower())
            except FileNotFoundError:
                s.Popen(['xdg-open',comando])
        else:
            print(frase)
        self.historico.append(frase)
