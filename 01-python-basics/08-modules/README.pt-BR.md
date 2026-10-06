# Aula 08 – Módulos e Pacotes

[English](README.md) | [Português (BR)](README.pt-BR.md) · [Voltar ao início](../../README.pt-BR.md)

## Foco
Dividir o código em vários arquivos e pastas e reutilizá-lo com `import`.

## Pré-requisitos
[Aula 05](../05-functions) e [Aula 07](../07-error-handling)

## Conceitos
- Um módulo é um arquivo `.py`
- `import modulo` vs `from modulo import nome`
- Apelidos com `as`
- Pacotes: uma pasta com `__init__.py`
- `if __name__ == "__main__":` para o arquivo poder ser importado e executado

## Arquivos
- [modules.py](modules.py): ponto de entrada que usa tudo abaixo
- [calculator.py](calculator.py): `add`, `subtract`, `multiply`, `divide`
- [conversions.py](conversions.py): conversões seguras para `int` e `float`
- [tools/](tools): pacote com [texts.py](tools/texts.py) (maiúsculas/minúsculas)

## Exercícios
1. Crie `calculator.py` com quatro operações e um `main()` protegido por `__main__`.
2. Crie `conversions.py` retornando `None` para entradas inválidas.
3. Crie o pacote `tools` com `__init__.py` e `texts.py`.
4. Em `modules.py`, importe com os três estilos (`import`, `from ... import`, `as`).
5. Execute cada arquivo isoladamente e depois execute `modules.py`.

## Resultado esperado
Rodar `python modules.py` a partir desta pasta imprime os resultados da calculadora, das conversões e dos textos, e cada módulo também roda sozinho.

## Por que importa para ML
Projetos de ML são organizados em pacotes (carga de dados, pré-processamento, modelos, avaliação), e toda biblioteca que você vai usar é importada assim.

## Checklist
- [ ] Sei explicar o que `__name__ == "__main__"` faz
- [ ] Sei quando uma pasta vira um pacote
- [ ] Sei escolher entre os três estilos de import
