create database hotel

CREATE TABLE hospedes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    telefone VARCHAR(15),
    preferencias_quarto VARCHAR  
);


CREATE TABLE quartos (
    id SERIAL PRIMARY KEY,
    numero_quarto VARCHAR(10) NOT NULL,  
    tipo VARCHAR NOT NULL, 
    capacidade INTEGER, 
    preco_diaria DECIMAL(10, 2) NOT NULL  
);


CREATE TABLE reservas (
    id SERIAL PRIMARY KEY,
    hospede_id INTEGER,  
    quarto_id INTEGER,   
    data_check_in DATE NOT NULL,  
    data_check_out DATE NOT NULL,  
    CONSTRAINT fk_hospede FOREIGN KEY (hospede_id) REFERENCES hospedes(id),
    CONSTRAINT fk_quarto FOREIGN KEY (quarto_id) REFERENCES quartos(id)
);


CREATE TABLE pagamentos (
    id SERIAL PRIMARY KEY,
    reserva_id INTEGER,  
    valor_pago DECIMAL(10, 2) NOT NULL, 
    metodo_pagamento VARCHAR NOT NULL,  
    data_pagamento DATE NOT NULL, 
    CONSTRAINT fk_reserva FOREIGN KEY (reserva_id) REFERENCES reservas(id)
);

