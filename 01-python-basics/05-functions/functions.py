notas = [8, 5, 9, 7, 4, 10]


def analisar_notas(notas, nota_minima=7):
    aprovados = 0

    for nota in notas:
        if nota >= nota_minima:
            aprovados += 1

    return aprovados


resultado_1 = analisar_notas(notas)
print("Quantidade de aprovados:", resultado_1)

resultado_2 = analisar_notas(notas, nota_minima=9)
print("Quantidade de aprovados (com nota mínima 9):", resultado_2)