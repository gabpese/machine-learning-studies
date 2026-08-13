def converter_para_inteiro(valor):
    try:
        return int(valor)

    except (ValueError, TypeError):
        return None


def converter_para_float(valor):
    try:
        return float(valor)

    except (ValueError, TypeError):
        return None


def main():
    print("===== TESTES DE CONVERSÃO =====")

    print(converter_para_inteiro("Dez"))
    print(converter_para_inteiro("10.0"))
    print(converter_para_inteiro("10"))

    print(converter_para_float("Dez"))
    print(converter_para_float("10.0"))
    print(converter_para_float("10"))


if __name__ == "__main__":
    main()