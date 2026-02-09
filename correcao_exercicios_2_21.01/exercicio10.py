turno_estudo = input("Digite o turno que você estuda:\
                     \n(M-Matutino)\
                     \n(V-Vespertino)\
                     \n(N-Noturno)\n").upper()

if turno_estudo == "M":
    print("Bom dia!")
elif turno_estudo == "V":
    print("Boa tarde!")
elif turno_estudo == "N":
    print("Boa noite!")
else:
    print("Valor inválido!")