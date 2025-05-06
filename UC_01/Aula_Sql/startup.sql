-- Tabela de Clientes
CREATE TABLE Clientes (
    ClienteID INTEGER NOT NULL,
    Nome VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Endereco VARCHAR(255),
    PRIMARY KEY (ClienteID)
);

-- Tabela de Produtos
CREATE TABLE Produtos (
    ProdutoID INTEGER NOT NULL,
    Nome VARCHAR(255) NOT NULL,
    Descricao VARCHAR(255),
    Preco FLOAT NOT NULL,
    Estoque INTEGER NOT NULL,
    PRIMARY KEY (ProdutoID)
);

-- Tabela de Pedidos
CREATE TABLE Pedidos (
    PedidoID INTEGER NOT NULL,
    ClienteID INTEGER NOT NULL,
    DataPedido DATE,
    Status VARCHAR(20),
    PRIMARY KEY(PedidoID),
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID)
);

-- Tabela de Itens do Pedido
CREATE TABLE ItensPedido (
    ItemID INTEGER AUTO_INCREMENT,
    PedidoID INTEGER NOT NULL,
    ProdutoID INTEGER NOT NULL,
    Quantidade INTEGER NOT NULL,
    PrecoUnitario FLOAT NOT NULL,
    PRIMARY KEY (ItemID),
    FOREIGN KEY (PedidoID) REFERENCES Pedidos(PedidoID),
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID)
);

