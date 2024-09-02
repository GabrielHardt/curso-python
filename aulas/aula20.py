valor1 = int(input("Digite o primeiro valor: "));
valor2 = int(input("Digite o segudo valor: "));

if valor1 > valor2:
    print(f"{valor1=} eh maior que {valor2=}");
elif valor1 < valor2:
    print(f"{valor2=} eh maior que {valor1=}");
else:
    print("Os valores sao iguais")
