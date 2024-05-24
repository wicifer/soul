from flask import Flask, render_template, request, redirect, url_for, flash
import json

def get_biblioteca():
    biblioteca = []
    try:
        file = open('arquivos/biblioteca.txt')
    except:
        print('Não há livros registrados em sua biblioteca.\n')
        return []
    else:
        for line in file:
            livro = json.loads(line)
            biblioteca.append(livro)
        file.close()

    return biblioteca

def compartilhar(livro, mensagem):
    livro = json.loads(livro.replace("'", '"'))
    
    if mensagem != "padrao":
        mensagem = f"{mensagem} \n{livro['titulo']} por {livro['autor']}"
    else:
        mensagem = f"Achei este livro a sua cara! Dê uma chance para {livro['titulo']} por {livro['autor']}."
    
    flash("Sua mensagem para compartilhar está pronta!")
    return render_template('compartilhar_livro.html', livro=livro, mensagem=mensagem)

def edicao(livro, atributo, novo_atributo):
    novo_atributo = novo_atributo.replace("'", "").replace('"', '')
    biblioteca = get_biblioteca()
    indice = achar_livro(biblioteca, livro)
    livro = biblioteca[indice]

    livro[atributo] = novo_atributo
    biblioteca[indice] = livro
    salvar_biblioteca(biblioteca)

    flash("Livro editado!")
    return render_template('livro.html', livro=livro)

def achar_livro(biblioteca, livro_editar):
    livro_editar = json.loads(livro_editar.replace("'", '"'))
    for index, livro in enumerate(biblioteca):
        if  livro['titulo'] == livro_editar['titulo']:
            return index

def deletar_livro(livro):
    biblioteca = get_biblioteca()
    indice = achar_livro(biblioteca, livro)

    biblioteca.pop(indice)
    salvar_biblioteca(biblioteca)
    flash("Livro deletado!")

    return render_template('biblioteca.html', biblioteca=biblioteca)

def adicionar_livro():
    biblioteca = get_biblioteca()

    titulo = request.form['titulo'].replace("'", "").replace('"', '')
    autor = request.form['autor'].replace("'", "").replace('"', '')
    genero = request.form['genero'].replace("'", "").replace('"', '')
    estrelas = request.form['estrelas'].replace("'", "").replace('"', '')

    livro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "estrelas": estrelas
    }

    biblioteca.append(livro)

    salvar_biblioteca(biblioteca)

    flash("Livro adicionado! \n")

    return render_template('biblioteca.html', biblioteca=biblioteca)

def salvar_biblioteca(biblioteca):
    file = open('arquivos/biblioteca.txt', 'w')

    for livro in biblioteca:
        livro = json.dumps(livro)
        file.write(livro + '\n')
    file.close()
