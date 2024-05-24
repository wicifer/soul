from flask import Flask, render_template, request, redirect, url_for, flash
import json

# Dicionário de livros com suas categorias
def biblioteca_recomendacoes():
    file = open('arquivos/recomendacoes.txt')
    livros = json.load(file)
    return livros

# Função para recomendar livros com base na categoria
def recomendar_livros_por_categoria(categoria):
    recomendacoes = []
    livros = biblioteca_recomendacoes()
    for livro, categorias in livros.items():
        if categoria in categorias:
            recomendacoes.append(livro)
    return recomendacoes

# Função principal
def recomendar(genero):
    recomendacoes = recomendar_livros_por_categoria(genero)
    if recomendacoes:
        print(f"\nRecomendações no gênero '{genero}':")
        for livro in recomendacoes:
            print("-", livro) 
    else:
        flash("Não foram encontradas recomendações para esse gênero.")
    
    return render_template('recomendacoes.html', recomendacoes=recomendacoes, genero=genero)
    
