# Projeto ETL de Vendas

Projeto introdutório de Engenharia de Dados desenvolvido para praticar um pipeline de ETL utilizando Python, Pandas e PostgreSQL.

O projeto realiza a extração de dados de vendas a partir de um arquivo CSV, aplica transformações e regras básicas de qualidade de dados e, por fim, carrega os dados tratados em um banco de dados PostgreSQL.

## Tecnologias utilizadas

* Python
* Pandas
* PostgreSQL
* psycopg2
* SQL
* Git e GitHub

## Arquitetura

```text
CSV
 ↓
Python / Pandas
 ↓
Extração
 ↓
Transformação
 ↓
PostgreSQL
```

## Estrutura do projeto

```text
projeto-etl-vendas/
│
├── data/
│   └── vendas.csv
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── main.py
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
│
├── requirements.txt
└── README.md
```

## Objetivos de aprendizado

Este projeto foi desenvolvido para praticar conceitos fundamentais de Engenharia de Dados:

* ETL;
* extração de dados;
* transformação e limpeza de dados;
* tratamento de valores nulos;
* tratamento de duplicidades;
* padronização de dados;
* manipulação de DataFrames com Pandas;
* integração entre Python e PostgreSQL;
* execução de comandos SQL através do Python;
* carregamento de dados em banco de dados;
* organização de um projeto de dados.


## Etapas do ETL

### 1. Extract

O arquivo `extract.py` realiza a leitura do arquivo CSV utilizando Pandas.

```python
df = pd.read_csv("data/vendas.csv")
```

Os dados são carregados em um DataFrame.

### 2. Transform

O arquivo `transform.py` realiza algumas etapas de tratamento e padronização dos dados:

* remoção de registros duplicados;
* remoção de registros sem preço;
* conversão dos tipos das colunas;
* conversão da coluna de data;
* padronização das categorias;
* criação da coluna `valor_total`.

O valor total é calculado utilizando:

```text
quantidade × preco
```

As categorias também são padronizadas para evitar que valores como:

```text
Eletrônicos
eletrônicos
ELETRÔNICOS
```

sejam tratados como categorias diferentes.

### 3. Load

O arquivo `load.py` realiza a conexão com o PostgreSQL e insere os dados transformados na tabela `vendas`.

A tabela possui as seguintes colunas:

```text
id
data
nome_cliente
produto
categoria
quantidade
preco
valor_total
```

### 4. Pipeline

O arquivo `main.py` integra as três etapas:

```text
Extract → Transform → Load
```

Para executar o pipeline:

```bash
python src/main.py
```

Ao finalizar, será exibida a mensagem:

```text
ETL executado com sucesso!
```

## Banco de dados

O projeto utiliza um banco PostgreSQL chamado:

```text
etl_vendas
```

A tabela utilizada é:

```text
vendas
```

Exemplo de criação da tabela:

```sql
CREATE TABLE vendas (
    id INTEGER PRIMARY KEY,
    data DATE,
    nome_cliente VARCHAR(100),
    produto VARCHAR(100),
    categoria VARCHAR(100),
    quantidade INTEGER,
    preco NUMERIC(10,2),
    valor_total NUMERIC(10,2)
);
```

## Consultando os dados

Depois da execução do ETL, os dados podem ser consultados utilizando SQL:

```sql
SELECT *
FROM vendas;
```

Quantidade de registros:

```sql
SELECT COUNT(*)
FROM vendas;
```

Categorias existentes:

```sql
SELECT DISTINCT categoria
FROM vendas;
```

Faturamento total:

```sql
SELECT SUM(valor_total) AS faturamento_total
FROM vendas;
```

## Como executar

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Entrar no projeto

```bash
cd projeto-etl-vendas
```

### 3. Criar o ambiente virtual

```bash
python3 -m venv .venv
```

### 4. Ativar o ambiente virtual

Linux/macOS:

```bash
source .venv/bin/activate
```

### 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 6. Configurar o PostgreSQL

Criar um banco chamado:

```text
etl_vendas
```

Criar a tabela `vendas` utilizando o SQL apresentado neste README.

### 7. Configurar as credenciais

No arquivo `src/load.py`, configurar as informações de conexão:

```python
conexao = psycopg2.connect(
    host="localhost",
    port="5433",
    database="etl_vendas",
    user="postgres",
    password="SUA_SENHA"
)
```

> Não publique sua senha do PostgreSQL no GitHub.

### 8. Executar o pipeline

```bash
python src/main.py
```

## Autor

Natália Santos


