from extract import extrair_dados


df = extrair_dados()

print("Primeiras linhas:")
print(df.head())

print("\nInformações:")
print(df.info())

print("\nTipos das colunas:")
print(df.dtypes)