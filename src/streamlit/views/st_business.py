import streamlit as st
from PIL import Image

st.title("Business Case")    
st.write(
        """
Since the pandemic, pet ownership has skyrocketed and the pet industry is booming, with Germany and France as the biggest and fastest growing markets in continental Europe. Germany has been hit hard by rising costs stemming from energy prices, inflation, and financial side effects from ongoing regional wars. Two steep increases in the national veterinary tariffs within the last three years mean that **pet owners are under immense financial pressure**.""")

# Columns for page design formatting 
col1, col2 = st.columns([4,1])

col1.write(
        """
Research has shown that **pet owners do not reduce their spending on pets even in times of economic crisis** and thus the pet industry is particularly robust. By comparing predicted dog ownership expenses with tracked data, **the Pet Expense Management feature aims to save pet owners money**, thereby reducing pet abandonment and avoidable debt. It functions by detecting cost data anomalies - highlighting unnecessary costs and indicating areas for potential saving

For this project, **we chose to focus on dog owners as they are the type of pet owner who spends the most**. We determined the real cost of dog ownership in Germany based on variables such as breed, lifespan, health issues, and behavioural traits. This was a prerequisite for exploring early warning indicators for avoidable expenses. 
     """)

# Expander for expense categories 
exp = col1.expander("Dog ownership expenses are numerous and complex.")
exp.write("""
                - Acquisition
                - Food
                - Accessories
                - Medical
                - Grooming
                - Training
                - Tax 
                - Insurance
                - Pet sitting
                - Funerary
                    """)

# Dog image 
col2.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/Doberman.png", caption=None, width=300)
