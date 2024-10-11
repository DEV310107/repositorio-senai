create database kitanda02;
use kitanda02;

create table produtos(
	id int auto_increment,
    tipo varchar(15) not null,
    nome varchar(15) not null,
    quantidade int(5) not null,
    valor decimal(10, 2) not null,
    primary key(id)
);


insert into produtos (tipo, nome, quantidade, valor)
values
("vegetal","alface", "30", "1.20"),
("Hortaliça","couve" , "20" , "1.50"),
("fruta","abacate", "12" , "4.00"),
("fruta","laranja", "40", "1.30"),
("fruta","maça","25","1.80"),
("fruta","banana","50","1.00"),
("fruta","manga","15","2.50"),
("fruta","limao","60","0.75");

-- retorna todos os registros da tabela "produtos"--
select
	id,
    tipo,
    nome,
    quantidade,
    valor as valor_uni,
    (quantidade * valor_uni) as valor_total
    
from
	produtos 
where
	quantidade > 10
order by   
	quantidade asc
-- sera ordenado de forma crescente --
    
