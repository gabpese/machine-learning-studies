def transformar_em_maiusculo(texto):
    return texto.upper()


def transformar_em_minusculo(texto):
    return texto.lower()


def main():
    texto = "Machine Learning"

    print("===== TESTES DE TEXTO =====")

    print(transformar_em_maiusculo(texto))
    print(transformar_em_minusculo(texto))


if __name__ == "__main__":
    main()