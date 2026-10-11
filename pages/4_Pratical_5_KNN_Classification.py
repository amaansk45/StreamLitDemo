import pandas as pd
import streamlit as st

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

st.title("K-Nearest Neighbors (KNN) Classification using Streamlit")

with st.expander("1. Home Page", expanded=True):
    st.write("**Student Name:** Amaan Shaikh")
    st.write("**Enrollment Number:** 25MCA30094")
    st.write("**Course Name:** Machine Learning (MCA 34)")
    st.write(
        "**Objective:** To develop an interactive Streamlit application "
        "for KNN classification, model evaluation and prediction."
    )

with st.expander("2. Dataset Explorer", expanded=True):
    uploaded_file = st.file_uploader(
        "Upload CSV Dataset",
        type=["csv"]
    )
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        data = data.drop(
            columns=["Unnamed: 0"],
            errors="ignore"
        )
        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
            "First 10",
            "Last 10",
            "Dimensions",
            "Columns",
            "Data Types",
            "Statistics",
            "Missing Values",
            "Classes"
        ])
        with tab1:
            st.subheader("First 10 Records")
            st.dataframe(data.head(10))
        with tab2:
            st.subheader("Last 10 Records")
            st.dataframe(data.tail(10))
        with tab3:
            st.subheader("Dataset Dimensions")
            st.write(data.shape)
        with tab4:
            st.subheader("Column Names")
            st.write(list(data.columns))
        with tab5:
            st.subheader("Data Types")
            st.write(data.dtypes)
        with tab6:
            st.subheader("Descriptive Statistics")
            st.dataframe(data.describe())
        with tab7:
            st.subheader("Missing Values")
            st.write(data.isnull().sum())
        with tab8:
            st.subheader("Number of Unique Classes")
            st.write(
                data["TARGET CLASS"].nunique()
            )
    else:
        st.info("Please upload a CSV dataset.")

# Stop until dataset is uploaded
if uploaded_file is None:
    st.stop()


# Remove rows with missing values
data = data.dropna()
X = data.drop(columns=["TARGET CLASS"])
y = data["TARGET CLASS"]

with st.expander("5. Train-Test Split"):
    test_size = st.slider(
        "Test Size (%)",
        10,
        40,
        30
    )
    random_state = st.number_input(
        "Random State",
        value=42
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size / 100,
        random_state=int(random_state),
        stratify=y
    )
    st.write("**Training Data Size:**", len(X_train))
    st.write("**Testing Data Size:**", len(X_test))

with st.expander("6. Model Training"):
    k = st.slider(
        "Select K Value",
        1,
        20,
        5
    )
    model = KNeighborsClassifier(
        n_neighbors=k
    )
    if st.button("Train Model"):
        model.fit(
            X_train,
            y_train
        )
        st.write("**Selected K Value:**", k)
        st.success(
            "Model training completed successfully."
        )

# Model required for following sections
model.fit(
    X_train,
    y_train
)

predictions = model.predict(
    X_test
)

with st.expander("7. Model Evaluation"):
    accuracy = accuracy_score(
        y_test,
        predictions
    )
    tab1, tab2, tab3 = st.tabs([
        "Accuracy Score",
        "Confusion Matrix",
        "Classification Report"
    ])
    with tab1:
        st.metric(
            "Accuracy Score",
            f"{accuracy:.2%}"
        )
    with tab2:
        matrix = confusion_matrix(
            y_test,
            predictions
        )

        st.dataframe(matrix)
    with tab3:
        report = classification_report(
            y_test,
            predictions,
            output_dict=True,
            zero_division=0
        )
        st.dataframe(
            pd.DataFrame(report).T
        )

with st.expander("8. Accuracy Comparison"):
    results = []
    for k_value in range(1, 21):
        knn = KNeighborsClassifier(
            n_neighbors=k_value
        )
        knn.fit(
            X_train,
            y_train
        )
        pred = knn.predict(
            X_test
        )
        score = accuracy_score(
            y_test,
            pred
        )
        results.append({
            "K": k_value,
            "Accuracy": score
        })
    comparison = pd.DataFrame(results)
    best = comparison.loc[
        comparison["Accuracy"].idxmax()
    ]
    tab1, tab2, tab3 = st.tabs([
        "K & Accuracy",
        "K vs Accuracy",
        "Best K"
    ])
    with tab1:
        st.dataframe(
            comparison,
            use_container_width=True
        )
    with tab2:
        st.line_chart(
            comparison.set_index("K")["Accuracy"]
        )
    with tab3:
        st.metric(
            "Best K Value",
            int(best["K"])
        )
        st.metric(
            "Highest Accuracy",
            f"{best['Accuracy']:.2%}"
        )

with st.expander("9. Prediction Module"):
    st.write("Enter feature values:")
    input_values = {}
    for feature in X.columns:
        input_values[feature] = st.number_input(
            feature,
            value=float(data[feature].median())
        )
    if st.button("Predict"):
        new_record = pd.DataFrame(
            [input_values]
        )
        predicted_class = model.predict(
            new_record
        )[0]
        st.success(
            f"Predicted Class: {predicted_class}"
        )

with st.expander("10. Conclusion"):
    st.write(
        "**Best K Value:**",
        int(best["K"])
    )
    st.write(
        "**Highest Accuracy:**",
        f"{best['Accuracy']:.2%}"
    )
    st.write(
        "The KNN model was successfully trained and evaluated. "
        "The best K value produced the highest classification accuracy "
        "for the given dataset."
    )