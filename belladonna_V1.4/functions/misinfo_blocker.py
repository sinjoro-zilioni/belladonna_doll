#!/usr/bin/env python
import datetime
import importlib
import re
import random
import logging
import os
import sys
from typing import Optional, Tuple, List

from telegram import Update, ForceReply
from telegram.ext import CommandHandler, ContextTypes
from keys import locked_out_reply
from functions.indicator import LOGGER
from functions.key_sys import  ag_key_holder


string_list = [
"{}, if you're getting your info from sites like:{} I find the fact that you’ve lived this long both surprising and disappointing.",
"{} You’ll become a real conversation starter sharing sites like {}, Not when you're around of course, but only after you leave.",
"{} I’m really glad that you’re stringing words into sentences now. You just need to find better sites to read than {}",
"{} I have seen people like you before, I had to buy a ticket to go in though. stop sharing this freakshow site! {}",
"{}, posting stuff like this: {} displays your massive sense of entitlement that people will just believe it. ",
"{}  I forgot the world revolves around you. My apologies, how silly of me. Carry on sharing nonsense like: {}",
"{} You'll make everyone so happy... You know, when you leave the group! Stop posting websites such as {}!",
"{} If ignorance is bliss, you must be the happiest person on the planet. Because {} is full of ignorance",
"{}, citing: {} Somewhere out there is a tree tirelessly producing oxygen for you. You owe it an apology.",
"{}, People like you are the reason the gods don't talk to us anymore - why post rubbish from {} ???",
"{} I’m glad to see you’re not letting education get in the way of your ignorance by citing this: {}",
"{}, Don't feel too bad about posting: {}, Brains aren’t everything. In your case, they’re nothing.",
"{}, citing this: {} I’m glad to see you’re not letting education get in the way of your ignorance.",
"{} The people who tolerate your citing nonsense like {} on the daily deserve medals for patience.",
"{} - posting this? {} - You should carry a plant around with you to replace the oxygen you waste.",
"{}, {}, seriously??? I don’t know what your problem is, but I’m guessing it’s hard to pronounce.",
"Hey genius! {}, posting from {} ??? If genius skips a generation, your children will brilliant.",
"{}, You think {} contains good information? Please don't tell me you home-school your children.",
"{}, if you prize the information in : {} - You would do well to take the time to read a book.",
"{} Do you think people are stupid enough to believe sources of misinformation like this: {}?",
"{}, People like you, who post nonsense like {} are the reason why shampoo has instructions.",
"{}, citing this: {} I bet your parents change the subject when their friends ask about you.",
"{} I deleted your post of this site: {} I could restore it... but where's the fun in that?",
"{} - {} this, really? Were you born on a motorway. That’s where lots of accidents happen. ",
"{} I don’t have any crayons to to explain to you why this site {} contains misinformation",
"{} This nonsense:{} ??? I could agree with that site too, but then I would be an idiot.",
"{}, did you skip your medication today? Evidently if you're posting such sites as: {}",
"{}, posting: {} ... *sigh* You'll bring everyone so much joy if you leave the group.",
"{}, posting this? {} You have an entire life to be an idiot. Why not take today off?",
"{}, citing {}?? How much of a refund do you expect on your head, since it’s empty?",
"{} People clap when they see this site: {} They clap their hands over their eyes.",
"{} - {}, seriously? You’re living proof it’s possible to survive without a brain.", 
"{} I could eat an encyclopedia and poo out something smarter than this site: {}",
"{} citing {}, you need to get a life instead of reading this crap all the time.",
"{} I thought of this website today: {} It reminded me to take out the rubbish.",
"{} You do realise this site: {} is a dubious source of information don't you?",
"{}, posting this: {} Your only purpose in life is to become an organ donor.",
"Hey bone-head! {} Yeah you! 🫵 Why did you share nonsense from this site? {}",
"{} if ignorance is bliss, you must be in zen, because you posted this {}",
"{} citing: {} Brains aren’t everything. In your case, they’re nothing.",
"{} with citing this {} You're proving that evolution can go backwards.",
"{} This site {} is stuffed full of so much crap, toilets are jealous.",
"{}, Life is full of disappointments and I just added {} to the list.",
"{}, Stop stinking up the group with rubbish from this website: {} !!",
"{} Zombies only eat brains, I know you're safe because you cited: {}",
"🫵 You!! {} that toxic site needs warning label, so I added one: {}",
"{}, {} wow... As an outsider, what do you think of the human race?",
"{}, {}??? If I had a brain like yours, I would sue my parents.",
"{} Sharing sites like {} You're lucky stupidity isn’t a crime.",
"{} This site? {} In the land of the brainless, you'd be king.",
"{}, {} Somewhere, you are robbing a village of their idiot.",
"{}, {}?? You’re the reason the gene pool needs a lifeguard.",
"{} posting this: {} proves the gods have a sense of humour",
"{}, posting: {} ... If I throw a stick, will you leave?",
"{} IGNORAMUS MAXIMUS! Why share a foolish site like {}?",
"{} Posting sites like; {}  is tantamount to littering.",
"{}, {} ?? Did your owner let you off the leesh today?",
"{}, {}??? What doesn’t kill you, disappoints me.",
"{} 🫵 YOU!! Why post dross like this? {}",
"{} Why share garbage like this? {}",
]

blocklist_persist  = 'misinfo_list.txt'

if not os.path.exists(blocklist_persist):
    open(blocklist_persist, 'w').close()

block_list = [line.rstrip() for line in open(blocklist_persist)]


def persist_update():
    blocklist_file = open(blocklist_persist, 'w')
    block_list_formatted = map(lambda x: x + '\r', block_list)
    blocklist_file.writelines(block_list_formatted)
    blocklist_file.close()

async def incipio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"💡 Winding up toy...  {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def misinfo_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if ag_key_holder(update.message.from_user.id, update):

        gear_train = []

        for trigger in range(0, len(block_list), 100):
            gear_train.append(block_list[trigger:trigger + 100])

        for gear in gear_train:
            await update.message.reply_text(str(gear))

    else:
        await update.message.reply_text(locked_out_reply)


async def plus(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if ag_key_holder(update.message.from_user.id, update):
        block_list.append(context.args[0])
        persist_update()
        await update.message.reply_text('additae {} ad criteria'.format(context.args[0]))
    else:
        await update.message.reply_text(locked_out_reply)

async def minus(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if ag_key_holder(update.message.from_user.id, update):
        block_list.remove(context.args[0])
        persist_update()
        await update.message.reply_text('detractus {} ex criteria'.format(context.args[0]))
    else:
        await update.message.reply_text(locked_out_reply)


async def scanner(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    html_text = update.message.text_html.casefold()
    regulator = [trigger for trigger in block_list if trigger in html_text]
    user = update.message.from_user.username
    if any(regulator):
        LOGGER.info("%s trigger from blocklist detected!", regulator)
        random_string = random.choice(string_list)
        await update.message.reply_text(random_string.format(user, regulator[0].rsplit('.',1)[0]))
        try:
            await update.message.delete()
        except:
            await update.message.reply_text('Unable to eliminate this user! Has this automaton been granted admin privilege?')
    else:
        pass


misinfo_index_command = CommandHandler("misinfo_list", misinfo_list)
adaugeo_command = CommandHandler("plus", plus)
expungo_command = CommandHandler("minus", minus)


