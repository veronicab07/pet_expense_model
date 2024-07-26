

# Import the necessary libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.preprocessing import OneHotEncoder

# Load the CSV files
df_breed = pd.read_csv('breed_basic_costs.csv')
ailments = pd.read_csv('ailments_scale.csv')
df = pd.read_csv('dogs_expenses_reviewed_bis.csv')
df2 = pd.read_csv('my_data.csv')


# ------------ AILMENTS PRE-PROCESSING ----------------

# Add 'average_cost' as the average of 'real_cost_min' and 'real_cost_max'
ailments['average_cost'] = (ailments['real_cost_min'] + ailments['real_cost_max']) / 2

# Drop now unnecessary cost columns
ailments.drop(columns=['real_cost_min', 'real_cost_max','average_cost'], axis=1, inplace=True)

print(ailments)

#------------ AILMENTS ONE HOT ENCODING -------------------

# Convert genetic_ailments column to strings
df_breed['genetic_ailments'] = df_breed['genetic_ailments'].astype(str)

# Clean and deduplicate ailments
def clean_and_deduplicate_ailments(ailments_str):
    if pd.isna(ailments_str):
        return []
    ailments_list = [ailment.strip() for ailment in ailments_str.split(',')]
    unique_ailments = sorted(set(ailments_list))  # Deduplicate and sort
    return unique_ailments

df_breed['cleaned_ailments'] = df_breed['genetic_ailments'].apply(clean_and_deduplicate_ailments)


# For one-hot encoding, transforming each row's list into a binary representation.
all_unique_ailments = sorted(set(ailment for row in df_breed['cleaned_ailments'] for ailment in row))

# Initialize columns for each unique ailment
for ailment in all_unique_ailments:
    df_breed[f'ailment_{ailment}'] = 0

# Populate the one-hot encoding columns
for index, row in df_breed.iterrows():
    for ailment in row['cleaned_ailments']:
        df_breed.at[index, f'ailment_{ailment}'] = 1


# Drop unnecessary columns in df_breed
df_breed.drop(columns=['insurance_tier','health_insurance', 'health_insurance_mid', 'health_insurance_old', 'liability_insurance', 'dog_tax',
                          'cleaned_ailments', 'genetic_ailments', 'ailment_nan',], axis=1, inplace=True)

# Rename columns in df_breed
df_breed = df_breed.rename(columns={'australian terrier': 'breed',                                  
                                       'ailment_allergies': 'allergies',
                                       'ailment_bleeding': 'bleeding',
                                       'ailment_bloat': 'bloat',
                                       'ailment_breathing': 'breathing', 
                                       'ailment_cleft palate': 'cleft_palate', 
                                       'ailment_dental': 'dental',
                                       'ailment_elbows': 'elbows',
                                       'ailment_eyes': 'eyes', 
                                       'ailment_heart': 'heart',
                                       'ailment_hips': 'hips',
                                       'ailment_kidney': 'kidney',
                                       'ailment_liver': 'liver',
                                       'ailment_metabolic': 'metabolic',
                                       'ailment_neurological': 'neurological', 
                                       'ailment_none' : 'none',
                                       'ailment_osteopathy': 'osteopathy',
                                       'ailment_patella': 'patella', 
                                       'ailment_respiratory': 'respiratory', 
                                       'ailment_skin': 'skin',
                                       'ailment_spine': 'spine', 
                                       'ailment_thyroid': 'thyroid', 
                                       'ailment_urinary': 'urinary'})

# Map each ailment to its severity_scale (assuming ailment_name is a unique identifier).
ailment_to_severity_scale = ailments.set_index('genetic_ailments')['severity_scale'].to_dict()


ailment_to_cost = {
    ailment: {'1': row['real_cost_min'], '2': row['average_cost'], '3': row['real_cost_max']}
    for ailment, row in df2.set_index('genetic_ailments').iterrows()
}

def calculate_final_yearly_costs(row, ailment_to_severity_scale, ailment_to_cost):
    severity_score = 0
    final_yearly_cost = 0

    for ailment, presence in row.items():
        # Ensure we only check for genetic ailments, excluding 'size' or other non-ailment columns
        if presence and ailment in ailment_to_severity_scale:
            severity_score += ailment_to_severity_scale[ailment]
            # Calculate cost based on breed size (1, 2, 3) using the size field from the input row
            size_key = str(row['size'])  # Assuming `row` has a 'size' field indicating the breed size
            if ailment in ailment_to_cost:
                final_yearly_cost += ailment_to_cost[ailment].get(size_key, 0)

    return final_yearly_cost

# Apply the function to calculate final yearly costs
df['yearly_final_cost'] = df.apply(calculate_final_yearly_costs, axis=1, args=(ailment_to_severity_scale, ailment_to_cost))

# Export dataframe to csv
df_breed.to_csv('my_data.csv', index=False)

# ----------------- PRE-PROCESSING DF -----------------------------------
# Drop unnecessary columns, clean up naming 
cols_to_drop = ['genetic_ailments', 'ailments_count', 'vet_cost', 'food_cost', 'dog_tax', 'liability_insurance',
                'tier', 'health_insurance_cost','Cost_1_5', 'Cost_6_7', 'Cost_8_plus', 'liability_insurance_year',
                'dog_tax_year', 'health_insurance_annual', 'severity_score']
df.drop(columns=cols_to_drop, inplace=True)

df = df.rename(columns={'Breed': 'breed',
                        'size_category': 'size',
                        'incredibly_kifriendly_dogs': 'kid_friendly',
                        'friendly_towarstrangers': 'stranger_friendly',
                        'severity_score': 'health_severity',
                        'category_Companion Dogs': 'category_companion', 
                        'category_Herding Dogs': 'category_herding',
                        'category_Hound Dogs': 'category_hound', 
                        'category_Sporting Dogs': 'category_sporting',
                        'category_Terrier Dogs': 'category_terrier', 
                        'category_Working Dogs': 'category_working'})                                 


# Basic left join to add new columns from df2 to df where 'breed' matches
df_combined = df.merge(df2, on=['breed', 'size'], how='left')

# Specify the new order as a list
new_order = ['breed','gender','age', 'longevity', 'size', 'category_companion', 
             'category_herding','category_hound', 'category_sporting',
             'category_terrier', 'category_working','grooming_required',
             'intelligence_category', 'sensitivity_level', 'tolerates_being_alone',
             'tolerates_cold_weather', 'tolerates_hot_weather',
             'kid_friendly', 'dog_friendly', 'stranger_friendly',
             'potential_for_mouthiness', 'prey_drive', 'tendency_to_bark_or_howl',
             'wanderlust_potential', 'exercise_needs', 'energy_level',
             'allergies', 'bleeding', 'bloat', 'breathing', 'cleft_palate', 'dental',
             'elbows', 'eyes', 'heart', 'hips', 'kidney', 'liver', 'metabolic',
             'neurological', 'none', 'osteopathy', 'patella', 'respiratory', 'skin',
             'spine', 'thyroid', 'urinary', 'severity_score', 'yearly_final_cost']

# Reorder the columns using reindex
df_combined = df_combined.reindex(columns=new_order)
df_combined.drop(columns=['none'])


# --------- ADDING TRAINING PROBABILITY -----------------

# Add 'training_multiplier' as the sum of behavioural points.
df_combined['training_multiplier'] = (df_combined['sensitivity_level'] + df_combined['tolerates_being_alone'] +
                                      df_combined['potential_for_mouthiness'] + df_combined['prey_drive'] + df_combined['tendency_to_bark_or_howl'] +
                                      df_combined['wanderlust_potential'] + df_combined['exercise_needs'] + df_combined['energy_level'])

# Add training costs to final cost
df_combined['training_cost'] = (df_combined['training_multiplier'] * 50)
df_combined['yearly_final_cost'] = (df_combined['training_cost'] + df_combined['yearly_final_cost'])

# Drop now unnecessary cost columns
df_combined.drop(columns=['training_multiplier', 'training_cost'], axis=1, inplace=True)

# Add an additional penalty for aggression, because behavioural problems of this type cost more
df_combined['training_penalty'] = 15 - (df_combined['kid_friendly'] + df_combined['dog_friendly'] + df_combined['stranger_friendly'])
df_combined['training_penalty'] = df_combined['training_penalty'].astype(int)

# Split training_penalty into 4 classes within the new column 'training_extra'
df_combined['training_extra'], bins = pd.qcut(df_combined['training_penalty'], 4, labels=[0,3,6,12], retbins=True, duplicates='drop')

# Use 'training_extra' to calculate additional yearly costs
# Convert training_extra to int for calculation, if it's not already
df_combined['training_extra'] = df_combined['training_extra'].astype(int)
df_combined['yearly_final_cost'] = df_combined['yearly_final_cost'] + (df_combined['training_extra'] * 100)

# Drop now unnecessary cost columns
df_combined.drop(columns=['training_penalty', 'training_extra'], axis=1, inplace=True)

# --------- ONE HOT ENCODE BREED -------------------------


# Convert breed column into strings
df_combined['breed'] = df_combined['breed'].astype(str)

# Perform one-hot encoding on the 'breed' column
df_encoded = pd.get_dummies(df_combined, columns=['breed'])

# Convert all boolean columns to integers (normally not needed, but for the sake of solving the issue)
df_encoded.replace([np.inf, -np.inf], np.nan, inplace=True)
df_encoded = df_encoded.fillna(0).astype(int)

# ---- EXPORT DATA FOR MODELLING ----------------------------
df_encoded.to_csv('combined_data.csv', index=False)

df_nobreed = df_combined.drop(columns=['training_penalty', 'training_extra','breed'], axis=1, inplace=True)
df_nobreed.to_csv('nobreed_data.csv', index=False)

df_encoded.info()
df_encoded.describe()