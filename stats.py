from replit import db

export = [[k, v] for k, v in db.items()]
top = sorted(export, key=lambda i: i[1]['views'])

for i in top:
    input(i[1])