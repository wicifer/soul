from funcionalidades import biblioteca
from funcionalidades import dicas_leitura
from funcionalidades import faq
from funcionalidades import login
from funcionalidades import ofertas
from funcionalidades import ranking
from funcionalidades import recomendacoes

def main_menu():
    print("\n Menu principal: \n")
    print("1. Minha biblioteca")
    print("2. Recomendações de livros")
    print("3. Ranking - Quem leu mais livros")
    print("4. Espaço de ofertas")
    print("5. FAQ do site")
    print("6. Dicas para melhorar sua sessão de leitura")
    print("7. Sair")

def menu_biblioteca(biblioteca_usuario):
    return biblioteca.main(biblioteca_usuario)

def recomendar_livros():
    recomendacoes.main()

def menu_ranking():
    ranking.main()

def menu_ofertas():
    ofertas.main()

def menu_faq():
    faq.mostrar_menu_perguntas()

def menu_dicas_leitura():
    dicas_leitura.main()

def menu_login():
    return login.main()

def sair():
    print("Saindo do programa...")
    exit()

def main():
    print("Soul v0.1")
    login = menu_login()

    if login["resultado"] == True:
        print(f"Olá, {login['username']}.")
        biblioteca_usuario = []

        while True:
            main_menu()
            choice = input("Escolha uma opção: ")

            if choice == '1':
                biblioteca_usuario =  menu_biblioteca(biblioteca_usuario)
            elif choice == '2':
                recomendar_livros()
            elif choice == '3':
                menu_ranking()
            elif choice == '4':
                menu_ofertas()
            elif choice == '5':
                menu_faq()
            elif choice == '6':
                menu_dicas_leitura()
            elif choice == '7':
                sair()
            else:
                print("Opção inválida.")
        else:
            sair()

if __name__ == "__main__":
    main()
