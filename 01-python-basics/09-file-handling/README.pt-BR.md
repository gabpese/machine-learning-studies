# Aula 09 – Manipulação de Arquivos

[English](README.md) | [Português (BR)](README.pt-BR.md) · [Voltar ao início](../../README.pt-BR.md)

## Foco
Ler e escrever arquivos de texto com segurança e montar caminhos que funcionam em qualquer máquina.

## Pré-requisitos
[Aula 04](../04-loops), [Aula 07](../07-error-handling) e [Aula 08](../08-modules)

## Conceitos
- `open(caminho, "r")` e `open(caminho, "w")` (`"w"` sobrescreve o arquivo)
- `with open(...) as arquivo` fecha o arquivo automaticamente
- `.read()` vs percorrer linha a linha
- `.strip()` para remover quebras de linha e `"\n".join(lista)` para montar texto
- Tratamento de `FileNotFoundError`
- `pathlib.Path`: `__file__`, `.resolve()`, `.parents`, operador `/`
- Verificação de caminhos e criação de pastas: `exists()`, `is_file()`, `is_dir()`, `mkdir(parents=True, exist_ok=True)`

## Arquivos
- [file_handling.py](file_handling.py)
- [data.txt](data.txt), [languages.txt](languages.txt), [grades.txt](grades.txt): dados de exemplo
- Anotações de exercícios: [exercises](exercises)

## Exercícios
1. Monte os caminhos do projeto com `pathlib` em vez de strings fixas.
2. Escreva uma linha em `data.txt` e leia o arquivo de volta.
3. Leia `grades.txt`, converta cada linha para `int` e conte as notas aprovadas.
4. Leia uma lista de linguagens ignorando linhas vazias, usando `try`/`except FileNotFoundError`.
5. Filtre valores vazios de uma lista, grave o restante em `languages.txt` com `"\n".join()` e leia de volta.
6. Verifique se caminhos existem e se são arquivos ou pastas, e crie pastas de resultados.

## Resultado esperado
Seu script roda a partir de qualquer diretório, lê e escreve os arquivos de exemplo e falha de forma elegante quando um arquivo não existe.

## Por que importa para ML
Datasets, modelos treinados e resultados ficam em arquivos. Lê-los com confiabilidade é o primeiro passo de todo pipeline de ML.

## Checklist
- [ ] Sei por que `with` é preferível a `close()` manual
- [ ] Sei explicar a diferença entre `"r"` e `"w"`
- [ ] Sei montar caminhos com `pathlib` sem fixá-los no código
