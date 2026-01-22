numero = int(input("Digite um número: "))
acumulador = 0
media = int(input("Digite o valor que vai dividir: "))

while numero != -1:
    acumulador += numero / media
    numero = int(input("Digite um número: "))
media = int(input("Digite o valor que vai dividir: "))
print(acumulador)