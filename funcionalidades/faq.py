from flask import Flask, render_template, request, redirect, url_for, flash

def mostrar_menu_perguntas():

    perguntas = [
        {"pergunta": "O que é o SOUL?", "resposta":  "SOUL é um aplicativo simples e fácil de usar que permite aos usuários catalogar os livros que mais apreciam, receber recomendações personalizadas e interagir com outros leitores. Facilitando a descoberta de novos títulos que vão enriquecer ainda mais a experiência literária do usuário."},
        {"pergunta": "Como faço para cadastrar um livro?", "resposta": "Para cadastrar um livro é muito fácil. No menu da sua conta, acesse 'Minha Biblioteca', depois 'Adicionar Livro'. Lá você pode editar todas as principais informações do seu livro. "},
        {"pergunta": "Como funciona a recomendação de livros?", "resposta":  "O sistema de recomendação de livros sugere leituras com base nos interesses do leitor, por exemplo: recomendação por gênero."},
        {"pergunta": "Como posso participar do Ranking?", "resposta":  "O ranking está disponível para todos os usuários. O ranking conta a quantidade de livros lidos pelo usuário durante todo o mês. O 1º, 2º e 3º colocados, recebem premiações."},
        {"pergunta": "Qual a melhor forma para adquirir novos livros?", "resposta":  "Temos um sistema que faz uma procura diariamente em diversas lojas, mostrando para o usuário as melhores ofertas da internet. Basta entrar no 'Espaço de Ofertas' e verificar se alguma oferta lhe agrada."},
    ]

    return render_template('faq.html', perguntas=perguntas)
