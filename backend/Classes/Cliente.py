from main import db


class tb_cliente(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    nm_cliente = db.Column(db.String)
    cpf_cliente = db.Column(db.String)
    rg_cliente = db.Column(db.String)
    endereco = db.Column(db.String)
    cep = db.Column(db.String)
    uf = db.Column(db.String)
    data_nascimento = db.Column(db.Date)
    estado_civil = db.Column(db.String)
    profissao = db.Column(db.String)

    def __init__(self, nm_cliente, cpf_cliente, rg_cliente, endereco, cep, uf, data_nascimento, estado_civil,
                 profissao):
        self.nm_cliente = nm_cliente
        self.cpf_cliente = cpf_cliente
        self.rg_cliente = rg_cliente
        self.endereco = endereco
        self.cep = cep
        self.uf = uf
        self.data_nascimento = data_nascimento
        self.estado_civil = estado_civil
        self.profissao = profissao