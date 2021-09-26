import streamlit as st

st.title('hello streamlit')
st.subheader('welcome to my first streamlit app')

# remove footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
