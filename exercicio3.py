def calcular_media(n1,n2,n3):
    return calcular_media(n1 and n2 and n3)

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
calcular_media = n1 + n2 + n3

if   calcular_media >= 7:
    print("O valor é verdadeiro")
else:
    print("O valor é falso")