from optparse import Values
from tkinter.constants import INSERT

import pyodbc

dados_conexao = (

    "Driver={SQL Server};"
    "SERVER=localhost\SQLEXPRESS;"
    "DATABASE=LOCADORA1;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexao bem sucedida")
cursor = conexao.cursor()



def select_genero():
    cursor.execute("SELECT * FROM Tbl_Genero")

    for Nome_Genero in cursor.fetchall():
        print(Nome_Genero)

select_genero()