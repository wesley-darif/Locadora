import banco
from CRUD import CRUDGenero, CRUDFuncionarios, CRUDCliente, CRUDFilme
from flask import Flask
from flask import jsonify
app = Flask(__name__)


from Routes import *
if __name__ == "__main__":
    app.run()


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
    except:
        print("Erro!! Digite apenas um numero inteiro 1, 2, 3 ou 4")