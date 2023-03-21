import streamlit as st

st.set_page_config(layout="wide")

st.header("About Me - 10 seconds")
mkd = """
I love to learn. I have a very structured mind that (currently?) fits well with anything related to data and programming. 
I also love to read and write.
"""
st.markdown(mkd)

st.header("About Me - 10 minutes")
mkd = """
I'm a geek and love to study. I have studied in 3 different countries:
- Mathematical Engineering, at Universidad Técnica Federico Santa María, Chile.
- Engeneur Diplome, at École Polytechique, France. This was a double diplome with UTFSM, which landed me a French Engineer Diploma and Master Degree.
- Master on Computational and Mathematical Engineering, at Stanford University, USA.
They were 3 complete different learning experiences. If I could, I would keep studying forever. Helas, I have to work to pay my bills.

I love to read. I don't avoid genres, but I have a preference for science fiction and suspense/mystery. Some of my favorite authors are:
Michael Crichton (Jurassic Park and Dragon Teeth), Andy Weir (The Martian, Project Hail Mary), 
and Joel Dicker (The Truth About the Harry Quebert Affair, Days of our Fathers, etc.)  

I also like to write. I wrote a book while at UTFSM, but in hindesight, it was not a good book. More of a cathartic one. Sometimes I write
short stories, and one of them was selected for Santiago en Cien Palabras.

I'm very respectful of my private life, so I won't share much about it.

If you want to know more about me, you can take a look at my [LinkedIn profile](https://www.linkedin.com/in/sebastiandres).
"""
st.markdown(mkd)

