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

