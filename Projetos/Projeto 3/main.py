# Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.

def contador_vogais(texto):
    vogais = ["a", "e", "i", "o", "u"]
    total = 0
    for vogal in vogais:
        total += texto.count(vogal)
    return f"O texto contém {total} vogais."

palavra = input("Digite um texto: ").lower()
print(contador_vogais(palavra))