def contar_letras(nome):
    return len(nome)

nome_usuario = input("Digite seu nome: ")
print(f"O nome {nome_usuario} tem {contar_letras(nome_usuario)} letras.")