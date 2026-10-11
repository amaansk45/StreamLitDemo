import streamlit as st

st.title("Python Fundamentals")

part = st.selectbox("select an part",
    options=(
        "Part A: Basic Python Programming", 
        "Part B: Working with Lists and Dictionaries", 
        "Part C: User Defined Functions",
        "Part D: Conditional Statements",
        "Part E: Additional Programming Exercise"
        ))


if(part == "Part A: Basic Python Programming"):
    st.header("Part A: Basic Python Programming")

    question = st.selectbox("select a Question",
        options=(
            "Q1. Personal Information",
            "Q2. Arithmetic Operation",
            "Q3. String Manipulation",
            "Q4. String Formatting",
        ))


    if(question == "Q1. Personal Information"):
        st.subheader("Q1. Personal Information")

        st.write("**CODE**")
        st.code('''name = input("Enter Your Name : ")\nage = int(input("Enter Your Age : "))\nprint(f"{name} - {age}") ''')

        st.write("**EXAMPLE**")
        name = st.text_input("Enter your Name:")
        age = st.number_input("Enter your Age",min_value=1,step=1,value=1)

        st.write("**OUTPUT**")
        if(name and age):
            st.write(f"*{name} - {age}*")


    if(question == "Q2. Arithmetic Operation"):
        st.subheader("Q2. Arithmetic Operation")

        st.write("**CODE**")
        st.code('''num = int(input("Enter a number : "))\npow = int(input("Enter power : "))\nprint(f"{num} ^ {pow} = {num ** pow}") ''')
        
        st.write("**EXAMPLE**")
        num = st.number_input("Enter a number : ",min_value=1,step=1,value=1)
        pow = st.number_input("Enter power : ",min_value=1,step=1,value=1)

        st.write("**OUTPUT**")
        st.write(f"*{num} ^ {pow} = {num ** pow }*")


    if(question == "Q3. String Manipulation"):
        st.subheader("Q3. String Manipulation")

        st.write("**CODE**")
        st.code('''s = input("Enter a text : ")\nwords = s.split()\nprint(words) ''')

        st.write("**EXAMPLE**")
        s = st.text_input("Enter a text : ")
        words = s.split()

        st.write("**OUTPUT**")
        st.write(f"*{words}*")


    if(question == "Q4. String Formatting"):
        st.subheader("Q4. String Formatting")

        st.write("**CODE**")
        st.code('''planet = "Earth"\ndiameter = 12742\nprint(f"The diameter of {planet} is {diameter} kilometers." ''')

        st.write("**EXAMPLE**")
        planet = st.text_input("Enter planet name :")
        diameter = st.number_input("Enter diameter :")

        st.write("**OUTPUT**")
        if(planet and diameter):
            st.write(f"*The diameter of {planet} is {diameter} kilometers.*")
        
if(part == "Part B: Working with Lists and Dictionaries"):
    st.header("Part B: Working with Lists and Dictionaries")

    question = st.selectbox("select a Question",
        options=(
            "Q5. Nested List Access",
            "Q6. Nested Dictionary Access",
            "Q7. Theory Question",
        ))

    if(question == "Q5. Nested List Access"):
        st.subheader("Q5. Nested List Access")

        st.write("**CODE**")
        st.code('''lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]\nprint(f"{lst[3][1][2][0]}")''')

        #Example
        lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
        
        st.write("**OUTPUT**")
        st.write(f"*{lst[3][1][2][0]}*")


    if(question == "Q6. Nested Dictionary Access"):
        st.subheader("Q6. Nested Dictionary Access")

        st.write("**CODE**")
        st.code('''d = { 'k1':[1,2,3,{
        'tricky':['oh','man','inception',{
        'target':[1,2,3,'hello']
        }]\n\t}]\n\t}\nprint(f"{d["k1"][3]["tricky"][3]["target"][3]}")''')
        
        #Example
        d = { 'k1':[1,2,3,{
                'tricky':['oh','man','inception',{
                'target':[1,2,3,'hello']
                }]
            }]
        }
                
        st.write("**OUTPUT**")
        st.write(f"*{d["k1"][3]["tricky"][3]["target"][3]}*")


    if(question == "Q7. Theory Question"):
        st.subheader("Q7. Theory Question")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("## List")

            st.write("**Definition:**")
            st.write("A List is an ordered, mutable collection of items.")

            st.write("**Example:**")
            st.code("""fruits = ["Apple", "Banana", "Mango"]\nfruits.append("Orange")\nprint(fruits)""", language="python")

            st.write("**Output:**")
            st.success("['Apple', 'Banana', 'Mango', 'Orange']")

        with col2:
            st.markdown("## Tuple")

            st.write("**Definition:**")
            st.write("A Tuple is an ordered, immutable collection of items.")

            st.write("**Example:**")
            st.code("""fruits = ("Apple", "Banana", "Mango")\nprint(fruits)""", language="python")

            st.write("**Output:**")
            st.success("('Apple', 'Banana', 'Mango')")

        st.divider()

        st.markdown("### Differences Between List and Tuple")

        st.table({
            "List": [
                "Mutable",
                "Uses []",
                "Elements can be modified",
                "Uses more memory",
                "Suitable for dynamic data"
            ],
            "Tuple": [
                "Immutable",
                "Uses ()",
                "Elements cannot be modified",
                "Uses less memory",
                "Suitable for fixed data"
            ]
        })

if(part == "Part C: User Defined Functions"):
    st.header("Part C: User Defined Functions")

    question = st.selectbox("select a Question",
        options=(
            "Q8. Email Domain Extractor",
            "Q9. Dog Finder",
            "Q10. Dog Counter",
        ))


    if(question == "Q8. Email Domain Extractor"):
        st.subheader("Q8. Email Domain Extractor")

        st.write("**CODE**")
        st.code("""def getEmail(email):\n\twords = email.split("@")\n\treturn words[-1]\nemail = input("Enter email")\nprint(f"Email Domain : {getEmail(email)}")
        """,language="python")

        st.write("**EXAMPLE**")
        def getEmail(email):
            words = email.split("@")
            return words[-1]

        email = st.text_input("Enter email")
        
        st.write("**OUTPUT**")
        st.write(f"*Email domain : {getEmail(email)}*")


    if(question == "Q9. Dog Finder"):
        st.subheader("Q9. Dog Finder")

        st.write("**CODE**")
        st.code("""def findDog(sentence):\n\twords = sentence.lower().split()\n\tif "dog" in words:\n\t   return "True"\n\telse:\n\t   return "False"\nprint(f"{findDog('is there a Dog here?')}")""")

        #Example
        def findDog(sentence):
            words = sentence.lower().split()
            if "dog" in words:
                return "True"
            else:
                return "False"
            
        st.write("**OUTPUT**")
        st.write(f"*{findDog('is there a Dog here?')}*")


    if(question == "Q10. Dog Counter"):
        st.subheader("Q10. Dog Counter")

        st.write("**CODE**")
        st.code("""def countDog(sentence):\n\tcount = sentence.lower().count("dog")\n\treturn count\nprint(f"{countDog('This dog runs faster than the other dog.')}")""")

        #Example
        def countDog(sentence):
            count = sentence.lower().count("dog")
            return count
            
        st.write("**OUTPUT**")
        st.write(f"*{countDog("This dog runs faster than the other dog.")}*")

if(part == "Part D: Conditional Statements"):
    st.header("Part D: Conditional Statements")

    question = st.selectbox("select a Question",
        options=(
            "Q11. Speeding Ticket Calculator",
        ))

    if(question == "Q11. Speeding Ticket Calculator"):
        st.subheader("Q11. Speeding Ticket Calculator")

        st.write("**CODE**")
        st.code('''
    def caught_speeding(speed, is_birthday):
        if is_birthday:
            speed -= 5

        if speed <= 60:
            return "No Ticket"
        elif speed <= 80:
            return "Small Ticket"
        else:
            return "Big Ticket"

    speed = int(input("Enter Speed: "))
    is_birthday = input("Is it Birthday? (True/False): ") == "True"

    print(caught_speeding(speed, is_birthday))
    ''', language="python")

        st.write("**EXAMPLE**")

        speed = st.number_input("Enter Speed:",min_value=0,step=1,value=60)

        is_birthday = st.checkbox("Is it Driver's Birthday?")

        def caught_speeding(speed, is_birthday):
            if is_birthday:
                speed -= 5

            if speed <= 60:
                return "No Ticket"
            elif speed <= 80:
                return "Small Ticket"
            else:
                return "Big Ticket"

        st.write("**OUTPUT**")
        st.success(caught_speeding(speed, is_birthday))

if(part == "Part E: Additional Programming Exercise"):
    st.header("Part E: Additional Programming Exercise")

    question = st.selectbox("select a Question",
        options=(
                "Q12. Menu-Driven Application",
                "Q13. Student Grade Calculator"
        ))

    if(question == "Q12. Menu-Driven Application"):
        st.subheader("Q12. Menu-Driven Application")

        st.write("**CODE**")
        st.code('''
    while True:
        print("\\n1. Extract Email Domain")
        print("2. Find Word 'dog' in Sentence")
        print("3. Count Occurrences of 'dog'")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            email = input("Enter Email: ")
            print("Domain:", email.split("@")[1])

        elif choice == 2:
            sentence = input("Enter Sentence: ")
            if "dog" in sentence.lower():
                print("'dog' found.")
            else:
                print("'dog' not found.")

        elif choice == 3:
            sentence = input("Enter Sentence: ")
            print("Occurrences:", sentence.lower().count("dog"))

        elif choice == 4:
            print("Exiting...")
            break

        else:
            print("Invalid Choice")
    ''', language="python")

        st.write("**EXAMPLE**")

        option = st.selectbox(
            "Select an Option",
            (
                "Extract Email Domain",
                "Find Word 'dog' in Sentence",
                "Count Occurrences of 'dog'"
            )
        )

        if option == "Extract Email Domain":
            email = st.text_input("Enter Email Address")

            st.write("**OUTPUT**")
            if email:
                if "@" in email:
                    st.success(email.split("@")[1])
                else:
                    st.error("Invalid Email Address")

        elif option == "Find Word 'dog' in Sentence":
            sentence = st.text_input("Enter Sentence")

            st.write("**OUTPUT**")
            if sentence:
                if "dog" in sentence.lower():
                    st.success("'dog' found in the sentence.")
                else:
                    st.error("'dog' not found in the sentence.")

        elif option == "Count Occurrences of 'dog'":
            sentence = st.text_input("Enter Sentence ")

            st.write("**OUTPUT**")
            if sentence:
                count = sentence.lower().count("dog")
                st.success(f"Occurrences of 'dog': {count}")
    if(question == "Q13. Student Grade Calculator"):
        st.subheader("Q13. Student Grade Calculator")

        st.write("**CODE**")
        st.code('''
    marks = []

    for i in range(1, 6):
        mark = int(input(f"Enter marks of Subject {i}: "))
        marks.append(mark)

    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "D"

    print("Total =", total)
    print("Percentage =", percentage)
    print("Grade =", grade)
    ''', language="python")

        st.write("**EXAMPLE**")

        m1 = st.number_input("Subject 1 Marks", min_value=0, max_value=100, value=80)
        m2 = st.number_input("Subject 2 Marks", min_value=0, max_value=100, value=80)
        m3 = st.number_input("Subject 3 Marks", min_value=0, max_value=100, value=80)
        m4 = st.number_input("Subject 4 Marks", min_value=0, max_value=100, value=80)
        m5 = st.number_input("Subject 5 Marks", min_value=0, max_value=100, value=80)

        total = m1 + m2 + m3 + m4 + m5
        percentage = total / 5

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        else:
            grade = "D"

        st.write("**OUTPUT**")
        st.success(f"Total Marks : {total}")
        st.success(f"Percentage : {percentage:.2f}%")
        st.success(f"Grade : {grade}")