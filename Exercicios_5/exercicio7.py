#Frufru para a senha não aparecer.
from getpass import getpass

def validar_senha(senha_funcao):
    #return len(senha >= 8) -> retorna verdadeiro ou falso.
    if len(senha_funcao) >= 8:
        print("Senha válida.")
        return True
    else:
        print("Senha inválida.")
        return False
    
def cadastro_terminal():
    usuario = input("Digite o seu nome de usuário: ")
    senha = getpass("Digite uma senha de 8 digitos ou mais: ")
    #Validação da senha usando a função.
    while not validar_senha(senha):
        senha = getpass("Digite uma senha de 8 digitos ou mais: ")
    print("Cadastro realizado com sucesso!")

cadastro_terminal()