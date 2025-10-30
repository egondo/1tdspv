import streamlit as st

st.set_page_config(layout="wide")

st.header("Exemplo de Formulário")
nome = st.text_input("Nome: ")
idade = st.number_input("Idade: ", min_value=0, max_value=140)

if st.button("cadastra"):
    st.write(f"SEu nome é {nome} e tem {idade} anos")
