"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero = input("Digite o numero a ser checado: ")


# if (numero.isdigit):
#     numero_int = int(numero)

#     if (numero_int % 2 == 0):
#         print(F"{numero_int} igual a par")
#     else:
#         print(F"{numero_int} = impar")
        
# else:
#     print("Numero nao inteiro")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# horario = input("Que horas sao?")

# if horario.isdigit():
#     horario_int = int(horario)

#     if (horario_int >= 0 and horario_int <= 11):
#         print(f"Sao {horario_int}, portanto bom dia lindo")
#     elif (horario_int > 11 and horario_int <= 17):
#         print(f"Sao {horario_int}, portanto boa tarde lindo")
#     else:
#         print(f"Sao {horario_int}, portanto boa noite lindo")

# else:
#     print("Horario digitado incorretamente")



# entrada = input('Digite a hora em números inteiros: ')

# try:
#     hora = int(entrada)

#     if hora >= 0 and hora <= 11:
#         print('Bom dia')
#     elif hora >= 12 and hora <= 17:
#         print('Bom tarde')
#     elif hora >= 18 and hora <= 23:
#         print('Bom noite')
#     else:
#         print('Não conheço essa hora')
# except:
#     print('Por favor, digite apenas números inteiros')





"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Qual seu nome?")
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print("Seu nome eh curto.")
    elif tamanho_nome == 5 and tamanho_nome <= 6:
        print("Seu nome eh normal")
    else:
        print("Seu nome eh gigantesco")
            
else:
    print("Por favor, escreva mais que uma letra")