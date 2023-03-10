"""
    DADA UMA VENDA PELO USUÁRIO E SE ELE TME OU NÃO UM CUPOM DE DESCONTO,
    CALCULAR 12% DE DESCONTO CASO A VENDA SEJA MAIOR DO QUE 500, 
    SENÃO O DESCONTO SERÁ DE 6%. CASO ELE TENHA O CUPOM, EFETUAR MAIS
    50 REAIS DE DESCONTO.
"""

# obter valor da venda e defenir a % de desconto
cupom = input("Você tem um cupom de desconto [s][n]: ");
venda = float(input("Digite o valor da venda: "))
descontoMaior = 12
descontoMenor = 6

# aplicar desconto caso a condição seja verdadeira
# &&
# aplicar desconto do cupom caso seja verdadeira
if venda > 500:
    venda = venda - (venda / 100 * descontoMaior)
else:
    venda = venda - (venda / 100 * descontoMenor)
    
if cupom == "s":
    venda = venda - 50;

# exibir valor da venda com o desconto total
print(f"O valor com desconto é de: {venda}")
