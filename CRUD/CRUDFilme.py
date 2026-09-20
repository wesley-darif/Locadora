from banco import conexao, cursor


#Função para listar filmes
def listar_filmes():
    cursor.execute("SELECT * FROM Tbl_Filmes")

    for Nome_Filme in cursor.fetchall():
        print(Nome_Filme)


# Função para Cadastrar Filmes
def cadastrar_filmes():
    try:
        Nome = (input("Informe o nome do filme: "))
        Codigo = (input("Informe o ID do filme: "))
        Classificacao = (input("Informe a classificação do filme: "))
        CodigoGenero = (input("Informe a codigo do genero do filme: "))
        Preco = (input("Informe o Preço do filme: "))
        Estoque = (input("Informe o estoque do filme: "))
        print("Filme cadastrado com sucesso")

        comando = """INSERT INTO Tbl_Filmes (Nome_Filme, Codigo_Filme, Classificacao, Codigo_Genero, Preco, Estoque) (?, ?, ?, ?, ?, ?)"""
        cursor.execute(comando, Nome, Codigo, Classificacao, CodigoGenero, Preco, Estoque)
        cursor.commit()
    except ValueError:
        print("Erro!! Digite apenas um numero inteiro")



#Função editar Genero

def Editar_filmes():
    try:

        Nome = (input("Informe o nome do filme: "))
        ID_NOVO = (input("Informe o novo ID: "))
        Classificacao = (input("Informe a classificação do filme: "))
        CodigoGenero = (input("Informe a codigo do genero do filme: "))
        Preco = (input("Informe o Preço do filme: "))
        Estoque = (input("Informe o estoque do filme: "))
        ID = (input("Informe o ID do filme: "))

        comando = """UPDATE Tbl_Filmes SET Nome_Filme = ?, Codigo_Filme = ?, Classificacao = ?, Codigo_Genero = ?, Preco = ?, Estoque = ? WHERE Codigo_Filme = ?"""
        cursor.execute(comando, Nome, ID_NOVO, Classificacao, CodigoGenero, Preco, Estoque, ID)
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