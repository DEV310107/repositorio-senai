create database jooin;
-- ----------------------------

use jooin;
-- -------------------------------

create table empresa(
	id int(3) primary key auto_increment,
    nome varchar(20),
    nome_fantasia varchar(20),
    cnpj float(14),
    endereco varchar(50),
    cidade varchar(20),
    estado varchar(20),
    pais varchar(20),
    telefone_01 float(12),
    telefone_02 float(12),
    celular float (12),
    representante varchar(20)
);
-- ----------------------------------------------------------------
create table produto(
	id int(3) primary key auto_increment,
    nome varchar(20),
    marca varchar(20),
    empresa int(3),
    estoque int(5),
    valor_bruto float(6),
    imposto float(6),
    margem_lucro float(6),
    valor_final float(6)
);
-- ------------------------------------------------------------------

create table cliente(
	id int(3) primary key auto_increment,
    nome varchar(20),
    cpf float(11),
    data_nascimento int(8),
    celular float(12),
    email varchar(50),
    item_comprado int(3)
);

INSERT INTO empresa (nome, nome_fantasia, cnpj, endereco, cidade, estado, pais, telefone_01, telefone_02, celular, representante) 
VALUES
('Empresa da Trapalhada LTDA', 'Trapalhada Inc.', 98765432109876, 'Avenida da Confusão, 456', 'Bagunçópolis', 'Confusão', 'Desordemlândia', 5551234567, 5559876543, 5553334444, 'Sr. Desastre'),
('Empresa dos Problemas S/A', 'Problemas Corp.', 12345678901234, 'Rua dos Erros, 789', 'Caosville', 'Incerto', 'Desenrolândia', 4449876543, 4445556789, 4442223333, 'Sra. Engano'),
('Fábrica da Confusão e Cia.', 'Confusion Factory', 55555555555555, 'Estrada da Desorganização, 123', 'Desajustópolis', 'Descontrole', 'Desarrumação', 6661112233, 6664445566, 6667778889, 'Dr. Caos'),
('Empresa do Caos Ltda', 'Caos e Cia.', 65498732145610, 'Rua da Desordem, 789', 'Desregulópolis', 'Desorganização', 'Descontroslândia', 7778889999, 7776665555, 7773331111, 'Sr. Bagunça'),
('Indústria do Equívoco S/A', 'Equívoco Ind.', 78965412330123, 'Avenida do Engano, 456', 'Desorientópolis', 'Desgovernado', 'Desconhecido', 8889991111, 8882223333, 8884445555, 'Sra. Engano'),
('Empresa da Bagunça & Cia.', 'Bagunça Ltda.', 99988877766644, 'Travessa da Desordem, 789', 'Bagunçalândia', 'Bagunçado', 'Bagunçalândia', 7774448888, 7772225555, 7773339999, 'Sr. Confusão'),
('Companhia do Descontrole Ltda.', 'Descontrole Corp.', 32165498798765, 'Rua do Descontrole, 123', 'Desatino', 'Desregrado', 'Descompasso', 5556667777, 5558889999, 5551113333, 'Sr. Caos');

INSERT INTO empresa (nome, nome_fantasia, cnpj, endereco, cidade, estado, pais, telefone_01, telefone_02, celular, representante) 
VALUES
('Familia Senai Ltda.', 'Odio Descontrolado.', 1233214566547, 'Rua Roberto Manje, 3000', 'Jundiai', 'São Paulo', 'Brasil', 5556667788, 5558880009, 5551115333, 'Sr. Carlos');

-- Inserir dados
INSERT INTO produto (nome, marca, empresa, estoque, valor_bruto, imposto, margem_lucro, valor_final) VALUES
('Smartwatch', 'WristTech', 1, 80, 150.00, 0.06, 0.25, (150.00 * (1 + 0.06) * (1 + 0.25))),
('Tablet', 'TouchPad', 2, 70, 300.00, 0.08, 0.2, (300.00 * (1 + 0.08) * (1 + 0.2))),
('Câmera', 'SnapLens', 3, 90, 250.00, 0.07, 0.22, (250.00 * (1 + 0.07) * (1 + 0.22))),
('Impressora', 'PrintTech', 4, 60, 200.00, 0.05, 0.18, (200.00 * (1 + 0.05) * (1 + 0.18))),
('Monitor', 'ViewScreen', 5, 40, 180.00, 0.04, 0.15, (180.00 * (1 + 0.04) * (1 + 0.15))),
('Caixa de Som', 'SoundWave', 6, 120, 80.00, 0.03, 0.2, (80.00 * (1 + 0.03) * (1 + 0.2))),
('Roteador', 'NetLink', 7, 95, 70.00, 0.02, 0.25, (70.00 * (1 + 0.02) * (1 + 0.25))),
('Webcam', 'EyeSee', 1, 75, 45.00, 0.01, 0.15, (45.00 * (1 + 0.01) * (1 + 0.15))),
('HD Externo', 'DataVault', 2, 110, 120.00, 0.03, 0.18, (120.00 * (1 + 0.03) * (1 + 0.18))),
('Carregador Portátil', 'PowerUp', 3, 130, 25.00, 0.02, 0.2, (25.00 * (1 + 0.02) * (1 + 0.2))),
('Cabo USB', 'LinkCable', 4, 140, 10.00, 0.01, 0.15, (10.00 * (1 + 0.01) * (1 + 0.15))),
('Hub USB', 'ConnectAll', 5, 105, 15.00, 0.01, 0.18, (15.00 * (1 + 0.01) * (1 + 0.18))),
('Adaptador HDMI', 'ScreenLink', 6, 85, 20.00, 0.01, 0.2, (20.00 * (1 + 0.01) * (1 + 0.2))),
('Case para HD', 'SafeCase', 7, 100, 8.00, 0.005, 0.15, (8.00 * (1 + 0.005) * (1 + 0.15))),
('Cooler para Notebook', 'CoolDown', 1, 65, 12.00, 0.005, 0.2, (12.00 * (1 + 0.005) * (1 + 0.2))),
('Pendrive', 'DataDrive', 2, 115, 18.00, 0.005, 0.18, (18.00 * (1 + 0.005) * (1 + 0.18))),
('Placa de Vídeo', 'Graphix', 3, 45, 300.00, 0.07, 0.3, (300.00 * (1 + 0.07) * (1 + 0.3))),
('Memória RAM', 'SpeedRAM', 4, 55, 80.00, 0.03, 0.25, (80.00 * (1 + 0.03) * (1 + 0.25))),
('Processador', 'SpeedCore', 5, 50, 250.00, 0.06, 0.35, (250.00 * (1 + 0.06) * (1 + 0.35))),
('Placa-Mãe', 'CoreBoard', 6, 30, 150.00, 0.05, 0.3, (150.00 * (1 + 0.05) * (1 + 0.3)));

INSERT INTO produto (nome, marca, empresa, estoque, valor_bruto, imposto, margem_lucro, valor_final) VALUES
('Mesa', 'TOPTOP', 20, 800, 155.00, 0.099, 0.60, (155.00 * (1 + 0.099) * (1 + 0.60)));


-- Gerando 50 registros de clientes com itens comprados variando de 1 a 20
INSERT INTO cliente (nome, cpf, data_nascimento, celular, email, item_comprado) VALUES 
('João Silva', 12345678901, 19900101, 11987654321, 'joao@example.com', 1),
('Maria Santos', 98765432109, 19851225, 11888888888, 'maria@example.com', 2),
('Carlos Oliveira', 45678912345, 19780315, 11777777777, 'carlos@example.com', 3),
('Ana Souza', 12309876543, 19870228, 11999999999, 'ana@example.com', 4),
('Pedro Lima', 54321678901, 19930415, 11666666666, 'pedro@example.com', 5),
('Juliana Pereira', 98712345678, 19801020, 115, 'juliana@example.com', 6),
('Mariana Castro', 65498732101, 19850912, 11444444444, 'mariana@example.com', 7),
('Fernando Santos', 98765432101, 19820507, 11333333333, 'fernando@example.com', 8),
('Lucas Oliveira', 45632178901, 19890730, 11222222222, 'lucas@example.com', 9),
('Gabriela Silva', 32198765432, 19980125, 11888888888, 'gabriela@example.com', 10),
('Bruno Souza', 12365498701, 19841218, 11777777777, 'bruno@example.com', 11),
('Patrícia Lima', 98745632109, 19800210, 11666666666, 'patricia@example.com', 12),
('Rafaela Pereira', 65412398701, 19900905, 115, 'rafaela@example.com', 13),
('Thiago Castro', 32178965401, 19760703, 11444444444, 'thiago@example.com', 14),
('Vanessa Santos', 78965412301, 19890115, 11333333333, 'vanessa@example.com', 15),
('Rodrigo Oliveira', 98765412309, 19811228, 11222222222, 'rodrigo@example.com', 16),
('Camila Silva', 45678932101, 19950410, 11888888888, 'camila@example.com', 17),
('Diego Souza', 12398745601, 19830807, 11777777777, 'diego@example.com', 18),
('Aline Lima', 98765412301, 19921120, 11666666666, 'aline@example.com', 19),
('Marcela Pereira', 65432198701, 19790415, 115, 'marcela@example.com', 20),
('Roberto Castro', 32165498701, 19860518, 11444444444, 'roberto@example.com', 1),
('Laura Santos', 78912365401, 19930928, 11333333333, 'laura@example.com', 2),
('Gustavo Oliveira', 98765432101, 19800710, 11222222222, 'gustavo@example.com', 3),
('Isabela Silva', 45698732109, 19850105, 11888888888, 'isabela@example.com', 4),
('Ricardo Souza', 12378965401, 19980320, 11777777777, 'ricardo@example.com', 5),
('Tatiane Lima', 98745612309, 19730815, 11666666666, 'tatiane@example.com', 6),
('Vinícius Pereira', 65412378901, 19870910, 115, 'vinicius@example.com', 7),
('Carolina Castro', 32198765401, 19801103, 11444444444, 'carolina@example.com', 8),
('Luiz Santos', 78932165401, 19911028, 11333333333, 'luiz@example.com', 9),
('Nathália Oliveira', 98765412301, 19760214, 11222222222, 'nathalia@example.com', 10),
('Paulo Silva', 45678912309, 19840430, 11888888888, 'paulo@example.com', 11),
('Fernanda Souza', 12365478901, 19920405, 11777777777, 'fernanda@example.com', 12),
('André Lima', 98712345601, 19820908, 11666666666, 'andre@example.com', 13),
('Beatriz Pereira', 65498712301, 19780923, 115, 'beatriz@example.com', 14),
('José Castro', 32178965401, 19951210, 11444444444, 'jose@example.com', 15),
('Sandra Santos', 78965432101, 19821205, 11333333333, 'sandra@example.com', 16),
('Leandro Oliveira', 98765432109, 19770818, 11222222222, 'leandro@example.com', 17),
('Cristina Silva', 45632198701, 19931007, 11888888888, 'cristina@example.com', 18),
('Daniel Souza', 12365498709, 19860412, 11777777777, 'daniel@example.com', 19),
('Renata Lima', 98745632101, 19910417, 11666666666, 'renata@example.com', 20),
('Luciana Pereira', 65412398701, 19721030, 115, 'luciana@example.com', 1),
('Marcos Castro', 32165412301, 19890525, 11444444444, 'marcos@example.com', 2),
('Simone Santos', 78912365401, 19830518, 11333333333, 'simone@example.com', 3),
('Henrique Oliveira', 98765432101, 19980410, 11222222222, 'henrique@example.com', 4),
('Catarina Silva', 45698732109, 19810715, 11888888888, 'catarina@example.com', 5),
('Lucas Souza', 12378965401, 19761020, 11777777777, 'lucas@example.com', 6),
('Mariana Lima', 98745612309, 19941205, 11666666666, 'mariana@example.com', 7),
('Diego Pereira', 65412378901, 19800308, 115, 'diego@example.com', 8),
('Carla Castro', 32198765401, 19960214, 11444444444, 'carla@example.com', 9),
('Roberto Santos', 78932165401, 19811227, 11333333333, 'roberto@example.com', 10);

INSERT INTO cliente (nome, cpf, data_nascimento, celular, email, item_comprado) VALUES 
('João Silva', 12345678901, 19900101, 11987654321, 'joao@example.com', 11);

SELECT 
	p.nome AS produto, e.nome_fantasia AS empresa
FROM 
	produto p
JOIN 
	empresa e ON p.empresa = e.id;

----- atividade 01 -----
SELECT 
	p.nome, p.estoque
FROM 
	produto p
WHERE 
	p.empresa = 1;

----- atividade 02 -----
SELECT 
    a.nome AS NOME_EMPRESA, 
    b.nome AS NOME_PRODUTO,
    b.estoque AS ESTOQUE
    
FROM 
	produto b 
    INNER JOIN empresa a ON b.empresa = a.id
WHERE 
    a.id = 2;

----- atividade 03 -----
SELECT 
	p.nome, p.estoque * p. valor_final AS valor_total_estoque
FROM 
	produto p 
JOIN 
	produto p1 ON p.id = p1.id;

----- atividade 10 -----
select
	b.nome_fantasia,
    truncate((total.soma / total.qtd),2) as media 
from(
	select 
		a.empresa,
        sum(a.valor_final) as soma
	from
		produto as a
	group by
		a.empresa
) as total
        
join
	empresa as b on total.empresa = b.id
group by
    b.nome_fantasia;