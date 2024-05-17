import json
from funcionalidades import faq

def main_menu():
    print("\n Menu principal: \n")
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

    print("\n Minha biblioteca:\n")
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
      else:
        biblioteca = menu_livro(biblioteca)
        return biblioteca
    elif choice == '3':
      return biblioteca
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
    count = 1
    for livro in biblioteca:
        print(f'{count}. {livro}\n')
        count += 1

def menu_livro(biblioteca):
    indice = int(input("Digite o número do livro gostaria que deseja selecionar: ")) - 1

    try:
        livro = biblioteca[indice]
    except:
        print("Não há livro com esse número em sua biblioteca.")
    else:
        print(f'\n Livro selecionado: \n {livro} \n')

        opcoes_livro()

        choice = input("Escolha uma opção: ")
        if choice == '1':
            compartilhar(livro)
        elif choice == '2':
            biblioteca = edicao(biblioteca, livro, indice)
        elif choice == '3':
            biblioteca = deletar_livro(biblioteca, indice)
        elif choice == '4':
            return biblioteca
        else:
            print("Opção inválida.")
    
    return biblioteca

def edicao(biblioteca, livro, indice):
    livro_editado = editar_livro(livro)
    biblioteca[indice] = livro_editado
    salvar_biblioteca(biblioteca)
    print("Livro editado!")
    return biblioteca

def deletar_livro(biblioteca, indice):
    confirmacao = int(input("Tem certeza que deseja deletar o livro de sua biblioteca? \n 1. Sim\n 2. Não\n"))
    if confirmacao == 1:
        biblioteca.pop(indice)
        salvar_biblioteca(biblioteca)
        print("Livro deletado!")
    elif confirmacao == 2: 
        print("Ok, livro não deletado!")
    else:
        print("Opção inválida.")
    return biblioteca
         
def opcoes_livro():
    print("1. Compartilhar")  
    print("2. Editar livro")
    print("3. Excluir livro")
    print("4. Voltar ao menu principal")

def editar_livro(livro):
    print(f"{livro} \n")

    chaves_livro(livro)

    choice = int(input("\n O que deseja alterar? "))

    if choice == 1:
        titulo = input("Digite o novo título: ")
        livro['titulo'] = titulo
    elif choice == 2:
        autor = input("Digite o novo título: ")
        livro['autor'] = autor
    elif choice == 3:
        genero = input("Digite o novo gênero: ")
        livro['genero'] = genero
    elif choice == 4:
        estrelas = int(input("Digite as novas estrelas: "))
        livro['estrelas'] = estrelas
    elif choice == 5:
        data_inicio = input("Digite a nova data de início: ")
        livro['data_inicio'] = data_inicio
    elif choice == 6:
        data_fim = input("Digite a nova data de fim: ")
        livro['data_fim'] = data_fim
    return livro

def chaves_livro(livro):
    counter = 1
    for line in livro:
        print(f'{counter}. {line}')
        counter += 1

def recomendar_livros():
    print("Recomendações de livros")

def ranking():
    print("Ranking - Quem leu mais livros")

def ofertas():
    print("Espaço de ofertas")

def menu_faq():
    faq.mostrar_menu_perguntas()

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
    print(f"Olá, {username}.")
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
            menu_faq()
        elif choice == '6':
            melhorar_sessao_de_leitura()
        elif choice == '7':
            sair()
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()