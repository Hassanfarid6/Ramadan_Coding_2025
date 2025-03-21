import streamlit as st


def main():

    st.title("Simple Calculator")
    st.write("Enter two numbers and choose an operation")

    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("Enter First Number")

    with col2:
        num2 = st.number_input("Enter Second Number")

    operation = st.selectbox(
        "Select Operation", ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"]
                            )

    if st.button("Calculate"):
        try:
            if operation == "Addition (+)":
                result = num1 + num2
                symbol = "+"
            elif operation == "Subtraction (-)":
                result = num1 - num2
                symbol = "-"
            elif operation == "Multiplication (*)":
                result = num1 * num2
                symbol = "x"
            else:
                if num2 == 0:
                    st.error("Cannot divide by zero")
                    return
                
                result = num1 / num2
                symbol = "/"

            st.success(f"The result of {num1} {symbol} {num2} is {result}")

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
