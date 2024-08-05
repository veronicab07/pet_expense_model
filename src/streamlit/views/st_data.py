import streamlit as st
from PIL import Image
import pandas as pd
df = pd.read_csv("https://miscprojects.fra1.digitaloceanspaces.com/ds/combined_data.csv")
dr = pd.read_csv("https://miscprojects.fra1.digitaloceanspaces.com/ds/dataset_review.csv")


st.title("Data Exploration")

st.write("*In this section, we will explore the dataset used to predict dog ownership related expenses.*")

st.subheader("Dataset Review")

st.write("""The foundation dataset 'Best In Show' is open source and available on [Kaggle](https://www.kaggle.com/datasets/paultimothymooney/best-in-show-data-about-dogs/data). It was chosen due its vast number of variables (69) and the inclusion of financial data. Further datasets were chosen on the basis of complementary data which could enhance the relationships between variables in our foundation dataset. 

A review of the combined datasets is provided below: 

""")

st.table(dr)

st.subheader("Data Limitations")

st.write("""

The biggest challenge was combining data from many sources and deciding which variables to
keep or drop. This is due to variance in data quality and data availability. For example, the longevity
data is abundant with 440k rows. Bite statistics, however, is limited to 9k rows, although the data is useful
as an enhancement. 
""")



st.subheader("Data Visualization")

st.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/p6.jpg", caption='Frequency of Most Popular Breeds')
st.write("""There was a correlation between certain behavioural elements, as well as between size and
breed, size and longevity, and size and cost. What we were uncertain of, and what required
further exploration was the extent to which these variables were related and could be used to
predict yearly dog ownership costs. 
""")
st.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/p7.jpg", caption="Food Cost Year (avg) by Breed", use_column_width=True)
st.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/p8-2.jpg", caption="Tendency to Bark or Howl by Size", use_column_width=True)
st.write("""The third plot shows the tendency of dogs to bark or howl based on their size category. This can be correlated with different breed groups but not so much with size. Behaviour-related variables such as this contribute to the costs of owning a dog when it comes to training.

A more appropriate correlation of the size variable is rather with longevity, where we can see small size is strongly linked to better longevity in years (see chart below):

""")

st.bar_chart(df, x="size", y="longevity", color="#faaa0088", stack=False)
