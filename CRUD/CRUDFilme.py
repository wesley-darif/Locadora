from banco import conexao, cursor

print("Escolha uma opção:\n 1 - Listar Filmes\n 2 - Cadastrar Filmes\n 3 - Editar Filmes\n 4 - Excluir Filmes" )



#Função para listar filmes
def listar_filmes():
    cursor.execute("SELECT * FROM Tbl_Filmes")

    for Nome_Filme in cursor.fetchall():
        print(Nome_Filme)


# Função para Cadastrar Filmes
def cadastrar_filmes():
    cursor.execute("SELECT * FROM Tbl_Filmes")
    Nome = (input("Informe o nome do filme: "))
    Codigo = int(input("Informe o ID do filme: "))
    Classificacao = int(input("Informe a classificação do filme: "))
    CodigoGenero = int(input("Informe a codigo do genero do filme: "))
    Preco = int(input("Informe o Preço do filme: "))
    Estoque = int(input("Informe o estoque do filme: "))
    print("Filme cadastrado com sucesso")


    comando = f"""INSERT INTO Tbl_Filmes (Nome_Filme, Codigo_Filme, Classificacao,Codigo_Genero, Preco, Estoque) VALUES ('{Nome}', {Codigo}, {Classificacao},{CodigoGenero}, {Preco}, {Estoque})"""
    cursor.execute(comando)
    cursor.commit()


#Função editar Genero

def Editar_filmes():
    cursor.execute("SELECT * FROM Tbl_Filmes")
    Nome = (input("Informe o nome do filme: "))
    ID = int(input("Informe o ID do filme: "))
    ID_NOVO = int(input("Informe o novo ID: "))
    Classificacao = int(input("Informe a classificação do filme: "))
    CodigoGenero = int(input("Informe a codigo do genero do filme: "))
    Preco = int(input("Informe o Preço do filme: "))
    Estoque = int(input("Informe o estoque do filme: "))

    comando = f"""UPDATE Tbl_Filmes SET Nome_Filme = '{Nome}', Codigo_Filme = {ID_NOVO}, Classificacao = {Classificacao}, Codigo_Genero = {CodigoGenero}, Preco = {Preco}, Estoque = {Estoque} WHERE Codigo_Filme = {ID}"""
    cursor.execute(comando)
    cursor.commit()
    print("Filme Editado com sucesso")


#Função excluir Genero

def Excluir_filmes():
    cursor.execute("SELECT * FROM Tbl_Filmes")
    ID = int(input("Informe o ID do Filme: "))

    comando = f"""DELETE FROM Tbl_Filmes WHERE Codigo_Filme = {ID}"""
    cursor.execute(comando,)
    cursor.commit()
    print("Filme excluido com sucesso")

opcao = int(input("Digite sua escolha: "))
if opcao == 1:
    listar_filmes()
elif opcao == 2:
    cadastrar_filmes()
elif opcao == 3:
    Editar_filmes()
else:
    Excluir_filmes()