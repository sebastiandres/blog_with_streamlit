import streamlit as st

def content():
    if st.session_state.language == "English":
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

    if st.session_state.language=="Español":
        st.header("Sobre mí - 10 segundos")
        mkd = """
        Me encanta aprender. Tengo una mente muy estructurada que (actualmente?) se adapta bien a todo lo relacionado con datos y programación.
        También me encanta leer y escribir.
        """
        st.markdown(mkd)

        st.header("Sobre mí - 10 minutos")
        mkd = """
        Soy un geek y me encanta estudiar. He estudiado en 3 países diferentes:
        - Ingeniería Matemática, en la Universidad Técnica Federico Santa María, Chile.
        - Engeneur Diplome, en la École Polytechique, Francia. Esto fue un doble diploma con la UTFSM, lo que me dio un título de Ingeniero Francés y un título de Maestría.
        - Maestría en Ingeniería Matemática y Computacional, en la Universidad de Stanford, Estados Unidos.
        Fueron 3 experiencias de aprendizaje completamente diferentes. Si pudiera, seguiría estudiando para siempre. Helas, tengo que trabajar para pagar mis cuentas.

        Me encanta leer. No evito géneros, pero tengo una preferencia por la ciencia ficción y el suspense/misterio. Algunos de mis autores favoritos son:
        Michael Crichton (Jurassic Park y Dragon Teeth), Andy Weir (The Martian, Project Hail Mary),
        y Joel Dicker (The Truth About the Harry Quebert Affair, Days of our Fathers, etc.)

        También me gusta escribir. Escribí un libro mientras estudiaba en la UTFSM, pero en retrospectiva, no era un buen libro. Más bien un catártico. A veces escribo
        historias cortas, y una de ellas fue seleccionada para Santiago en Cien Palabras.

        Soy muy respetuoso de mi vida privada, así que no compartiré mucho sobre ella.

        Si quieres saber más sobre mí, puedes echar un vistazo a mi [perfil de LinkedIn](https://www.linkedin.com/in/sebastiandres).
        """
        st.markdown(mkd)
        
