def tabuada(numero):
    for i in range(1,11):
        print(f"{numero} X {i} = {numero*i}")

numero_usuario = int(input("Digite o número da tabuada: "))
tabuada(numero_usuario)