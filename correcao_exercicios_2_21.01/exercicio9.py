numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

maior = numero1 if numero1 > numero2 else numero2
maior = numero3 if numero3 > maior else maior

menor = numero1 if numero1 < numero2 else numero2
menor = numero3 if numero3 < menor else menor

if numero1 != maior and numero1 != menor:
    meio = numero1
if numero2 != maior and numero2 != menor:
    meio = numero2
if numero3 != maior and numero3 != menor:
    meio = numero3

print(f"{maior} | {meio} | {menor}")