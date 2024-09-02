# exercicio calculadora

while True:
    numero1 = input("Digite um numero: ")
    numero2 = input("Digite outro numero: ")
    operador = input("Digite um operador(+-*/): ")

    numeros_validos = None
    numero1_float = 0
    numero2_float = 0

    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Um ou ambos os numeros sao invalidos")
        continue

    operadores_permitidos = "+-*/"

    if operador not in operadores_permitidos:
        print("Seu operador digitado nao e permitido")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador")
        continue

    print("Realizando sua conta")
    if operador == "+":
        print(numero1_float + numero2_float)
    elif operador == "-":
        print(numero1_float - numero2_float)
    elif operador == "*":
        print(numero1_float * numero2_float)
    elif operador == "/":
        print(numero1_float / numero2_float)
    else:
        print("Nao deveria chegar ate aqui")
    


    sair = input("Gostaria de Sair? [s]im: ").lower().startswith("s")
    print(sair)

    if sair:
        break
