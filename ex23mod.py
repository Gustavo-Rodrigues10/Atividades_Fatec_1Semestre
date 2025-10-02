# Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.
def ordenar_valores():
    valor1 = float(input("Digite o primeiro valor (em ordem crescente): "))
    valor2 = float(input("Digite o segundo valor (em ordem crescente): "))
    valor3 = float(input("Digite o terceiro valor (em ordem crescente): "))
    valor4 = float(input("Digite o quarto valor (não necessariamente em ordem): "))

    if valor4 < valor1:
        print(valor4, valor1, valor2, valor3)
    elif valor4 < valor2:
        print(valor1, valor4, valor2, valor3)
    elif valor4 < valor3:
        print(valor1, valor2, valor4, valor3)
    else:
        print(valor1, valor2, valor3, valor4)

ordenar_valores()
