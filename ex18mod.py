# Receba dois valores inteiros. Calcule e mostre a diferença do maior pelo menos valor
def calcular_diferenca():
    numero_a = int(input("Digite o primeiro valor inteiro: "))
    numero_b = int(input("Digite o segundo valor inteiro: "))

    if numero_a > numero_b:
        diferenca = numero_a - numero_b
    else:
        diferenca = numero_b - numero_a

    print(f"O resultado da diferença do maior pelo menor valor é: {diferenca}")

calcular_diferenca()
