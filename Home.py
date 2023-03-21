import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

with st.sidebar:
    language = st.selectbox("Language", ["English", "Español"])
    st.session_state.language = language

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        .css-1y4p8pa .e1tzin5v0 {padding-top: 0rem;}
        .header {visibility: hidden; !important}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

if language == "English":
    menu_options = ["Home", "About Me",  "Tasks", 'Settings']

if language=="Español":
    menu_options = ["Inicio", "Sobre Mí",  "Tareas", 'Configuración']

# 3. CSS style definitions
menu_sel = option_menu(None, menu_options,
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    }
)

if menu_sel == "Home":
    st.header("Home")
    st.write("This is the home page")

if menu_options.index(menu_sel) == 1:
    st.title(menu_sel)
    from menu_options import about_me
    about_me.content()