from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
from gtts import gTTS

bot= ChatBot('Bot')
#bot.set_trainer(ListTrainer)

trainer= ChatterBotCorpusTrainer(bot)


#for files in os.listdir('/Users/urmikakasi/Desktop/Urmika/securelyshare/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
#    data= open('/Users/urmikakasi/Desktop/Urmika/securelyshare/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files, 'r')
#    trainer.train(data)

trainer.train('chatterbot.corpus.english')

while True:
    #try to do speech to text here
    message= input('You: ')
    reply= bot.get_response(message)
    #print('Bot: ', reply)
    if message.strip()=='bye':
        obj = gTTS(text='good bye!!!', lang='en', slow=False)
        obj.save('test.mp3')
        os.system('mpg321 test.mp3')
        os.remove('test.mp3')
        break

    obj = gTTS(text=str(reply), lang='en', slow=False)
    obj.save('test.mp3')
    os.system('mpg321 test.mp3')
    os.remove('test.mp3')
#    if message.strip() == ('Bye'| 'bye'):
#        print('Bot: Bye!!')
#        break

