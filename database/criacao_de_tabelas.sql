CREATE TABLE tb_proprietario (
    id_proprietario SERIAL PRIMARY KEY,
    nm_proprietario VARCHAR(50) NOT NULL,
    cpf_proprietario VARCHAR(30) NOT NULL,
    rg_proprietario VARCHAR(30),
    data_nascimento DATE,
    estado_civil VARCHAR(30),
    profissao VARCHAR(30);
);

CREATE TABLE tb_imovel(
                    id_imovel SERIAL PRIMARY KEY,
                    tipo_imovel VARCHAR(255) NOT NULL,
                    endereco_imovel VARCHAR(255) NOT NULL,
                    cep VARCHAR(30) NOT NULL,
                    UF VARCHAR(2) NOT NULL,
                    id_proprietario INTEGER UNIQUE,
                    nm_proprietario VARCHAR(50) UNIQUE,
                    FOREIGN KEY (id_proprietario) REFERENCES tb_proprietario (id_proprietario)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                    FOREIGN KEY (nm_proprietario) REFERENCES tb_proprietario (nm_proprietario)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                    adquirido_em DATE,
                    valor_imovel INT,
                    status_imovel BOOLEAN
);

CREATE TABLE tb_cliente (
    id_cliente SERIAL PRIMARY KEY,
    nm_cliente VARCHAR(50) NOT NULL,
    cpf_cliente VARCHAR(30) NOT NULL,
    rg_cliente VARCHAR(30),
    data_nascimento DATE,
    estado_civil VARCHAR(30),
    profissao VARCHAR(30),
    endereco VARCHAR(50),
    uf VARCHAR(2)
);

CREATE TABLE tb_compra (
    id_compra SERIAL PRIMARY KEY,
    id_imovel INTEGER UNIQUE,
    nm_proprietario VARCHAR(50) UNIQUE,
    id_cliente INTEGER UNIQUE,
    nm_cliente VARCHAR(50) UNIQUE,
    FOREIGN KEY (id_imovel) REFERENCES tb_imovel( id_imovel)
    ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (nm_proprietario) REFERENCES tb_proprietario (nm_proprietario)
    ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_cliente) REFERENCES tb_cliente(id_cliente)
    ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (nm_cliente) REFERENCES tb_cliente(nm_cliente)
    ON UPDATE CASCADE ON DELETE CASCADE,
    valor_imovel INTEGER,
    tipo_de_compra VARCHAR(20)
);