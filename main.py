from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api, Resource, fields
from sqlalchemy import ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/compra_imoveis'
app.debug = True
appi = Api(app=app, version="1.0", title="Venda de Imoveis",
           description="Sistema MVP para compra e venda de imoveis")
db = SQLAlchemy(app)

# Criaçao dos namespaces & models
nms_cliente = appi.namespace('clientes/v1', description="Operaçoes com clientes")
model_cliente = appi.model('Name Model',
                           {})
nms_proprietario = appi.namespace('proprietarios/v1', description="Operaçoes com proprietarios")
model_proprietario = appi.model('Name Model',
                                {})

nms_imovel = appi.namespace('imoveis/v1', description="Operaçoes com imoveis")
model_imovel = appi.model('Name Model', {'tipo_imovel': fields.String(required=True,
                                                                      help="Tipo do Imovel"),
                                         'endereço': fields.String(required=True,
                                                                   help="Endereço do Imovel"),
                                         'complemento ': fields.String(required=True,
                                                                       help="Complemento do Endereço do Imovel"),
                                         'cep': fields.String(required=True,
                                                              help="Cep da localizaçao do Imovel"),
                                         'uf': fields.String(required=True,
                                                             help="UF do Imovel"),
                                         'id_proprietario': fields.Integer(required=True,
                                                                           help="ID do Proprietario do Imovel"),
                                         'adquirido_em ': fields.String(required=True,
                                                                        help="Quando o imovel foi adquirido"),
                                         'valor_imovel ': fields.String(required=True,
                                                                        help="Valor de Venda do Imovel")})

nms_compra = appi.namespace('compras/v1', description="Operaçoes de compra de imoveis")
model_compra = appi.model('Name Model',
                          {})

nms_banco = appi.namespace('banco/v1', description="Operaçoes com banco")
model_banco = appi.model('Name Model',
                         {})

#criação dos OBJETOS (sao os mesmos do banco de dados)
class tb_proprietario(db.Model):
    id_proprietario = db.Column(db.Integer, primary_key=True, autoincrement=True)
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

class tb_imovel(db.Model):
    id_imovel = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    tipo_imovel = db.Column(db.String)
    endereco = db.Column(db.String)
    complemento = db.Column(db.String)
    cep = db.Column(db.String)
    uf = db.Column(db.String)
    id_proprietario = db.Column(db.Integer, ForeignKey('tb_proprietario.id_proprietario'))
    adquirido_em = db.Column(db.Date)
    valor_imovel = db.Column(db.Integer, unique=True)

    def __init__(self, tipo_imovel, endereco, complemento, cep, uf, id_proprietario, adquirido_em, valor_imovel):
        self.tipo_imovel = tipo_imovel
        self.endereco = endereco
        self.complemento = complemento
        self.cep = cep
        self.uf = uf
        self.id_proprietario = id_proprietario
        self.adquirido_em = adquirido_em
        self.valor_imovel = valor_imovel

class tb_cliente(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    nm_cliente = db.Column(db.String)
    cpf_cliente = db.Column(db.String)
    rg_cliente = db.Column(db.String)
    data_nascimento = db.Column(db.Date)
    estado_civil = db.Column(db.String)
    profissao = db.Column(db.String)

    def __init__(self, nm_cliente, cpf_cliente, rg_cliente, data_nascimento, estado_civil, profissao):
        self.nm_cliente = nm_cliente
        self.cpf_cliente = cpf_cliente
        self.rg_cliente = rg_cliente
        self.data_nascimento = data_nascimento
        self.estado_civil = estado_civil
        self.profissao = profissao

class tb_banco(db.Model):
    id_banco = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    nm_banco = db.Column(db.String)

class tb_compra(db.Model):
    id_compra = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_imovel = db.Column(db.Integer, ForeignKey('tb_imovel.id_imovel'), unique=True)
    id_cliente = db.Column(db.Integer, ForeignKey('tb_cliente.id_cliente'), unique=True)
    tipo_pagamento = db.Column(db.String)
    id_banco = db.Column(db.Integer, ForeignKey('tb_banco.id_banco'), unique=True)
    valor_pagamento = db.Column(db.Integer)

    def __init__(self, id_compra, id_imovel, id_cliente, tipo_pagamento, id_banco, valor_pagamento):
        self.id_compra = id_compra
        self.id_imovel = id_imovel
        self.id_cliente = id_cliente
        self.tipo_pagamento = tipo_pagamento
        self.id_banco = id_banco
        self.valor_pagamento = valor_pagamento


@nms_proprietario.route("/proprietario")
class MainClass(Resource):
    @appi.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    def get(self):
        try:
            # if request.method == 'GET':
            proprietarios = tb_proprietario.query.all()
            prop = []
            for proprietario in proprietarios:
                currProprietario = {}
                currProprietario['id_proprietario'] = proprietario.id_proprietario
                currProprietario['nm_proprietario'] = proprietario.nm_proprietario
                currProprietario['cpf_proprietario'] = proprietario.cpf_proprietario
                currProprietario['rg_proprietario'] = proprietario.rg_proprietario
                currProprietario['data_nascimento'] = proprietario.data_nascimento
                currProprietario['estado_civil'] = proprietario.estado_civil
                currProprietario['profissao'] = proprietario.profissao
                prop.append(currProprietario)
            return jsonify(prop)
        except KeyError as error:
            nms_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nms_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")

    @appi.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    def post(self):
        try:
            proprietarioData = request.get_json()
            proprietario = tb_proprietario(
                nm_proprietario=proprietarioData['nm_proprietario'],
                cpf_proprietario=proprietarioData['cpf_proprietario'],
                rg_proprietario=proprietarioData['rg_proprietario'],
                data_nascimento=proprietarioData['data_nascimento'],
                estado_civil=proprietarioData['estado_civil'],
                profissao=proprietarioData['profissao'])
            db.session.add(proprietario)
            db.session.commit()
            return jsonify(proprietarioData)
        except KeyError as error:
            nms_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nms_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")

@nms_proprietario.route("/proprietario/<int:id_proprietario>")
class MainClass(Resource):
    def delete(self, id_proprietario):
        try:
            proprietario_deletado = tb_proprietario.query.filter(tb_proprietario.id_proprietario==id_proprietario).delete()
            db.session.commit()
            return jsonify(proprietario_deletado)
        except KeyError as error:
            nms_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nms_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")


@nms_imovel.route('/imoveis')
class MainClass(Resource):
    def get(self):
        try:
            imoveis = tb_imovel.query.all()
            imo = []
            for imovel in imoveis:
                currImovel = {}
                currImovel['id_imovel'] = imovel.id_imovel
                currImovel['tipo_imovel'] = imovel.tipo_imovel
                currImovel['endereco'] = imovel.endereco
                currImovel['complemento'] = imovel.complemento
                currImovel['cep'] = imovel.cep
                currImovel['uf'] = imovel.uf
                currImovel['id_proprietario'] = imovel.id_proprietario
                currImovel['adquirido_em'] = imovel.adquirido_em
                currImovel['valor_imovel'] = imovel.valor_imovel
                imo.append(currImovel)
            return jsonify(imo)
        except KeyError as error:
            nms_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nms_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")

    @appi.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, params={'id': 'Specify the Id associated with the person'})

    @appi.expect(model_imovel)
    def post(self):
        imovelData = request.get_json()
        imovel = tb_imovel(
            tipo_imovel=imovelData['tipo_imovel'],
            endereco=imovelData['endereco'],
            complemento=imovelData['complemento'],
            cep=imovelData['cep'],
            uf=imovelData['uf'],
            id_proprietario=imovelData['id_proprietario'],
            adquirido_em=imovelData['adquirido_em'],
            valor_imovel=imovelData['valor_imovel'])
        db.session.add(imovel)
        db.session.commit()
        return jsonify(imovelData)


@nms_cliente.route('/clientes', methods=['GET', 'POST'])
class MainClass(Resource):

    @appi.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    def get(self):
        try:
            clientes = tb_cliente.query.all()
            cli = []
            for cliente in clientes:
                currCliente = {}
                currCliente['id_cliente'] = cliente.id_cliente
                currCliente['nm_cliente'] = cliente.nm_cliente
                currCliente['cpf_cliente'] = cliente.cpf_cliente
                currCliente['rg_cliente'] = cliente.rg_cliente
                currCliente['data_nascimento'] = cliente.data_nascimento
                currCliente['estado_civil'] = cliente.estado_civil
                currCliente['profissao'] = cliente.profissao
                cli.append(currCliente)
            return jsonify(cli)
        except KeyError as error:
            nms_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nms_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")

    def post(self):
        try:
            clienteData = request.get_json()
            cliente = tb_cliente(
                nm_cliente=clienteData['nm_cliente'],
                cpf_cliente=clienteData['cpf_cliente'],
                rg_cliente=clienteData['rg_cliente'],
                data_nascimento=clienteData['data_nascimento'],
                estado_civil=clienteData['estado_civil'],
                profissao=clienteData['profissao'])
            db.session.add(cliente)
            db.session.commit()
            return jsonify(clienteData)
        except KeyError as error:
            nms_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nms_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")


@nms_compra.route('/compra', methods=['GET', 'POST'])
class MainClass(Resource):
    @appi.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    def get(self):
        try:
            compras = tb_compra.query.all()
            comp = []
            for compra in compras:
                currCompra = {}
                currCompra['id_compra'] = compra.id_compra
                currCompra['id_imovel '] = compra.id_imovel
                currCompra['id_cliente '] = compra.id_cliente
                currCompra['tipo_pagamento'] = compra.tipo_pagamento
                currCompra['id_banco'] = compra.id_banco
                currCompra['valor_pagamento'] = compra.valor_pagamento
                comp.append(currCompra)
            return jsonify(comp)
        except KeyError as error:
            nms_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nms_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")
