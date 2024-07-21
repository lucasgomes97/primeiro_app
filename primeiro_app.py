import streamlit as st

#titulo do app

st.title('Minha primeira aplicação')

#texto
st.write('Bem-vindo a minha aplicação')

# input
nome = st.text_input('Digite seu nome: ')
#input 
idade = st.number_input('Digite sua idade: ')

#botão 
if st.button('Enviar'):
    st.write(f'Olá, {nome}! Você tem {idade} anos.')