from st_on_hover_tabs import on_hover_tabs
import streamlit as st
st.set_page_config(layout="wide")

st.header("Custom tab component for on-hover navigation bar")

st.title("Navigation Bar")
st.write('Name of option is')

with st.sidebar:
    st.write("Another option")
    st.button("Click me")