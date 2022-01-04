CREATE DATABASE banco;
USE banco;

CREATE TABLE cliente(
	idCliente INT NOT NULL PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    endereco VARCHAR(45) NOT NULL
);

SELECT * FROM cliente;

INSERT INTO cliente (idCliente, nome, cpf, endereco) VALUES (1, 'Gabriel', '000.000.000-00', 'Rua Paulo Terceiro');
INSERT INTO cliente (idCliente, nome, cpf, endereco) VALUES (2, 'Vitoria', '111.111.111-11', 'Rua Paulo Segundo');

ALTER TABLE cliente ADD COLUMN ano_nascimento INT NOT NULL;

UPDATE cliente SET ano_nascimento = 2000 WHERE idCliente = 1;
UPDATE cliente SET ano_nascimento = 2003 WHERE idCliente = 2;

DELETE FROM cliente WHERE idCliente = 1;

DROP TABLE cliente;
