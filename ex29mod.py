# Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento.
# Calcule e mostre o valor corrigido em 30 dias, sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos serão desconsiderados.
def calcular_valor_investimento():
    tipo_investimento = int(input("Digite o tipo de investimento (1 = poupança, 2 = renda fixa): "))
    valor_investimento = float(input("Digite o valor do investimento: "))

    if tipo_investimento == 1:
        valor_corrigido = valor_investimento * 1.03
    elif tipo_investimento == 2:
        valor_corrigido = valor_investimento * 1.05
    else:
        valor_corrigido = valor_investimento

    print(f"O valor corrigido em 30 dias é: {valor_corrigido}")

calcular_valor_investimento()
