# Erros estudados:
#
# TypeError         -> operação incompatível com o tipo do dado
# NameError         -> nome/variável inexistente
# IndexError        -> índice inexistente em uma sequência
# KeyError          -> chave inexistente em um dicionário
# ValueError        -> valor inválido para determinada operação
# ZeroDivisionError -> tentativa de divisão por zero
#
# Estrutura:
#
# try:
#     código que pode gerar erro
# except TipoDoErro:
#     tratamento do erro
# else:
#     executa se nenhum erro ocorrer
# finally:
#     executa sempre


# ============================================================
# VALUEERROR E TYPEERROR
# ============================================================

def converter_para_inteiro(valor):
    try:
        return int(valor)

    except ValueError as erro:
        print("Valor inválido:", erro)
        return None

    except TypeError as erro:
        print("Tipo inválido:", erro)
        return None


# ============================================================
# INDEXERROR
# ============================================================

def buscar_item(lista, indice):
    try:
        return lista[indice]

    except IndexError as erro:
        print("Posição inexistente:", erro)
        return None


# ============================================================
# KEYERROR
# ============================================================

def buscar_valor(dicionario, chave):
    try:
        return dicionario[chave]

    except KeyError as erro:
        print("Chave inexistente:", erro)
        return None


# ============================================================
# ZERODIVISIONERROR E TYPEERROR
# ============================================================

def dividir(a, b):
    try:
        return a / b

    except ZeroDivisionError as erro:
        print("Não é possível dividir por zero:", erro)
        return None

    except TypeError as erro:
        print("Tipo inválido para divisão:", erro)
        return None


# ============================================================
# TRY / EXCEPT / ELSE / FINALLY
# ============================================================

def validar_numero(valor):
    try:
        numero = int(valor)

    except ValueError as erro:
        print("Valor inválido:", erro)

    except TypeError as erro:
        print("Tipo inválido:", erro)

    else:
        print("Conversão realizada com sucesso.")
        print("Número:", numero)

    finally:
        print("Validação concluída.")


# ============================================================
# TESTES
# ============================================================

print("----- CONVERSÃO -----")

resultado = converter_para_inteiro("42")

if resultado is not None:
    print("Resultado:", resultado)


print("\n----- CONVERSÃO INVÁLIDA -----")

resultado = converter_para_inteiro("Python")

if resultado is not None:
    print("Resultado:", resultado)


print("\n----- LISTA -----")

nomes = ["Ana", "Carlos"]

resultado = buscar_item(nomes, 1)

if resultado is not None:
    print("Item encontrado:", resultado)


print("\n----- ÍNDICE INVÁLIDO -----")

resultado = buscar_item(nomes, 10)

if resultado is not None:
    print("Item encontrado:", resultado)


print("\n----- DICIONÁRIO -----")

usuario = {
    "nome": "Gabriel",
    "idade": 30
}

resultado = buscar_valor(usuario, "idade")

if resultado is not None:
    print("Valor encontrado:", resultado)


print("\n----- CHAVE INVÁLIDA -----")

resultado = buscar_valor(usuario, "cidade")

if resultado is not None:
    print("Valor encontrado:", resultado)


print("\n----- DIVISÃO -----")

resultado = dividir(100, 2)

if resultado is not None:
    print("Resultado:", resultado)


print("\n----- DIVISÃO POR ZERO -----")

resultado = dividir(100, 0)

if resultado is not None:
    print("Resultado:", resultado)


print("\n----- ELSE E FINALLY -----")

validar_numero("50")


print("\n----- FIM DO PROGRAMA -----")

