create database eventos

CREATE TABLE organizadores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    telefone VARCHAR(15)
);

CREATE TABLE fornecedores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR NOT NULL,
    descricao VARCHAR,
    telefone VARCHAR(15)
);

CREATE TABLE participantes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    telefone VARCHAR(15),
    evento_id INTEGER, 
    CONSTRAINT fk_evento FOREIGN KEY (evento_id) REFERENCES eventos(id)
);

CREATE TABLE eventos ( 
    id SERIAL PRIMARY KEY,
    nome VARCHAR NOT NULL,
    descricao VARCHAR,
    data DATE NOT NULL,
    local VARCHAR NOT NULL,
    organizador_id INTEGER,  
    CONSTRAINT fk_organizador FOREIGN KEY (organizador_id) REFERENCES organizador(id)
);

CREATE TABLE fornecedores_eventos (
    evento_id INTEGER,
    fornecedor_id INTEGER,
    PRIMARY KEY (evento_id, fornecedor_id),
    CONSTRAINT fk_evento FOREIGN KEY (evento_id) REFERENCES eventos(id),
    CONSTRAINT fk_fornecedor FOREIGN KEY (fornecedor_id) REFERENCES fornecedores(id)
);
