from flask import Flask, render_template, request, redirect, url_for, flash
import bcrypt
import json

def criar_usuario():
    username = request.form['username_create']
    password = request.form['password_create'].encode('utf-8')
    print("Form data received:", request.form)
    # Gerar um salt e encriptar a senha
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)

    # Salvar o nome de usuário e a senha encriptada em um arquivo JSON
    users = carregar_usuarios()
    users[username] = hashed_password.decode('utf-8')
    save_users(users)
    flash('Usuário criado!')
    return redirect(url_for('index'))

# Função para carregar usuários do arquivo JSON
def carregar_usuarios():
    try:
        with open('arquivos/users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Função para salvar usuários no arquivo JSON
def save_users(users):
    with open('arquivos/users.json', 'w') as file:
        json.dump(users, file)

# Função para verificar o login
def login():
    username = request.form['username']
    password = request.form['password']
    users = carregar_usuarios()

    if username in users:
        hashed_password = users[username]
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            flash('Login bem sucedido!')
            return redirect(url_for('main_menu'))
        else:
            flash("\nSenha incorreta.")
            return redirect(url_for('index'))
    else:
        flash("\nUsuário não encontrado.")
        return redirect(url_for('index'))
