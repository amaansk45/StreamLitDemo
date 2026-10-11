import numpy as np
import pandas as pd
import streamlit as st


st.title("Pandas Data Analysis")
st.write(
    "Explore both Assignment 3 case studies with executable pandas examples. "
    "Upload the original CSV files or use the built-in sample data."
)


def ecommerce_sample():
    return pd.DataFrame(
        {
            "Company": ["Acme", "Globex", "Acme", "Initech", "Umbrella", "Globex", "Stark", "Wayne", "Acme", "Stark", "Wayne", "Initech"],
            "Purchase Price": [25.50, 72.00, 48.25, 91.40, 15.75, 63.20, 120.00, 55.50, 35.00, 82.30, 28.90, 67.75],
            "Language": ["en", "fr", "de", "en", "en", "fr", "de", "en", "fr", "en", "de", "en"],
            "CC Provider": ["Visa", "Mastercard", "American Express", "Visa", "Visa", "Mastercard", "American Express", "Visa", "Mastercard", "Visa", "American Express", "Mastercard"],
            "Job": ["Engineer", "Teacher", "Engineer", "Manager", "Designer", "Teacher", "Doctor", "Manager", "Engineer", "Doctor", "Designer", "Engineer"],
            "Email": ["a@gmail.com", "b@yahoo.com", "c@gmail.com", "d@outlook.com", "e@gmail.com", "f@yahoo.com", "g@outlook.com", "h@gmail.com", "i@yahoo.com", "j@gmail.com", "k@outlook.com", "l@gmail.com"],
            "Browser Info": ["Chrome", "Firefox", "Chrome", "Edge", "Safari", "Firefox", "Chrome", "Edge", "Safari", "Chrome", "Firefox", "Edge"],
        }
    )


def salary_sample():
    return pd.DataFrame(
        {
            "EmployeeName": ["Aarav", "Diya", "Kabir", "Meera", "Rohan", "Sara", "Vikram", "Anaya", "Arjun", "Isha", "Neel", "Tara"],
            "JobTitle": ["Police Officer", "Firefighter", "Engineer", "Manager", "Police Officer", "Firefighter", "Director", "Engineer", "Manager", "Police Officer", "Firefighter", "Director"],
            "BasePay": [85000, 92000, 78000, 110000, 88000, 95000, 145000, 82000, 115000, 90000, 97000, 150000],
            "OvertimePay": [15000, 22000, 5000, 2000, 18000, 25000, 0, 6500, 1500, 16000, 24000, 0],
            "OtherPay": [3000, 4500, 2000, 5000, 3200, 4000, 10000, 2500, 6000, 3500, 4200, 12000],
            "Benefits": [20000, 22000, 18000, 25000, 20500, 22500, 35000, 18500, 26000, 21000, 23000, 36000],
            "Year": [2022, 2022, 2022, 2022, 2023, 2023, 2023, 2023, 2024, 2024, 2024, 2024],
        }
    ).assign(
        TotalPay=lambda x: x["BasePay"] + x["OvertimePay"] + x["OtherPay"],
        TotalPayBenefits=lambda x: x["BasePay"] + x["OvertimePay"] + x["OtherPay"] + x["Benefits"],
    )


def show_code(code):
    st.write("**CODE**")
    st.code(code.strip(), language="python")


def show_result(value):
    st.write("**OUTPUT**")
    if isinstance(value, pd.DataFrame):
        st.dataframe(value, width="stretch", hide_index=True)
    elif isinstance(value, pd.Series):
        st.dataframe(value.rename("Value").reset_index(), width="stretch", hide_index=True)
    else:
        st.success(str(value))


case_study = st.selectbox(
    "Select a case study",
    ("1. E-Commerce Customer Purchase Analysis", "2. SF Employee Salary Analysis"),
)

uploaded_file = st.file_uploader(
    "Upload the corresponding CSV file (optional)",
    type="csv",
    key="ecommerce_upload" if case_study.startswith("1") else "salary_upload",
)

try:
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.caption(f"Using uploaded data: {len(data):,} rows and {len(data.columns)} columns")
    elif case_study.startswith("1"):
        data = ecommerce_sample()
        st.info("Using built-in sample E-Commerce data. Upload the assignment CSV for its actual results.")
    else:
        data = salary_sample()
        st.info("Using built-in sample SF Salary data. Upload the assignment CSV for its actual results.")
except Exception as error:
    st.error(f"The CSV could not be read: {error}")
    st.stop()

st.divider()


if case_study.startswith("1"):
    parts = {
        "Part A: Data Exploration": (
            "1. Load the dataset into a DataFrame",
            "2. Display the first and last five records",
            "3. Find shape, data types, missing values, and duplicates",
        ),
        "Part B: Customer Analytics": (
            "1. Average, maximum, and minimum purchase price",
            "2. Top 10 most expensive purchases",
            "3. Count English, French, and German customers",
            "4. Count Visa, MasterCard, and American Express users",
            "5. Five most common job titles",
        ),
        "Part C: Business Insights": (
            "1. Email provider with the highest number of users",
            "2. Total sales, average sales, and median purchase price",
            "3. Create the Purchase Category column",
            "4. Percentage of customers in each category",
        ),
        "Part D: Advanced Pandas": (
            "1. Company with the highest average purchase price",
            "2. Credit card provider contributing the highest revenue",
            "3. Browser users who spend the most",
        ),
    }
    part = st.selectbox("Select a part", tuple(parts))
    question = st.selectbox("Select a question", parts[part])
    st.subheader(question)

    if part == "Part A: Data Exploration" and question.startswith("1."):
        show_code("""
import pandas as pd
df = pd.read_csv("Ecommerce Purchases.csv")
print(df)
""")
        show_result(data)

    elif part == "Part A: Data Exploration" and question.startswith("2."):
        show_code("""
print(df.head())
print(df.tail())
""")
        first, last = st.tabs(["First five records", "Last five records"])
        with first:
            show_result(data.head())
        with last:
            show_result(data.tail())

    elif part == "Part A: Data Exploration":
        show_code("""
print("Rows and columns:", df.shape)
print(df.dtypes)
print(df.isna().sum())
print("Duplicate records:", df.duplicated().sum())
""")
        choice = st.radio("Select information", ("Shape", "Data types", "Missing values", "Duplicates"), horizontal=True)
        outputs = {
            "Shape": f"{data.shape[0]} rows x {data.shape[1]} columns",
            "Data types": data.dtypes.astype(str),
            "Missing values": data.isna().sum(),
            "Duplicates": int(data.duplicated().sum()),
        }
        show_result(outputs[choice])

    elif part == "Part B: Customer Analytics" and question.startswith("1."):
        show_code("""
print("Average:", df["Purchase Price"].mean())
print("Maximum:", df["Purchase Price"].max())
print("Minimum:", df["Purchase Price"].min())
""")
        prices = pd.to_numeric(data["Purchase Price"], errors="coerce")
        show_result(pd.DataFrame({"Measure": ["Average", "Maximum", "Minimum"], "Price": [prices.mean(), prices.max(), prices.min()]}))

    elif part == "Part B: Customer Analytics" and question.startswith("2."):
        show_code('top_10 = df.nlargest(10, "Purchase Price")\nprint(top_10)')
        show_result(data.nlargest(10, "Purchase Price"))

    elif part == "Part B: Customer Analytics" and question.startswith("3."):
        show_code('counts = df[df["Language"].isin(["en", "fr", "de"])]["Language"].value_counts()\nprint(counts)')
        language_names = {"en": "English", "fr": "French", "de": "German"}
        counts = data["Language"].str.lower().map(language_names).value_counts().reindex(language_names.values(), fill_value=0)
        show_result(counts)

    elif part == "Part B: Customer Analytics" and question.startswith("4."):
        show_code('providers = ["Visa", "Mastercard", "American Express"]\nprint(df[df["CC Provider"].isin(providers)]["CC Provider"].value_counts())')
        providers = data["CC Provider"].replace({"MasterCard": "Mastercard"})
        show_result(providers[providers.isin(["Visa", "Mastercard", "American Express"])].value_counts())

    elif part == "Part B: Customer Analytics":
        show_code('print(df["Job"].value_counts().head(5))')
        show_result(data["Job"].value_counts().head(5))

    elif part == "Part C: Business Insights" and question.startswith("1."):
        show_code('df["Email Provider"] = df["Email"].str.split("@").str[-1]\nprint(df["Email Provider"].value_counts().head(1))')
        providers = data["Email"].str.extract(r"@(.+)$", expand=False).value_counts()
        show_result(providers.head(1))

    elif part == "Part C: Business Insights" and question.startswith("2."):
        show_code('print("Total:", df["Purchase Price"].sum())\nprint("Average:", df["Purchase Price"].mean())\nprint("Median:", df["Purchase Price"].median())')
        prices = pd.to_numeric(data["Purchase Price"], errors="coerce")
        show_result(pd.DataFrame({"Measure": ["Total sales", "Average sales", "Median purchase price"], "Amount": [prices.sum(), prices.mean(), prices.median()]}))

    elif part == "Part C: Business Insights" and question.startswith("3."):
        show_code("""
df["Purchase Category"] = df["Purchase Price"].apply(
    lambda price: "Low" if price < 30 else "Medium" if price <= 60 else "High"
)
print(df[["Purchase Price", "Purchase Category"]])
""")
        result = data.copy()
        result["Purchase Category"] = result["Purchase Price"].apply(lambda price: "Low" if price < 30 else "Medium" if price <= 60 else "High")
        show_result(result[["Purchase Price", "Purchase Category"]])

    elif part == "Part C: Business Insights":
        show_code('percentages = df["Purchase Category"].value_counts(normalize=True).mul(100)\nprint(percentages)')
        categories = data["Purchase Price"].apply(lambda price: "Low" if price < 30 else "Medium" if price <= 60 else "High")
        show_result(categories.value_counts(normalize=True).mul(100).round(2).rename("Percentage"))

    elif part == "Part D: Advanced Pandas" and question.startswith("1."):
        show_code('result = df.groupby("Company")["Purchase Price"].mean().sort_values(ascending=False)\nprint(result.head(1))')
        show_result(data.groupby("Company")["Purchase Price"].mean().sort_values(ascending=False).head(1))

    elif part == "Part D: Advanced Pandas" and question.startswith("2."):
        show_code('result = df.groupby("CC Provider")["Purchase Price"].sum().sort_values(ascending=False)\nprint(result.head(1))')
        show_result(data.groupby("CC Provider")["Purchase Price"].sum().sort_values(ascending=False).head(1))

    else:
        show_code('result = df.groupby("Browser Info")["Purchase Price"].sum().sort_values(ascending=False)\nprint(result)')
        browser = data["Browser Info"].str.extract(r"(Chrome|Firefox|Safari|Edge|Opera)", expand=False).fillna(data["Browser Info"])
        show_result(data.assign(Browser=browser).groupby("Browser")["Purchase Price"].sum().sort_values(ascending=False))

else:
    parts = {
        "Part A: Data Understanding": (
            "1. Import the dataset",
            "2. Display head, tail, shape, data types, and summary statistics",
        ),
        "Part B: Salary Analysis": (
            "1. Highest salary",
            "2. Lowest salary",
            "3. Average BasePay",
            "4. Average OvertimePay",
            "5. Average TotalPayBenefits",
            "6. Employee receiving maximum TotalPayBenefits",
        ),
        "Part C: Employee Analytics": (
            "1. Count employees by Job Title",
            "2. Top 15 highest-paid employees",
            "3. Top 10 job titles by average salary",
            "4. Employees earning more than $100,000",
            "5. Average salary for Police Officers",
            "6. Average salary for Firefighters",
        ),
        "Part D: Trend Analysis": (
            "1. Number of employee records each year",
            "2. Average salary by year",
            "3. Job title with highest average salary each year",
            "4. Year paying the highest total salary",
            "5. Compare BasePay, OvertimePay, and OtherPay",
        ),
        "Part E: Data Cleaning": (
            "1. Replace missing values appropriately",
            "2. Convert salary columns to numeric",
            "3. Remove duplicate rows",
            "4. Create the Salary Grade column",
        ),
    }
    part = st.selectbox("Select a part", tuple(parts))
    question = st.selectbox("Select a question", parts[part])
    st.subheader(question)
    salary_columns = ["BasePay", "OvertimePay", "OtherPay", "Benefits", "TotalPay", "TotalPayBenefits"]

    if part == "Part A: Data Understanding" and question.startswith("1."):
        show_code('import pandas as pd\ndf = pd.read_csv("Salaries.csv")\nprint(df)')
        show_result(data)

    elif part == "Part A: Data Understanding":
        show_code('print(df.head())\nprint(df.tail())\nprint(df.shape)\nprint(df.dtypes)\nprint(df.describe())')
        view = st.radio("Select information", ("Head", "Tail", "Shape", "Data types", "Summary statistics"), horizontal=True)
        outputs = {"Head": data.head(), "Tail": data.tail(), "Shape": f"{data.shape[0]} rows x {data.shape[1]} columns", "Data types": data.dtypes.astype(str), "Summary statistics": data.describe().T.reset_index(names="Column")}
        show_result(outputs[view])

    elif part == "Part B: Salary Analysis":
        total_column = "TotalPay" if "TotalPay" in data.columns else "BasePay"
        if question.startswith("1."):
            show_code('print(df["TotalPay"].max())')
            show_result(pd.to_numeric(data[total_column], errors="coerce").max())
        elif question.startswith("2."):
            show_code('print(df["TotalPay"].min())')
            show_result(pd.to_numeric(data[total_column], errors="coerce").min())
        elif question.startswith("3."):
            show_code('print(df["BasePay"].mean())')
            show_result(pd.to_numeric(data["BasePay"], errors="coerce").mean())
        elif question.startswith("4."):
            show_code('print(df["OvertimePay"].mean())')
            show_result(pd.to_numeric(data["OvertimePay"], errors="coerce").mean())
        elif question.startswith("5."):
            show_code('print(df["TotalPayBenefits"].mean())')
            show_result(pd.to_numeric(data["TotalPayBenefits"], errors="coerce").mean())
        else:
            show_code('employee = df.loc[df["TotalPayBenefits"].idxmax()]\nprint(employee)')
            numeric = pd.to_numeric(data["TotalPayBenefits"], errors="coerce")
            show_result(data.loc[[numeric.idxmax()]])

    elif part == "Part C: Employee Analytics":
        if question.startswith("1."):
            show_code('print(df["JobTitle"].value_counts())')
            show_result(data["JobTitle"].value_counts())
        elif question.startswith("2."):
            show_code('print(df.nlargest(15, "TotalPayBenefits"))')
            show_result(data.nlargest(15, "TotalPayBenefits"))
        elif question.startswith("3."):
            show_code('result = df.groupby("JobTitle")["TotalPayBenefits"].mean().nlargest(10)\nprint(result)')
            show_result(data.groupby("JobTitle")["TotalPayBenefits"].mean().nlargest(10))
        elif question.startswith("4."):
            show_code('count = (df["TotalPay"] > 100000).sum()\nprint(count)')
            show_result(int((pd.to_numeric(data["TotalPay"], errors="coerce") > 100000).sum()))
        elif question.startswith("5."):
            show_code('average = df[df["JobTitle"].str.contains("Police", case=False, na=False)]["TotalPay"].mean()\nprint(average)')
            mask = data["JobTitle"].str.contains("Police", case=False, na=False)
            show_result(pd.to_numeric(data.loc[mask, "TotalPay"], errors="coerce").mean())
        else:
            show_code('average = df[df["JobTitle"].str.contains("Fire", case=False, na=False)]["TotalPay"].mean()\nprint(average)')
            mask = data["JobTitle"].str.contains("Fire", case=False, na=False)
            show_result(pd.to_numeric(data.loc[mask, "TotalPay"], errors="coerce").mean())

    elif part == "Part D: Trend Analysis":
        if question.startswith("1."):
            show_code('print(df.groupby("Year").size())')
            show_result(data.groupby("Year").size().rename("Employees"))
        elif question.startswith("2."):
            show_code('print(df.groupby("Year")["TotalPay"].mean())')
            show_result(data.groupby("Year")["TotalPay"].mean())
        elif question.startswith("3."):
            show_code('averages = df.groupby(["Year", "JobTitle"])["TotalPay"].mean()\nresult = averages.loc[averages.groupby(level=0).idxmax()]\nprint(result)')
            averages = data.groupby(["Year", "JobTitle"])["TotalPay"].mean()
            result = averages.reset_index().sort_values(["Year", "TotalPay"], ascending=[True, False]).drop_duplicates("Year")
            show_result(result)
        elif question.startswith("4."):
            show_code('print(df.groupby("Year")["TotalPay"].sum().nlargest(1))')
            show_result(data.groupby("Year")["TotalPay"].sum().nlargest(1))
        else:
            show_code('comparison = df.groupby("Year")[["BasePay", "OvertimePay", "OtherPay"]].agg(["mean", "sum"])\nprint(comparison)')
            show_result(data.groupby("Year")[["BasePay", "OvertimePay", "OtherPay"]].agg(["mean", "sum"]).round(2))

    else:
        if question.startswith("1."):
            show_code('df[salary_columns] = df[salary_columns].fillna(0)\ndf["EmployeeName"] = df["EmployeeName"].fillna("Unknown")')
            cleaned = data.copy()
            existing = [column for column in salary_columns if column in cleaned.columns]
            cleaned[existing] = cleaned[existing].fillna(0)
            if "EmployeeName" in cleaned:
                cleaned["EmployeeName"] = cleaned["EmployeeName"].fillna("Unknown")
            show_result(cleaned)
        elif question.startswith("2."):
            show_code('for column in salary_columns:\n    df[column] = pd.to_numeric(df[column], errors="coerce")\nprint(df.dtypes)')
            converted = data.copy()
            for column in [column for column in salary_columns if column in converted.columns]:
                converted[column] = pd.to_numeric(converted[column], errors="coerce")
            show_result(converted.dtypes.astype(str))
        elif question.startswith("3."):
            show_code('df = df.drop_duplicates()\nprint(df)')
            before = len(data)
            cleaned = data.drop_duplicates()
            st.caption(f"Removed {before - len(cleaned)} duplicate row(s).")
            show_result(cleaned)
        else:
            show_code("""
df["Salary Grade"] = df["TotalPay"].apply(
    lambda salary: "C" if salary < 50000 else "B" if salary <= 100000 else "A"
)
print(df[["TotalPay", "Salary Grade"]])
""")
            result = data.copy()
            result["Salary Grade"] = pd.to_numeric(result["TotalPay"], errors="coerce").apply(lambda salary: "C" if salary < 50000 else "B" if salary <= 100000 else "A")
            show_result(result[["EmployeeName", "TotalPay", "Salary Grade"]])