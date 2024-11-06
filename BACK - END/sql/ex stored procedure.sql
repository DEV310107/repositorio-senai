delimiter //
    create procedure calcular_desconto(in valor_prod int, out desconto int)
    begin
        set desconto = valor_prod -(valor_prod * 0.1);
    end //
delimiter //;

set @resultado = 0;
call calcular_desconto (100, @resultado);
select @resultado;


DELIMITER novo_delimitador




SELECT coluna1, coluna2, ...
INTO @variavel1, @variavel2, ...
FROM tabela
WHERE condição;



SET @variavel_resultado = operação_matemática;


ADIÇÃO
SET @soma = valor1 + valor2;

SUBTAÇÃO
SET @diferenca = valor1 - valor2;

MULTIPLICAÇÃO
SET @produto = valor1 * valor2;

DIVISÃO
SET @divisao = valor1 / valor2;




CREATE PROCEDURE CalcularSalarioAnual(IN salario_mensal DECIMAL(10, 2))
BEGIN
    DECLARE salario_anual DECIMAL(10, 2);
    SET salario_anual = salario_mensal * 12;
    
    SELECT salario_anual AS 'Salário Anual';
END;


