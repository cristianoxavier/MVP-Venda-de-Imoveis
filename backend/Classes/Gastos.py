from main import db, ForeignKey


class tb_gastos_imovel(db.Model):
    id_gasto = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    id_imovel = db.Column(db.Integer, ForeignKey('tb_imovel.id_imovel'))
    tipo_gasto = db.Column(db.String)
    valor_gasto = db.Column(db.Integer)

    def __init__(self, id_imovel, tipo_gasto, valor_gasto):
        self.id_imovel = id_imovel
        self.tipo_gasto = tipo_gasto
        self.valor_gasto = valor_gasto