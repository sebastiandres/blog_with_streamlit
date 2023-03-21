import streamlit as st

st.set_page_config(layout="wide")

st.header("Streamlit")

mkd = """
Stuff related to Python:
- Learned Python in 2006, while working at the Centro de Modelamiento Matemático, Universidad de Chile.
- I have given several talks about Python, including:
    - PyDay Chile meetup.
    - PyCon Chile.
    - PyCon Latam.
    - PyCon Colombia.
    - PyCon Argentina.
    - PyCon Chile.
- I have also given some other talks about Python, including:
"""
st.markdown(mkd)