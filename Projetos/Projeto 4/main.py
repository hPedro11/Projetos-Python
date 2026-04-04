# Crie um programa que receba um texto e exiba todas as palavras que possuem mais de 10 letras. 
# Caso nenhuma palavra longa seja encontrada, o programa deve avisar o usuário.

def palavras_longas():
    texto = input("Digite um texto: ")
    palavras_encontradas = []
    
    for palavra in texto.split():
        if len(palavra) > 10:
            palavras_encontradas.append(palavra)

    if palavras_encontradas:
        print("Palavras longas encontradas: ", ", ".join(palavras_encontradas))
    else:
        print("Nenhuma palavra longa foi encontrada no texto.")

    # if palavras_longas:
    #     print("Palavras longas encontradas:")
    # for palavra in palavras_longas:
    #     print(palavra)
    # else:
    #     print("Nenhuma palavra longa foi encontrada no texto.")

palavras_longas()