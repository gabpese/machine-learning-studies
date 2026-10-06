# Aula 07 – Tratamento de Erros

[English](README.md) | [Português (BR)](README.pt-BR.md) · [Voltar ao início](../../README.pt-BR.md)

## Foco
Antecipar e tratar erros de execução para que o programa não quebre.

## Pré-requisitos
[Aula 06](../06-dictionaries)

## Conceitos
- Erros comuns: `TypeError`, `NameError`, `IndexError`, `KeyError`, `ValueError`, `ZeroDivisionError`
- `try` / `except` / `else` / `finally`
- Capturar exceções específicas e usar `as error`
- Retornar `None` para sinalizar falha e verificar `is not None`

## Arquivos
- [error_handling.py](error_handling.py)

## Exercícios
1. Escreva `convert_to_integer()` tratando `ValueError` e `TypeError`.
2. Escreva buscas seguras em listas (`IndexError`) e dicionários (`KeyError`).
3. Escreva `divide()` tratando divisão por zero e tipos inválidos.
4. Escreva `validate_number()` usando os quatro blocos e observe a ordem de execução.

## Resultado esperado
Você consegue provocar cada erro de propósito, explicar por que ocorreu e tratá-lo de forma elegante.

## Por que importa para ML
Dados reais são sujos: valores ausentes, tipos errados, linhas malformadas. Código robusto sobrevive a pipelines de dados e treinos longos.

## Checklist
- [ ] Sei nomear os seis erros e o que causa cada um
- [ ] Sei quando `else` e `finally` executam
- [ ] Capturo erros específicos, não tudo
