import pyodbc

from optparse import Values
from tkinter.constants import INSERT

dados_conexao = (

    "Driver={SQL Server};"
    "SERVER=localhost\SQLEXPRESS;"
    "DATABASE=LOCADORA1;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexao bem sucedida")
cursor = conexao.cursor()
