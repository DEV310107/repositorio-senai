create database levantamento
use levantamento

create table pessoas(
    id int auto_increment,
    name varchar(15),
    street varchar(15),
    city varchar(15),
    state char(10),
    credit_limit decimal(7,2),
    primary key(id)

);

insert into pessoas (name,street,city,state,credit_limit,)
values
("Pedro Augusto da Rocha", "Rua Pedro Carlos Hoffman", 	"Porto Alegre", "Porto Alegre","RS", "700,00"),
("Antonio Carlos Mamel", "Av. Pinheiros", "	Belo Horizonte","MG", "3500,50"),
("Luiza Augusta Mhor", "Rua Salto Grande", "Niteroi","RJ","4000,00"  ),
("Jane Ester", "Av 7 de setembro", "Erechim","RS","800,00" ),
("Marcos Antônio dos Santos", "Av Farrapos", "Porto Alegre","RS","4250,25" ),

select
    id,
    name,
    street,
    city,
    state,
    credit_limit

from
    pessoas
where
    state = RS
order by
    state asc