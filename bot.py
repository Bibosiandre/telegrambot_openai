import telebot
from telebot import types
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai
import os


bot_token = 'Токен бота телеграма(YOUR_TOKEN)'
updater = Updater(token=bot_token, use_context=True)
bot = telebot.TeleBot(token=bot_token)
openai.api_key = 'Токен OpenAI(YOUR_TOKEN)'


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Пишите запрос ChatGPT на английском!")


def echo(update, context):

    user_message = update.message.text


    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_message,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )


    context.bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)


start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(echo_handler)


updater.start_polling()
updater.idle()