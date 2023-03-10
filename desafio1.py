"""
    DADA UMA VENDA PELO USUÁRIO, CALCULAR 12% DE DESCONTO CASO A VENDA SEJA
    MAIOR DO QUE 500, SENÃO O DESCONTO SERÁ DE 6%. NO FINAL, EXIBIR O VALOR DA VENDA.
"""

# obter valor da venda e defenir a % de desconto
venda = float(input("Digite o valor da venda: "))
descontoMaior = 12
descontoMenor = 6

# aplicar desconto caso a condição seja verdadeira
if venda > 500:
    venda = venda - (venda / 100 * descontoMaior)
else:
    venda = venda - (venda / 100 * descontoMenor)

# exibir valor da venda com desconto
print(f"O valor com desconto é de: {venda}")