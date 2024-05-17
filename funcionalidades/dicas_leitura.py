def main():
    print("\n")
    file = open('arquivos/dicas_leitura.txt')
    for line in file:
        livro = print(line)
    file.close()
