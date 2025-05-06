"data_base de matricula escolar de alunos e professores"

"Alunos"

CREATE DATABASE Escolar;
CREATE TABLE Alunos (
id_aluno INTEGER AUTO_INCREMENT,
numero_matricula VARCHAR(20) NOT NULL,
nome_completo VARCHAR(255) not null,
data_nascimento DATE,
endereco_rua VARCHAR(255)not NULL,
endereco_numero VARCHAR(10)not null,
endereco_complemento VARCHAR(50)not null,
endereco_bairro VARCHAR(100)not null,
endereco_cidade VARCHAR(100)not null,
endereco_estado VARCHAR(50)not null,
endereco_cep VARCHAR(10)not null,
telefone VARCHAR(20)not null,
email VARCHAR(100)not null,
data_matricula DATE,
PRIMARY KEY (numero_matricula)
);

"Professores"

CREATE TABLE Professores (
id_professor INTEGER AUTO_INCREMENT,
numero_registro VARCHAR(20) NOT NULL,
nome_completo VARCHAR(255)not null,
data_nascimento DATE,
endereco_rua VARCHAR(255)not null,
endereco_numero VARCHAR(10)not null,
endereco_complemento VARCHAR(50)not null,
endereco_bairro VARCHAR(100)not null,
endereco_cidade VARCHAR(100)not null,
endereco_estado VARCHAR(50)not null,
endereco_cep VARCHAR(10)not null,
ANALISTA DE DADOS – BIG DATA SCIENCE
telefone VARCHAR(20)not null,
email VARCHAR(100)not null,
areas_especializacao VARCHAR(255),
PRIMARY KEY (numero_registro)
);