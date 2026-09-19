import pyodbc

from optparse import Values
from tkinter.constants import INSERT

dados_conexao = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=LOCADORA1;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexao bem sucedida")
cursor = conexao.cursor()
