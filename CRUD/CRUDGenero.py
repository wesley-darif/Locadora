from banco import conexao, cursor

#Função para listar generos
def listar_genero():
    cursor.execute("SELECT * FROM Tbl_Genero")

    for Nome_Genero in cursor.fetchall():
        print(Nome_Genero)


# Função para Cadastrar generos
def cadastrar_genero():
    try:
        NomeCad = (input("Informe o nome do genero: "))
        IDCad = int(input("Informe o ID do genero: "))

        comando = """INSERT INTO Tbl_Genero (Nome_Genero, Codigo_Genero) VALUES (?, ?)"""
        cursor.execute(comando, NomeCad, IDCad)
        cursor.commit()
        print("Genero cadastrado com sucesso")
    except ValueError:
        print("Erro!! Digite apenas um numero inteiro")



#Função editar Genero

def Editar_genero():
    try:
        Nome = (input("Informe o nome do genero: "))
        ID_NOVO = int(input("Informe o novo ID: "))
        ID = int(input("Informe o ID do genero: "))

        comando = """UPDATE Tbl_Genero SET Nome_Genero = ?, Codigo_Genero = ? WHERE Codigo_Genero = ?"""
        cursor.execute(comando, Nome, ID_NOVO, ID)
        cursor.commit()
        print("Genero Editado com sucesso")
    except ValueError:
        print("Erro!! Digite apenas um numero inteiro")


#Função excluir Genero

def Excluir_genero():
    try:
        ID = int(input("Informe o ID do genero: "))

        comando = """DELETE FROM Tbl_Genero WHERE Codigo_Genero = ?"""
        cursor.execute(comando, ID)
        cursor.commit()
        print("Genero excluido com sucesso")
    except ValueError:
        print("Erro!! Digite apenas um numero inteiro")



def menu_genero():

    try:
        print("1 - Listar gêneros")
        print("2 - Cadastrar gênero")
        print("3 - Editar gênero")
        print("4 - Excluir gênero")

        opcao = int(input("Digite sua escolha: "))

        if opcao == 1:
            listar_genero()

        elif opcao == 2:
            cadastrar_genero()

        elif opcao == 3:
            Editar_genero()

        elif opcao == 4:
            Excluir_genero()
    except ValueError:
        print("Erro!! Digite apenas um numero inteiro")
