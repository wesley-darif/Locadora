import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

servidor = os.getenv("DB_SERVER")
banco = os.getenv("DB_DATABASE")
usuario = os.getenv("DB_USER")
senha = os.getenv("DB_PASSWORD")

try:
    conexao = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER=tcp:{servidor},1433;"
        f"DATABASE={banco};"
        f"UID={usuario};"
        f"PWD={senha};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

    cursor = conexao.cursor()

    print("Conectado ao Azure SQL com sucesso!")
    cursor.execute("SELECT DB_NAME()")
    resultado = cursor.fetchone()

    print("Banco conectado:", resultado[0])

except Exception as erro:
    print("Erro ao conectar ao banco de dados:")
    print(erro)