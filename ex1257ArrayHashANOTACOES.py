testes = int(input())
# número de testes:
while testes != 0:
    testes += -1

    # número de elementos a serem testas:
    elementos = int(input())
    elemento = 0

    N_posições = 0
    valor_da_letra = 0

    # repetidor atua na quantidade de testes:
    while elementos > elemento:
        elemento += +1

        posiçãoL = 0

        # string inserida na entrada, com um upper em caso do usuário inserir letras minúsculas, igualando aos caracteres cadastrados em maúsculas.
        verificar = input().upper()
        alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        # cálculo do valor da letra, indexando as strings do alfabeto:
        for letra in verificar:
            posiçãoL += +1
            indice = alfabeto.index(letra)
            valor_da_letra += indice

        # contador de posições:
        for posições in range(1, posiçãoL):
            N_posições += posições

        #leitura de caracteres:
        caracteres = len(verificar)

        # contador de elementos:
        elementos_contados = 0
        for contador in range (0, elementos):
            elementos_contados += contador*caracteres


        soma_dos_dados = N_posições + valor_da_letra + elementos_contados

    print(soma_dos_dados)