import streamlit as st
import pandas as pd
import pickle
from PIL import Image
import os

# Load dataset
df = pd.read_csv('https://miscprojects.fra1.digitaloceanspaces.com/ds/combined_data.csv')

# Function to load pickled files
def load_pickle(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)

# Load models and other artifacts
models = {
    "Random Forest (Original)": {
        "model_performance": None,
        "classification_report": 'https://miscprojects.fra1.digitaloceanspaces.com/ds/classification_report_before_PCA.JPG',
        "confusion_matrix": 'https://miscprojects.fra1.digitaloceanspaces.com/ds/confusion_matrix_before_PCA.JPG',
        "interpretability": None
    },    
    "Random Forest (After PCA)": {
        "model_performance": None,
        "classification_report": 'https://miscprojects.fra1.digitaloceanspaces.com/ds/classification_report_after_PCA.JPG',
        "confusion_matrix": 'https://miscprojects.fra1.digitaloceanspaces.com/ds/confusion_matrix_after_PCA.JPG',
        "interpretability": None
    },
    "Random Forest (Feature Selected)": {
        "model_performance": 'https://miscprojects.fra1.digitaloceanspaces.com/ds/rf_model_performance_manually_tuned.JPG',
        "classification_report": 'https://miscprojects.fra1.digitaloceanspaces.com/ds/rf_classification_report_first_tuning.JPG',
        "confusion_matrix": None,
        "interpretability": 'https://miscprojects.fra1.digitaloceanspaces.com/ds/shap_plot_rf_manually_tuned.png'
    },
    "Random Forest (Best Parameters)": {
        "model_performance": ['https://miscprojects.fra1.digitaloceanspaces.com/ds/rf_model_performance.JPG', 'https://miscprojects.fra1.digitaloceanspaces.com/ds/rf_best_cv.JPG'],
        "classification_report": 'https://miscprojects.fra1.digitaloceanspaces.com/ds/rf_classification_report.JPG',
        "confusion_matrix": None,
        "interpretability": 'https://miscprojects.fra1.digitaloceanspaces.com/ds/rf_shap_best_param.JPG'
    },
    "Decision Tree (Feature Selected)": {
        "model_performance": 'https://miscprojects.fra1.digitaloceanspaces.com/ds/dt_model_performance_manually_tuned.JPG',
        "classification_report": 'https://miscprojects.fra1.digitaloceanspaces.com/ds/dt_classification_report_first_tuning.JPG',
        "confusion_matrix": None,
        "interpretability": None
    },
    "Decision Tree (Best Parameters)": {
        "model_performance": ['https://miscprojects.fra1.digitaloceanspaces.com/ds/dt_model_performance.JPG','https://miscprojects.fra1.digitaloceanspaces.com/ds/dt_best_cv.JPG'],
        "classification_report": 'https://miscprojects.fra1.digitaloceanspaces.com/ds/dt_classification_report.JPG',
        "confusion_matrix": None,
        "interpretability": 'https://miscprojects.fra1.digitaloceanspaces.com/ds/dt_shap_best_param.JPG'
    }
}

st.title("Modelling")
st.write ("*This section provides an overview of the results from the models we selected for advanced tuning.*")


model_name = st.selectbox("Select model to load more details", list(models.keys()))
    
if model_name:
    selected_model = models[model_name]
    #st.subheader(f"{model_name}")

    # Display model performance if available
    if selected_model.get("model_performance"):
        st.subheader("Model Performance")
            # Check if the value is a list of images
        if isinstance(selected_model["model_performance"], list):
            for image_pr_path in selected_model["model_performance"]:
                try:
                    #image_pr = Image.open(image_pr_path)
                    st.image(image_pr_path, caption=f"{model_name} Model Performance", use_column_width=True)
                except FileNotFoundError:
                    st.write(f"Model Performance Report file '{image_pr_path}' not found.")
                except Exception as e:
                    st.write(f"An error occurred while loading the Model performance report '{image_pr_path}': {e}")
            else:
                try:
                    image_pr_path = selected_model["model_performance"]
                # image_pr = Image.open(image_pr_path)
                    st.image(image_pr_path, caption=f"{model_name} Model Performance", use_column_width=True)
                except FileNotFoundError:
                    st.write("Model Performance Report file not found.")
                except Exception as e:
                    st.write(f"An error occurred while loading the Model performance report: {e}")

# Display classification report if available
    if selected_model.get("classification_report"):
        st.subheader("Classification Report")
        try:
            image_pr_path = selected_model["classification_report"]
            st.image(image_pr_path, caption=f"{model_name} Classification Report", use_column_width=True)
        except FileNotFoundError:
            st.write("Classification Report file not found.")
        except Exception as e:
            st.write(f"An error occurred while loading the Classification report: {e}")

# Display confusion matrix if available
    if selected_model.get("confusion_matrix"):
        st.subheader("Confusion Matrix")
        try:
            image_cm_path = selected_model["confusion_matrix"]
            st.image(image_cm_path, caption=f"{model_name} Confusion Matrix", use_column_width=True)
        except FileNotFoundError:
            st.write("Confusion Matrix file not found.")
        except Exception as e:
            st.write(f"An error occurred while loading the confusion matrix: {e}")

# Display interpretability if available
    if selected_model.get("interpretability"):
        st.subheader("Interpretability")
        try:
            image_shap_path = selected_model["interpretability"]
            st.image(image_shap_path, caption="SHAP-Interaction Summary Plot", use_column_width=True)
        except FileNotFoundError:
            st.write("SHAP Plot file not found.")
        except Exception as e:
            st.write(f"An error occurred while loading the SHAP plot: {e}")

# Cache the dataframe
@st.cache_data
def get_data():
    return df

# Call to display the dataframe
df = get_data()