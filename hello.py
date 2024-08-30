import streamlit as st

st.header("This is my First web app")
st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.header("This is a header with a divider", divider="gray")

code = '''def cat():
    print("Hello, Cat!")'''
st.code(code, language="python")


cat = st.checkbox("Do you think I am awesome?")

if cat:
    st.write("Great!")