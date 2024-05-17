def espaco_de_ofertas():
    ofertas = {"R$ 15.00", "R$ 17.50", "R$ 20,00", "R$ 30,00", "R$ 35,50", "R$ 40,00", "R$ 55,50", "R$ 70,00", "R$ 85,50", "R$ 100,00"}
    resultado = ofertas
    input(f"Digite o valor das ofertas {resultado} dos livros: ")

livros = []    

for i in range(10):
  livro_de_ofertas = input(f"Digite o valor do {i+1}° livro das ofertas: ")

resultado = espaco_de_ofertas / livro_de_ofertas

if espaco_de_ofertas == '0':
   print(livro_de_ofertas)
elif espaco_de_ofertas == '1':
   print(livro_de_ofertas)
else:
   print("Valor inválido. Escolha dos livros das ofertas.")

print(f'''Valor total das ofertas: {resultado} ''')