from banco import conexao, cursor

print("Escolha uma opção:\n 1 - Listar Generos\n 2 - Cadastrar Genero\n 3 - Editar Genero\n 4 - Excluir Genero" )



#Função para listar generos
def listar_genero():
    cursor.execute("SELECT * FROM Tbl_Genero")

    for Nome_Genero in cursor.fetchall():
        print(Nome_Genero)


# Função para Cadastrar generos
def cadastrar_genero():
    cursor.execute("SELECT * FROM Tbl_Genero")
    NomeCad = (input("Informe o nome do genero: "))
    IDCad = int(input("Informe o ID do genero: "))
    print("Genero cadastrado com sucesso")


    comando = f"""INSERT INTO Tbl_Genero (Nome_Genero, Codigo_Genero) VALUES ('{NomeCad}', {IDCad})"""
    cursor.execute(comando)
    cursor.commit()


#Função editar Genero

def Editar_genero():
    cursor.execute("SELECT * FROM Tbl_Genero")
    Nome = (input("Informe o nome do genero: "))
    ID = int(input("Informe o ID do genero: "))
    ID_NOVO = int(input("Informe o novo ID: "))

    comando = f"""UPDATE Tbl_Genero SET Nome_Genero = '{Nome}', Codigo_Genero = {ID_NOVO} WHERE Codigo_Genero = {ID}"""
    cursor.execute(comando,)
    cursor.commit()
    print("Genero Editado com sucesso")


#Função excluir Genero

def Excluir_genero():
    cursor.execute("SELECT * FROM Tbl_Genero")
    ID = int(input("Informe o ID do genero: "))

    comando = f"""DELETE FROM Tbl_Genero WHERE Codigo_Genero = {ID}"""
    cursor.execute(comando,)
    cursor.commit()
    print("Genero excluido com sucesso")

opcao = int(input("Digite sua escolha: "))
if opcao == 1:
    listar_genero()
elif opcao == 2:
    cadastrar_genero()
elif opcao == 3:
    Editar_genero()
else:
    Excluir_genero()