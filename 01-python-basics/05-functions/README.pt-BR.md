# Aula 05 – Funções

[English](README.md) | [Português (BR)](README.pt-BR.md) · [Voltar ao início](../../README.pt-BR.md)

## Foco
Empacotar lógica reutilizável em funções com parâmetros e valores de retorno.

## Pré-requisitos
[Aula 04](../04-loops)

## Conceitos
- `def` e chamada de função
- Parâmetros e valores padrão (`minimum_grade=7`)
- Argumentos nomeados (`minimum_grade=9`)
- `return` vs `print`
- Reutilizar a mesma função com entradas diferentes

## Arquivos
- [functions.py](functions.py)

## Exercícios
1. Transforme o contador de aprovados da Aula 04 na função `analyze_grades(grades, minimum_grade=7)`.
2. Chame-a com a nota mínima padrão e com uma personalizada.
3. Faça a função retornar o resultado e imprima fora dela.

## Resultado esperado
Você consegue encapsular uma lógica em uma função, dar bons valores padrão e reutilizá-la sem copiar código.

## Por que importa para ML
Etapas de pré-processamento, métricas e rotinas de treino são funções. Valores padrão e argumentos nomeados são exatamente como bibliotecas como o scikit-learn são configuradas.

## Checklist
- [ ] Sei explicar a diferença entre parâmetro e argumento
- [ ] Sei quando usar um valor padrão
- [ ] Minhas funções retornam valores em vez de apenas imprimir
