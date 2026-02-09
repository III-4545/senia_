numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

maior = numero1 if numero1 > numero2 else numero2
maior = numero3 if numero3 > maior else maior

menor = numero1 if numero1 < numero2 else numero2
menor = numero3 if numero3 < menor else menor


print(f"O maior é {maior}\nO menor é {menor}")