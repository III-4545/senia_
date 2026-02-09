import streamlit as st


def cadastrar_usuario(nome,email,senha):
    with open("./usuarios.txt","a") as arquivo:
        arquivo.write(f"Nome: {nome:<30} E-mail: {email:<20} | Senha: {senha}")



st.title("Cadastro de novo usuário")


login = st.text_input("Digite seu nome de login: ")
email = st.text_input("Digite seu e-mail: ")
senha = st.text_input("Digite sua senha: ",type="password")
confirma_senha = st.text_input("Confirme sua senha: ",type="password")


if st.button("Cadastrar"):
    if senha == confirma_senha:
        cadastrar_usuario(nome = login ,email = email, senha = confirma_senha)
        st.toast("Cadastro realizado com sucesso!",icon="✅")
    else:
        st.error("As senhas são diferentes!")