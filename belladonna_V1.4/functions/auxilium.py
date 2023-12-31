#!/usr/bin/env python
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from functions.key_sys import LOGGER, ag_key_holder


async def auxilium_func(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if ag_key_holder(update.message.from_user.id, update):
        await update.message.reply_text(
            f'Here is a list of all commands for this toy: @{context.bot.username} \n' \
            '---user_commands--- \n' \
            '/incipio - 💡 winds up the toy. \n' \
            '/auxilium - 🔍 shows this message. \n' \
            '/groups - 🔍 shows list of groups this toy resides in. \n' \
            '---------------------- \n' \
            '- ☽︎ AG_key_commands- \n' \
            '/plus - 💾 adds content to the block_list. \n' \
            '/minus - 🗑 removes a website from the block_list. \n' \
            '/misinfo_list - 📋 shows all blocked websites. \n' \
            '---------------------- \n' \
            '- ☉︎ AU_key_commands- \n' \
            '/observatio_canalium - 🔍 shows list of channels the toy resides within. \n' \
            '/observatio_fororum - 🔍 shows list of groups and corresponding IDs the toy is in. \n' \
            '/observatio_populum - 🔍 shows list of users who are engaging with the toy. \n' \
            '/key_list - 📋 used to see AG key_bearers \n' \
            '/bestow_key - 🔑 used to promote users. \n' \
            '/confiscate_key - 🔐 used to demote users. \n' \
            '/relinquo_forum - 🚫 leaves the group specified ID number. \n' \
            '/terminatio - 🔌 winds down the toy \n' \
            )
    else:
        await update.message.reply_text(
            f'Here is a list of user_commands for this toy: @{context.bot.username} \n' \
            '/auxilium - 🔍 shows user_commands for toy in english. \n' \
            '/groups - 🔍 shows list of groups the toy resides in \n' \
)

auxilium_command = CommandHandler("auxilium", auxilium_func)


