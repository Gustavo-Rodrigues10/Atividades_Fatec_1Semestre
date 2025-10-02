# Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de dependentes. Calcule o salário
# que serão as horas trabalhadas x o valor por hora. Calcule o salário líquido (= Salário Bruto - desconto). A cada dependente será
# acrescido R$ 100 no salário líquido. Exiba o salário a receber.
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valor_hora = float(input("Digite o valor recebido por hora (R$): "))
percentual_desconto = float(input("Digite o percentual de desconto (ex: 15 para 15%): "))
numero_dependentes = int(input("Digite o número de dependentes: "))

salario_bruto = horas_trabalhadas * valor_hora
valor_desconto = salario_bruto * (percentual_desconto / 100)
salario_base = salario_bruto - valor_desconto
bonus_dependentes = numero_dependentes * 100
salario_final = salario_base + bonus_dependentes

print(f"O salário bruto é: R$ {salario_bruto}")
print(f"O desconto total é: R$ {valor_desconto}")
print(f"O salário a receber (líquido + bônus) é: R$ {salario_final}")