from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_restplus import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/compra_imoveis'
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app=app, methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'], resources={r"*"})

appi = Api(app=app, version="1.0", title="Venda de Imoveis",
           description="Sistema MVP para compra e venda de imoveis")
db = SQLAlchemy(app)

from Classes.Proprietario import tb_proprietario
from Classes.Imovel import tb_imovel
from Classes.Cliente import tb_cliente
from Classes.Banco import tb_banco
from Classes.Gastos import tb_gastos_imovel
from Classes.Compra import tb_compra
from Models.Models import *

db.create_all()


# METHOD'S POST, GET, PUT E DELETE - Cliente
@nms_cliente.route('/clientes')
class ClienteClass(Resource):

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
                currCliente['endereco'] = cliente.endereco
                currCliente['cep'] = cliente.cep
                currCliente['uf'] = cliente.uf
                currCliente['data_nascimento'] = cliente.data_nascimento
                currCliente['estado_civil'] = cliente.estado_civil
                currCliente['profissao'] = cliente.profissao
                cli.append(currCliente)
            return jsonify(cli)
        except KeyError as error:
            nms_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nms_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")

    @appi.expect(model_cliente)
    def post(self):
        try:
            clienteData = request.get_json()
            cliente = tb_cliente(
                nm_cliente=clienteData['nm_cliente'],
                cpf_cliente=clienteData['cpf_cliente'],
                rg_cliente=clienteData['rg_cliente'],
                endereco=clienteData['endereco'],
                cep=clienteData['cep'],
                uf=clienteData['uf'],
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


@nms_cliente.route('/clientes/<int:id_cliente>')
class ClienteClass(Resource):
    def get(self, id_cliente):
        try:
            clientes = tb_cliente.query.filter(tb_cliente.id_cliente == id_cliente)
            saida = []
            for cliente in clientes:
                dados_cliente = {}
                dados_cliente['id_cliente'] = cliente.id_cliente
                dados_cliente['nm_cliente'] = cliente.nm_cliente
                dados_cliente['cpf_cliente'] = cliente.cpf_cliente
                dados_cliente['rg_cliente'] = cliente.rg_cliente
                dados_cliente['endereco'] = cliente.endereco
                dados_cliente['cep'] = cliente.cep
                dados_cliente['uf'] = cliente.uf
                dados_cliente['data_nascimento'] = cliente.data_nascimento
                dados_cliente['estado_civil'] = cliente.estado_civil
                dados_cliente['profissao'] = cliente.profissao
                saida.append(dados_cliente)
            return jsonify(saida)
        except KeyError as error:
            nms_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nms_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")

    def delete(self, id_cliente):
        try:
            cliente_deletado = tb_cliente.query.filter(
                tb_cliente.id_cliente == id_cliente).delete()
            db.session.commit()
            return jsonify(cliente_deletado)
        except KeyError as error:
            nms_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nms_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")


@nms_cliente.route('/clientes/<int:id>')
class ClienteClass(Resource):
    @appi.expect(model_put_cliente)
    def put(self, id):
        try:
            cliente_put = tb_cliente.query.get(id)
            cliente_put.nm_cliente = request.json.get('nm_cliente', cliente_put.nm_cliente)
            cliente_put.cpf_cliente = request.json.get('cpf_cliente', cliente_put.cpf_cliente)
            cliente_put.rg_cliente = request.json.get('rg_cliente', cliente_put.rg_cliente)
            cliente_put.endereco = request.json.get('endereco', cliente_put.endereco)
            cliente_put.cep = request.json.get('cep', cliente_put.cep)
            cliente_put.uf = request.json.get('uf', cliente_put.uf)
            cliente_put.data_nascimento = request.json.get('data_nascimento', cliente_put.data_nascimento)
            cliente_put.estado_civil = request.json.get('estado_civil', cliente_put.estado_civil)
            cliente_put.profissao = request.json.get('profissao', cliente_put.profissao)

            db.session.commit()
            return jsonify({
                'nm_cliente': cliente_put.nm_cliente,
                'cpf_cliente': cliente_put.cpf_cliente,
                'rg_cliente': cliente_put.rg_cliente,
                'endereco': cliente_put.endereco,
                'cep': cliente_put.cep,
                'uf': cliente_put.uf,
                'data_nascimento': cliente_put.data_nascimento,
                'estado_civil': cliente_put.estado_civil,
                'profissao': cliente_put.profissao
            })
        except KeyError as error:
            nms_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nms_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")


# METHOD'S POST, GET E DELETE - Banco
@nms_banco.route('/banco')
class BancoClass(Resource):
    def get(self):
        try:
            bancos = tb_banco.query.all()
            ban = []
            for banco in bancos:
                currBanco = {}
                currBanco['id_banco'] = banco.id_banco
                currBanco['nm_banco'] = banco.nm_banco
                ban.append(currBanco)
            return jsonify(ban)
        except KeyError as error:
            nms_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nms_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")

    @appi.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @appi.expect(model_banco)
    def post(self):
        try:
            bancoData = request.get_json()
            banco = tb_banco(
                nm_banco=bancoData['nm_banco'])
            db.session.add(banco)
            db.session.commit()
            return jsonify(bancoData)
        except KeyError as error:
            nms_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nms_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")


@nms_banco.route('/banco/<int:id_banco>')
class BancoClass(Resource):
    def get(self, id_banco):
        try:
            bancos = tb_banco.query.filter(tb_banco.id_banco == id_banco)
            ban = []
            for banco in bancos:
                currBanco = {}
                currBanco['id_banco'] = banco.id_banco
                currBanco['nm_banco'] = banco.nm_banco
                ban.append(currBanco)
            return jsonify(ban)
        except KeyError as error:
            nms_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nms_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")

    def delete(self, id_banco):
        banco_deletado = tb_banco.query.filter(tb_banco.id_banco == id_banco).delete()
        db.session.commit()
        return jsonify(banco_deletado)


# METHOD'S POST, GET, PUT E DELETE - Proprietario
@nms_proprietario.route("/proprietario")
class ProprietarioClass(Resource):
    @cross_origin()
    @appi.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    def get(self):
        try:
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
    @cross_origin()
    @appi.expect(model_proprietario)
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
class ProprietarioClass(Resource):
    def get(self, id_proprietario):
        try:
            proprietarios = tb_proprietario.query.filter(tb_proprietario.id_proprietario == id_proprietario)
            saida = []
            for proprietario in proprietarios:
                dados_proprietario = {}
                dados_proprietario['id_proprietario'] = proprietario.id_proprietario
                dados_proprietario['nm_proprietario'] = proprietario.nm_proprietario
                dados_proprietario['cpf_proprietario'] = proprietario.cpf_proprietario
                dados_proprietario['rg_proprietario'] = proprietario.rg_proprietario
                dados_proprietario['data_nascimento'] = proprietario.data_nascimento
                dados_proprietario['estado_civil'] = proprietario.estado_civil
                dados_proprietario['profissao'] = proprietario.profissao
                saida.append(dados_proprietario)
            return jsonify(saida)
        except KeyError as error:
            nms_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nms_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")

    @cross_origin()
    def delete(self, id_proprietario):
        try:
            proprietario_deletado = tb_proprietario.query.filter(
                tb_proprietario.id_proprietario == id_proprietario).delete()
            db.session.commit()
            return jsonify(proprietario_deletado)
        except KeyError as error:
            nms_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nms_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")


@nms_proprietario.route("/proprietario/<int:id>")
class ProprietarioClass(Resource):
    @appi.expect(model_put_proprietario)
    def put(self, id):
        try:
            put_proprietario = tb_proprietario.query.get(id)
            put_proprietario.nm_proprietario = request.json.get('nm_proprietario', put_proprietario.nm_proprietario)
            put_proprietario.cpf_proprietario = request.json.get('cpf_proprietario', put_proprietario.cpf_proprietario)
            put_proprietario.rg_proprietario = request.json.get('rg_proprietario', put_proprietario.rg_proprietario)
            put_proprietario.data_nascimento = request.json.get('data_nascimento', put_proprietario.data_nascimento)
            put_proprietario.estado_civil = request.json.get('estado_civil', put_proprietario.estado_civil)
            put_proprietario.profissao = request.json.get('profissao', put_proprietario.profissao)

            db.session.commit()
            return jsonify({
                'nm_proprietario': put_proprietario.nm_proprietario,
                'cpf_proprietario': put_proprietario.cpf_proprietario,
                'rg_proprietario': put_proprietario.rg_proprietario,
                'data_nascimento': put_proprietario.data_nascimento,
                'estado_civil': put_proprietario.estado_civil,
                'profissao': put_proprietario.profissao
            })
        except KeyError as error:
            nms_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nms_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")


# METHOD'S POST, GET E DELETE - Imovel
@nms_imovel.route('/imoveis')
class ImovelClass(Resource):
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

    @appi.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
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


@nms_imovel.route('/imoveis/<int:id_imovel>')
class ImovelClass(Resource):

    def get(self, id_imovel):
        try:
            imoveis = tb_imovel.query.filter(tb_imovel.id_imovel == id_imovel)
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

    def delete(self, id_imovel):
        imovel_deletado = tb_imovel.query.filter(tb_imovel.id_imovel == id_imovel).delete()
        db.session.commit()
        return jsonify(imovel_deletado)


@nms_imovel.route('/imoveis/<int:id>')
class ImovelClass(Resource):
    @appi.expect(model_put_imovel)
    def put(self, id):
        try:
            put_imovel = tb_imovel.query.get(id)
            put_imovel.tipo_imovel = request.json.get('tipo_imovel', put_imovel.tipo_imovel)
            put_imovel.endereco = request.json.get('endereco', put_imovel.endereco)
            put_imovel.complemento = request.json.get('complemento', put_imovel.complemento)
            put_imovel.cep = request.json.get('cep', put_imovel.cep)
            put_imovel.uf = request.json.get('uf', put_imovel.uf)
            put_imovel.id_proprietario = request.json.get('id_proprietario', put_imovel.id_proprietario)
            put_imovel.adquirido_em = request.json.get('adquirido_em', put_imovel.adquirido_em)
            put_imovel.valor_imovel = request.json.get('valor_imovel', put_imovel.valor_imovel)

            db.session.commit()
            return jsonify({
                'tipo_imovel': put_imovel.tipo_imovel,
                'endereco': put_imovel.endereco,
                'complemento': put_imovel.complemento,
                'cep': put_imovel.cep,
                'uf': put_imovel.uf,
                'id_proprietario': put_imovel.id_proprietario,
                'adquirido_em': put_imovel.adquirido_em,
                'valor_imovel': put_imovel.valor_imovel
            })
        except KeyError as error:
            nms_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nms_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")


# METHOD'S POST, GET E DELETE - Gastos Imovel
@nms_gasto_imovel.route('/gastos_imovel')
class GastosClass(Resource):
    def get(self):
        try:
            gastos = tb_gastos_imovel.query.all()
            gas = []
            for gasto in gastos:
                currGasto = {}
                currGasto['id_gasto'] = gasto.id_gasto
                currGasto['id_imovel'] = gasto.id_imovel
                currGasto['tipo_gasto'] = gasto.tipo_gasto
                currGasto['valor_gasto'] = gasto.valor_gasto
                gas.append(currGasto)
            return jsonify(gas)
        except KeyError as error:
            nms_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nms_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")

    @appi.expect(model_gasto_imovel)
    def post(self):
        gastoData = request.get_json()
        gasto = tb_gastos_imovel(
            id_imovel=gastoData['id_imovel'],
            tipo_gasto=gastoData['tipo_gasto'],
            valor_gasto=gastoData['valor_gasto'])
        db.session.add(gasto)
        db.session.commit()
        return jsonify(gastoData)


@nms_gasto_imovel.route('/gastos_imovel/<int:id>')
class GastosClass(Resource):
    @appi.expect(model_put_gasto_imovel)
    def put(self, id):
        try:
            put_gasto = tb_gastos_imovel.query.get(id)
            put_gasto.id_imovel = request.json.get('id_imovel', put_gasto.id_imovel)
            put_gasto.tipo_gasto = request.json.get('tipo_gasto', put_gasto.tipo_gasto)
            put_gasto.valor_gasto = request.json.get('valor_gasto', put_gasto.valor_gasto)

            db.session.commit()
            return jsonify({
                'id_imovel': put_gasto.id_imovel,
                'tipo_gasto': put_gasto.tipo_gasto,
                'valor_gasto': put_gasto.valor_gasto
            })
        except KeyError as error:
            nms_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nms_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")


@nms_gasto_imovel.route('/gastos_imovel/<int:id_gasto>')
class GastosClass(Resource):
    def get(self, id_gasto):
        try:
            gastos = tb_gastos_imovel.query.filter(tb_gastos_imovel.id_gasto == id_gasto)
            gas = []
            for gasto in gastos:
                currGasto = {}
                currGasto['id_gasto'] = gasto.id_gasto
                currGasto['id_imovel'] = gasto.id_imovel
                currGasto['tipo_gasto'] = gasto.tipo_gasto
                currGasto['valor_gasto'] = gasto.valor_gasto
                gas.append(currGasto)
            return jsonify(gas)
        except KeyError as error:
            nms_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nms_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")


# METHOD'S POST , PUT e GET - Compra
@nms_compra.route('/compra')
class CompraClass(Resource):
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

    @appi.expect(model_compra)
    def post(self):
        compra_data = request.get_json()
        compra = tb_compra(
            id_imovel=compra_data['id_imovel'],
            id_cliente=compra_data['id_cliente'],
            tipo_pagamento=compra_data['tipo_pagamento'],
            id_banco=compra_data['id_banco'],
            valor_pagamento=compra_data['valor_pagamento'])
        db.session.add(compra)
        db.session.commit()
        return jsonify(compra_data)


@nms_compra.route('/compra/<int:id>')
class CompraClass(Resource):
    @appi.expect(model_put_compra)
    def put(self, id):
        try:
            put_compra = tb_compra.query.get(id)
            put_compra.id_imovel = request.json.get('id_imovel', put_compra.id_imovel)
            put_compra.id_cliente = request.json.get('id_cliente', put_compra.id_cliente)
            put_compra.tipo_pagamento = request.json.get('tipo_pagamento', put_compra.tipo_pagamento)
            put_compra.id_banco = request.json.get('id_banco', put_compra.id_banco)
            put_compra.valor_pagamento = request.json.get('valor_pagamento', put_compra.valor_pagamento)

            db.session.commit()
            return jsonify({
                'id_imovel': put_compra.id_imovel,
                'id_cliente': put_compra.id_cliente,
                'tipo_pagamento': put_compra.tipo_pagamento,
                'id_banco': put_compra.id_banco,
                'valor_pagamento': put_compra.valor_pagamento
            })
        except KeyError as error:
            nms_proprietario.abort(500, error.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as exception:
            nms_proprietario.abort(400, exception.__doc__, status="Could not retrieve information", statusCode="400")


@nms_compra.route('/compra/<int:id_compra>')
class CompraClass(Resource):
    def get(self, id_compra):
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
