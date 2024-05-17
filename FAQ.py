def mostrar_menu_perguntas():
    perguntas = {
        "Como faço para cadastrar um livro?": "Para cadastrar um livro é muito fácil. No menu da sua conta, acesse 'Minha Biblioteca', depois 'Adicionar Livro'. Lá você pode editar todas as principais informações do seu livro. ",
        "EXEMPLO - Qual é o seu animal favorito?": "Meu animal favorito é o cachorro.",
        "EXEMPLO - Qual é o seu filme favorito?": "Meu filme favorito é O Senhor dos Anéis."
    }
    
    print("Bem vindo ao FAQ - SOUL!\nEscolha uma pergunta digitando o número correspondente:")
    for i, pergunta in enumerate(perguntas.keys(), 1):
        print(f"{i}. {pergunta}")
    
    escolha = input("Sua escolha: ")
    try:
        escolha = int(escolha)
        if escolha >= 1 and escolha <= len(perguntas):
            pergunta = list(perguntas.keys())[escolha - 1]
            resposta = perguntas[pergunta]
            print(f"Pergunta: {pergunta}")
            print(f"Resposta: {resposta}")
        else:
            print("Escolha inválida. Por favor, escolha um número válido.")
    except ValueError:
        print("Por favor, insira um número válido.")

mostrar_menu_perguntas()
