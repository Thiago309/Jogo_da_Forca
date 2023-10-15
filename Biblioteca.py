import random
def game():

    lista_palavras = ["python", "programacao", "jogos", "desenvolvimento", "computador", "tecnologia"]

    palavra = random.choice(lista_palavras)
    tentativas = 4
    letras_corretas = []
    letras_erradas = []
    acertos = 0

    # Função para mostrar a palavra com letras adivinhadas
    def mostrar_palavra():
        resultado = ""
        for letra in palavra:
            if letra in letras_corretas:
                resultado += letra
            else:
                resultado += "_ "
        return resultado

    # Loop principal do jogo
    while acertos < len(palavra) and len(letras_erradas) < tentativas:
        print("\nPalavra: " + mostrar_palavra())
        print("Letras erradas: " + ", ".join(letras_erradas))

        palpite = input("Digite uma letra: ").lower()

        if len(palpite) != 1 or not palpite.isalpha():
            print("Por favor, digite uma única letra válida.")
            continue

        if palpite in palavra:
            letras_corretas.append(palpite)
            acertos = mostrar_palavra().count(palpite)
        else:
            letras_erradas.append(palpite)

        # Figura da forca
        print("\nForca:")
        if len(letras_erradas) >= 1:
            print("____________")
            print("           |")
        else:
            print("|")
        if len(letras_erradas) >= 2:
            print("|.         @")
        else:
            print("|")
        if len(letras_erradas) >= 3:
            print("|.        /|\\")
        else:
            print("|")
        if len(letras_erradas) >= 4:
            print("|.        / \\")
        else:
            print("|")

    if acertos == len(palavra):
        print(f"\nVocê ganhou! A palavra era: {palavra}.")
        print("Tente novamente")

    else:
        print(f"\nVocê perdeu! A palavra era: {palavra}")
        print("Tente novamente!")
 