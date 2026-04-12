# Crie um programa que gere uma senha aleatória de 12 caracteres, contendo pelo menos uma letra maiúscula, uma minúscula, 
# um número e um caractere especial. Exiba a senha gerada.

import random
import string

def gerador_senha(tamanho):
    maiusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    pontuacao = string.punctuation
    senha = ""

    for _ in range(tamanho):
        senha += random.choice(maiusculas + minusculas + numeros + pontuacao)

    return f"Sua senha é: {senha}"

print(gerador_senha(12))