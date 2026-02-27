# arquivo = open("arquivo.txt")

# linhas = arquivo.readlines()

# print(linhas)

# arquivo = open("arquivo.txt")

# linhas = arquivo.read()

# print(linhas)

# criaR UM ARQUIVO E ESCREVER NELE ===========================

w = open("arquivo2.txt", "a")

w.write("leo esta ficando brabo nisso de python")

w.close()

arquivo = open("arquivo2.txt")

linhas = arquivo.read()

print(linhas)
