from flask import Flask, render_template, request, redirect, url_for, flash
from funcionalidades import biblioteca
from funcionalidades import dicas_leitura
from funcionalidades import faq
from funcionalidades import login
from funcionalidades import ofertas
from funcionalidades import ranking
from funcionalidades import recomendacoes

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/main_menu')
def main_menu():
    return render_template('main_menu.html')

@app.route('/biblioteca')
def menu_biblioteca():
    livros = biblioteca.get_biblioteca()
    return render_template('biblioteca.html', biblioteca=livros)

@app.route('/biblioteca/adicionar_info', methods=['POST'])
def adicionar_livro_info():
    return render_template('adicionar_livro.html')

@app.route('/biblioteca/adicionar_livro', methods=['POST'])
def adicionar_livro_biblioteca():
    return biblioteca.adicionar_livro()

@app.route('/biblioteca/selecionar_livro', methods=['POST'])
def selecionar_livro():
    livro = request.form['book_info']
    return render_template('livro.html', livro=livro)

@app.route('/biblioteca/editar_livro_menu', methods=['POST'])
def editar_livro_menu():
    livro = request.form['book_info']
    return render_template('editar_livro_menu.html', livro=livro)

@app.route('/biblioteca/editar_livro_atributo', methods=['POST'])
def editar_livro_atributo():
    livro = request.form['book_info']
    atributo = request.form['edit_info']

    return render_template('editar_livro_atributo.html', livro=livro, atributo=atributo)

@app.route('/biblioteca/editar_livro', methods=['POST'])
def editar_livro():
    livro = request.form['book_info']
    atributo = request.form['edit_info']
    novo_atributo = request.form['novo_atributo']

    return biblioteca.edicao(livro, atributo, novo_atributo)

@app.route('/biblioteca/excluir_livro_menu', methods=['POST'])
def excluir_livro_menu():
    livro = request.form['book_info']
    return render_template('excluir_livro.html', livro=livro)

@app.route('/biblioteca/excluir_livro', methods=['POST'])
def excluir_livro():
    livro = request.form['book_info']
    return biblioteca.deletar_livro(livro)

@app.route('/biblioteca/compartilhar_livro_menu', methods=['POST'])
def compartilhar_livro_menu():
    livro = request.form['book_info']
    return render_template('compartilhar_livro_menu.html', livro=livro)

@app.route('/biblioteca/compartilhar_livro', methods=['POST'])
def compartilhar_livro():
    livro = request.form['book_info']
    mensagem = request.form['mensagem']
    return biblioteca.compartilhar(livro, mensagem)

@app.route('/recomendacoes_menu', methods=['GET'])
def recomendacoes_menu():
    return render_template('recomendacoes_menu.html')

@app.route('/recomendacoes', methods=['POST'])
def recomendar():
    genero = request.form['genero']
    return recomendacoes.recomendar(genero)

@app.route('/ranking', methods=['GET'])
def menu_ranking():
    return ranking.main()

@app.route('/ofertas', methods=['GET'])
def menu_ofertas():
    return ofertas.main()

@app.route('/faq', methods=['GET'])
def menu_faq():
    return faq.mostrar_menu_perguntas()

@app.route('/dicas_leitura', methods=['GET'])
def menu_dicas_leitura():
   return dicas_leitura.main()

@app.route('/login', methods=['POST'])
def menu_login():
    return login.login()

@app.route('/signin', methods=['POST'])
def signin():
    return render_template('create_user.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    return login.criar_usuario()

if __name__ == "__main__":
    app.run(debug=True)
