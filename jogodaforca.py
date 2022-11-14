import random
import os

os.system("cls")
tentativa = 0

lista_palavras = ['banana', 'abacaxi','uva','ameixa', 'caqui']
tot_palavras: int = len(lista_palavras)
rand_palavras = random.randint(0, tot_palavras-1)
palavra = lista_palavras[rand_palavras]

acerto = "-" * len(palavra)

print(acerto)

while "-" in acerto:
    
    letra = input('Entre com a letra: ')
    charPos = list(acerto)
    constaAcerto = False
    for pos, char in enumerate(palavra):
        if char == letra:
            charPos[pos] = letra
            acerto = "".join(charPos)
            constaAcerto = True
    if not constaAcerto:
        tentativa += 1
        print(f"Letra não existe nessa palavra, erro {tentativa} de 10")
    if tentativa >= 10:
        print(f"Game Over")
        print(f"a palavra era: {palavra}")
        exit()    
    print("Pista: ", acerto)    
print("Palavra final: ", acerto)