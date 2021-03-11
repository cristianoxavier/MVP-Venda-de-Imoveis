from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api, fields, Resource
from sqlalchemy import ForeignKey

app = Flask(__name__)
appi = Api(app=app,
           version="1.0",
           title="Venda de Imoveis",
           description="Sistema MVP para compra e venda de imoveis")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/compra_imoveis'
app.debug = True
db = SQLAlchemy(app)

# criaçao dos namespaces

nms_cliente = appi.namespace('clientes/resources/v1', description="Operaçoes com clientes")
nms_proprietario = appi.namespace('proprietarios/resources/v1', description="Operaçoes com proprietarios")
nms_imovel = appi.namespace('imoveis/resources/v1', description="Operaçoes com imoveis")
nms_compra = appi.namespace('compras/resources/v1', description="Operaçoes de compra de imoveis")


class tb_proprietario(db.Model):
    id_proprietario = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    nm_proprietario = db.Column(db.String, unique=True)
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

model_proprietario = appi.model('Modelo Proprietario', {
    'nm_proprietario': fields.String(required=True,
                                     description='Insira o nome do Proprietario',
                                     help='Ex: Miguel da Silva'),
    'cpf_proprietario': fields.String(required=True,
                                      description='Insira o Cpf do proprietario',
                                      help='Ex: 12323434556'),
    'rg_proprietario': fields.String(required=True,
                                     description='Insira o rg do proprietario',
                                     help='Ex: 127658906'),
    'data_nascimento': fields.String(required=True,
                                     description='Insira a Data de nascimento do proprietario',
                                     help='04/11/1998'),
    'estado_civil': fields.String(required=True,
                                  description='Insira o Estado Civil do proprietario',
                                  help='Ex: Solteiro, Casado, Viuvo'),
    'profissao': fields.String(required=True,
                               description='Insira a Profissao do proprietario',
                               help='Ex: Padeiro, Contador, Policial...')
})


class tb_imovel(db.Model):
    id_imovel = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    tipo_imovel = db.Column(db.String)
    endereco_imovel = db.Column(db.String)
    cep = db.Column(db.String)
    uf = db.Column(db.String)
    id_proprietario = db.Column(db.Integer, ForeignKey('tb_proprietario.id_proprietario'), unique=True)
    nm_proprietario = db.Column(db.String, ForeignKey('tb_proprietario.nm_proprietario'), unique=True)
    adquirido_em = db.Column(db.Date)
    valor_imovel = db.Column(db.Integer, unique=True)
    status = db.Column(db.Boolean)

    def __init__(self, tipo_imovel, endereco_imovel, cep, uf, id_proprietario, nm_proprietario, adquirido_em,
                 valor_imovel, status):
        self.tipo_imovel = tipo_imovel
        self.endereco_imovel = endereco_imovel
        self.cep = cep
        self.uf = uf
        self.id_proprietario = id_proprietario
        self.nm_proprietario = nm_proprietario
        self.adquirido_em = adquirido_em
        self.valor_imovel = valor_imovel
        self.status = status


class tb_cliente(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    nm_cliente = db.Column(db.String)
    cpf_cliente = db.Column(db.String)
    rg_cliente = db.Column(db.String)
    data_nascimento = db.Column(db.Date)
    estado_civil = db.Column(db.String)
    profissao = db.Column(db.String)
    endereco = db.Column(db.String)
    uf = db.Column(db.String)

    def __init__(self, nm_cliente, cpf_cliente, rg_cliente, data_nascimento, estado_civil, profissao, endereco, uf):
        self.nm_cliente = nm_cliente
        self.cpf_cliente = cpf_cliente
        self.rg_cliente = rg_cliente
        self.data_nascimento = data_nascimento
        self.estado_civil = estado_civil
        self.profissao = profissao
        self.endereco = endereco
        self.uf = uf


class tb_compra(db.Model):
    id_compra = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_imovel = db.Column(db.Integer, ForeignKey('tb_imovel.id_imovel'), unique=True)
    id_cliente = db.Column(db.Integer, ForeignKey('tb_cliente.id_cliente'), unique=True)
    valor_imovel = db.Column(db.Integer, ForeignKey('tb_imovel.valor_imovel'), unique=True)
    tipo_de_compra = db.Column(db.String)

    def __init__(self, id_compra, id_imovel, valor_imovel, tipo_de_compra):
        self.id_compra = id_compra
        self.id_imovel = id_imovel
        self.valor_imovel = valor_imovel
        self.tipo_de_compra = tipo_de_compra


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

    @appi.expect(model_proprietario)
    def post(self):
        # elif request.method == 'POST':
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


@app.route('/imoveis', methods=['GET', 'POST'])
def imovel():
    if request.method == 'GET':
        imoveis = tb_imovel.query.all()
        imo = []
        for imovel in imoveis:
            currImovel = {}
            currImovel['id_imovel'] = imovel.id_imovel
            currImovel['tipo_imovel'] = imovel.tipo_imovel
            currImovel['endereco_imovel'] = imovel.endereco_imovel
            currImovel['cep'] = imovel.cep
            currImovel['uf'] = imovel.uf
            currImovel['id_proprietario'] = imovel.id_proprietario
            currImovel['nm_proprietario'] = imovel.nm_proprietario
            currImovel['uf'] = imovel.uf,
            currImovel['adquirido_em'] = imovel.adquirido_em,
            currImovel['valor_imovel'] = imovel.valor_imovel,
            currImovel['status'] = imovel.status
            imo.append(currImovel)
        return jsonify(imo)
    """elif request.method == 'POST':
        imovelData = request.get_json()
        imovel = tb_imovel(
            tipo_imovel=imovelData['tipo_imovel'],
            endereco_imovel=imovelData['endereco_imovel'],
            cep=imovelData['cep'],
            uf=imovelData['uf'],
            id_proprietario= imovelData['id_proprietario'],
            nm_proprietario= imovelData['nm_proprietario'],
            adquirido_em=imovelData['adquirido_em'],
            valor_imovel=imovelData['valor_imovel'],
            status = imovelData['status'])
        db.session.add(imovel)
        db.session.commit()
        return jsonify(imovelData)"""


@app.route('/clientes', methods=['GET', 'POST'])
def cliente():
    if request.method == 'GET':
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
            currCliente['endereco'] = cliente.endereco
            currCliente['uf'] = cliente.uf
            cli.append(currCliente)
        return jsonify(cli)
    elif request.method == 'POST':
        clienteData = request.get_json()
        cliente = tb_cliente(
            nm_cliente=clienteData['nm_cliente'],
            cpf_cliente=clienteData['cpf_cliente'],
            rg_cliente=clienteData['rg_cliente'],
            data_nascimento=clienteData['data_nascimento'],
            estado_civil=clienteData['estado_civil'],
            profissao=clienteData['profissao'],
            endereco=clienteData['endereco'],
            uf=clienteData['uf'])
        db.session.add(cliente)
        db.session.commit()
        return jsonify(clienteData)
