import streamlit as st

st.title("Contoh program Streamlit")

with st.form(key='my_form'):
    nama = st.text_input(label='Nama lengkap')
    jenis_kelamin = st.radio("Jenis kelamin",("Laki-laki", "Perempuan"))
    submit_button = st.form_submit_button(label='Kirim')