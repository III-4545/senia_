def somar():
    #Como a função não recebe parâmetros, é necessário pegar os valores.
    valor_1 = int(input("Digite o primeiro número: "))
    valor_2 = int(input("Digite o segundo número: "))
    print(valor_1 + valor_2)
    #Função sem retorno, só mostra o resultado usando a função print.

resultado = somar()
print(f"O valor do resultado da {resultado}")