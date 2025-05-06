CREATE DATABASE Evento_academico;


-- Tabela de Alunos
CREATE TABLE Alunos (
    Matricula VARCHAR (20)
    CPF VARCHAR(11) NOT NULL,
    Nome VARCHAR(100) NOT NULL,
    Telefone VARCHAR(14),
    Instituicao VARCHAR (20) NOT NULL,
    Email VARCHAR (20) NOT NULL,
    PRIMARY KEY (CPF)
);

-- Tabela de Professores
CREATE TABLE Professores (
    
    CPF VARCHAR(11) NOT NULL,
    Nome VARCHAR(100) NOT NULL,
    Telefone VARCHAR(14),
    Email VARCHAR (20) NOT NULL,
    Instituicao VARCHAR(20) NOT NULL,
    PRIMARY KEY (CPF)
);
-- Tabela de Comunidade_Externa

CREATE TABLE Comunidade_Externa ( 
    
    CPF VARCHAR(11) NOT NULL,
    Nome VARCHAR(100) NOT NULL,
    Telefone VARCHAR(14) NOT NULL,
    Instituicao VARCHAR(20),
    Email VARCHAR (20) NOT NULL,
    PRIMARY KEY (CPF)
);

-- Tabela de Palestrante
CREATE TABLE Palestrante (
    
    Nome_completo VARCHAR(50) NOT NULL,
    Mini_curriculo VARCHAR(100) NOT NULL,
    Contato VARCHAR(255),
    
    PRIMARY KEY (Nome_completo)
);

-- Tabela do Local
CREATE TABLE Local_evento(
    
    lotacao VARCHAR (100) NOT NULL,
    Nome VARCHAR(10) NOT NULL,
    localizacao VARCHAR (100) not null,
    Equipamentos VARCHAR (50) NOT NULL
);

-- Tabela de Inscritos
CREATE TABLE Incritos(
    Data_hora VARCHAR(8),
    CPF VARCHAR (11)not NULL,
    Local_evento VARCHAR (100) NOT NULL,
    Tema VARCHAR (20) NOT NULL,
    PRIMARY key (Data_hora)


);


-- Tabela de Eventos
CREATE TABLE Eventos (
    
    Local_evento VARCHAR(50) NOT NULL,
    Data_hora_inicio VARCHAR(10),
    Data_hora_fim VARCHAR(10),
    Tema VARCHAR (20),
    Palestrante VARCHAR(50),
    
    PRIMARY KEY (Local_evento),
      
); 

-- Tabela Certificados
CREATE TABLE Certificados(
    Nome_completo VARCHAR (100) NOT NULL,
    CPF VARCHAR (11) NOT NULL,
    EventoID VARCHAR(100) NOT NULL,
    Data_hora_inicio VARCHAR (10) NOT NULL,
    Palestrante VARCHAR (100) NOT NULL, 
    Tema VARCHAR(20) NOT NULL

);