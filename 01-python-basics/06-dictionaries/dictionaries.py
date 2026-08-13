#   NameError  → nome/variável inexistente
#   IndexError → índice inexistente em lista
#   KeyError   → chave inexistente em dicionário

curso ={
    "nome": "Machine Learning com Python",
    "duracao_meses": 12,
    "ativo": True
}

pessoa = {
    "nome": "Ana",
    "idade": 29
}

usuario = {
    "nome": "Gabriel",
    "idade": 30,
    "ativo": True
}

produto_1 = {
    "nome": "Teclado",
    "preco": 150,
    "estoque": 8
}

produto_2 = {
    "nome": "Mouse",
    "preco": 80,
    "estoque": 0
}

def mostrar_items_dicionario(dicionario):
    for chave, valor in dicionario.items():
        print(chave, valor)

def mostrar_chaves_dicionario(dicionario):
    for chave in dicionario.keys():
        print(chave)

def mostrar_valores_dicionario(dicionario):
    for valor in dicionario.values():
        print(valor)

def verificar_produto(produto):
    if produto.get("estoque", 0) > 0:
        print(produto["nome"], "Disponível")
    else:
        print(produto["nome"], "Sem estoque")

dicionarios = [curso, pessoa, usuario, produto_1, produto_2]

for dicionario in dicionarios:
    print("Items do dicionário:")
    mostrar_items_dicionario(dicionario)
    print("-----")
    print("Chaves do dicionário:")
    mostrar_chaves_dicionario(dicionario)
    print("-----")
    print("Valores do dicionário:")
    mostrar_valores_dicionario(dicionario)
    print("=====================================")

verificar_produto(produto_1)
verificar_produto(produto_2)

