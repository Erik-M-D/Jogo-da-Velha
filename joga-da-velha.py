import random
from os import system, name
import re

# Função para limpar a tela a cada execução


def limpa_tela():
    # Windows
    if name == "nt":
        _ = system("cls")
        
    # Mac ou Linux
    else:
        _ = system("clear")


# Função que desenha

def display_hangman(chances):
    
    #Lista de estágios da forca
    estagios = [ #Estagio 6 [final]
                """
                    ----------
                    |        |
                    |        O
                    |       \|/
                    |        |
                    |       / \
                """,
                #Estagio 5 
                """
                    ----------
                    |        |
                    |        O
                    |       \|/
                    |        |
                    |       / 
                """,
                #Estagio 4 
                """
                    ----------
                    |        |
                    |        O
                    |       \|/
                    |        |
                    |                   
                """,
                #Estagio 3 
                """
                    ----------
                    |        |
                    |        O
                    |       \|/
                    |        
                    |       
                """,
                #Estagio 2
                """
                    ----------
                    |        |
                    |        O
                    |       \|
                    |        
                    |       
                """,                
                #Estagio 1
                """
                    ----------
                    |        |
                    |        O
                    |       
                    |        
                    |       
                """,
                #Estagio 0
                """
                    ----------
                    |        |
                    |        
                    |       
                    |        
                    |       
                """,
        ]
    return estagios[chances]

# Função

#Verifica se está válido a entrada de dados!
def check_tentativa(letras_erradas, letras_descobertas):
    
    while True:
        tentativa = input("\nDigite uma letra: ").lower()
        try:
            if tentativa in letras_descobertas or tentativa in letras_erradas:
                raise ValueError("Letra já usada!")
            elif not re.match(r'^[a-z]$', tentativa):
                raise ValueError("Entrada inválida: não é uma letra única entre A-Z")
            else: 
                break
        except ValueError as ve:
            print(f'\nErro: {ve}')
        
    return tentativa

def game():
    
    limpa_tela()
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Advinhe a palavra abaixo:\n")
    
    
    
    #lista de palavras para o jogo
    palavras = ['coco', 'banana', 'laranja', 'uva', 'morango', 'abacaxi', 'manga', 'melancia', 'kiwi', 'pera', 'jabuticaba', 'ameixa', 'cereja', 'amora', 'abacate']
    
    #Estagio
    
    
    # Escolhe randomicamente uma palavra
    palavra = random.choice(palavras)
    
    # Lista da palavra oculta
    letras_descobertas = ['_' for letra in palavra]
    
    #Numero de chances
    chances = 6
    
    
    
    # Lista para as palavras erradas
    letras_erradas = []
    
    # Loop enquanto número de chances for maior que zero
    while chances > 0:
        
        #Print
        ## Display Boneco
        print(display_hangman(chances),"\n")
        print(" ".join(letras_descobertas))
        print(f"\nChances restantes: {chances}")
        # print(f"\nLetras erradas: {' '.join(letras_erradas)}")
        print("letras erradas:", " ".join(letras_erradas))
        
        #Tentativa é o retorno de check_tentativa
      
        tentativa = check_tentativa(letras_erradas, letras_descobertas)
        
        #Teste de função verificação de LETRA
        
        # Condicional 1
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        
        else:
            chances -= 1
            letras_erradas.append(tentativa)
                    
        # Condicional 2
        if "_" not in letras_descobertas:
            print(f"\nVocê venceu! A palavra era: {palavra}")
            break
        
    # Condicional 3
    if "_" in letras_descobertas:
        print(f"\nVocê perdeu! A palavra era: {palavra}")


# Bloco MAIN

if __name__ == "__main__":
    game()
    print("\nParabéns. você está aprendendo programação em Python com a DSA :)\n")


