Pet Expense prediction (WIP)
==============================

DataScientest Bootcamp Project

This repository is part of a data science project for the DataScientest Bootcamp, a partner of Sorbonne University.

Project Overview
This data science project has its origins in the business case of Paw à Peau (a pet tech company founded by Natasha Azza). Paw à Peau is building a platform to convert animal health and behavioural data into actionable insights for pet owners. The project’s challenge was thus to translate the benefits of collecting data into financial terms. The idea was to create an alert system to integrate with a planned expense management feature on the platform. 

The team members consist of Natasha Azza (startup veteran and former Head of Product) and Veronica Benzi (experienced data analyst with a PhD in Biology). Both team members are avid animal lovers and thus shared a special interest in this somewhat niche topic. The division of work was made according to skill set, with Natasha focusing primarily on the business side of things and bringing domain knowledge to the table, and Veronica acting as the technical lead. The project consisted of three phases: 
Data exploration
Data modelling 
Presentation

Objectives

Determine the key criteria most correlated with dog ownership expenses. 
Identify risk factors associated with higher costs for individual dogs. 
Explore KPIs that could be used as early warning indicators for avoidable expenses. 

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data               <- Should be in your computer but not on Github (only in .gitignore)
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's name, and a short `-` delimited description, e.g.
    │                         `1.0-alban-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, links, and all other explanatory materials.
    │
    ├── reports            <- The reports that you'll make during this project as PDF
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   ├── visualization  <- Scripts to create exploratory and results oriented visualizations
    │   │   └── visualize.py

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
