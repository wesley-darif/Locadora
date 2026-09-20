import pyodbc

dados_conexao = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost\SQLEXPRESS;"
    "DATABASE=LOCADORA1;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexao bem sucedida")
cursor = conexao.cursor()
