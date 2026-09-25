from load import conectar_banco


conexao = conectar_banco()

print("Conexão realizada com sucesso!")

conexao.close()