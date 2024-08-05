import streamlit as st
from PIL import Image

st.title("Team Intro")

st.write("""

Both team members are animal lovers and thus shared a special interest in the project. The division of work was made according to skill set, with Natasha focusing primarily on the business perspective and presentation and Veronica acting as the technical data lead.
         
        """)

# Columns for page design formatting 

col6, col7 = st.columns([1,1])
col6.subheader("Natasha Azza")
col7.subheader("Veronica Benzi")

col1, col2, col3, col4, col5 = st.columns([2,2,1,2,2])

col1.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/n_c.png")
col2.write("""Startup veteran, former Head of Product.""")
col2.link_button("LinkedIn", "https://www.linkedin.com/in/natashaaa/")
col2.link_button("Github", "https://github.com/natasha-a-a")


col4.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/foto1.jpg")
col5.write("Senior Data Analyst, with a PhD in Biology")
col5.link_button("LinkedIn", "https://www.linkedin.com/in/ver%C3%B3nica-benzi-ph-d-168ba81a/")

