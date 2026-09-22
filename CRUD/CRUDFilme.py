from banco import conexao, cursor
from flask import jsonify


#Função para listar filmes
def listar_filmes():
    cursor.execute("SELECT * FROM Tbl_Filmes")

    filmes = [    "Apresentando filmes com sucesso"]

    for filme in cursor.fetchall():
        filmes.append({


            "Nome_Filme": filme[0],
            "Codigo_Genero": filme[1],
            "Classificacao": filme[2],
            "Preco": filme[3],
            "Estoque": filme[4],
            "Codigo_Filme": filme[5]

        })

    return filmes


# Função para Cadastrar Filmes
def cadastrar_filmes(Nome, Classificacao, CodigoGenero, Preco, Estoque):
    try:

        comando = """INSERT INTO Tbl_Filmes (Nome_Filme, Classificacao, Codigo_Genero, Preco, Estoque) VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(comando, Nome, Classificacao, CodigoGenero, Preco, Estoque)
        cursor.commit()
        print("Filme cadastrado com sucesso")
        return ("Filme cadastrado com sucesso")
    except Exception as erro:
        return f"Erro: {erro}"



#Função editar Genero

def Editar_filmes():
    try:

        Nome = (input("Informe o nome do filme: "))
        Classificacao = (input("Informe a classificação do filme: "))
        CodigoGenero = (input("Informe a codigo do genero do filme: "))
        Preco = (input("Informe o Preço do filme: "))
        Estoque = (input("Informe o estoque do filme: "))
        ID = (input("Informe o ID do filme: "))

        comando = """UPDATE Tbl_Filmes SET Nome_Filme = ?, Classificacao = ?, Codigo_Genero = ?, Preco = ?, Estoque = ? WHERE Codigo_Filme = ?"""
        cursor.execute(comando, Nome, Classificacao, CodigoGenero, Preco, Estoque, ID)
        cursor.commit()
        print("Filme Editado com sucesso")
    except ValueError:
        print("Erro!! Digite apenas um numero inteiro")

#Função excluir Genero

def Excluir_filmes():
    try :
        ID = int(input("Informe o ID do Filme: "))

        comando = """DELETE FROM Tbl_Filmes WHERE Codigo_Filme = ?"""
        cursor.execute(comando, ID)
        cursor.commit()
        print("Filme excluido com sucesso")
    except ValueError:
        print("Erro!! Digite apenas um numero inteiro")



def menu_filme():

    try:
        print("1 - Listar filme")
        print("2 - Cadastrar filme")
        print("3 - Editar filme")
        print("4 - Excluir filme")

        opcao = int(input("Digite sua escolha: "))

        if opcao == 1:
            listar_filmes()

        elif opcao == 2:
            cadastrar_filmes()

        elif opcao == 3:
            Editar_filmes()

        elif opcao == 4:
            Excluir_filmes()
    except ValueError:
        print("Erro!! Digite apenas um numero inteiro")
