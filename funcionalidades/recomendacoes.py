# Dicionário de livros com suas categorias

# TO DO: colocar num arquivo
livros = {
    "A Culpa é das Estrelas": ["Romance", "Drama"],
    "1984": ["Ficção Científica", "Distopia"],
    "O Senhor dos Anéis": ["Fantasia", "Aventura"],
    "Dom Quixote": ["Clássico", "Aventura"],
    "Percy Jackson e o Ladrão de Raios": ["Fantasia", "Aventura"],
    "O Código Da Vinci": ["Suspense", "Mistério"],
    "Harry Potter e a Pedra Filosofal": ["Fantasia", "Aventura"],
    "A Arte da Guerra": ["Filosofia", "Estratégia"],
    "O Pequeno Príncipe": ["Clássico", "Fantasia"],
    "Orgulho e Preconceito": ["Romance", "Clássico"]
}
def opcoes_recomendacoes():
    print("\nEscolha uma categoria para receber recomendações:")
    print("1. Romance")
    print("2. Ficção Científica")
    print("3. Fantasia")
    print("4. Suspense")
    print("5. Clássico")
    print("6. Outro")
    print("7. Voltar ao menu principal")

# Função para recomendar livros com base na categoria
def recomendar_livros_por_categoria(categoria):
    recomendacoes = []
    for livro, categorias in livros.items():
        if categoria in categorias:
            recomendacoes.append(livro)
    return recomendacoes

# Função principal
def main():
    categoria = []
    print("\nBem-vindo ao sistema de recomendação de livros!")

    while True:
        opcoes_recomendacoes()
        escolha = input("\nDigite o número correspondente à categoria desejada: ")

        if escolha == "1":
            categoria = "Romance"
        elif escolha == "2":
            categoria = "Ficção Científica"
        elif escolha == "3":
            categoria = "Fantasia"
        elif escolha == "4":
            categoria = "Suspense"
        elif escolha == "5":
            categoria = "Clássico"
        elif escolha == "6":
            categoria = input("Digite outra categoria: ")
        elif escolha == "7":
            return
        else:
            print("Opção inválida.")

        if bool(categoria):
            recomendacoes = recomendar_livros_por_categoria(categoria)
            if recomendacoes:
                print(f"\nRecomendações na categoria '{categoria}':")
                for livro in recomendacoes:
                    print("-", livro) 
            else:
                print("Não foram encontradas recomendações para essa categoria.")

        


