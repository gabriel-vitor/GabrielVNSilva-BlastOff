CREATE DATABASE IF NOT EXISTS TopSecret;
USE TopSecret;

CREATE TABLE IF NOT EXISTS Agente(
	idAgente INT NOT NULL,
	nome VARCHAR(45) NOT NULL,
	endereco VARCHAR(45) NULL,
	nascimento DATE NULL,
	habilidade VARCHAR(45) NULL,
	sexo VARCHAR(45) NULL,
	email VARCHAR(45) NULL,
	PRIMARY KEY (idAgente)
  );

CREATE TABLE IF NOT EXISTS vilao(
	idvilao INT NOT NULL,
	nome VARCHAR(45) NOT NULL,
	num_crimes INT NOT NULL,
	PRIMARY KEY (idvilao)
  );

CREATE TABLE IF NOT EXISTS missao(
	idmissao INT NOT NULL,
	data VARCHAR(45) NOT NULL,
	nome VARCHAR(45) NOT NULL,
	localizacao VARCHAR(45) NULL,
	duracao VARCHAR(45) NULL,
	vilao_idvilao INT NOT NULL,
	PRIMARY KEY (idmissao),
    CONSTRAINT vilao_idvilao
    FOREIGN KEY (vilao_idvilao)
    REFERENCES vilao (idvilao)
);

CREATE TABLE IF NOT EXISTS Agente_has_missao(
	Agente_idAgente INT NOT NULL,
	missao_idmissao INT NOT NULL,
	PRIMARY KEY (Agente_idAgente, missao_idmissao),
	CONSTRAINT fk_Agente_has_missao_Agente
	FOREIGN KEY (Agente_idAgente)
	REFERENCES Agente (idAgente)
	ON DELETE CASCADE
	ON UPDATE CASCADE,
	CONSTRAINT fk_Agente_has_missao_missao
	FOREIGN KEY (missao_idmissao)
	REFERENCES missao (idmissao)
	ON DELETE CASCADE
	ON UPDATE CASCADE
);

SELECT * FROM Agente;

