import streamlit as st

st.title("Tabuada📚")
st.subheader("Gerador de Tabuada Simples👍")

n1 = st.number_input("Digite um numero para ver a tabuada",0)
n2 = st.number_input("Digite onde a tabuada vai começar",0)
n3 = st.number_input("Digite onde vai acabar",0)

if st.button("Gerar Tabuada"):
    st.write(f"tabuada do {n1}:")
    for i in range(n2, n3 +1):
        st.write(f"{n1} x {i} = {n1 * i}")
