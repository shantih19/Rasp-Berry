import subprocess
import sqlite3
import random
import emoji

def parseText(message, status, name, id, db):
    cr = db.cursor()
    if 'ciao' in message or 'hey' in message or 'heila' in message or 'salve' in message:
        if status == 'neutral':
            return random.choice(['Ciao', 'Heila', 'Hey', 'Salve', 'Hola', 'Buonsalve']) + ' ' + name.lower()
        elif status == 'angry':
            return random.choice(['...', 'Cazzo vuoi?'])
    if 'come va?' in message or 'come stai?' in message:
        if status == 'neutral':
            return random.choice(['Bene dai uwu', 'Non male uwu', 'Come sempre uwu'])
        elif status == 'angry':
            return random.choice(['Non sono cazzi tuoi.', 'Che ti frega a te?', 'Non rompere.', '...'])
    if message == 'giada':
        return emoji.emojize(':smiling_face_with_heart-eyes::smiling_face_with_heart-eyes::smiling_face_with_heart-eyes::smiling_face_with_heart-eyes::smiling_face_with_heart-eyes:')
    if message == 'temp':
        return subprocess.check_output(['/opt/vc/bin/vcgencmd', 'measure_temp'])
    if 'che fai' in message or 'cosa fai' in message:
        cr.execute("SELECT count(*) FROM users;")
        users =str(cr.fetchone()[0])
        if status == 'neutral':
            return random.choice(['Chatto con te, ' + name, 'Niente di che uwu', 'Chatto con ' + users + ' utenti uwu']) 
        elif status == 'angry':
            return random.choice(['Che te ne frega a te?', 'Non rompere.', 'Fra tutte le ' + users + ' persone con cui chatto, odio te.'])
    if 'vaffanculo' in message or 'fottiti' in message or 'stronzo' in message or 'crepa' in message or 'ti odio' in message:
        cr.execute("UPDATE users SET status = 'angry' WHERE id = ?;", [id])
        db.commit()
        return random.choice(['Ma vacci te.', '...', 'Ti odio', 'Ma che cazzo vuoi?', 'Ma.'])
    if 'come ti chiami?' in message:
        return 'Berry. Rasp-Berry. Il mio creatore è originale quanto ' + random.choice(['una calza ', 'una marmotta ', 'una marmitta ', 'una barca a vela ']) + random.choice(['ubriaca.', 'morta.', 'in fiamme.' , 'a rotelle'])
    if 'scusa' in message or 'perdonami' in message:
        cr.execute("UPDATE users SET status = 'neutral' WHERE id = ?;" , [id])
        db.commit()
        return random.choice(['Okay uwu', 'Sei perdonato per stavolta', 'Si figuri milord'])
