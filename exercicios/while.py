
# somaidades = 0
# contadordepessoas = 0
# media = 0

# idade = int(input("Digite as idades: "))    
# if idade < 0:
#     print("Impossivel calcular")
# else:
    
#     while idade > 0:
#         contadordepessoas += 1
#         somaidades = idade + somaidades
#         idade = int(input("Digite as idades: "))
#         media = somaidades / contadordepessoas
#     print(f"Media = {media:.2f}")

# Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de
# senha incorreta informada, escrever a mensagem "Senha Invalida! Tente novamente:". Quando a senha
# for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo
# encerrado. Considere que a senha correta é o valor 2002.


# senha_correta = "2002"
# senha = input("Digite a senha: ")
# while senha != senha_correta:
#     senha = input("Senha invalida! Tente novamente: ")
# print("Acesso permitido")

# Problema "quadrante" (adaptado de URI 1115)
# Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no
# sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence (Q1, Q2, Q3 ou Q4). O
# algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem
# escrever mensagem alguma).



# print("Digite as coordenadas x e y")
# x = int(input())
# y = int(input())

# while x and y != 0:
    
#     if x > 0 and y > 0:
#         print("Quadrante Q1")
#     elif x < 0 and y > 0:
#         print("Quadrante Q2")
#     elif x < 0 and y < 0:
#         print("Quadrante Q3")
#     else:
#         print("Quadrante Q4")

#     print("Digite as coordenadas x e y")
#     x = int(input())
#     y = int(input())

# Problema "validacao_de_nota" (adaptado de URI 1117)
# Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a
# média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao
# intervalo [0,10]). Cada nota deve ser validada separadamente. 

# nota1 = float(input("Digite a primeira nota: "))

# while nota1 < 0 or nota1 > 10:
#     nota1 = float(input("Valor invalido! Tente novamente: "))


# nota2 = float(input("Digite a primeira nota: "))    

# while nota2 < 0 or nota2 > 10:
#     nota2 = float(input("Valor invalido! Tente novamente: "))

# media = (nota1 + nota2) / 2

# print(f"Media = {media}")

# Problema "combustivel" (adaptado de URI 1134)
# Um posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes.
# Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma:
# 1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a
# 4) deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o
# código informado for o número 4, devendo então mostrar a mensagem "MUITO OBRIGADO", bem
# como as quantidades de cada combustível. 

# tipo = int(input("Informe um codigo (1, 2, 3) ou 4 para parar: "))
# alcool = 0
# gasolina = 0
# diesel = 0

# while tipo != 4:
#     if tipo == 1:
#         alcool += 1 
#     elif tipo == 2:
#         gasolina += 1
#     elif tipo == 3:
#         diesel += 1
#     tipo = int(input("Informe um codigo (1, 2, 3) ou 4 para parar: "))

# print("Muito Obrigado")
# print(f"Alcool: {alcool}")
# print(f"Gasolina: {gasolina}")
# print(f"Diesel: {diesel}")

# Problema "pares_consecutivos" (adaptado de URI 1159)
# O programa deve ler um valor inteiro X indefinidas vezes. (O programa irá parar quando o valor de X
# for igual a 0). Para cada X lido, imprima a soma dos 5 pares consecutivos a partir de X, inclusive o X
# , se for par. Se o valor de entrada for 4, por exemplo, a saída deve ser 40, que é o resultado da operação:
# 4+6+8+10+12, enquanto que se o valor de entrada for 11, por exempo, a saída deve ser 80, que é a
# soma de 12+14+16+18+20. 

# numero = int(input("Digite um numero inteiro: "))
# soma = 0

# while numero != 0:
#     if numero % 2 != 0:
#         numero += 1
#     else:
#         soma = 5 * numero + 20
#         print("Soma = ", soma)
#         numero = int(input("Digite um numero inteiro: "))
       

   
 

