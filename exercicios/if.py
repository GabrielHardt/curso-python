#  Fazer um programa para ler as duas notas que um aluno obteve no primeiro e segundo semestres de
# uma disciplina anual. Em seguida, mostrar a nota final que o aluno obteve (com uma casa decimal) no
# ano juntamente com um texto explicativo. Caso a nota final do aluno seja inferior a 60.00, mostrar a
# mensagem "REPROVADO", conforme exemplos. 

# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# notafinal = (nota1 + nota2) / 2

# print(f"Nota final: {notafinal}")

# if notafinal < 60:
#     print("Reprovado")

# Problema "baskara"
# Fazer um programa para ler os três coeficientes de uma equação do segundo grau. Usando a fórmula
# de Baskara, calcular e mostrar os valores das raízes x1 e x2 da equação com quatro casas decimais,
# conforme exemplo. Se a equação não possuir raízes reais, mostrar uma mensagem. 

# import math
# a = float(input("Coeficiente a :"))
# b = float(input("Coeficiente b :"))
# c = float(input("Coeficiente c :"))

# delta = (b*b) - (4 * a * c)


# if delta < 0:
#     print("Equacao sem raizes reais")
# else:
#     x1 = (-b + math.sqrt(delta)) / (2 * a)
#     x2 = (-b - math.sqrt(delta)) / (2 * a)
#     print(f"X1 = {x1:.4f}")
#     print(f"X2 = {x2:.4f}")

# Problema "menor_de_tres"
# Fazer um programa para ler três números inteiros. Em seguida, mostrar qual o menor dentre os três
# números lidos. Em caso de empate, mostrar apenas uma vez. 

# valor1 = int(input("Digite o primeiro valor: "))
# valor2 = int(input("Digite o segundo valor: "))
# valor3 = int(input("Digite o terceiro valor: "))

# menor = 0
# if valor1 < valor2 and valor1 < valor3:
#     menor = valor1
# elif valor2 < valor3:
#     menor = valor2
# else:
#     menor = valor3
# print(f"Menor valor = {menor}")

# Problema "operadora"
# Uma operadora de telefonia cobra R$ 50.00 por um plano básico que dá direito a 100 minutos de
# telefone. Cada minuto que exceder a franquia de 100 minutos custa R$ 2.00. Fazer um programa para
# ler a quantidade de minutos que uma pessoa consumiu, daí mostrar o valor a ser pago.
# Exemplo 1:
# Digite a quantidade de minutos: 22
# Valor a pagar: R$ 50.00
# Exemplo 2:
# Digite a quantidade de minutos: 103
# Valor a pagar: R$ 56.00 


# minutos = int(input("Minutos utilizados: "))
# pagar = 50

# if minutos > 100:
#     pagar = ((minutos - 100) * 2) + pagar

# print(f"Valor a pagar: R${pagar}")

# Problema "troco_verificado"
# Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
# O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
# e o valor em dinheiro dado pelo cliente. Seu programa deve mostrar o valor do troco a ser devolvido
# ao cliente. Se o dinheiro dado pelo cliente não for suficiente, mostrar uma mensagem informando o
# valor restante conforme exemplo. 

# preco = float(input("Preço unitário do produto: "))
# quantidade = int(input("Quantidade comprada: "))
# recebido = float(input("Dinheiro recebido: "))

# divida = preco * quantidade
# troco = 0

# if recebido < divida:
#     divida = divida - recebido
#     print(f"Valor insuficiente, faltam R${divida:.2f} reais")
# else:
#     troco = recebido - divida
#     print(f"Troco = {troco}")

