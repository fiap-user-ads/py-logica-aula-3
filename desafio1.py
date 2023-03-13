"""
    DADA UMA VENDA PELO USUÁRIO, CALCULAR 12% DE DESCONTO CASO A VENDA SEJA
    MAIOR DO QUE 500, SENÃO O DESCONTO SERÁ DE 6%. NO FINAL, EXIBIR O VALOR DA VENDA.
"""

# obter valor da venda e definir a % de desconto
venda = float(input("Digite o valor da venda: "))

descontoMaior = 0.88 # 0.96 == 12%
descontoMenor = 0.94 # 0.96 == 6%

# aplicar desconto caso a condição seja verdadeira
if venda > 500:
    venda = venda * descontoMaior
else:
    venda = venda * descontoMenor

# exibir valor da venda com desconto
print(f"O valor com desconto é de: {venda}")
