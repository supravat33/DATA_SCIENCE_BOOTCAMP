import streamlit as st

def calculate(num1, num2, operation):
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtract":
        return num1 - num2
    elif operation == "Multiply":
        return num1 * num2
    elif operation == "Divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Invalid operation"

def main():
    st.title("Simple Calculator")

    num1 = st.number_input("Enter first number", value=0.0, format="%.2f")
    num2 = st.number_input("Enter second number", value=0.0, format="%.2f")
    operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

    if st.button("Calculate"):
        result = calculate(num1, num2, operation)
        st.success(f"Result: {result}")

if __name__ == "__main__":
    main()