numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

#Inicio do Algoritmo de encontrar o maior entre os três
if numero1 > numero2:
    maior = numero1
else:
    maior = numero2

if numero3 > maior:
    maior = numero3
#Final do Algoritmo do maior entre os três

#Inicio do Algoritmo menor entre os três
if numero1 < numero2:
    menor = numero1
else:
    menor = numero2
    
if numero3 < menor:
    menor = numero3
#Final do Algoritmo do menor entre os três

print(f"O maior é: {maior}\nO menor é: {menor}")