-- Tabela de Alunos
CREATE TABLE Alunos (
    Matricula INTEGER NOT NULL,
    Nome VARCHAR(100) NOT NULL,
    Endereco VARCHAR(255),
    Telefone VARCHAR(14),
    PRIMARY KEY (Matricula)
);

-- Tabela de Funcionários
CREATE TABLE Funcionarios (
    SIAPE INTEGER NOT NULL,
    Nome VARCHAR(100) NOT NULL,
    Endereco VARCHAR(255),
    Telefone VARCHAR(14),
    Tipo VARCHAR(20),
    PRIMARY KEY (SIAPE)
);

-- Tabela de Livros
CREATE TABLE Livros (
    ISBN INTEGER NOT NULL,
    Titulo VARCHAR(100) NOT NULL,
    Autores VARCHAR(255),
    Editora VARCHAR(30),
    PRIMARY KEY (ISBN)
);

-- Tabela de Empréstimos
CREATE TABLE Emprestimos (
    EmprestimoID INTEGER AUTO_INCREMENT,
    Numero INTEGER NOT NULL,
    Data_Emp DATE,
    Data_Dev DATE,
    ISBN INTEGER,
    SIAPE INTEGER,
    Matricula INTEGER,
    PRIMARY KEY (EmprestimoID),
    FOREIGN KEY (ISBN) REFERENCES Livros(ISBN),
    FOREIGN KEY (SIAPE) REFERENCES Funcionarios(SIAPE),
    FOREIGN KEY (Matricula) REFERENCES Alunos(Matricula)  
);