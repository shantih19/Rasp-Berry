import telepot
import sqlite3
import sys
def sendAll(text, bot, cr):
    cr.execute("SELECT id FROM users where id = 129434903;")
    users = cr.fetchall()
    print(users)
    for i in users:
        bot.sendMessage(users[users.index(i)][0], text)
        
def panic(text, bot, cr):
    sendAll(text,bot,cr)
    sys.exit(0)
