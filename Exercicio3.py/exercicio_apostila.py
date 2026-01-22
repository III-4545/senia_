numero = int(input("Digite o número da tabuada que deseja: "))
inicio_tabuada = int(input("Digite o início da tabuada: "))
fim_tabuada = int(input("Digite o final da tabuada: "))


#for variavel_temporaria in lista_elementos
for multiplicador in range(inicio_tabuada, fim_tabuada + 1):
    print(f"{numero} X {multiplicador} = {numero*multiplicador}")