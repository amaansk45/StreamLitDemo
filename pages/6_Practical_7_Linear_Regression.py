from pathlib import Path

import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression


st.title("Practical 7 - Regression Analysis")
st.write("Linear Regression with one variable and multiple variables.")

DATA_DIRECTORY = Path(__file__).resolve().parents[1] / "data"


@st.cache_data
def load_data(file_name):
    data = pd.read_csv(DATA_DIRECTORY / file_name)
    data.columns = data.columns.str.strip()
    return data


def train_model(data, features, target):
    model = LinearRegression()
    model.fit(data[features], data[target])
    return model


def show_dataset(data, features, target):
    with st.expander("Load and preview dataset", expanded=True):
        st.success(f"Dataset loaded: {data.shape[0]} rows and {data.shape[1]} columns")
        st.dataframe(data.head(10), width="stretch", hide_index=True)

    with st.expander("Describe dataset"):
        st.write("**Feature columns:**", features)
        st.write("**Target column:**", target)
        st.write("**Missing values:**", int(data.isna().sum().sum()))
        st.dataframe(data.describe().T, width="stretch")

    with st.expander("Feature engineering"):
        st.info(
            "All required columns are numeric and contain no missing values, "
            "so no feature engineering is required."
        )


def show_model(model, features):
    with st.expander("Trained model", expanded=True):
        st.success("Linear Regression model trained successfully.")
        coefficients = pd.DataFrame(
            {"Feature": features, "Coefficient": model.coef_}
        )
        st.dataframe(coefficients, width="stretch", hide_index=True)
        st.write(f"**Intercept:** {model.intercept_:,.2f}")


simple_data = load_data("homeprices.csv")
multiple_data = load_data("house_dataset.csv")

simple_model = train_model(simple_data, ["area"], "price")
multiple_model = train_model(
    multiple_data,
    ["Area", "Bedrooms", "Age"],
    "Price",
)

simple_tab, multiple_tab = st.tabs(
    ["Linear Regression", "Multiple Linear Regression"]
)

with simple_tab:
    st.header("Linear Regression with One Variable")
    st.write("Predict house price using its area.")
    show_dataset(simple_data, ["area"], "price")
    show_model(simple_model, ["area"])

    st.subheader("Predict New House Price")
    area = st.number_input(
        "Area (square feet)",
        min_value=1,
        value=3300,
        step=100,
        key="simple_area",
    )
    if st.button("Predict Price", key="simple_predict", type="primary"):
        new_house = pd.DataFrame({"area": [area]})
        predicted_price = simple_model.predict(new_house)[0]
        st.success(f"Predicted price: {predicted_price:,.2f}")

with multiple_tab:
    st.header("Multiple Linear Regression")
    st.write("Predict house price using area, bedrooms, and house age.")
    show_dataset(multiple_data, ["Area", "Bedrooms", "Age"], "Price")
    show_model(multiple_model, ["Area", "Bedrooms", "Age"])

    st.subheader("Predict New House Price")
    input_columns = st.columns(3)
    area = input_columns[0].number_input(
        "Area (square feet)",
        min_value=1,
        value=3000,
        step=100,
        key="multiple_area",
    )
    bedrooms = input_columns[1].number_input(
        "Bedrooms",
        min_value=1,
        value=3,
        step=1,
    )
    age = input_columns[2].number_input(
        "House age (years)",
        min_value=0,
        value=40,
        step=1,
    )

    if st.button("Predict Price", key="multiple_predict", type="primary"):
        new_house = pd.DataFrame(
            {"Area": [area], "Bedrooms": [bedrooms], "Age": [age]}
        )
        predicted_price = multiple_model.predict(new_house)[0]
        st.success(f"Predicted price: {predicted_price:,.2f}")