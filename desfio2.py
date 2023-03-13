"""
    DADA UMA VENDA PELO USUÁRIO E SE ELE TME OU NÃO UM CUPOM DE DESCONTO,
    CALCULAR 12% DE DESCONTO CASO A VENDA SEJA MAIOR DO QUE 500, 
    SENÃO O DESCONTO SERÁ DE 6%. CASO ELE TENHA O CUPOM, EFETUAR MAIS
    50 REAIS DE DESCONTO.
"""

# obter valor da venda e defenir a % de desconto
venda = float(input("Digite o valor da venda: "))
cupom = input("Você tem um cupom de desconto? [s]im ou [n]ão? ");

descontoMaior = 0.88 # 0.96 == 12%
descontoMenor = 0.94 # 0.96 == 6%

# aplicar desconto caso a condição seja verdadeira
# &&
# aplicar desconto do cupom caso seja verdadeira
if venda > 500:
    venda = venda * descontoMaior
else:
    venda = venda * descontoMenor

if cupom == "s":
    venda = venda - 50;

# exibir valor da venda com o desconto total
print(f"O valor com desconto é de: {venda}")
