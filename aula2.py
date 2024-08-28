#crlf = carriage return line feed (\r\n) QUEBRA DE LINHA
#caractere do windows que faz com que o contador quebre a linha, por exemplo no linux e mac eh so lf(\n)
#o windows 11 ja considera o /n como uma quebra de linha, nao precisando do carriage return (\r) ao lado do \n
# \r\n -> crlf (windows mais antigos)
# \n -> lf (sistemas baseados em unix)


#comando print recebe varios argumentos os quais voce pode passar um argumento nomeado, como o sep para separa de forma que quiser o end pra terminar como quiser

print(12, 34, 1011, sep="-", end="#\n")
print(56, 78, sep="-")

# sep=
# end= \n (quebra de linha, que ja e o padrao). se mudar a quebra de linha sera substituida pelo novo elemento. E PODE SER MISTURADA