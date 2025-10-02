# Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço
# sabendo que:
# Venda Mensal       Preço atual        Preço Novo
# < 500              <30                +10%
# >= 500 e < 1000    >= 30 e < 80       +15%
# >= 1000            >= 80              -5%

# Observação: Para outras condições, preço novo será igual preço atual.
preco_atual = float(input("Digite o preço atual do produto: "))
venda_mensal = float(input("Digite a venda mensal do produto: "))

if venda_mensal < 500 and preco_atual < 30:
    preco_novo = preco_atual * 1.10
elif 500 <= venda_mensal < 1000 and 30 <= preco_atual < 80:
    preco_novo = preco_atual * 1.15
elif venda_mensal >= 1000 and preco_atual >= 80:
    preco_novo = preco_atual * 0.95
else:
    preco_novo = preco_atual

print(f"O novo preço do produto é: {preco_novo}")
