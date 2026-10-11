from pathlib import Path

import pandas as pd
import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC


st.title("Practical 8 - SVM and Logistic Regression")
st.write("Binary classification using Logistic Regression and Support Vector Machine.")

DATA_FILE = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "Classified Data - Classified Data.csv"
)
TARGET_COLUMN = "TARGET CLASS"


@st.cache_data
def load_data():
    return pd.read_csv(DATA_FILE)


data = load_data()
clean_data = data.drop(columns=["Unnamed: 0"], errors="ignore").dropna()
features = clean_data.drop(columns=[TARGET_COLUMN])
target = clean_data[TARGET_COLUMN]

logistic_model = LogisticRegression(max_iter=1000)
logistic_model.fit(features, target)

svm_model = SVC()
svm_model.fit(features, target)

dataset_tab, logistic_tab, svm_tab, prediction_tab = st.tabs(
    ["Dataset", "Logistic Regression", "SVM", "Predict New Record"]
)

with dataset_tab:
    st.header("Classified Dataset")

    with st.expander("Load and preview dataset", expanded=True):
        st.success(
            f"Dataset loaded: {clean_data.shape[0]} rows and "
            f"{clean_data.shape[1]} columns"
        )
        st.dataframe(clean_data.head(10), width="stretch", hide_index=True)

    with st.expander("Describe dataset"):
        st.write("**Feature columns:**", features.columns.tolist())
        st.write("**Target column:**", TARGET_COLUMN)
        st.write("**Missing values:**", int(clean_data.isna().sum().sum()))
        st.write("**Classes:**", sorted(target.unique().tolist()))
        st.dataframe(clean_data.describe().T, width="stretch")

    with st.expander("Feature engineering"):
        st.write(
            "The unused index column is removed using the pandas `drop()` method."
        )
        st.info("All model features are already numeric.")

with logistic_tab:
    st.header("Logistic Regression")
    st.success("Logistic Regression model trained successfully.")

with svm_tab:
    st.header("Support Vector Machine")
    st.success("SVM model trained successfully.")

with prediction_tab:
    st.header("Predict a New Record")
    selected_model_name = st.radio(
        "Select model", ["Logistic Regression", "SVM"], horizontal=True
    )
    selected_model = (
        logistic_model if selected_model_name == "Logistic Regression" else svm_model
    )

    input_values = {}
    with st.expander("Enter feature values", expanded=True):
        input_columns = st.columns(2)
        for index, feature in enumerate(features.columns):
            series = features[feature]
            input_values[feature] = input_columns[index % 2].number_input(
                feature,
                min_value=float(series.min()),
                max_value=float(series.max()),
                value=float(series.median()),
                format="%.6f",
            )

    if st.button("Predict", type="primary"):
        new_record = pd.DataFrame([input_values], columns=features.columns)
        prediction = selected_model.predict(new_record)[0]
        st.success(f"Predicted class: {prediction}")