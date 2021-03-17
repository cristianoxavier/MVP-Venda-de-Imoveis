from main import db


class tb_banco(db.Model):
    id_banco = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    nm_banco = db.Column(db.String)