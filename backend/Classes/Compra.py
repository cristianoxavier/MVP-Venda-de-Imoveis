from main import db, ForeignKey


class tb_compra(db.Model):
    id_compra = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_imovel = db.Column(db.Integer, ForeignKey('tb_imovel.id_imovel'), unique=True)
    id_cliente = db.Column(db.Integer, ForeignKey('tb_cliente.id_cliente'))
    tipo_pagamento = db.Column(db.String)
    id_banco = db.Column(db.Integer, ForeignKey('tb_banco.id_banco'))
    valor_pagamento = db.Column(db.Integer)

    def __init__(self, id_imovel, id_cliente, tipo_pagamento, id_banco, valor_pagamento):
        self.id_imovel = id_imovel
        self.id_cliente = id_cliente
        self.tipo_pagamento = tipo_pagamento
        self.id_banco = id_banco
        self.valor_pagamento = valor_pagamento