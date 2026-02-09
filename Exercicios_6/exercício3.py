nota = []
for i in range(4):
    n = float(input("digite as quatro notas: "))
    nota.append(n)

media = sum(nota) / len(nota)

print("As notas digitadas foram: ", nota)
print("A média das notas é: ", media)

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")