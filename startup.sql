-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 10-Abr-2025 às 22:41
-- Versão do servidor: 5.7.36
-- versão do PHP: 8.1.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `startup`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `cliente`
--

CREATE TABLE `cliente` (
  `CPF` varchar(14) NOT NULL,
  `NOME` varchar(50) NOT NULL,
  `ENDERECO` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `equipamentos`
--

CREATE TABLE `equipamentos` (
  `CODIGO` int(11) NOT NULL,
  `NOME` varchar(50) NOT NULL,
  `DESCRICAO` varchar(100) NOT NULL,
  `VALOR` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `forcenedores`
--

CREATE TABLE `forcenedores` (
  `CNPJ` varchar(17) NOT NULL,
  `NOME` varchar(100) NOT NULL,
  `ENDERECO` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `pedidos`
--

CREATE TABLE `pedidos` (
  `NUMERO` int(11) NOT NULL,
  `DATA` date NOT NULL,
  `STATUS` varchar(30) NOT NULL,
  `CPF` varchar(14) NOT NULL,
  `CNPJ` varchar(17) NOT NULL,
  `CODIGO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`CPF`);

--
-- Índices para tabela `equipamentos`
--
ALTER TABLE `equipamentos`
  ADD PRIMARY KEY (`CODIGO`);

--
-- Índices para tabela `forcenedores`
--
ALTER TABLE `forcenedores`
  ADD PRIMARY KEY (`CNPJ`);

--
-- Índices para tabela `pedidos`
--
ALTER TABLE `pedidos`
  ADD PRIMARY KEY (`NUMERO`,`CPF`,`CNPJ`,`CODIGO`),
  ADD KEY `CPF` (`CPF`),
  ADD KEY `CNPJ` (`CNPJ`),
  ADD KEY `CODIGO` (`CODIGO`);

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `pedidos`
--
ALTER TABLE `pedidos`
  ADD CONSTRAINT `pedidos_ibfk_1` FOREIGN KEY (`CPF`) REFERENCES `cliente` (`CPF`),
  ADD CONSTRAINT `pedidos_ibfk_2` FOREIGN KEY (`CNPJ`) REFERENCES `forcenedores` (`CNPJ`),
  ADD CONSTRAINT `pedidos_ibfk_3` FOREIGN KEY (`CODIGO`) REFERENCES `equipamentos` (`CODIGO`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
