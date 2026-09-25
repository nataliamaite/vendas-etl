from extract import extrair_dados
from transform import transformar_dados
from load import carregar_dados


df = extrair_dados()

print("Quantidade antes da transformação:", len(df))

df = transformar_dados(df)

print("Quantidade depois da transformação:", len(df))
print(df)

carregar_dados(df)

print("ETL executado com sucesso!")