# Receba 2 valores reais. Calcule e mostre o maior deles.
def calcular_maior_valor():
    valor1 = float(input("Digite o primeiro valor real: "))
    valor2 = float(input("Digite o segundo valor real: "))

    if valor1 > valor2:
        maior_valor = valor1
    else:
        maior_valor = valor2

    print(f"O maior valor é: {maior_valor}")

calcular_maior_valor()
