# 30. Receba a data de nascimento e atual em ano, mês e dia. Calcule e mostre a
# idade em anos, meses e dias, considerando os anos bissextos.
def calcular_idade():
    diaNascimento = int(input("Digite o dia de seu nascimento: "))
    mesNascimento = int(input("Digite o mês de seu nascimento: "))
    anoNascimento = int(input("Digite o ano de seu nascimento: "))

    diaAtual = int(input("Digite o dia de hoje: "))
    mesAtual = int(input("Digite o mês atual: "))
    anoAtual = int(input("Digite o ano atual: "))

    anosTotais = anoAtual - anoNascimento
    mesesTotais = 0
    diasTotais = 0

    if mesAtual > mesNascimento:
        mesesTotais = mesAtual - mesNascimento - 1
        if diaAtual >= diaNascimento:
            mesesTotais += 1
            diasTotais = diaAtual - diaNascimento
        else:
            diasTotais = 30 - diaNascimento + diaAtual

    elif mesAtual < mesNascimento:
        mesesTotais = 12 - mesNascimento + mesAtual - 1
        if diaAtual >= diaNascimento:
            mesesTotais += 1
            diasTotais = diaAtual - diaNascimento
        else:
            diasTotais = 30 - diaNascimento + diaAtual

    else:
        if diaAtual >= diaNascimento:
            diasTotais = diaAtual - diaNascimento
            mesesTotais = 0
        else:
            diasTotais = 30 - diaNascimento + diaAtual
            mesesTotais = -1  # Ajuste se necessário

    print(f"Você tem {anosTotais} anos, {mesesTotais} meses e {diasTotais} dias.")

calcular_idade()
