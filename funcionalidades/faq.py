def mostrar_menu_perguntas():
    while True:
        perguntas = {
            "Como faço para cadastrar um livro?": "Para cadastrar um livro é muito fácil. No menu da sua conta, acesse 'Minha Biblioteca', depois 'Adicionar Livro'. Lá você pode editar todas as principais informações do seu livro. ",
            "EXEMPLO - Qual é o seu animal favorito?": "Meu animal favorito é o cachorro.",
            "EXEMPLO - Qual é o seu filme favorito?": "Meu filme favorito é O Senhor dos Anéis."
        }
        
        print("\nBem vindo ao FAQ - SOUL!\nEscolha uma pergunta digitando o número correspondente:")
        for i, pergunta in enumerate(perguntas.keys(), 1):
            print(f"{i}. {pergunta}")
        print(f"{(len(perguntas) + 1)}. Voltar ao menu principal")
        
        escolha = int(input("Sua escolha: "))
        try:
            escolha >= 1 and escolha <= len(perguntas) + 1
        except ValueError:
            print("Escolha inválida. Por favor, escolha um número válido.")
        else:
            if escolha <= len(perguntas):
                pergunta = list(perguntas.keys())[escolha - 1]
                resposta = perguntas[pergunta]
                print(f"\nPergunta: {pergunta}")
                print(f"Resposta: {resposta}")
            else:
                return
