# 37. Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu
# N’nésimo termo
numero = int(input("Insira um número inteiro: "))

termo1 = 0
termo2 = 1
contador = 1

while contador <= numero:
    print(termo1)
    proximo_termo = termo1 + termo2
    termo1 = termo2
    termo2 = proximo_termo
    contador += 1

print(f"O {numero}° termo da sequência de Fibonacci é: {termo1}")
