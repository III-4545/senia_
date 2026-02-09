from exercicio1 import somar
from exercicio2 import eh_par


def menu():
    opcao = input("[1] - somar números\n[2] - Verificação de par\n [0] - sair\n")

    if opcao == "1":
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        print(n1,n2)
    
    elif opcao == "2":
        numero = int(input("Digite um número para verificação: "))
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
        else:
            print(f"O número {numero} é ímpar.")
    elif opcao == "0":
        print("Sair")
    else:
        print("Opção inválida.")
    
menu()