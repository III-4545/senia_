def contar_pares(inicio,fim):
    contador = 0
    for numero in range(inicio,fim+1):  
        #validar se o numero é par
        if numero % 2 == 0:
            contador += 1
    print(contador)

contar_pares(1, 10)