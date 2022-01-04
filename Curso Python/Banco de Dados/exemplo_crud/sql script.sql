CREATE DATABASE Empresa;
USE Empresa;

CREATE TABLE Empregado(
	idEmpregado INT NOT NULL PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    endereco VARCHAR(45) NOT NULL
);

CREATE TABLE Dependentes(
	idDependente INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY(idDependente),
    nome VARCHAR(45) NOT NULL,
    endereco VARCHAR(45) NOT NULL,
    idEmpregado INT NOT NULL,
    CONSTRAINT fk_Empregado
		FOREIGN KEY(idEmpregado) REFERENCES Empregado(idEmpregado)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

SELECT * FROM Empregado;
SELECT * FROM Dependentes;

DELETE FROM Empregado WHERE idEmpregado = 4;

