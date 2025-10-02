# 35. Receba 2 números inteiros, verifique qual o maior entre eles. Calcule e
# mostre o resultado da somatória dos números ímpares entre esses valores.
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

if numero1 > numero2:
    maior = numero1
    menor = numero2
else:
    maior = numero2
    menor = numero1

soma_impares = 0
contador = menor

while contador <= maior:
    if contador % 2 != 0:
        soma_impares += contador
    contador += 1

print(f"A soma dos números ímpares entre {menor} e {maior} é {soma_impares}")
