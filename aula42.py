# frase = 'aaaooo'

# i = 0
# qtd_apareceu_mais_vezes = 0
# letra_apareceu_mais_vezes = ''

# while i < len(frase):
#     letra_atual = frase[i]

#     if letra_atual == ' ':
#         i += 1
#         continue

#     qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

#     if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
#         qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
#         letra_apareceu_mais_vezes = letra_atual

#     i += 1

# print(
#     'A letra que apareceu mais vezes foi '
#     f'"{letra_apareceu_mais_vezes}" que apareceu '
#     f'{qtd_apareceu_mais_vezes}x'
# )

# frase = "O python e uma linguagem de programacao multiparadigma. Python foi criado por Guido van Rossum"

# # Qual letra apareceu mais vezes nesta frase?

# i = 0
# qtd_apareceu_mais_vezes = 0
# letra_apareceu_mais_vezes = " "

# while i < len(frase):
#     letra_atual = frase[i]
    

#     if letra_atual == ' ':
#         i += 1
#         continue

#     qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)
    

#     if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
#         qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
#         letra_apareceu_mais_vezes = letra_atual

#     i += 1

# print(f"A letra que apareceu mais vezes foi {qtd_apareceu_mais_vezes_atual}, aparecendo {qtd_apareceu_mais_vezes}X")
import random

palpite = None
numero = random.randint(1, 50)


while palpite != numero:
    palpite = int(input("Digite um numero entre 1 e 50: "))
    if numero > palpite:
        print("Numero certo eh mais alto")
    elif numero < palpite:
        print("Numero certo eh mais baixo")
    else:
        print(f"voce acertou, o numero era {numero}")
    

