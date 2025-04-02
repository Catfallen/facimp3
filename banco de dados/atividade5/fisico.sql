CREATE TABLE remetentes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR,
    telefone VARCHAR
);

CREATE TABLE destinatarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR,
    telefone VARCHAR
);

CREATE TABLE entregadores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR,
    placa_veiculo VARCHAR
);

CREATE TABLE pacote (
    id SERIAL PRIMARY KEY,
    informacoes VARCHAR,
    destino VARCHAR,
    remetente_id INT REFERENCES remetentes(id) ON DELETE CASCADE,
    destinatario_id INT REFERENCES destinatarios(id) ON DELETE CASCADE,
    entregador_id INT REFERENCES entregadores(id) ON DELETE SET NULL
);