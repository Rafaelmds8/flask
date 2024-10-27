from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('formulario.html')

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome']
    email = request.form['email']
    mensagem = request.form['mensagem']
    telefone = request.form.get('telefone', '')
    idade = request.form.get('idade', '')

    # Aqui você pode processar os dados como quiser, por exemplo, salvá-los em um banco de dados

    return f"Dados recebidos: Nome: {nome}, E-mail: {email}, Mensagem: {mensagem}, Telefone: {telefone}, Idade: {idade}"

if __name__ == '__main__':
    app.run(debug=True)




