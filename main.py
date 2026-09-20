import banco
#from CRUD.CRUDGenero import listar_genero, cadastrar_genero, Editar_genero
#from CRUD.CRUDFilme import listar_filmes, cadastrar_filmes, Editar_filmes, Excluir_filmes
#from CRUD.CRUDCliente import listar_cliente, cadastrar_cliente, Editar_cliente, Excluir_cliente
#from CRUD.CRUDFuncionarios import listar_funcionario, cadastrar_funcionario, Editar_funcionario, Excluir_funcionario
from CRUD import CRUDGenero, CRUDFuncionarios, CRUDCliente, CRUDFilme


if __name__ == "__main__":
    print("1 - Genero")
    print("2 - Filme")
    print("3 - Cliente")
    print("4 - Funcionario")

    try:
        opcao = int(input("Digite sua escolha: "))
        if opcao == 1:
            CRUDGenero.menu_genero()
        elif opcao == 2:
            CRUDFilme.menu_filme()
        elif opcao == 3:
            CRUDCliente.menu_cliente()
        elif opcao == 4:
            CRUDFuncionarios.menu_funcionario()
    except ValueError:
        print("Erro!! Digite apenas um numero inteiro 1, 2, 3 ou 4")