import pandas as pd


def transformar_dados(df):

    # Remover registros duplicados
    df = df.drop_duplicates()

    # Remover vendas sem preço
    df = df.dropna(subset=["preco"])

    # Converter tipos
    df["id"] = df["id"].astype(int)
    df["quantidade"] = df["quantidade"].astype(int)
    df["preco"] = df["preco"].astype(float)

    # Converter data
    df["data"] = pd.to_datetime(df["data"])

    # Padronizar categoria
    df["categoria"] = df["categoria"].str.strip().str.lower()

    # Criar valor total
    df["valor_total"] = df["quantidade"] * df["preco"]

    return df