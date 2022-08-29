from telegram.ext import Updater, CallbackContext, CallbackQueryHandler, CommandHandler
from telegram import Update
import telegram,os,json

class Like_click:
    def __init__(self):
        self.TOKEN = os.environ["TOKEN"]
        self.updater = Updater(self.TOKEN)
        self.bot = telegram.Bot(self.TOKEN)

    def start(self,update: Update, context: CallbackContext):
        data = self.jsonLoad()
        user_id = update.message.from_user.id

        like = 0
        liked = 0
        for k,v in data.items():
            if v == '👍':
                like += 1
            if v == '👎':
                liked += 1

        self.bot.sendMessage(user_id, 'Welcome to our bot!!!')
        self.bot.sendPhoto(user_id,'AgACAgQAAxkBAAIDRWMKwetyB1780z7pgiXRE6S2r4bFAAJrqDEbJY5tUKddARBW8l0kAQADAgADcwADKQQ')
        text = 'Feel free to click like, don   t think not to like'
        inlineKeyboard = telegram.InlineKeyboardButton(f'👎{liked}',callback_data='👎')
        inlineKeyboard1 = telegram.InlineKeyboardButton(f'👍{like}',callback_data='👍')
        reply_markup = telegram.InlineKeyboardMarkup([[inlineKeyboard,inlineKeyboard1]])
        update.message.reply_text(text, reply_markup=reply_markup)

    def jsonDump(self,data):
        with open('bot/json.json', 'w') as f:
            json.dump(data, f, indent=2)

    def jsonLoad(self):
        with open('bot/json.json', 'r') as f:
            data = json.load(f)
        return  data

    def getQuery(self,update: Update, context: CallbackContext):
        query = update.callback_query
        query.answer('Like', show_alert=False)
        text = query.data
        id = query.from_user.id

        data = self.jsonLoad()
        data[id] = text
        self.jsonDump(data)
        data = self.jsonLoad()
        like = 0
        liked = 0
        for k,v in data.items():
            if v == '👍':
                like += 1
            if v == '👎':
                liked += 1

        text = 'Feel free to click like, don   t think not to like'
        inlineKeyboard = telegram.InlineKeyboardButton(f'👎{liked}',callback_data='👎')
        inlineKeyboard1 = telegram.InlineKeyboardButton(f'👍{like}',callback_data='👍')
        reply_markup = telegram.InlineKeyboardMarkup([[inlineKeyboard,inlineKeyboard1]])
        query.edit_message_text(text, reply_markup=reply_markup)

like = Like_click()
like.updater.dispatcher.add_handler(CommandHandler('start',like.start))
like.updater.dispatcher.add_handler(CallbackQueryHandler(like.getQuery))
like.updater.start_polling()
like.updater.idle()