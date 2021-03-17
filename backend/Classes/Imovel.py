from main import db, ForeignKey

class tb_imovel(db.Model):
    id_imovel = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    tipo_imovel = db.Column(db.String)
    endereco = db.Column(db.String)
    complemento = db.Column(db.String)
    cep = db.Column(db.String)
    uf = db.Column(db.String)
    id_proprietario = db.Column(db.Integer, ForeignKey('tb_proprietario.id_proprietario'))
    adquirido_em = db.Column(db.Date)
    valor_imovel = db.Column(db.Integer)

    def __init__(self, tipo_imovel, endereco, complemento, cep, uf, id_proprietario, adquirido_em, valor_imovel):
        self.tipo_imovel = tipo_imovel
        self.endereco = endereco
        self.complemento = complemento
        self.cep = cep
        self.uf = uf
        self.id_proprietario = id_proprietario
        self.adquirido_em = adquirido_em
        self.valor_imovel = valor_imovel