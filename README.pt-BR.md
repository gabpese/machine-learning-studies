# Estudos de Machine Learning

[English](README.md) | [Português (BR)](README.pt-BR.md)

> Do Python básico ao Machine Learning, uma aula de cada vez.

## Sobre

Este repositório documenta minha jornada de aprendizado, de **zero em Python** até **Machine Learning**.

Cada linha de código aqui foi digitada por mim, à mão, sem código gerado por IA. O objetivo é aprender, não entregar rápido. Uma IA é usada apenas como *professora*: planeja as aulas, explica conceitos e revisa meu entendimento.

Cada aula é documentada com seu **foco**, **exercícios** e **resultado esperado**, de modo que o repositório também pode ser seguido por quem quiser percorrer o mesmo caminho.

## Como usar este repositório

1. Siga as fases e aulas **em ordem**.
2. Leia o `README.pt-BR.md` da aula antes de mexer no código.
3. Tente os exercícios **antes** de olhar o código.
4. Compare seu resultado com o *resultado esperado* da aula.
5. Use o checklist no final de cada aula para verificar se você consegue explicar o tema com suas próprias palavras.

## Roteiro

| Fase | Pasta | Tema | Status |
|------|-------|------|--------|
| 01 | `01-python-basics` | Fundamentos de Python | 🚧 Em andamento |
| 02 | `02-python-for-data` | NumPy, Pandas, visualização de dados | ⏳ Planejado |
| 03 | `03-math-stats` | Matemática e estatística para ML | ⏳ Planejado |
| 04 | `04-ml-fundamentals` | Regressão, classificação, avaliação | ⏳ Planejado |
| 05 | `05-classical-ml` | Árvores, ensembles, clustering, pipelines | ⏳ Planejado |
| 06 | `06-deep-learning-intro` | Redes neurais | ⏳ Planejado |

## Fase 01 – Python Básico

| # | Aula | Foco | Status |
|---|------|------|--------|
| 01 | [Primeiro Programa](01-python-basics/01-first-program) | `print`, tipos básicos, `type()`, conversão | ✅ |
| 02 | [Variáveis](01-python-basics/02-variables) | Variáveis e aritmética | ✅ |
| 03 | [Condicionais](01-python-basics/03-conditionals) | `if`/`elif`/`else`, `and`/`or`/`not` | ✅ |
| 04 | [Laços de Repetição](01-python-basics/04-loops) | `for`, listas, contadores | ✅ |
| 05 | [Funções](01-python-basics/05-functions) | `def`, parâmetros, valores padrão, `return` | ✅ |
| 06 | [Dicionários](01-python-basics/06-dictionaries) | dados chave/valor, `.items()`, `.get()` | ✅ |
| 07 | [Tratamento de Erros](01-python-basics/07-error-handling) | `try`/`except`/`else`/`finally` | ✅ |
| 08 | [Módulos e Pacotes](01-python-basics/08-modules) | `import`, módulos próprios, pacotes | ✅ |
| 09 | [Manipulação de Arquivos](01-python-basics/09-file-handling) | `open`, `with`, `pathlib` | ✅ |
| 10 | Listas, Tuplas e Sets | comprehensions | ⏳ |
| 11 | Programação Orientada a Objetos | classes, herança | ⏳ |
| 12 | Ambientes Virtuais e pip | `venv`, `requirements.txt` | ⏳ |
| 13 | JSON e CSV | biblioteca padrão | ⏳ |
| 14 | **Projeto 1** | App de linha de comando usando tudo acima | ⏳ |


## Modelo de README das aulas

Cada pasta de aula contém um `README.md` (inglês) e um `README.pt-BR.md` (português) com:

- **Foco**: o que a aula ensina
- **Pré-requisitos**: aulas que devem ter sido feitas antes
- **Conceitos**: as ideias principais
- **Exercícios**: o que praticar
- **Resultado esperado**: o que você deve conseguir fazer depois
- **Por que importa para ML**: como se conecta ao objetivo final
- **Checklist**: autoavaliação

## Configuração

```bash
# clonar
git clone https://github.com/<seu-usuario>/machine-learning-studies.git
cd machine-learning-studies

# criar e ativar um ambiente virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Linux / macOS

# instalar dependências (vazio até a Fase 02)
pip install -r requirements.txt
```

Execute qualquer aula de dentro da própria pasta, por exemplo:

```bash
cd 01-python-basics/08-modules
python modules.py
```

## Convenções

- Nomes de pastas e arquivos em **inglês**.
- Identificadores, comentários e mensagens do código estão em **inglês**.
- Commits seguem o [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `chore:`, `docs:`).

## Autor

**Gabriel Pesegoginski**
