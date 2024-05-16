import json

def main_menu():
    print("Menu principal:")
    print("1. Minha biblioteca")
    print("2. Recomendações de livros")
    print("3. Ranking - Quem leu mais livros")
    print("4. Espaço de ofertas")
    print("5. FAQ do site")
    print("6. Seção de como melhorar sua sessão de leitura")
    print("7. Sair")

def minha_biblioteca(biblioteca):
    if not biblioteca:
        biblioteca = get_biblioteca(biblioteca)

    print("Minha biblioteca:\n")
    mostrar_biblioteca(biblioteca)

    print("1. Adicionar livro")
    print("2. Selecionar livro")
    print("3. Voltar ao menu principal")
    # TO DO: método opções biblioteca?

    choice = input("Escolha uma opção: ")
    if choice == '1':
      biblioteca = adicionar_livro(biblioteca)
      return biblioteca
    elif choice == '2':
      if len(biblioteca) == 0:
        print("Não há livros registrados em sua biblioteca.\n")
        # loo voltar pro adicionar
      else:
        selecionar_livro(biblioteca)
        choice = input("Escolha uma opção: ")
        # TO DO: move this to selecionar_livro method
    elif choice == '3':
      return
    else:
        print("Opção inválida.")

def get_biblioteca(biblioteca):
    try:
        file = open('biblioteca.txt')
    except:
        print('Não há livros registrados em sua biblioteca.\n')
        return []
    else:
        for line in file:
            livro = json.loads(line)
            biblioteca.append(livro)

    return biblioteca

def mostrar_biblioteca(biblioteca):
    for livro in biblioteca:
        print(f'{livro}\n')

def selecionar_livro():
    print("Selecionar livro:")
    print("1. Compartilhar")

    print("2. Editar livro")
    print("3. Excluir livro")
    print("4. Voltar ao menu principal")
          # TO DO: Handle options for selecting a book

def recomendar_livros():
    print("Recomendações de livros")

def ranking():
    print("Ranking - Quem leu mais livros")

def ofertas():
    print("Espaço de ofertas")

def faq():
    print("FAQ do site")

def melhorar_sessao_de_leitura():
    print("Seção de como melhorar sua sessão de leitura")

def sair():
    print("Saindo do programa...")
    exit()

def adicionar_livro(biblioteca):
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor: ")
    genero = input("Digite o gênero: ")
    estrelas = input("Quantas estrelas? (1-5)")
    data_inicio = input("Quando começou a ler? (formato dd/mm/aaaa) ")
    data_fim = input("Quando terminou de ler? (formato dd/mm/aaaa) ")

    livro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "estrelas": estrelas,
        "data_inicio": data_inicio,
        "data_fim": data_fim
    }

    biblioteca.append(livro)

    salvar_biblioteca(biblioteca)

    print("Livro adicionado! \n")

    return biblioteca

def salvar_biblioteca(biblioteca):
    file = open('biblioteca.txt', 'w')
    for livro in biblioteca:
        livro = json.dumps(livro)
        file.write(livro + '\n')
    file.close()

def main():
    # TO DO: login
    # Salvar senha em um arquivo, checar se a senha bate com o login etc
    # talvez encriptar
    # username = login()

    username = 'João'
    print(f"Olá, {username}. \n")
    biblioteca = []

    while True:
        main_menu()
        choice = input("Escolha uma opção: ")

        if choice == '1':
            biblioteca = minha_biblioteca(biblioteca)
        elif choice == '2':
            recomendar_livros()
        elif choice == '3':
            ranking()
        elif choice == '4':
            ofertas()
        elif choice == '5':
            faq()
        elif choice == '6':
            melhorar_sessao_de_leitura()
        elif choice == '7':
            sair()
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()