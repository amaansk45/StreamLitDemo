from pathlib import Path

import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


st.title("Practical 6 - Decision Tree and Random Forest")
st.write("Classification using the Kyphosis and Loan datasets.")

DATA_DIRECTORY = Path(__file__).resolve().parents[1] / "data"

DATASETS = {
    "Kyphosis": {
        "file": DATA_DIRECTORY / "kyphosis.csv",
        "target": "Kyphosis",
        "categorical": [],
    },
    "Loan Data": {
        "file": DATA_DIRECTORY / "loan_data.csv",
        "target": "not.fully.paid",
        "categorical": ["purpose"],
    },
}


@st.cache_data
def load_dataset(file_path):
    return pd.read_csv(file_path)


def prepare_dataset(data, target, categorical_columns):
    prepared_data = pd.get_dummies(
        data,
        columns=categorical_columns,
        drop_first=True,
        dtype=int,
    )
    features = prepared_data.drop(columns=[target])
    labels = prepared_data[target]
    return features, labels


def split_dataset(features, labels, test_size, random_state):
    return train_test_split(
        features,
        labels,
        test_size=test_size,
        random_state=random_state,
        stratify=labels,
    )


def train_and_evaluate(model, x_train, x_test, y_train, y_test):
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    return {
        "model": model,
        "predictions": predictions,
        "accuracy": accuracy_score(y_test, predictions),
        "matrix": confusion_matrix(y_test, predictions),
        "report": classification_report(
            y_test, predictions, output_dict=True, zero_division=0
        ),
    }


dataset_name = st.selectbox("Select dataset", DATASETS.keys())
dataset_config = DATASETS[dataset_name]
data = load_dataset(dataset_config["file"])
target_column = dataset_config["target"]
categorical_columns = dataset_config["categorical"]

st.sidebar.header("Model Settings")
test_percentage = st.sidebar.slider("Test data (%)", 10, 40, 30, 5)
random_state = st.sidebar.number_input("Random state", 0, value=101, step=1)
tree_depth = st.sidebar.slider("Decision tree maximum depth", 1, 20, 5)
number_of_trees = st.sidebar.slider("Random forest trees", 50, 600, 100, 50)

features, labels = prepare_dataset(data, target_column, categorical_columns)
x_train, x_test, y_train, y_test = split_dataset(
    features,
    labels,
    test_percentage / 100,
    int(random_state),
)

decision_tree = DecisionTreeClassifier(
    max_depth=tree_depth,
    random_state=int(random_state),
)
random_forest = RandomForestClassifier(
    n_estimators=number_of_trees,
    random_state=int(random_state),
)

tree_result = train_and_evaluate(
    decision_tree, x_train, x_test, y_train, y_test
)
forest_result = train_and_evaluate(
    random_forest, x_train, x_test, y_train, y_test
)

dataset_tab, tree_tab, forest_tab, prediction_tab = st.tabs(
    ["Dataset", "Decision Tree", "Random Forest", "Predict New Record"]
)


with dataset_tab:
    st.header(f"{dataset_name} Dataset")

    with st.expander("Load and preview dataset", expanded=True):
        st.success(f"Dataset loaded: {data.shape[0]} rows and {data.shape[1]} columns")
        st.dataframe(data.head(10), width="stretch", hide_index=True)

    with st.expander("Dataset description"):
        st.write("**Columns:**", data.columns.tolist())
        st.write("**Target column:**", target_column)
        st.write("**Missing values:**", int(data.isna().sum().sum()))
        st.dataframe(data.describe(include="all").T, width="stretch")

    with st.expander("Feature engineering"):
        if categorical_columns:
            engineered_data = pd.get_dummies(
                data, columns=categorical_columns, drop_first=True, dtype=int
            )
            st.write(
                "The categorical `purpose` column is converted into numeric dummy "
                "variables before model training."
            )
            st.dataframe(engineered_data.head(), width="stretch", hide_index=True)
        else:
            st.info("All input features are numeric, so no feature engineering is required.")

    with st.expander("Train-test split"):
        st.write(f"Training records: **{len(x_train)}**")
        st.write(f"Testing records: **{len(x_test)}**")


def display_evaluation(result, y_test_values):
    st.metric("Accuracy", f"{result['accuracy']:.2%}")

    with st.expander("Confusion Matrix", expanded=True):
        labels = sorted(y_test_values.unique().tolist())
        matrix_data = pd.DataFrame(
            result["matrix"],
            index=[f"Actual {label}" for label in labels],
            columns=[f"Predicted {label}" for label in labels],
        )
        st.table(matrix_data)

    with st.expander("Classification Report"):
        st.dataframe(pd.DataFrame(result["report"]).T.round(3), width="stretch")


with tree_tab:
    st.header("Decision Tree Classification")
    st.write(f"Maximum tree depth: **{tree_depth}**")
    display_evaluation(tree_result, y_test)

with forest_tab:
    st.header("Random Forest Classification")
    st.write(f"Number of trees: **{number_of_trees}**")
    display_evaluation(forest_result, y_test)

    with st.expander("Model comparison"):
        comparison = pd.DataFrame(
            {
                "Model": ["Decision Tree", "Random Forest"],
                "Accuracy": [tree_result["accuracy"], forest_result["accuracy"]],
            }
        )
        st.dataframe(
            comparison.style.format({"Accuracy": "{:.2%}"}),
            width="stretch",
            hide_index=True,
        )
        best_model = comparison.loc[comparison["Accuracy"].idxmax(), "Model"]
        st.success(f"Higher test accuracy: {best_model}")

with prediction_tab:
    st.header("Predict a New Record")
    selected_model_name = st.radio(
        "Select model", ["Decision Tree", "Random Forest"], horizontal=True
    )
    selected_model = (
        tree_result["model"]
        if selected_model_name == "Decision Tree"
        else forest_result["model"]
    )

    input_values = {}
    with st.expander("Enter feature values", expanded=True):
        form_columns = st.columns(2)
        feature_columns = [column for column in data.columns if column != target_column]

        for index, feature in enumerate(feature_columns):
            container = form_columns[index % 2]
            if feature in categorical_columns:
                input_values[feature] = container.selectbox(
                    feature,
                    sorted(data[feature].dropna().unique().tolist()),
                )
            else:
                series = data[feature]
                default_value = float(series.median())
                if pd.api.types.is_integer_dtype(series):
                    input_values[feature] = container.number_input(
                        feature,
                        min_value=int(series.min()),
                        max_value=int(series.max()),
                        value=int(default_value),
                        step=1,
                    )
                else:
                    input_values[feature] = container.number_input(
                        feature,
                        min_value=float(series.min()),
                        max_value=float(series.max()),
                        value=default_value,
                        format="%.4f",
                    )

    if st.button("Predict", type="primary"):
        new_record = pd.DataFrame([input_values])
        combined_data = pd.concat(
            [data.drop(columns=[target_column]), new_record],
            ignore_index=True,
        )
        prepared_record = pd.get_dummies(
            combined_data,
            columns=categorical_columns,
            drop_first=True,
            dtype=int,
        ).tail(1)
        prepared_record = prepared_record.reindex(columns=features.columns, fill_value=0)
        prediction = selected_model.predict(prepared_record)[0]

        if dataset_name == "Loan Data":
            result_text = "Not fully paid" if prediction == 1 else "Fully paid"
        else:
            result_text = str(prediction).title()

        st.success(f"Predicted output: {result_text}")