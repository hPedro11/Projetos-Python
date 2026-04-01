# Calculando a gorjeta em um restaurante

# João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes deixam ao pagar a conta. O restaurante sugere uma gorjeta de 10%, 
# mas alguns clientes podem escolher dar mais ou menos.
# Para agilizar o processo, João quer um programa que receba o valor total da conta e a porcentagem de gorjeta desejada e exiba o valor final que o cliente deverá pagar.
# Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.

def cal_conta():
    vl_conta = float(input("Digite o valor da conta: "))
    gorjeta = float(input("Digite a porcentagem da gorjeta: "))
    vl_gorjeta= vl_conta * (gorjeta / 100)
    vl_total = vl_conta + vl_gorjeta
    print(f"O valor da gorjeta foi: {vl_gorjeta}\nTotal à ser pago é: {vl_total}")

cal_conta()