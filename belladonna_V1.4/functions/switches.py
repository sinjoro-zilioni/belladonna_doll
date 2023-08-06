#!/usr/bin/env python

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from keys import locked_out_reply
from keys import LOG_CHANNEL, locked_out_reply
from functions.indicator import LOGGER
from functions.key_sys import au_key_holder


async def incipio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'💡 winding up  @{context.bot.username}')


async def relinquo_forum(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if au_key_holder(update.message.from_user.id, update) and len(context.args) == 1:
        chat_id = context.args[0]
        try:
            chat_id = int(context.args[0])
            await update.message.reply_text(f'successfully left the group with ID: {chat_id}')
            await context.bot.leave_chat(chat_id)
        except:
            await update.message.reply_text(f'Could not leave {chat_id}')
    else:
        await update.message.reply_text(
        f"You must bear the tao key and also specify the chat id as follows: /command -00000001"
    )

async def check_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if au_key_holder(update.message.from_user.id, update) and len(context.args) == 1:
        user_id = int(context.args[0])
        id = update.message.from_user.id
        user = update.message.from_user.username
        name = update.message.from_user.full_name
        try:
            await update.message.reply_text(f'ID: {user_id}, username: @{user} , name: {name}')
        except:
            await update.message.reply_text(f'Could not get details for ID: {user_id}')
    else:
        await update.message.reply_text(
        f"You must bear the AU key and also specify the user id as follows: /command 00000001"
    )

async def terminatio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if au_key_holder(update.message.from_user.id, update):
        await update.message.reply_text(f'🔌 Winding down @{context.bot.username}')
        exit()
    else:
        await update.message.reply_text(locked_out_reply)


incipio_command = CommandHandler("incipio", incipio)
check_id_command = CommandHandler("check_id", check_id)
relinquo_command = CommandHandler("relinquo_forum", relinquo_forum)
terminatio_command = CommandHandler("terminatio", terminatio)
