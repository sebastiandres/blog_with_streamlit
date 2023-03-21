import streamlit as st

st.set_page_config(layout="wide")

st.header("Streamlit")

mkd = """
Stuff related to streamlit:
- Talked about streamlit at PyDay Chile meetup.
- Participated on Streamlit Hackathon and won a prize for streamlit-book.
- Talked about steramlit at PyCon Chile.
- Become a Streamlit Creator
- Participated on Streamlit Hackathon and won a prize for the datasaurus app.

Apps:
* https://notangrybirds.streamlit.app/
* https://datasaurus.streamlit.app/
* https://pythonchile.streamlit.app/
* https://confusion-matrix.streamlit.app/

Blog Posts at Streamlit Blog:
- [How to create interactive books with Streamlit in 5 steps](https://blog.streamlit.io/how-to-create-interactive-books-with-streamlit-and-streamlit-book-in-5-steps/): an example app to illustrate how to use streamlit-book.
- [Fostering data processing innovation with Streamlit](https://blog.streamlit.io/uplanner-fosters-data-processing-innovation-with-streamlit/): a discussion of how to use Streamlit to support data processing in a company.
- [Create a search engine with Streamlit and Google Sheets](https://blog.streamlit.io/create-a-search-engine-with-streamlit-and-google-sheets/): explaining how to mix google sheets and streamlit to create a search engine. Actually, many other applications.
- markdown link example: 

Libraries:
- streamlit-book (https://streamlit-book.readthedocs.io/): A library I created to handle multipaging, quizzes and goodies. Not updated lately, as Streamlit ended up "absorving" several features I provided through my library.
"""
st.markdown(mkd)