#!/usr/bin/env python
import time

from typing import Optional, Tuple, List

from telegram import Update, Message, Chat, ChatMember, ChatMemberUpdated, ForceReply, ChatMember,  Bot, User, MessageEntity
from telegram.ext import Application, ChatMemberHandler, CommandHandler, MessageHandler, filters
from keys import clavis_ii
from functions.indicator import LOGGER
from functions import auxilium, group_sys, key_sys, misinfo_blocker, indicator, switches


def main() -> None:
    time.sleep(30)
    application = Application.builder().token(clavis_ii).build()
    application.add_handler(misinfo_blocker.misinfo_index_command)
    application.add_handler(misinfo_blocker.adaugeo_command)
    application.add_handler(misinfo_blocker.expungo_command)
    application.add_handler(auxilium.auxilium_command)
    application.add_handler(switches.incipio_command)
    application.add_handler(switches.relinquo_command)
    application.add_handler(switches.check_id_command)
    application.add_handler(switches.terminatio_command)
    application.add_error_handler(indicator.error_handler)
    application.add_handler(ChatMemberHandler(group_sys.track_chats, ChatMemberHandler.MY_CHAT_MEMBER))
    application.add_handler(key_sys.bestow_key_command)
    application.add_handler(key_sys.confiscate_key_command)
    application.add_handler(key_sys.key_list_command)
    application.add_handler(group_sys.group_list_command)
    application.add_handler(group_sys.groups_command)
    application.add_handler(group_sys.users_command)
    application.add_handler(group_sys.channels_command)
    application.add_handler(MessageHandler(filters.TEXT, misinfo_blocker.scanner, group_sys.private_chat))
    application.run_polling()

if __name__ == '__main__':
    main()