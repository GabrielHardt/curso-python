import os
lista = []

while True:
    print("Selecione uma opcao: ")
    opcao = input("[i]nserir [a]pagar [l]istar: ")

    if opcao == "i":
        os.system("cls")
        valor = input("valor: ")
        lista.append(valor)

    elif opcao == "a":
        indice_str = input("Escolha um indice para apagar: ")

        try:
            indice = int(indice_str)
            del lista[indice]
        except TypeError:
            print("por favor digite numeros inteiros")
        except IndexError:
            print("indice nao existe na lista")
        except Exception: 
            print("Erro desconhecido")
    
    elif opcao == "l":
        os.system("cls")

        if len(lista) == 0:
            print("Lista vazia")

        for i, valor in enumerate(lista):
            print(i, valor)
