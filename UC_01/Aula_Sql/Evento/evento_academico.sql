-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 24-Abr-2025 às 21:59
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
-- Banco de dados: `evento_academico`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `alunos`
--

CREATE TABLE `alunos` (
  `Matricula` int(11) NOT NULL,
  `CPF` varchar(11) NOT NULL,
  `Nome` varchar(100) NOT NULL,
  `Endereco` varchar(255) DEFAULT NULL,
  `Telefone` varchar(14) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `alunos`
--

INSERT INTO `alunos` (`Matricula`, `CPF`, `Nome`, `Endereco`, `Telefone`) VALUES
(2025155478, '12365498778', 'Carlos', 'Rua Alagada, 452', '2198546');

-- --------------------------------------------------------

--
-- Estrutura da tabela `certificados`
--

CREATE TABLE `certificados` (
  `Nome_completo` varchar(100) NOT NULL,
  `CPF` varchar(11) NOT NULL,
  `EventoID` varchar(100) NOT NULL,
  `Data_hora_inicio` varchar(10) NOT NULL,
  `Palestrante` varchar(100) NOT NULL,
  `Tema` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `certificados`
--

INSERT INTO `certificados` (`Nome_completo`, `CPF`, `EventoID`, `Data_hora_inicio`, `Palestrante`, `Tema`) VALUES
('Carlos Daquela', '21546547841', '01', '21/04/25', 'Bebeto', 'E-commerce');

-- --------------------------------------------------------

--
-- Estrutura da tabela `comunidade_externa`
--

CREATE TABLE `comunidade_externa` (
  `CPF` varchar(11) NOT NULL,
  `Nome` varchar(100) NOT NULL,
  `Telefone` varchar(14) NOT NULL,
  `Instituicao` varchar(20) DEFAULT NULL,
  `Email` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `comunidade_externa`
--

INSERT INTO `comunidade_externa` (`CPF`, `Nome`, `Telefone`, `Instituicao`, `Email`) VALUES
('1235468798', 'Evandro do dende', '21354654551', 'trabalhador clt', 'dendeenois@gmail.com');

-- --------------------------------------------------------

--
-- Estrutura da tabela `eventos`
--

CREATE TABLE `eventos` (
  `Local_evento` varchar(50) NOT NULL,
  `Data_hora_inicio` varchar(10) DEFAULT NULL,
  `Data_hora_fim` varchar(10) DEFAULT NULL,
  `Tema` varchar(20) DEFAULT NULL,
  `Palestrante` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `eventos`
--

INSERT INTO `eventos` (`Local_evento`, `Data_hora_inicio`, `Data_hora_fim`, `Tema`, `Palestrante`) VALUES
('Sala 3', '21/04/25', '21/04/25', 'E-commerce', 'Bebeto');

-- --------------------------------------------------------

--
-- Estrutura da tabela `incritos`
--

CREATE TABLE `incritos` (
  `Data_hora` varchar(8) NOT NULL,
  `CPF` varchar(11) NOT NULL,
  `Local_evento` varchar(100) NOT NULL,
  `Tema` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `incritos`
--

INSERT INTO `incritos` (`Data_hora`, `CPF`, `Local_evento`, `Tema`) VALUES
('21/04/25', '2025155478', 'Faculdade X, 3º andar, sala 3', 'E-commerce');

-- --------------------------------------------------------

--
-- Estrutura da tabela `local_evento`
--

CREATE TABLE `local_evento` (
  `lotacao` varchar(100) NOT NULL,
  `Nome` varchar(10) NOT NULL,
  `localizacao` varchar(100) NOT NULL,
  `Equipamentos` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `local_evento`
--

INSERT INTO `local_evento` (`lotacao`, `Nome`, `localizacao`, `Equipamentos`) VALUES
('200 pessoas', 'sala 3', 'Faculdade X', '1 microfone  1 projetor');

-- --------------------------------------------------------

--
-- Estrutura da tabela `palestrante`
--

CREATE TABLE `palestrante` (
  `Nome_completo` varchar(50) NOT NULL,
  `Mini_curriculo` varchar(100) NOT NULL,
  `Contato` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `palestrante`
--

INSERT INTO `palestrante` (`Nome_completo`, `Mini_curriculo`, `Contato`) VALUES
('Bebeto', 'Especialista em E-commerce', 'bebeto@gmail.com');

-- --------------------------------------------------------

--
-- Estrutura da tabela `professores`
--

CREATE TABLE `professores` (
  `CPF` varchar(11) NOT NULL,
  `Nome` varchar(100) NOT NULL,
  `Telefone` varchar(14) DEFAULT NULL,
  `Email` varchar(20) NOT NULL,
  `Instituicao` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `professores`
--

INSERT INTO `professores` (`CPF`, `Nome`, `Telefone`, `Email`, `Instituicao`) VALUES
('21351874554', 'Burgos da Pasta Verde', '2015468749', 'burgos@gmail.com', 'URRJ');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `alunos`
--
ALTER TABLE `alunos`
  ADD PRIMARY KEY (`Matricula`);

--
-- Índices para tabela `comunidade_externa`
--
ALTER TABLE `comunidade_externa`
  ADD PRIMARY KEY (`CPF`);

--
-- Índices para tabela `eventos`
--
ALTER TABLE `eventos`
  ADD PRIMARY KEY (`Local_evento`);

--
-- Índices para tabela `incritos`
--
ALTER TABLE `incritos`
  ADD PRIMARY KEY (`Data_hora`);

--
-- Índices para tabela `palestrante`
--
ALTER TABLE `palestrante`
  ADD PRIMARY KEY (`Nome_completo`);

--
-- Índices para tabela `professores`
--
ALTER TABLE `professores`
  ADD PRIMARY KEY (`CPF`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
