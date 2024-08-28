# Ler um número inteiro N, daí mostrar na tela a tabuada de N para 1 a 10, conforme exemplo. 

# numero = int(input("Digite um numero: "))
# i = 0

# for i in range(1, 11):
#     print(numero * i)


# Leia 2 valores inteiros X e Y (em qualquer ordem). A seguir, calcule e mostre a soma dos números
# impares entre eles

# print("Digite dois numeros: ")
# x = int(input())
# y = int(input())
# soma = 0
# troca = 0

# if x > y:
#     troca = x
#     x = y
#     y = troca

# for i in range(x+1, y):
#     if i % 2 != 0:
#         soma = i + soma
# print(soma)

# Leia um valor inteiro X. Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X,
# se for o caso. 

# x = int(input("Digite um numero: "))

# for i in range(1, x+1):
#     if i % 2 != 0:
#         print(i)


# Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
# Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo,
# conforme exemplo

# n = int(input("Quantos numeros voce vai digitar? "))
# fora = 0
# dentro = 0

# for x in range(0, n):
#     x = int(input("Digite um numero: "))
#     if x >= 10 and x <= 20:
#         dentro = dentro + 1
#         print(f"{x}, esta dentro do intervalo")
#     else:
#         fora = fora + 1
#         print(f"{x}, esta fora do intervalo")
# print(f"Fora = {fora}")
# print(f"Dentro = {dentro}")


# Leia um valor inteiro N. Este valor será a quantidade de números inteiros que serão lidos em seguida.
# Para cada valor lido, mostre uma mensagem dizendo se este valor lido é PAR ou IMPAR, e também
# se é POSITIVO ou NEGATIVO. No caso do valor ser igual a zero (0), seu programa deverá imprimir
# apenas NULO

# n = int(input("Quantos inteiros serao lidos "))

# for i in range(0, n):
#     i = int(input("Digite um inteiro: "))

#     if i == 0:
#         print("Nulo")
#     else:
#         if i % 2 == 0:
#             print("par", end=" ")
#         else:
#             print("impar", end=" ")

#         if i > 0:
#             print("positivo")
#         else:
#             print("negativo")


# Leia um valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de
# teste consiste de 3 valores reais, para os quais você deverá calcular e mostrar a média ponderada, sendo
# que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5. Vale lembrar
# que a média ponderada é a soma de todos os valores multiplicados pelo seu respectivo peso, dividida
# pela soma dos pesos.

# n = int(input("Digite quantos testes vem a seguir: "))
# x = 0
# y = 0
# z = 0

# for i in range(0, n):
#     x = float(input("Digite um valor: "))
#     y = float(input("Digite um valor: "))
#     z = float(input("Digite um valor: "))
    
#     media = (x * 2.0 + y * 3.0 + z * 5.0) / 10

#     print(f"Media = {media:.1f}")


# Escreva um algoritmo que leia dois números e imprima o resultado da divisão do primeiro pelo
# segundo. Caso não for possível, mostre a mensagem “DIVISAO IMPOSSIVEL”.


# n = int(input("Quantos casos vai digitar? "))
# x = 0
# y = 0

# for i in range(n):
#     x = int(input("Digite um numerador: "))
#     y = int(input("Digite o denominador: "))

#     if y == 0:
#         print("Divisao impossivel")
#     else:
#         print(f"Divisao = {x / y}")

# Fazer um programa para ler um número natural N (valor máximo: 15), e depois calcular e mostrar o
# fatorial de N.

# n = int(input("Digite um numero natural: "))
# fatorial = 1
# if n > 15:
#     n = int(input("Valor maximo igual a 15, digite outro numero: "))

# for i in range(n, 0, -1):
#     fatorial = fatorial * i
#     print(fatorial)

# Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para
# organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano,
# quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. Este
# laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas
# informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia
# utilizada e a quantidade de cobaias utilizadas em cada experimento. Faça um programa que leia um
# valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um
# inteiro que representa a quantidade de cobaias utilizadas e uma letra ('C', 'R' ou 'S'), indicando o tipo
# de cobaia (R:Rato S:Sapo C:Coelho). Apresente o total de cobaias utilizadas, o total de cada tipo de
# cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o
# percentual deve ser apresentado com dois dígitos após o ponto. 

n = int(input("Quantos testes serao realizados? "))
total = 0
c = 0
r = 0
s = 0

for i in range(n):
    quantidade = int(input("Qauntidade de cobaias: "))
    tipo = str(input("Tipo da cobaia: "))
    
    if tipo == "c":
        c = quantidade + c
    elif tipo == "r":
        r = quantidade + r
    else:
        s = quantidade + s

        
    total = c + r + s


print("Relatorio final: ")
print(f"total = {total}")
print(f"total de coelhos = {c}")
print(f"total de ratos = {r}")
print(f"total de sapos = {s}")
print(f"Percentual de coelhos = {(c/total)*100:.2f} ")
print(f"Percentual de ratos = {(r/total) * 100:.2f}")
print(f"Percentual de sapos = {(s/total)*100:.2f}")
       


