import bcrypt
import json

def criar_usuario(username, password):
    # Gerar um salt e encriptar a senha
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Salvar o nome de usuário e a senha encriptada em um arquivo JSON
    users = carregar_usuarios()
    users[username] = hashed_password.decode('utf-8')
    save_users(users)

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
def login(username, password):
    users = carregar_usuarios()

    if username in users:
        hashed_password = users[username].encode('utf-8')
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            print("\nLogin bem-sucedido!")
            return True
        else:
            print("\nSenha incorreta.")
            return False
    else:
        print("\nUsuário não encontrado.")
        return False

def main():
    while True:
        print("\n1. Login")
        print("2. Criar novo usuário")
        print("3. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            username = input("Digite o nome de usuário: ")
            password = input("Digite a senha: ")
            resultado_login = login(username, password)
            print(resultado_login)
            if resultado_login == True:
                return { "resultado": True, "username": username }
        elif choice == '2':
            username = input("Digite o nome de usuário: ")
            password = input("Digite a senha: ")
            criar_usuario(username, password)
            print("\nUsuário criado com sucesso!")
        elif choice == '3':
            return { "resultado": False }
        else:
            print("Opção inválida.")
