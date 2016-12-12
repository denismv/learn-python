from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
       
def greet_user(bot, update):
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')

def wordcount(bot, update):
    print(update.message.text)
    #params="Привет как дела"
    params=update.message.text.replace('/wordcount ','')
    print(params)
    params_split=params.split(' ')
    print(params_split)
    words_num=len(params_split)
#    print('Found', words_num, 'words')
    print('Found {} words'.format(words_num))
    bot.sendMessage(update.message.chat_id, text=words_num)

def calc(bot, update):
    params=update.message.text.replace('/calc ','')
    params=params.replace('=','')
#    print(params)
    if '-' in params:
        params_split=params.split('-')
        result=int(params_split[0])-int(params_split[1])
        print (result)
    elif '+' in params:
        params_split=params.split('+')
        result=int(params_split[0])+int(params_split[1])
        print (result)
    elif '*' in params:
        params_split=params.split('*')
        result=int(params_split[0])*int(params_split[1])
        print (result)
    elif '/' in params:
        params_split=params.split('/')
        result=int(params_split[0])/int(params_split[1])
        print (result)
    bot.sendMessage(update.message.chat_id, text=result)

def show_error(bot, update, error):
    print('Update "{}" caused error "{}"'.format(update, error))

def talk_to_me(bot, update):
    print('Пришло сообщение: {}'.format(update.message.text))
#    bot.sendMessage(update.message.chat_id, update.message.text)
#    print(update.message.message_id) # https://core.telegram.org/bots/api#message

def main():
    updater = Updater("245495281:AAEXR8mhSrtYfJJKT_GsS0g96pgH0bncS24")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    dp.add_handler(CommandHandler("calc", calc))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_error_handler(show_error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

