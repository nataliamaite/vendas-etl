#Importa o Pandas
import pandas as pd


def extrair_dados():
    df = pd.read_csv("data/vendas.csv") #Lê o CSV e armazena em df(DataFrame)

    return df