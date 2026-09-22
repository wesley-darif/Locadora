from banco import conexao, cursor

#Função para listar Funcionarios
def listar_funcionario():
    cursor.execute("SELECT * FROM Tbl_Funcionarios")

    for Nome_Do_Funcionario in cursor.fetchall():
        print(Nome_Do_Funcionario)


# Função para Cadastrar funcionarios
def cadastrar_funcionario():
    try:
        Nome = (input("Informe o nome do funcionario: "))
        Sexo = (input("Informe o sexo do funcionario: "))

        comando = """INSERT INTO Tbl_Funcionarios (Nome_do_Funcionario, Sexo) VALUES (?, ?, ?)"""
        cursor.execute(comando, Nome, Sexo)
        cursor.commit()
        print("Funcionario cadastrado com funcionario")
    except ValueError:
        print("Erro!! Digite apenas um numero inteiro")




#Função editar Funcionario

def Editar_funcionario():
    try:

        Nome = (input("Informe o nome do Funcionario: "))
        Sexo = (input("Informe o sexo do Funcionario: "))
        ID = int(input("Informe o ID do Funcionario: "))

        comando = """UPDATE Tbl_Funcionarios SET Nome_do_Funcionario = ?, sexo = ? WHERE Codigo = ?"""
        cursor.execute(comando, Nome, Sexo, ID)
        cursor.commit()
        print("Funcionario Editado com sucesso")
    except ValueError:
        print("Erro!! Digite apenas um numero inteiro")


#Função excluir Funcionario

def Excluir_funcionario():
    try:

        ID = int(input("Informe o ID do funcionario: "))

        comando = """DELETE FROM Tbl_Funcionarios WHERE Codigo = ?"""
        cursor.execute(comando, ID)
        cursor.commit()
        print("Funcionario excluido com sucesso")
    except ValueError:
        print("Erro!! Digite apenas um numero inteiro")


def menu_funcionario():

    try:
        print("1 - Listar funcionario")
        print("2 - Cadastrar funcionario")
        print("3 - Editar funcionario")
        print("4 - Excluir funcionario")

        opcao = int(input("Digite sua escolha: "))

        if opcao == 1:
            listar_funcionario()

        elif opcao == 2:
            cadastrar_funcionario()

        elif opcao == 3:
            Editar_funcionario()

        elif opcao == 4:
            Excluir_funcionario()
    except ValueError:
        print("Erro!! Digite apenas um numero inteiro")