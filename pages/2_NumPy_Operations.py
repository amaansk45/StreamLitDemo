import numpy as np
import streamlit as st


st.title("Introduction to NumPy - Basic Array Operations")
st.write(
    "Select a question to view the NumPy code, try the example, and inspect its output."
)

questions = (
    "Q1. Import NumPy and display its version number",
    "Q2. Create and display basic arrays",
    "Q3. Create a 3 x 3 identity matrix",
    "Q4. Create 15 equally spaced values between 0 and 1",
    "Q5. Create the given matrix",
    "Q6. Reshape an array into a 4 x 5 matrix",
    "Q7. Generate random matrices",
    "Q8. Create a matrix without typing each element",
    "Q9. Array indexing and slicing",
    "Q10. Replace all even numbers with 0",
    "Q11. Find the transpose of a matrix",
    "Q12. Calculate basic statistics",
    "Q13. Calculate row-wise and column-wise statistics",
    "Q14. Find indices of elements greater than 20",
    "Q15. Create an 8 x 8 checkerboard pattern",
    "Q16. Normalize a random array between 0 and 1",
    "Q17. Perform operations on two 3 x 3 matrices",
)

question = st.selectbox("Select a question", questions)
st.divider()


def show_code(code):
    st.write("**CODE**")
    st.code(code.strip(), language="python")


def show_output(value):
    st.write("**OUTPUT**")
    st.code(str(value), language="text")


if question == questions[0]:
    st.subheader(questions[0])
    show_code("""
import numpy as np
print(np.__version__)
""")
    st.write("**EXAMPLE**")
    show_output(np.__version__)

elif question == questions[1]:
    st.subheader(questions[1])
    show_code("""
import numpy as np

numbers = np.arange(1, 11)
even_numbers = np.arange(2, 21, 2)
zeros = np.zeros((5, 5), dtype=int)
ones = np.ones((4, 4), dtype=int)

print(numbers)
print(even_numbers)
print(zeros)
print(ones)
""")
    st.write("**EXAMPLE**")
    tab1, tab2, tab3, tab4 = st.tabs(
        ["1 to 10", "Even numbers", "5 x 5 zeros", "4 x 4 ones"]
    )
    with tab1:
        show_output(np.arange(1, 11))
    with tab2:
        show_output(np.arange(2, 21, 2))
    with tab3:
        show_output(np.zeros((5, 5), dtype=int))
    with tab4:
        show_output(np.ones((4, 4), dtype=int))

elif question == questions[2]:
    st.subheader(questions[2])
    show_code("""
identity_matrix = np.eye(3, dtype=int)
print(identity_matrix)
""")
    st.write("**EXAMPLE**")
    show_output(np.eye(3, dtype=int))

elif question == questions[3]:
    st.subheader(questions[3])
    show_code("""
values = np.linspace(0, 1, 15)
print(values)
""")
    st.write("**EXAMPLE**")
    precision = st.slider("Decimal places", 2, 8, 6)
    show_output(np.round(np.linspace(0, 1, 15), precision))

elif question == questions[4]:
    st.subheader(questions[4])
    st.warning(
        "The matrix for Q5 is not visible in the supplied assignment PDF. "
        "This example demonstrates direct matrix creation and can be updated when the matrix is provided."
    )
    show_code("""
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(matrix)
""")
    st.write("**EXAMPLE**")
    show_output(np.arange(1, 10).reshape(3, 3))

elif question == questions[5]:
    st.subheader(questions[5])
    show_code("""
array = np.arange(1, 21)
matrix = array.reshape(4, 5)
print(matrix)
""")
    st.write("**EXAMPLE**")
    show_output(np.arange(1, 21).reshape(4, 5))

elif question == questions[6]:
    st.subheader(questions[6])
    show_code("""
rng = np.random.default_rng()
decimal_matrix = rng.random((3, 3))
integer_matrix = rng.integers(10, 51, size=(4, 4))

print(decimal_matrix)
print(integer_matrix)
""")
    st.write("**EXAMPLE**")
    seed = st.number_input("Random seed", min_value=0, value=42, step=1)
    rng = np.random.default_rng(seed)
    col1, col2 = st.columns(2)
    with col1:
        st.caption("3 x 3 random values between 0 and 1")
        show_output(np.round(rng.random((3, 3)), 4))
    with col2:
        st.caption("4 x 4 random integers between 10 and 50")
        show_output(rng.integers(10, 51, size=(4, 4)))

elif question == questions[7]:
    st.subheader(questions[7])
    show_code("""
matrix = np.arange(10, 100, 10).reshape(3, 3)
print(matrix)
""")
    st.write("**EXAMPLE**")
    show_output(np.arange(10, 100, 10).reshape(3, 3))

elif question == questions[8]:
    st.subheader(questions[8])
    show_code("""
mat = np.arange(1, 26).reshape(5, 5)

print("Element 13:", mat[2, 2])
print("Last row:", mat[-1])
print("Third column:", mat[:, 2])
print("Submatrix:\\n", mat[1:4, 1:4])
print("Fourth column:", mat[:, 3])
""")
    st.write("**EXAMPLE**")
    mat = np.arange(1, 26).reshape(5, 5)
    st.caption("Original matrix")
    st.code(str(mat), language="text")
    results = {
        "a. Element 13": mat[2, 2],
        "b. Last row": mat[-1],
        "c. Third column": mat[:, 2],
        "d. 3 x 3 submatrix": mat[1:4, 1:4],
        "e. Elements [4, 9, 14, 19, 24]": mat[:, 3],
    }
    operation = st.radio("Select an extraction", tuple(results), horizontal=True)
    show_output(results[operation])

elif question == questions[9]:
    st.subheader(questions[9])
    show_code("""
mat = np.arange(1, 26).reshape(5, 5)
mat[mat % 2 == 0] = 0
print(mat)
""")
    st.write("**EXAMPLE**")
    mat = np.arange(1, 26).reshape(5, 5)
    mat[mat % 2 == 0] = 0
    show_output(mat)

elif question == questions[10]:
    st.subheader(questions[10])
    show_code("""
mat = np.arange(1, 26).reshape(5, 5)
transpose = mat.T
print(transpose)
""")
    st.write("**EXAMPLE**")
    show_output(np.arange(1, 26).reshape(5, 5).T)

elif question == questions[11]:
    st.subheader(questions[11])
    show_code("""
mat = np.arange(1, 26).reshape(5, 5)

print("Sum:", np.sum(mat))
print("Mean:", np.mean(mat))
print("Standard deviation:", np.std(mat))
print("Maximum:", np.max(mat))
print("Minimum:", np.min(mat))
""")
    st.write("**EXAMPLE**")
    mat = np.arange(1, 26).reshape(5, 5)
    st.table(
        {
            "Measure": ["Sum", "Mean", "Standard deviation", "Maximum", "Minimum"],
            "Value": [mat.sum(), mat.mean(), mat.std(), mat.max(), mat.min()],
        }
    )

elif question == questions[12]:
    st.subheader(questions[12])
    show_code("""
mat = np.arange(1, 26).reshape(5, 5)

print("Row-wise sums:", np.sum(mat, axis=1))
print("Column-wise sums:", np.sum(mat, axis=0))
print("Row-wise means:", np.mean(mat, axis=1))
print("Column-wise means:", np.mean(mat, axis=0))
""")
    st.write("**EXAMPLE**")
    mat = np.arange(1, 26).reshape(5, 5)
    operation = st.selectbox(
        "Select a calculation",
        ("Row-wise sums", "Column-wise sums", "Row-wise means", "Column-wise means"),
    )
    results = {
        "Row-wise sums": mat.sum(axis=1),
        "Column-wise sums": mat.sum(axis=0),
        "Row-wise means": mat.mean(axis=1),
        "Column-wise means": mat.mean(axis=0),
    }
    show_output(results[operation])

elif question == questions[13]:
    st.subheader(questions[13])
    show_code("""
mat = np.arange(1, 26).reshape(5, 5)
indices = np.argwhere(mat > 20)
print(indices)
""")
    st.write("**EXAMPLE**")
    mat = np.arange(1, 26).reshape(5, 5)
    show_output(np.argwhere(mat > 20))
    st.caption("NumPy indices are zero-based and shown as [row, column].")

elif question == questions[14]:
    st.subheader(questions[14])
    show_code("""
checkerboard = np.zeros((8, 8), dtype=int)
checkerboard[::2, 1::2] = 1
checkerboard[1::2, ::2] = 1
print(checkerboard)
""")
    st.write("**EXAMPLE**")
    checkerboard = np.indices((8, 8)).sum(axis=0) % 2
    show_output(checkerboard)

elif question == questions[15]:
    st.subheader(questions[15])
    show_code("""
rng = np.random.default_rng()
array = rng.random(20)
normalized = (array - array.min()) / (array.max() - array.min())

print("Original:", array)
print("Normalized:", normalized)
""")
    st.write("**EXAMPLE**")
    seed = st.number_input("Random seed", min_value=0, value=42, step=1)
    array = np.random.default_rng(seed).random(20)
    normalized = (array - array.min()) / (array.max() - array.min())
    st.caption("Original array")
    st.code(str(np.round(array, 4)), language="text")
    st.caption("Normalized array")
    st.code(str(np.round(normalized, 4)), language="text")
    st.info(f"Normalized range: {normalized.min():.1f} to {normalized.max():.1f}")

elif question == questions[16]:
    st.subheader(questions[16])
    show_code("""
matrix_a = np.arange(1, 10).reshape(3, 3)
matrix_b = np.arange(9, 0, -1).reshape(3, 3)

print("Addition:\\n", matrix_a + matrix_b)
print("Subtraction:\\n", matrix_a - matrix_b)
print("Element-wise multiplication:\\n", matrix_a * matrix_b)
print("Matrix multiplication:\\n", matrix_a @ matrix_b)
""")
    st.write("**EXAMPLE**")
    matrix_a = np.arange(1, 10).reshape(3, 3)
    matrix_b = np.arange(9, 0, -1).reshape(3, 3)
    col1, col2 = st.columns(2)
    with col1:
        st.caption("Matrix A")
        st.code(str(matrix_a), language="text")
    with col2:
        st.caption("Matrix B")
        st.code(str(matrix_b), language="text")

    operation = st.selectbox(
        "Select an operation",
        ("Addition", "Subtraction", "Element-wise multiplication", "Matrix multiplication"),
    )
    results = {
        "Addition": matrix_a + matrix_b,
        "Subtraction": matrix_a - matrix_b,
        "Element-wise multiplication": matrix_a * matrix_b,
        "Matrix multiplication": matrix_a @ matrix_b,
    }
    show_output(results[operation])