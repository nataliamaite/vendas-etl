from extract import extrair_dados
from transform import transformar_dados


# EXTRACT
df = extrair_dados()

print("Dados antes da transformação:")
print(df)

print("\nQuantidade antes da transformação:")
print(len(df))

print("\nValores nulos:")
print(df.isnull().sum())

print("\nDuplicados:")
print(df.duplicated().sum())

print("\nTipos antes da transformação:")
print(df.dtypes)


# TRANSFORM
df = transformar_dados(df)


# RESULTADOS
print("\nDados depois da transformação:")
print(df)

print("\nQuantidade depois da transformação:")
print(len(df))

print("\nTipos depois da transformação:")
print(df.dtypes)

print("\nCategorias depois da transformação:")
print(df["categoria"].unique())