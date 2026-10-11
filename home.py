import streamlit as st

st.title("Python Programming Lab")

st.markdown("""
Welcome to the **Python Programming Lab**.

This web application provides interactive demonstrations and practical examples to help students understand Python programming concepts, perform numerical computations using NumPy, and analyze data using Pandas.
""")

st.divider()

st.subheader("Modules")

with st.expander("Python Fundamentals", expanded=True):
    st.markdown("""
    This module covers the core concepts of Python programming, including:

    - Basic Python Programming
    - Variables and Data Types
    - Input and Output
    - Arithmetic Operations
    - String Manipulation
    - Conditional Statements
    - Loops
    - User Defined Functions
    - Lists
    - Tuples
    - Dictionaries
    - Sets
    - Basic Programming Exercises
    """)

with st.expander("NumPy Operations"):
    st.markdown("""
    This module introduces NumPy for numerical computing and array manipulation.

    Topics include:

    - Creating NumPy Arrays
    - Array Indexing and Slicing
    - Mathematical Operations
    - Statistical Functions
    - Reshaping Arrays
    - Matrix Operations
    - Random Number Generation
    """)

with st.expander("Pandas Operations"):
    st.markdown("""
    This module focuses on data analysis using the Pandas library.

    Topics include:

    - Creating Series and DataFrames
    - Reading and Writing CSV Files
    - Data Selection and Filtering
    - Handling Missing Values
    - Sorting Data
    - GroupBy Operations
    - Merging DataFrames
    - Basic Data Analysis
    """)

st.divider()

st.subheader("Purpose")

st.markdown("""
The objectives of this application are to:

- Understand the fundamentals of Python programming.
- Practice problem-solving through interactive examples.
- Learn numerical computing using NumPy.
- Explore data manipulation and analysis using Pandas.
- Execute programs and observe their outputs in an interactive environment.

Use the **navigation menu** to select a module and begin exploring the available practical exercises.
""")