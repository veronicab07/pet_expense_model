import streamlit as st
from PIL import Image

st.title("Experiments")
st.write("""
We were convinced that our advanced models suffered from overfitting and so we examined the performance of other models. Another strategy we employed was to play around with the dataset and variables:
""")
col1, col2, col3 = st.columns([1,3,1])
col1.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/Husky.png")
col2.write("""
- Split the dataset vertically, to test for variable bias. 
- Remove "breed" variable, to reduce dimensionality with groups of breeds. 
- Reorganize the breed groups, to improve variable correlation.
- Binarize the target variable, to improve model learning
- Change the target variable, to better understand variable relations.
""") 
col3.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/German_Shepherd.png")

st.subheader("Classification Model Performance")

st.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/acc_score_experiment.JPG", caption="Classification Model Performance")
    
# Display the second table image
st.subheader("Random Forest - Regression Model Performance")
st.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/regression_rf.JPG", caption="Regression Model Performance")