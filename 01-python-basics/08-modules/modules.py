import calculadora

from conversoes import converter_para_inteiro, converter_para_float
from ferramentas.textos import transformar_em_maiusculo as maiusculo
from ferramentas.textos import transformar_em_minusculo


def main():
    print("===== CALCULADORA =====")

    print("Soma:", calculadora.somar(10, 5))
    print("Subtração:", calculadora.subtrair(10, 5))
    print("Multiplicação:", calculadora.multiplicar(10, 5))

    resultado_divisao = calculadora.dividir(10, 2)

    if resultado_divisao is not None:
        print("Divisão:", resultado_divisao)


    print("\n===== CONVERSÕES =====")

    numero_inteiro = converter_para_inteiro("25")
    numero_float = converter_para_float("10.5")
    valor_invalido = converter_para_inteiro("Python")

    print("Inteiro:", numero_inteiro)
    print("Float:", numero_float)
    print("Conversão inválida:", valor_invalido)


    print("\n===== TEXTOS =====")

    texto = "Machine Learning"

    print(maiusculo(texto))
    print(transformar_em_minusculo(texto))


if __name__ == "__main__":
    main()