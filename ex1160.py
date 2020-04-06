# Quantidade de testes. Quantas vezes o repetidor irá atual sobre os inputs, PA, PB, G1 e G2.
T = int(input())

while T != 0:
    PA, PB, G1, G2 = input().split()

    PA = int(PA)
    PB = int(PB)
    G1 = float(G1)
    G2 = float(G2)


    populaçãoA = PA
    populaçãoB = PB
    anos = 0

    # Este repetir irá atuar até 101, que seria os 101 anos. Sempre que o repetidor atual irá atualizar as variáveis populaçãoA e populaçãoB:
    for valor in range(1,101+1):
      populaçãoA += int(populaçãoA*(G1/100))
      populaçãoB += int(populaçãoB*(G2/100))
      anos = valor

      # A variável anos é submetida por uma condição, se for maior que 100 anos, o repetidor irá mostrar uma mensagem e parar de atuar:
      if anos > 100:
        print("Mais de 1 seculo.")
        break
      # Esta condição serve para mostrar com quantos anos o a populaçãoA terá quando os valores da mesma ultrapassarem a populaçãoB:
      elif populaçãoA > populaçãoB:
        print("%d anos." % (anos))
        break

    T += -1