# 36. Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!
numero = float(input("Digite um número: "))
soma = 1
fatorial = 1
contador = 1

while contador <= numero:
    fatorial *= contador
    soma += 1 / fatorial
    contador += 1

print(f"A soma da série até 1/{numero}! é {soma}")
