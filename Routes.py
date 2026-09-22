from codecs import make_identity_dict

from flask import request, jsonify, make_response

from CRUD import CRUDFilme
from main import app

#Rotas
@app.route("/")
def index():
    return "Site"
if __name__ == "__main__":
    app.run(debug=True)

@app.route("/Filmes", methods=['GET'])
def get_filmes():
    filmes = {'Nome_Filme'}
    return make_response(
        jsonify({"filmes": CRUDFilme.listar_filmes(
        )}),
        200,
    )



@app.route("/Filmes", methods=["POST"])
def post_filme():

    filme = request.get_json()

    resultado = CRUDFilme.cadastrar_filmes(
        filme["Nome"],
        filme["Classificacao"],
        filme["CodigoGenero"],
        filme["Preco"],
        filme["Estoque"]
    )

    return jsonify({
            "mensagem": resultado
        }),201
