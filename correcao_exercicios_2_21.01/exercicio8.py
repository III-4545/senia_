preco_produto1 = float(input("Digite o valor do primeiro produto: "))
preco_produto2 = float(input("Digite o valor do segundo produto: "))
preco_produto3 = float(input("Digite o valor do terceiro produto: "))

if preco_produto1 < preco_produto2:
    saida = "O produto mais barato é o produto 1."
    mais_barato = preco_produto1
else:
    saida = "O produto mais barato é o produto 2."
    mais_barato = preco_produto2

if preco_produto3 < mais_barato:
    mais_barato = preco_produto3
    saida = "O produto mais barato é o produto 3."

print(f"{saida} Com preço: R$ {mais_barato:.2f}")



