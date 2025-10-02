# Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3° ângulo
angulo1 = float(input("Digite o valor do primeiro ângulo do triângulo: "))
angulo2 = float(input("Digite o valor do segundo ângulo do triângulo: "))
soma_total = 180.0

angulo3 = soma_total - (angulo1 + angulo2)

print(f"O valor do terceiro ângulo é: {angulo3} graus")