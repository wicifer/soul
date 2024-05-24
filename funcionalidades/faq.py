from flask import Flask, render_template, request, redirect, url_for, flash

def mostrar_menu_perguntas():

    perguntas = [
        {"pergunta": "Como faço para cadastrar um livro?", "resposta": "Para cadastrar um livro é muito fácil. No menu da sua conta, acesse 'Minha Biblioteca', depois 'Adicionar Livro'. Lá você pode editar todas as principais informações do seu livro. "},
        {"pergunta": "EXEMPLO - Qual é o seu animal favorito?", "resposta":  "Meu animal favorito é o cachorro."},
        {"pergunta": "EXEMPLO - Qual é o seu filme favorito?", "resposta":  "Meu filme favorito é O Senhor dos Anéis."}
    ]

    return render_template('faq.html', perguntas=perguntas)
