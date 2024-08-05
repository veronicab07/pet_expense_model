import streamlit as st
from PIL import Image

# ---- PAGE SETUP
overview = st.Page(
    page = "views/st_overview.py", 
    title = "Project",
    icon = "🏠",
    default = True, 
) 

business = st.Page(
    page = "views/st_business.py", 
    title = "Business Case",
    icon = "💰",
) 

data_exp = st.Page(
    page = "views/st_data.py", 
    title = "Data Exploration",
    icon = "🔍",
) 
features = st.Page(
    page = "views/st_features.py", 
    title = "Feature Engineering",
    icon = "📐",
) 

feature_imp = st.Page(
    page = "views/st_featureimp.py", 
    title = "Feature Importance",
    icon = "📈", 
) 

modelling = st.Page(
    page = "views/st_modelling.py", 
    title = "Modelling",
    icon = "🔢", 
) 

experiments = st.Page(
    page = "views/st_experiments.py", 
    title = "Experiments",
    icon = "📊",
) 

prototype = st.Page(
    page = "views/st_prototype.py", 
    title = "Prototype",
    icon = "🗝️",
) 

team = st.Page(
    page = "views/st_team.py", 
    title = "Team",
    icon = "📎", 
) 


# NAVIGATION

pg = st.navigation(
    {
    "About":[team, overview, business],
    "Pet Expense Management": [prototype, data_exp, features, feature_imp, modelling, experiments],
    }
                  )
pg.run()

# SHARED ON ALL PAGES
