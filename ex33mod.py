# 33. Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.
def calcular_serie():
    numero = int(input("Digite um número: "))
    soma = 0
    contador = 1

    while contador <= numero:
        soma += 1 / contador
        contador += 1

    print(f"A soma da série até {numero} é {soma}")

calcular_serie()
