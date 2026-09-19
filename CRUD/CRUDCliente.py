from datetime import date

from banco import conexao, cursor

print("Escolha uma opção:\n 1 - Listar Clientes\n 2 - Cadastrar Clientes\n 3 - Editar Clientes\n 4 - Excluir Clientes" )



#Função para listar Clientes
def listar_cliente():
    cursor.execute("SELECT * FROM Tbl_Clientes")

    for Nome_Cliente in cursor.fetchall():
        print(Nome_Cliente)


# Função para Cadastrar Clientes
def cadastrar_cliente():
    cursor.execute("SELECT * FROM Tbl_Clientes")
    Nome = (input("Informe o nome do Cliente: "))
    ID = int(input("Informe o ID do Cliente: "))
    Nascimento = (input("Informe o nascimento do Cliente: "))
    Sexo = (input("Informe o sexo do Cliente: "))
    Telefone = int(input("Informe o telefone do Cliente: "))
    Endereco = (input("Informe o endereco do Cliente: "))
    print("Cliente cadastrado com sucesso")


    comando = f"""INSERT INTO Tbl_Clientes (Nome_Cliente, Codigo_Cliente, Data_Nascimento, Sexo, Telefone, Endereco) VALUES ('{Nome}', {ID}, '{Nascimento}', '{Sexo}', '{Telefone}', '{Endereco}')"""
    cursor.execute(comando)
    cursor.commit()


#Função editar Genero

def Editar_cliente():
    cursor.execute("SELECT * FROM Tbl_Clientes")
    Nome = (input("Informe o nome do Cliente: "))
    ID = (input("Informe o ID do Cliente: "))
    ID_NOVO = int(input("Informe o novo ID: "))
    Nascimento = (input("Informe o nascimento do Cliente: "))
    Sexo = (input("Informe o sexo do Cliente: "))
    Telefone = int(input("Informe o telefone do Cliente: "))
    Endereco = (input("Informe o endereco do Cliente: "))


    comando = f"""UPDATE Tbl_Clientes SET Nome_Cliente = '{Nome}', Codigo_Cliente = '{ID_NOVO}', Data_Nascimento = '{Nascimento}', Sexo = '{Sexo}', Telefone = {Telefone}, Endereco = '{Endereco}' WHERE Codigo_Cliente = '{ID}'"""
    cursor.execute(comando,)
    cursor.commit()
    print("Cliente Editado com sucesso")


#Função excluir Cliente

def Excluir_cliente():
    cursor.execute("SELECT * FROM Tbl_Clientes")
    ID = (input("Informe o ID do Cliente: "))

    comando = f"""DELETE FROM Tbl_Clientes WHERE Codigo_Cliente = '{ID}'"""
    cursor.execute(comando,)
    cursor.commit()
    print("Genero excluido com sucesso")

opcao = int(input("Digite sua escolha: "))
if opcao == 1:
    listar_cliente()
elif opcao == 2:
    cadastrar_cliente()
elif opcao == 3:
    Editar_cliente()
else:
    Excluir_cliente()