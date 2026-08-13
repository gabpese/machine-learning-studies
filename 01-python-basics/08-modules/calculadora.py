def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    try:
        return a / b

    except ZeroDivisionError as erro:
        print("Não é possível dividir por zero:", erro)
        return None

    except TypeError as erro:
        print("Tipo inválido para divisão:", erro)
        return None


def main():
    print("===== TESTES DA CALCULADORA =====")

    print("Soma:", somar(10, 5))
    print("Subtração:", subtrair(10, 5))
    print("Multiplicação:", multiplicar(10, 5))
    print("Divisão:", dividir(10, 5))

    print("\nTeste de divisão por zero:")
    print(dividir(10, 0))


if __name__ == "__main__":
    main()