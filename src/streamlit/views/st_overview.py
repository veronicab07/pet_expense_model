import streamlit as st
from PIL import Image

st.title("Pet Expense Management")
st.write("### About the Project")
col1, col2 = st.columns([1,2])
col1.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/cover.png", caption=None,)
col2.write(
        """
        This presentation is the culmination of a three-month capstone data science project completed with DataScientest. 
        
        The Pet Expense Management concept has its origins in the business case of Paw à Peau, which is building a platform to convert pet data into actionable insights for pet owners. 
        
        The project’s challenge was to
        translate the benefits of collecting data into financial terms and create an anomaly-based alert system.
        """)
st.write("""
        The project consisted of three phases:
        - Data exploration
        - Data modelling
        - Project defense
        """)
col3, col4, col5, col6 = st.columns([1,1,1,1])
col4.link_button("Download Report", "https://miscprojects.fra1.digitaloceanspaces.com/ds/final_report.pdf")
col5.link_button("View Source Code", "https://github.com/DataScientest-Studio/may24_bds_int_pet_expense")


