from main import appi, fields

nms_cliente = appi.namespace('mvp')
model_cliente = appi.model('Cliente Model', {'nm_cliente': fields.String(required=True,
                                                                         description="Nome do Cliente"),
                                             'cpf_cliente': fields.String(required=True,
                                                                          description="CPF do Cliente"),
                                             'rg_cliente': fields.String(required=True,
                                                                         description="RG do Cliente"),
                                             'endereco': fields.String(required=True,
                                                                       description="Endereço do Cliente"),
                                             'cep': fields.String(required=True,
                                                                  description="CEP do endereço do Cliente"),
                                             'uf': fields.String(required=True,
                                                                 description="UF do endereço do Cliente"),
                                             'data_nascimento': fields.Date(required=True,
                                                                            description="Data de nascimento do Cliente"),
                                             'estado_civil': fields.String(required=True,
                                                                           description="Estado Civil atual do Cliente"),
                                             'profissao': fields.String(required=True,
                                                                        description="Profissão do Cliente")})
model_get_cliente = appi.model('Cliente Model', {'Id': fields.Integer(description="Id do cliente")})
model_put_cliente = appi.model('Cliente Model', {'nm_cliente': fields.String(description="Nome do Cliente"),
                                                 'cpf_cliente': fields.String(description="CPF do Cliente"),
                                                 'rg_cliente': fields.String(description="RG do Cliente"),
                                                 'endereco': fields.String(description="Endereço do Cliente"),
                                                 'cep': fields.String(description="CEP do endereço do Cliente"),
                                                 'uf': fields.String(description="UF do endereço do Cliente"),
                                                 'data_nascimento': fields.Date(
                                                     description="Data de nascimento do Cliente"),
                                                 'estado_civil': fields.String(
                                                     description="Estado Civil atual do Cliente"),
                                                 'profissao': fields.String(description="Profissão do Cliente")})

nms_proprietario = appi.namespace('mvp')
model_proprietario = appi.model('Proprietario Model', {'nm_proprietario': fields.String(required=True,
                                                                                        description="Nome do Proprietario"),
                                                       'cpf_proprietario': fields.String(required=True,
                                                                                         description="CPF do Proprietario"),
                                                       'rg_proprietario': fields.String(required=True,
                                                                                        description="RG do Proprietario"),
                                                       'data_nascimento': fields.String(required=True,
                                                                                        description="Data de Nascimento do Proprietario"),
                                                       'estado_civil': fields.String(required=True,
                                                                                     description="Estado Civil do Proprietario"),
                                                       'profissao': fields.String(required=True,
                                                                                  description="Profissão do Proprietario"),
                                                       })
model_put_proprietario = appi.model('Proprietario Model',
                                    {'nm_proprietario': fields.String(description="Nome do Proprietario"),
                                     'cpf_proprietario': fields.String(description="CPF do Proprietario"),
                                     'rg_proprietario': fields.String(description="RG do Proprietario"),
                                     'data_nascimento': fields.String(description="Data de Nascimento do Proprietario"),
                                     'estado_civil': fields.String(description="Estado Civil do Proprietario"),
                                     'profissao': fields.String(description="Profissão do Proprietario")
                                     })

nms_imovel = appi.namespace('mvp')
model_imovel = appi.model('Imovel Model', {'tipo_imovel': fields.String(required=True,
                                                                        description="Tipo do Imovel"),
                                           'endereco': fields.String(required=True,
                                                                     description="Endereço do Imovel"),
                                           'complemento': fields.String(required=True,
                                                                        description="Complemento do Endereço do Imovel"),
                                           'cep': fields.String(required=True,
                                                                description="Cep da localizaçao do Imovel"),
                                           'uf': fields.String(required=True,
                                                               description="UF do Imovel"),
                                           'id_proprietario': fields.Integer(required=True,
                                                                             description="ID do Proprietario do Imovel"),
                                           'adquirido_em': fields.String(required=True,
                                                                         description="Quando o imovel foi adquirido"),
                                           'valor_imovel': fields.String(required=True,
                                                                         description="Valor de Venda do Imovel")})
model_put_imovel = appi.model('Imovel Model', {'tipo_imovel': fields.String(description="Tipo do Imovel"),
                                               'endereco': fields.String(description="Endereço do Imovel"),
                                               'complemento': fields.String(
                                                   description="Complemento do Endereço do Imovel"),
                                               'cep': fields.String(description="Cep da localizaçao do Imovel"),
                                               'uf': fields.String(description="UF do Imovel"),
                                               'id_proprietario': fields.Integer(
                                                   description="ID do Proprietario do Imovel"),
                                               'adquirido_em': fields.String(
                                                   description="Quando o imovel foi adquirido"),
                                               'valor_imovel': fields.String(description="Valor de Venda do Imovel")})

nms_gasto_imovel = appi.namespace('mvp')
model_gasto_imovel = appi.model('Despesa Imovel Model', {'id_imovel': fields.Integer(required=True,
                                                                                     description="Id do Imovel"),
                                                         'tipo_gasto': fields.Integer(required=True,
                                                                                      description="Tipo de gasto/despesa"),
                                                         'valor_gasto': fields.Integer(required=True,
                                                                                       description="Valor gasto com as despesas do Imovel"),
                                                         })
model_put_gasto_imovel = appi.model('Despesa Imovel Model', {'id_imovel': fields.Integer(description="Id do Imovel"),
                                                             'tipo_gasto': fields.Integer(
                                                                 description="Tipo de gasto/despesa"),
                                                             'valor_gasto': fields.Integer(
                                                                 description="Valor gasto com as despesas do Imovel"),
                                                             })

nms_compra = appi.namespace('mvp')
model_compra = appi.model('Compra Model', {'id_imovel': fields.Integer(required=True,
                                                                       description="ID do Imovel que esta sendo comprado"),
                                           'id_cliente': fields.Integer(required=True,
                                                                        description="ID do Imovel que esta sendo comprado"),
                                           'tipo_pagamento': fields.String(required=True,
                                                                           description="ID do Imovel que esta sendo comprado"),
                                           'id_banco': fields.Integer(required=True,
                                                                      description="ID do Imovel que esta sendo comprado"),
                                           'valor_pagamento': fields.Integer(required=True,
                                                                             description="ID do Imovel que esta sendo comprado"),
                                           })
model_put_compra = appi.model('Compra Model',
                              {'id_imovel': fields.Integer(description="ID do Imovel que esta sendo comprado"),
                               'id_cliente': fields.Integer(description="ID do Imovel que esta sendo comprado"),
                               'tipo_pagamento': fields.String(description="ID do Imovel que esta sendo comprado"),
                               'id_banco': fields.Integer(description="ID do Imovel que esta sendo comprado"),
                               'valor_pagamento': fields.Integer(description="ID do Imovel que esta sendo comprado"),
                               })

nms_banco = appi.namespace('mvp')
model_banco = appi.model('Banco Model', {'nm_banco': fields.String(required=True,
                                                                   description="Nome do Banco")})