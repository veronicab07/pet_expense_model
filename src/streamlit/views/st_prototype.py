import streamlit as st
from PIL import Image

st.title("Prototype")

st.subheader("MVP Wireframes")
tab1, tab2, = st.tabs(["User Input", "Display Result"])

with tab1:
    st.header("Expense Risk Estimator")
    st.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/wfinput.jpg", use_column_width=True)
with tab2:
    st.header("Expense Risk Result")
    st.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/wfresult.jpg", use_column_width=True)
    

st.subheader("Integrated Concept")

st.write(
        """
The MVP assumes no prior data on the individual dog and focuses on purebred dogs. These limitations mean that the model is currently only relevant to a third of the serviceable demographic. The final integrated feature is expected to use historical data and user adjustments to fine tune the machine learning model. The following screen illustrates the concept as it would appear on the perPETual platform.  
        """
        )

st.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/dashboard.png", use_column_width=True)
