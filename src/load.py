import psycopg2


def conectar_banco():
    conexao = psycopg2.connect(
        host="localhost",
        port="5433",
        database="etl_vendas",
        user="postgres",
        password="sua_senha"
    )

    return conexao


def carregar_dados(df):
    print("Quantidade de registros recebidos pelo LOAD:", len(df))

    conexao = conectar_banco()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO vendas (
            id,
            data,
            nome_cliente,
            produto,
            categoria,
            quantidade,
            preco,
            valor_total
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    for _, row in df.iterrows():

        print("Inserindo ID:", row["id"])

        cursor.execute(
            sql,
            (
                int(row["id"]),
                row["data"].date(),
                row["nome_cliente"],
                row["produto"],
                row["categoria"],
                int(row["quantidade"]),
                float(row["preco"]),
                float(row["valor_total"])
            )
        )

    conexao.commit()

    cursor.close()
    conexao.close()