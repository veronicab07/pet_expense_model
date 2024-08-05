import streamlit as st
from PIL import Image
import pandas as pd
df = pd.read_csv("https://miscprojects.fra1.digitaloceanspaces.com/ds/combined_data.csv")

st.title("Feature Engineering")

st.write(
        """

The most time-consuming part of the project was the data cleaning and preparation. After joining many different datasets, we went through an extensive feature engineering process due to missing, dirty, or incorrectly formatted data. 
""")

st.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/pem_datamap.jpg")

st.subheader("Data Enrichment")

st.write("""
To begin with, the financial data available in the foundation dataset was incomplete and based on dogs living in the US: the costs were not at all accurate for Germany. So, we enriched the dataset with financial data from German scientific literature, our own primary research within the Berlin pet community and our own calculations for training and medical costs. We aimed to generate multipliers for training probability, insurance premiums, and other variables to the available mean data. 

- Pet sitting expenses were not included in the overall cost calculation due to the irregularity of this variable. Not all dog owners use professional services and instead may opt to use their social circle, meaning costs may be non-existent (and at best unpredictable). 

- Veterinary costs make up a large amount of pet owner expenses due to the low incidence of insurance (±5%), however
these costs were not included in our foundation data set. As there is an abundance of recent
economic studies on pet ownership in Germany, this financial data was used to enrich our dataset.

- The hourly fee range of local trainers was readily available online. The probability that a dog needs training could be extracted from the dataset through variable correlation (breed, intelligence, size, age etc.).

- Retail financial data was readily available for the US and UK markets, but not for continental
Europe - itt was necessary to approximate based on the differences in cost of living. 

- Grooming costs depend on both size and coat type. We calculated these for certain breeds based on
local groomer fees.

Following the calculations, we removed all cost data apart from *yearly_final_costs*, which we used as our target variable.
""")

st.subheader("Resampling")
st.write("""

We further standardized the data by ensuring certain thresholds for breed inclusion in the dataset, this
included the minimum number of dogs which belonged to a given breed population (>=100 records), as well as
the acceptable amount of missing key data. For example, dog breeds missing our key behaviour
traits were dropped from the dataset. 

""")


col1, col2, col3 = st.columns([1,1,1])
col2.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/Poodle.png", caption='Poodles unfortunately did not make the cut!', width=200)

st.subheader("Standardization")

st.write("""

We chose to represent mixed breeds by splitting them into three different size categories and using the mode for missing data, i.e. for behaviour traits, as well as figures from research findings such as longevity, reduced insurance cost. We made the decision not to associate the mixed breed population with any specific genetic ailments.

""")

st.subheader("Transformation")


st.write("""

The foundation dataset had provided breed categorization based on the American Kennel Club, but we later changed this to the categorization provided by the Fédération Cynologique Internationale (an umbrella organization governing pedigree dogs in most of regions of the world) as these were breed function-specific and more relevant to Germany. 

Additionally, much of the financial data was provided in weekly or monthly format, which had to be normalized 

""")

st.subheader("Dimensionality Reduction")

st.write("""    

The shelter datasets were  dropped entirely due to an insufficient number of rows (it made no sense to
combine datasets with such discrepancy). Nevertheless, we have kept the numerous datasets
with the goal of using them to verify the data in our foundation dataset. We also dropped a number of individual variables due to better representation through other variables, irrelevance or insufficient data. 
""")

st.subheader("Variable Selection")
exp1 = st.expander("Our pre-cleaning variable shortlist:")
exp1.write("""
'breed', 'lifetime_cost', 'longevity', 'food_cost_year', 'grooming required ', 'size_category',
'weight_kg', 'shoulder_height_cm', 'intelligence_category', 'avg_food_per_week_£',
'food_per_week_$', 'genetic_ailments', 'category', 'Specie', 'Gender', 'where_bitten',
'sensitivity_level', 'tolerates_being_alone', 'tolerates_cold_weather', 'tolerates_hot_weather',
'incredibly_kifriendly_dogs', 'dog_friendly', 'friendly_towarstrangers', 'easy_to_groom',
'potential_for_mouthiness', 'prey_drive', 'tendency_to_bark_or_howl', 'wanderlust_potential',
'exercise_needs', 'energy_level', 'adapts_well_to_apartment_living'
                    """)

exp = st.expander("Dropped variables:")
exp.write("""
- *neutered*
- *grooming_required*
- *food_cost_year*
- *lifetime_cost*
- *adapts_well_to_apartment_living*
- *bite_statistics*
- *weight_kg*
- *shoulder_height_cm*
- *avg_food_per_week_£*
- *food_per_week_$* 
- *Specie*
- *where_bitten*
- *adaptability*
- *adapts_well_to_apartment_living*

""")

exp2 = st.expander("Our post-cleaning variable shortlist:")
exp2.write("""
'breed', 'breed_group', 'longevity', 'size_category', 'intelligence_category', 'genetic_ailments', 'sex', 'food_cost_year', 'lifetime_cost', 'sensitivity_level','tolerates_being_alone', 'tolerates_cold_weather', 'tolerates_hot_weather',
'incredibly_kifriendly_dogs', 'dog_friendly', 'friendly_towarstrangers', 'potential_for_mouthiness',
'prey_drive', 'tendency_to_bark_or_howl', 'wanderlust_potential', 'exercise_needs',
'energy_level'
                    """)

st.subheader("One-Hot Encoding")

st.write("""

As a final step, we expanded 'breed' and ‘genetic_ailments’ through one hot encoding in order to have a more
detailed breakdown of the costs and to transform different breeds into variables. 

        """)

st.write("Below is an overview of the final dataset created.")
st.dataframe(df.head())


st.subheader("Modelling Strategy")

st.write("""We decided to go for a classification model, due to the impossibility of accurately calculating expenses of an individual dog. Costs over an individual dog's lifetime can be influenced by too many environmental factors, such as location-based pricing, unforeseen accidents, and pet service quality and availability.""")
