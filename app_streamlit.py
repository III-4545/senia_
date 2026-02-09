import streamlit as st

st.title("Calculadora Simples🧮")
st.subheader("Feito com Streamlit👍")

valor1 = st.number_input("Digite o primeiro valor",0)
valor2 = st.number_input("Digite o segundo valor",0)

opcao = st.selectbox(
    "Qual operação deseja realizar?",
    ("Adição", "Subtração", "Multiplicação", "Divisão"))

if st.button("Calcular"):

    if opcao == "Adição":
        st.success(f"O resultado da adição é: {valor1 + valor2}")
    elif opcao == "Subtração":
        st.success(f"O resultado da subtração é: {valor1 - valor2}")
    elif opcao == "Multiplicação":
        st.success(f"O resultado da multiplicação é: {valor1 * valor2}")
    elif opcao == "Divisão":
        if valor2 == 0:
            st.error("Erro! Não é possível dividir por zero.")
        else:
            st.success(f"O resultado da divisão é: {valor1 / valor2}")