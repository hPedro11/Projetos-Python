# Sua tarefa é criar um programa que gere um número aleatório entre 1 e 100 e permita que o usuário tente adivinhar o número. 
# O programa deve informar se o palpite é maior ou menor que o número correto, até que o usuário acerte. 
# Se o usuário digitar um valor inválido ou um número fora do intervalo, uma exceção ValueError deve ser lançada.

import random

def adivinha():
    # Gerando número aleatorio.
    numero = random.randint(1, 100)
    
    # Laço de repetição
    while True:
        try:
            usuario = int(input("Tente adivinhar o número (1-100): "))
        except ValueError:
            print(f"Entrada inválida: invalid literal for int() with base 10: {usuario}")
            continue # Reincia o loop.

        # Validando entrada do usúario dentro do intervalo
        if usuario > 100:
            raise ValueError("Entrada inválida: Número fora do intervalo! Digite um número entre 1 e 100.") # O raise lança o erro.
        elif usuario < 1:
            raise ValueError("Entrada inválida: Número fora do intervalo! Digite um número entre 1 e 100.")
        else:
            print(f"Número escolhido: {usuario}")

        # Condições de tentativa
        if usuario == numero:
            print(f"Parabéns! Você acertou o número {numero}")
            break
        elif usuario < numero:
            print(f"Muito baixo! Tente novamente: {usuario}")
        else:
            print(f"Muito alto! Tente novamente: {usuario}")
    
adivinha()