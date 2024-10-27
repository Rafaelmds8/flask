
from flask import Flask, abort, redirect, url_for

app = Flask(__name__)


@app.route("/")
def hello():
    return "Primeira API com Flask"


list = ["Rafael", "Anna", "Arthur", "Anne"]


@app.route("/nomeFamilia")
def nFamily():
    return f"{list}"


# redirecionando para outra página
@app.route("/r")
def index():
    return redirect(url_for("nFamily"))


class DadosUsuario:
    def __init__(self, nome, idade, sexo, estado_civil, id):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.id = id

    # def confirmar_usuario(self):
    #     if user1 == 35 and user1.sexo == "Masculino":
    #         print(
    #             f" Dados do Usuario:\nNome:{user1.nome}\nIdade:{user1.idade}\nSexo:{user1.sexo}\nEstado Civil:{user1.estado_civil}\n"
    #         )
    #     else:
    #         print("Usuario não encontrado")


user1 = DadosUsuario(
    nome="Rafael", idade=35, sexo="Masculino", estado_civil="Casado", id=1
)


@app.route("/2")
def dados_usuario():
    if user1.idade >= 35:
        dados_user1 = f" Dados do Usuario:\nNome:{user1.nome}\nIdade:{user1.idade}\nSexo:{user1.sexo}\nEstado Civil:{user1.estado_civil}\nID:{user1.id}\n"
    else:
        dados_user1 = f"Usuario não encontrado"

    return f"{dados_user1}"


# Exemplo de método PUT
@app.route("/3", methods=["PUT"])
def alterar_user():
    # alterando uma variável após uma condição
    if user1.idade > 30:
        user1.nome = "Rafael Monte"

    return f"Dados do Usuario:\nNome:{user1.nome}\nIdade:{user1.idade}\nSexo:{user1.sexo}\nEstado Civil:{user1.estado_civil}\nID:{user1.id}\n"


# Exemplo do metódo DELETE
@app.route("/<id>", methods=["DELETE"])
def delete_user(id):
    return id


@app.route("/4", methods=["POST"])
def add_user():
    list.append("Richard T")
    return f"{list}"


if __name__ == "__main__":
    app.run(debug=True)