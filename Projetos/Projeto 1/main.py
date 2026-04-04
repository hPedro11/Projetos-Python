# Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.

def cal_conta():
    vl_conta = float(input("Digite o valor da conta: "))
    gorjeta = float(input("Digite a porcentagem da gorjeta: "))
    vl_gorjeta= vl_conta * (gorjeta / 100)
    vl_total = vl_conta + vl_gorjeta
    print(f"O valor da gorjeta foi: {vl_gorjeta}\nTotal à ser pago é: {vl_total}")

cal_conta()