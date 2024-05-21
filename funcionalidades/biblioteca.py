import json

def main(biblioteca):
    if not biblioteca:
      biblioteca = get_biblioteca(biblioteca)

    print("\n Minha biblioteca:\n")
    mostrar_biblioteca(biblioteca)

    opcoes_biblioteca()

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

def compartilhar(livro):
    print("\nCompartilhando o livro:")
    print("Título:", livro["titulo"])
    print("Autor:", livro["autor"])
    print("Gênero:", livro["genero"])
    print("Estrelas:", livro["estrelas"])

    compartilhar_opcao = input("Deseja compartilhar este livro? (s/n): ")
    if compartilhar_opcao.lower() == 's':
        personalizar = input("Deseja personalizar a mensagem? (s/n): ")
        if personalizar.lower() == 's':
            mensagem = input("Adicione uma mensagem para compartilhar o livro: ")
            mensagem = f"{mensagem} \n{livro['titulo']} por {livro['autor']}"
        else:
            mensagem = f"Achei este livro a sua cara! Dê uma chance para {livro['titulo']} por {livro['autor']}."
        print(f"\nMensagem compartilhada: {mensagem}\n")
    else:
        print("Livro não compartilhado.\n")

def edicao(biblioteca, livro, indice):
    livro_editado = editar_livro(livro)
    biblioteca[indice] = livro_editado
    salvar_biblioteca(biblioteca)
    print("Livro editado!")
    return biblioteca

def deletar_livro(biblioteca, indice):
    confirmacao = input("Tem certeza que deseja deletar o livro de sua biblioteca? (s/n): ")
    if confirmacao.lower() == 's':
        biblioteca.pop(indice)
        salvar_biblioteca(biblioteca)
        print("Livro deletado!")
    elif confirmacao.lower() == 'n': 
        print("Ok, livro não deletado!")
    else:
        print("Opção inválida.")
    return biblioteca
         
def opcoes_livro():
    print("1. Compartilhar")  
    print("2. Editar livro")
    print("3. Excluir livro")
    print("4. Voltar ao menu principal")

def opcoes_biblioteca():
    print("1. Adicionar livro")
    print("2. Selecionar livro")
    print("3. Voltar ao menu principal")

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
    return livro

def chaves_livro(livro):
    counter = 1
    for line in livro:
        print(f'{counter}. {line}')
        counter += 1

def adicionar_livro(biblioteca):
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor: ")
    genero = input("Digite o gênero: ")
    estrelas = input("Quantas estrelas? (1-5)")

    livro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "estrelas": estrelas
    }

    biblioteca.append(livro)

    salvar_biblioteca(biblioteca)

    print("Livro adicionado! \n")

    return biblioteca

def salvar_biblioteca(biblioteca):
    file = open('arquivos/biblioteca.txt', 'w')

    for livro in biblioteca:
        livro = json.dumps(livro)
        file.write(livro + '\n')
    file.close()
