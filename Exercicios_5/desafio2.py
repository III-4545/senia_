def adiçao(n1, n2):
    return (n1 + n2)  

def subtraçao(n1, n2):
    return n1 - n2

def multiplicaçao(n1, n2):
    return n1 * n2

def divisao (n1,n2):
    divisao != 0
    if divisao==0:
        print("Erro! Não é possível dividir por zero.")
    else:
        print ("Divisão realizada com sucesso.")
    return n1 / n2



opcao = input("----CALCULADORA----\n[1] - Adição\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão\n[0] - Sair\nEscolha uma opção: ")

if opcao == "0":
        print("Sair")
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
elif opcao == "1":
        n1 = float(input("Digite o primeiro número: ")) 
        n2 = float(input("Digite o segundo número: "))
        resultado = n1+n2
        print(f"O resultado da adição é: {resultado:.2f}")
elif opcao == "2":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resultado = n1-n2
        print(f"O resultado da subtração é: {resultado:.2f}")
elif opcao == "3":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resultado = n1*n2
        print(f"O resultado da multiplicação é: {resultado:.2f}")
elif opcao == "4":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resultado = n1/n2
        print(f"O resultado da divisão é: {resultado:.2f}") 
else:
        print("Opção inválida.")
try:
        resultado =10 / 0
except ZeroDivisionError:
        print("Erro! Não é possível dividir por zero.")
    
        resultado = divisao(n1, n2)

