#   append()    adiciona no final
#   insert()    adiciona em uma posição específica
#   remove()    remove pelo valor
#   pop()       remove pelo índice
#   len()       quantidade de elementos

notas = [8, 5, 9, 4, 7, 10]

quantidade_aprovados = 0

for nota in notas:
    if nota >= 7:
        quantidade_aprovados += 1
        print(nota, "Aprovado")
    else:
        print(nota, "Reprovado")


print("Quantidade de aprovados:", quantidade_aprovados)
