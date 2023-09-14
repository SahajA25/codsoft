

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot= ChatBot(name='AI')
trainer = ListTrainer(bot)

trainer.train(['hi',
               'hello',
               'how r u?',
               'fine',
               'wats ur name?',
               'im AIchat bot'])

while True:
   request=input('you :')
   if request == 'OK' or request == 'ok':
        print('AI Bot: bye')
        break
   else:
        response=bot.get_response(request)
        print('AI Bot:',response)
