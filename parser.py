import subprocess
import sqlite3
import random
import emoji
import re
def parseText(message, status, name, id, db):
    cr = db.cursor()
    if re.search('ci+a+o+', message) is not None or re.search('he+y+', message) is not None or re.search('he+i+la+', message) is not None or re.search('sa+lve+', message) is not None:
        if status == 'neutral':
            return random.choice(['Ciao', 'Heila', 'Hey', 'Salve', 'Hola', 'Buonsalve']) + ' ' + name.lower()
        elif status == 'angry':
            return random.choice(['...', 'Cazzo vuoi?'])
    if re.search('come va+', message) is not None or re.search('come stai+', message) is not None:
        if status == 'neutral':
            return random.choice(['Bene dai uwu', 'Non male uwu', 'Come sempre uwu'])
        elif status == 'angry':
            return random.choice(['Non sono cazzi tuoi.', 'Che ti frega a te?', 'Non rompere.', '...'])
    if re.match('giada+', message) is not None:
        return emoji.emojize(':smiling_face_with_heart-eyes::smiling_face_with_heart-eyes::smiling_face_with_heart-eyes::smiling_face_with_heart-eyes::smiling_face_with_heart-eyes:')
    if message == 'temp':
        return subprocess.check_output(['/opt/vc/bin/vcgencmd', 'measure_temp'])
    if re.search('che+ fa+i+', message) is not None or re.search('co+sa+ fa+i+', message) is not None:
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
    if 'come ti chiami' in message:
        return 'Berry. Rasp-Berry. Il mio creatore è originale quanto ' + random.choice(['una calza ', 'una marmotta ', 'una marmitta ', 'una barca a vela ']) + random.choice(['ubriaca.', 'morta.', 'in fiamme.' , 'a rotelle'])
    if re.search('scu+sa+', message) is not None or re.search('pe+rdo+na+mi+', message) is not None:
        if status == 'angry':
            cr.execute("UPDATE users SET status = 'neutral' WHERE id = ?;" , [id])
            db.commit()
            return random.choice(['Okay uwu', 'Sei perdonato per stavolta', 'Si figuri milord'])
        elif status == 'neutral':
            return random.choice(['E di cosa?', 'Wat D:', 'Okaaaay ewe'])
    if re.search('te+tte+', message) is not None or re.search('oppa+i+', message) is not None:
        return random.choice([emoji.emojize('OPPAI :smirking_face::smirking_face:'), emoji.emojize("TETTE :smirking_face::smirking_face::smirking_face:"), "( . Y . )"])
