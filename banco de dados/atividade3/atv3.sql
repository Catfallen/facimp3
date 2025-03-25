create database rede_social

CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR NOT NULL,
    email VARCHAR NOT NULL UNIQUE,
    senha VARCHAR NOT NULL, 
    data_nascimento DATE,
    bio TEXT,  
    interesses VARCHAR, 
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE conexoes (
    usuario_id INTEGER,  
    amigo_id INTEGER,    
    data_conexao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  
    PRIMARY KEY (usuario_id, amigo_id),
    CONSTRAINT fk_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    CONSTRAINT fk_amigo FOREIGN KEY (amigo_id) REFERENCES usuarios(id)
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER,
    texto TEXT NOT NULL, 
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  
    CONSTRAINT fk_usuario_post FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE comentarios (
    id SERIAL PRIMARY KEY,
    post_id INTEGER, 
    usuario_id INTEGER, 
    texto TEXT NOT NULL,  
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    CONSTRAINT fk_post FOREIGN KEY (post_id) REFERENCES posts(id),
    CONSTRAINT fk_usuario_comentario FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE curtidas (
    id SERIAL PRIMARY KEY,
    post_id INTEGER,
    usuario_id INTEGER,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_post_curtida FOREIGN KEY (post_id) REFERENCES posts(id),
    CONSTRAINT fk_usuario_curtida FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);
