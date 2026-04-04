# Crie um programa que peça ao usuário um número de CPF e verifique se ele tem 11 dígitos e contém apenas números.

def verificador_cpf(cpf):
    if not cpf.isdigit():
        return "Erro: O CPF deve conter apenas números."
    if len(cpf) != 11:
        return "Erro: O CPF deve ter exatamente 11 dígitos."
    return "CPF válido."

cpf = input("Digite seu CPF: ")
print(verificador_cpf(cpf))   