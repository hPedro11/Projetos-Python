# Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura. 
# O computador escolherá aleatoriamente uma opção. O programa deve exibir quem venceu a partida. Lembrando que:

# Pedra ganha de Tesoura (Pedra quebra Tesoura);
# Tesoura ganha de Papel (Tesoura corta Papel);
# Papel ganha de Pedra (Papel cobre Pedra);
# Se ambos escolherem a mesma opção, é um empate.

import random

def jogo():
    opcoes = ["pedra", "papel", "tesoura"]
    escolha = input("Escolha: pedra, papel ou tesoura? ").lower()
    if escolha not in opcoes:
        print(f"Opção inválida. Por favor escolha uma das opções.")


    computador = random.choice(opcoes)
    print(f"Computador escolheu: {computador}")

    if escolha == computador:
        print("Empate!")
    elif (escolha == "pedra" and computador == "tesoura" or escolha == "tesoura" and computador == "papel" or escolha == "papel" and computador == "pedra"):
        print("Você venceu!")
    else:
        print("Você perdeu!")

jogo()