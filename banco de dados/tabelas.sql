-- Criação do tipo ENUM
CREATE TYPE tipo_usuario AS ENUM ('aluno', 'professor');

-- Drop na ordem correta

DROP TABLE IF EXISTS emprestimo CASCADE;
DROP TABLE IF EXISTS livro CASCADE;
DROP TABLE IF EXISTS categoria CASCADE;
DROP TABLE IF EXISTS usuario CASCADE;
-- Tabela categoria
CREATE TABLE categoria (
    id SERIAL PRIMARY KEY,
    nome VARCHAR NOT NULL
);

-- Tabela livro
CREATE TABLE livro (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR NOT NULL,
    autor VARCHAR,
    ano INT,
    categoria_id INT,
    FOREIGN KEY (categoria_id) REFERENCES categoria(id)
);

-- Tabela usuario
CREATE TABLE usuario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR,
    tipo tipo_usuario NOT NULL
);


--Emprestimo
CREATE TABLE emprestimo(
    id SERIAL PRIMARY KEY,
    livro_id INT,
    usuario_id INT,
    data_emprestimo date,
    data_devolução date,
    FOREIGN KEY (livro_id) REFERENCES livro(id),
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
)
