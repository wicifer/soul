def main():
    print("\n Ofertas:")
    file = open("arquivos/ofertas.txt")
    for line in file:
        livro = print(f"- {line}")
    file.close()
