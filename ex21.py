# Receba quatro notas bimestrais de um aluno. Calcule e mostre a média aritmética.
# Mostre a mensagem de acordo com a média:
# Se a média for >= 6,0 exibir "APROVADO";
# Se a média for >= 3,0 E < 6,0 exibir "EXAME";
# Se a média for < 3,0 exibir "RETIDO";
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))
nota_4 = float(input("Digite a quarta nota: "))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print(f"A média aritmética do aluno é {media}")

if media >= 6.0:
    print("Aprovado")
elif media < 3.0:
    print("Retido")
else:
    print("Exame")