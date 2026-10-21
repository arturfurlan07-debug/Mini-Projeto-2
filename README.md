# Mini Projeto 2 - LGPD

Projeto da Fatec Rio Claro sobre a Lei Geral de Proteção de Dados (LGPD, Lei nº 13.709/2018).

O código lê usuários de um banco PostgreSQL, anonimiza os dados pessoais, exporta os resultados em arquivos CSV e mede o tempo de execução com um decorator, gravando os tempos em um arquivo de log.

## Tecnologias

- Python
- PostgreSQL
- SQLAlchemy
- Google Colab

## O que cada atividade faz

- **Atividade 1:** função `LGPD` que anonimiza os dados de cada registro:
  - nome: `Olivia Araújo` vira `O***** Araújo`
  - CPF: `237.615.809-59` vira `237.***.***-**`
  - e-mail: `nuneserick@example.com` vira `n*********@example.com`
  - telefone: `+55 (011) 9483-6810` vira `6810`
- **Atividade 2:** gera um arquivo CSV para cada ano de nascimento (`csv/1990.csv`, `csv/1991.csv`, ...) com os dados anonimizados.
- **Atividade 3:** gera `csv/todos.csv` com o nome e o CPF de todos os usuários, sem anonimização, conforme o enunciado.
- **Atividade 4:** o `decorator_tempo.py` mede o tempo de execução das atividades 2 e 3 e grava o resultado em `execucao.log`.

## Como executar

1. Abra o notebook no Google Colab.
2. Rode as células em ordem (Ambiente de execução > Executar tudo).
3. Os arquivos são criados na pasta `csv/` e os tempos de execução ficam em `execucao.log`.

As dependências estão listadas em `requirements.txt`.

## Arquivos do repositório

- Notebook `.ipynb` com o código das atividades
- `decorator_tempo.py`: decorator que mede o tempo e grava em log
- `execucao.log`: registro dos tempos de execução
- `requirements.txt`: bibliotecas necessárias
- `csv/`: arquivos gerados (um por ano de nascimento e `todos.csv`)
