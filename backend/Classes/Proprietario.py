from main import db

class tb_proprietario(db.Model):
    id_proprietario = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    nm_proprietario = db.Column(db.String)
    cpf_proprietario = db.Column(db.String)
    rg_proprietario = db.Column(db.String)
    data_nascimento = db.Column(db.Date)
    estado_civil = db.Column(db.String)
    profissao = db.Column(db.String)

    def __init__(self, nm_proprietario, cpf_proprietario, rg_proprietario, data_nascimento, estado_civil, profissao):
        self.nm_proprietario = nm_proprietario
        self.cpf_proprietario = cpf_proprietario
        self.rg_proprietario = rg_proprietario
        self.data_nascimento = data_nascimento
        self.estado_civil = estado_civil
        self.profissao = profissao