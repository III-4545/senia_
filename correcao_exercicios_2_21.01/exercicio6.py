numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

if numero1 > numero2:
    maior = numero1
else:
    maior = numero2

if numero3 > maior:
    maior = numero3

print("O maior número é:",maior)
    