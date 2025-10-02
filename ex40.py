# 40. Receba 2 números inteiros. Verifique e mostre todos os números primos
# existentes entre eles.
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

if numero1 > numero2:
    inicio = numero2
    fim = numero1
else:
    inicio = numero1
    fim = numero2

print("Números primos entre eles:")
num = inicio
while num <= fim:
    if num > 1:
        divisor = 2
        primo = True
        while divisor <= num // 2:
            if num % divisor == 0:
                primo = False
                break
            divisor += 1
        if primo:
            print(num)
    num += 1
