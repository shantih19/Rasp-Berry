import telepot
import sqlite3
import sys
def sendAll(text, bot, cr):
    cr.execute("SELECT id FROM users;")
    users = cr.fetchall()
    print(users)
    for i in users[0]:
        bot.sendMessage(i, text)
        
def panic(text, bot, cr):
    sendAll(text,bot,cr)
    sys.exit(0)
