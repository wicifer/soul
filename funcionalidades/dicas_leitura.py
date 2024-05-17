def menu():
    print("01. Como melhorar a leitura")
    print("02. Dicas para melhorar o desempenho na leitura")
    print("03. Sair")

def melhorar_leitura(): 
    print("1-Leitura Ativa: Entenda o conteúdo de antemão. Comece lendo o sumário, o resumo e a conclusão. Desenvolva atividades como pesquisar termos desconhecidos, prestar atenção nos trechos destacados e marcar trechos importantes;"
    " 2-Concentração: A concentração é importante para desenvolver a habilidade de leitura. O método Pomodoro, por exemplo, sugere que você leia por 25 minutos e faça uma pausa de 5;"
    " 3-Vocabulário: Quanto mais uma pessoa lê, mais ela expande o seu conhecimento e vocabulário;"
    " 4-Planejamento: Estabelecer metas de leitura e elaborar um plano de estudos são passos fundamentais para otimizar seu tempo e alcançar seus objetivos de leitura;"
    " 5-Técnica de Scanning: Scanning envolve uma varredura rápida do texto em busca de palavras-chave e informações relevantes;"
    " 6-Audiolivros: Se o tempo é escasso, os audiolivros podem ser a solução ideal. Você pode ouvir narrativas enquanto realiza outras atividades;"
    " 7-Evite reler trechos: Resistir à tentação de reler trechos é essencial para manter o fluxo da leitura;"
    " 8-Clube do Livro: Juntar-se a um clube do livro não apenas acelera o ritmo de leitura, mas também torna a experiência mais envolvente e enriquecedora;")
    


def dicas_desempenho_leitura():
    print("1-Reservar um tempo específico de leitura diária;"
    " 2-Ler o que desperta interesse;"
    " 3-Ao ler, termine o capítulo;"
    " 4-Resumir o que foi lido à mão;"
    " 5-Meditar o que foi lido;"
    " 6-Ter sempre à mão um caderno de anotações;"
    " 7-Buscar acompanhamento com professores renomados na área de estudos;"
    " 8-Conversar com outras pessoas sobre os estudos;"
    " 9-Melhorar habilidades distintas como foco, memória, agilidade, linguagem e resolução de problemas;"
    " 10-Adquira ordem interior;"
    " 11-Estudar sobre como ler melhor.")
    

    
def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            melhorar_leitura()
        elif opcao == '2':
            dicas_desempenho_leitura()
        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
