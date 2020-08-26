#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import signal
import sys
import sqlite3
import time
import telepot
import alert
from telepot.loop import MessageLoop
import parser
db = sqlite3.connect('bot.db', check_same_thread = False)
bot=telepot.Bot('')
cr = db.cursor()
alert.sendAll("I'm back uwu", bot, cr)
def handle(msg):
    content_type, chat_type, chat_id, date, message_id = telepot.glance(msg, 'chat', True)
    print(content_type, chat_type, chat_id, date, msg['text'], msg['chat']['first_name'])
    cr.execute("SELECT EXISTS(SELECT 1 FROM users WHERE id= ? LIMIT 1);", [chat_id])
    if cr.fetchone()[0] == 0:
        cr.execute("INSERT INTO users VALUES (?,?,?,'neutral');", [chat_id, msg['chat']['first_name'], date])
        db.commit()
    else:
        cr.execute("UPDATE users SET date = ? WHERE id = ?;",[date, chat_id])
        db.commit()
    cr.execute("SELECT status FROM users WHERE id = ?;", [chat_id])
    status = cr.fetchone()[0]
    if content_type == 'text':
        text = parser.parseText(msg['text'].lower(), status, msg['chat']['first_name'], chat_id, db)
        if text is not None:
            bot.sendMessage(chat_id, text)

 
MessageLoop(bot, handle).run_as_thread()
print("Loaded.")
try:
    while(1):
        time.sleep(10)
except KeyboardInterrupt:
    signal.signal(signal.SIGINT, alert.panic("AIUT MUOIO! x_x", bot, cr))
