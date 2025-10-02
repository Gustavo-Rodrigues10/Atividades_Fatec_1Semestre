# Receba dois valores inteiros e diferentes. Mostre seus valores em ordem crescente.
def ordem_crescente():
    valor_1 = int(input("Digite o primeiro valor: "))
    valor_2 = int(input("Digite o segundo valor: "))

    if valor_1 == valor_2:
        print("Os valores são iguais.")
    elif valor_1 > valor_2:
        print(valor_2, valor_1)
    else:
        print(valor_1, valor_2)

ordem_crescente()