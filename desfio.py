def converter_dolar_para_real(valor_d, valor_r):
    valor_r = int(input("Digite o valor em dólar que deseja converter: "))
    valor_d = valor_r * 5.25
    return valor_d


def converter_real_para_dolar(valor_r, valor_d):
    valor_r = int(input("Digite o valor em real que deseja converter: "))
    valor_d = valor_r / 5.25
    return valor_d

def menu(coverter_dolar_para_real, converter_real_para_dolar):
    opcao = input("[1] - Converter Dólar para Real\n[2] - Converter Real para Dólar\n")
    if opcao == "1":
        resultado = converter_dolar_para_real(0,0)
        print(f"O valor convertido em Real é: R$ {resultado:.2f}")
    elif opcao == "2":
        resultado = converter_real_para_dolar(0,0)
        print(f"O valor convertido em Dólar é: $ {resultado:.2f}")
    else:
        print("Opção inválida.")
menu(converter_dolar_para_real, converter_real_para_dolar)