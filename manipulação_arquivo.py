nome = input("Digite o nome: ")
email = input("Digite o E-mail: ")
senha = input("Digite sua senha: ")
idade = input("Digite sua idade: ")

with open("./pesoa.text", "a") as arquivo:
    arquivo.write(f"Nome: {nome} | E-mail: {email}\n Senha: {senha} | Idade: {idade}")