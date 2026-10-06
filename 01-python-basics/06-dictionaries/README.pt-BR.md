# Aula 06 – Dicionários

[English](README.md) | [Português (BR)](README.pt-BR.md) · [Voltar ao início](../../README.pt-BR.md)

## Foco
Representar dados estruturados com pares chave/valor.

## Pré-requisitos
[Aula 05](../05-functions)

## Conceitos
- Criar dicionários `{"chave": valor}`
- Ler com `dict["chave"]` e com segurança usando `dict.get("chave", padrao)`
- `.items()`, `.keys()`, `.values()`
- Listas de dicionários
- `KeyError` quando a chave não existe

## Arquivos
- [dictionaries.py](dictionaries.py)

## Exercícios
1. Modele um curso, uma pessoa, um usuário e dois produtos como dicionários.
2. Escreva funções que imprimam os itens, chaves e valores de qualquer dicionário.
3. Escreva `check_product()`, que diz se um produto está disponível usando `.get("stock", 0)`.
4. Percorra uma lista de dicionários aplicando as funções a cada um.

## Resultado esperado
Você consegue representar um registro do mundo real como dicionário, iterar sobre ele e ler chaves ausentes sem quebrar o programa.

## Por que importa para ML
Registros de JSON/APIs, hiperparâmetros de modelos e relatórios de resultados são dicionários. Uma linha do Pandas se comporta de forma parecida.

## Checklist
- [ ] Sei explicar a diferença entre `dict["chave"]` e `dict.get("chave")`
- [ ] Sei iterar sobre chaves, valores e itens
- [ ] Fiz os exercícios sem olhar o código
