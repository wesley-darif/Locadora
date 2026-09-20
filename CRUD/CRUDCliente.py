
from banco import conexao, cursor



#Função para listar Clientes
def listar_cliente():
    cursor.execute("SELECT * FROM Tbl_Clientes")

    for Nome_Cliente in cursor.fetchall():
        print(Nome_Cliente)


# Função para Cadastrar Clientes
def cadastrar_cliente():
    try:

        Nome = (input("Informe o nome do Cliente: "))
        ID = int(input("Informe o ID do Cliente: "))
        Nascimento = (input("Informe o nascimento do Cliente: "))
        Sexo = (input("Informe o sexo do Cliente: "))
        Telefone = (input("Informe o telefone do Cliente: "))
        Endereco = (input("Informe o endereco do Cliente: "))

        comando = """INSERT INTO Tbl_Clientes (Nome_Cliente, Codigo_Cliente, Data_Nascimento, Sexo, Telefone, Endereco) VALUES (?, ?, ?, ?, ?, ?)"""
        cursor.execute(comando, Nome, ID, Nascimento, Sexo, Telefone, Endereco)
        cursor.commit()
        print("Cliente cadastrado com sucesso")
    except ValueError:
        print("Erro!! Digite apenas um numero inteiro")


#Função editar Genero

def Editar_cliente():
    try:

        Nome = (input("Informe o nome do Cliente: "))
        ID_NOVO = int(input("Informe o novo ID: "))
        Nascimento = (input("Informe o nascimento do Cliente: "))
        Sexo = (input("Informe o sexo do Cliente: "))
        Telefone = (input("Informe o telefone do Cliente: "))
        Endereco = (input("Informe o endereco do Cliente: "))
        ID = (input("Informe o ID do Cliente: "))

        comando = """UPDATE Tbl_Clientes SET Nome_Cliente = ?, Codigo_Cliente = ?, Data_Nascimento = ?, Sexo = ?, Telefone = ?, Endereco = ? WHERE Codigo_Cliente = ?"""
        cursor.execute(comando, Nome, ID_NOVO, Nascimento, Sexo, Telefone, Endereco, ID)
        cursor.commit()
        print("Cliente Editado com sucesso")
    except ValueError:
        print("Erro!! Digite apenas um numero inteiro")


#Função excluir Cliente

def Excluir_cliente():
    try:

        ID = (input("Informe o ID do Cliente: "))

        comando = """DELETE FROM Tbl_Clientes WHERE Codigo_Cliente = ?"""
        cursor.execute(comando, ID)
        cursor.commit()
        print("Genero excluido com sucesso")
    except ValueError:
        print("Erro!! Digite apenas um numero inteiro")


def menu_cliente():

    print("1 - Listar cliente")
    print("2 - Cadastrar cliente")
    print("3 - Editar cliente")
    print("4 - Excluir cliente")

    opcao = int(input("Digite sua escolha: "))

    if opcao == 1:
        listar_cliente()

    elif opcao == 2:
        cadastrar_cliente()

    elif opcao == 3:
        Editar_cliente()

    elif opcao == 4:
        Excluir_cliente()