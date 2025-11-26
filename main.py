import streamlit as st
from google import genai


# Configuração da página
st.set_page_config(page_title="Minha App", page_icon="🚀")

# Título da aplicação
st.title("Minha Primeira App Streamlit")

# Texto simples
st.write("Olá, mundo!")

# Executar com: streamlit run app.py

# Entrada de texto
nome = st.text_input("Digite seu nome:")
biografia = st.text_area("Conte sobre você:")

# Números
idade = st.number_input("Idade:", min_value=0, max_value=120)
altura = st.slider("Altura (cm):", 100, 250, 170)

# Seleção
opcao = st.selectbox("Escolha uma opção:", ["A", "B", "C"])
multiplas = st.multiselect("Múltiplas escolhas:", ["X", "Y", "Z"])

# Checkbox e radio
aceito = st.checkbox("Eu aceito os termos")
genero = st.radio("Gênero:", ["Masculino", "Feminino", "Outro"])

# Botões
if st.button("Clique aqui"):
    st.write("Botão foi clicado!")


    