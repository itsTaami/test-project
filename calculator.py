"""Basic Calculator Application - Streamlit Version"""

import streamlit as st


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


st.title("Basic Calculator")

col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("First number", value=0.0)

with col2:
    num2 = st.number_input("Second number", value=0.0)

operation = st.selectbox(
    "Select operation",
    ["Add", "Subtract", "Multiply", "Divide"]
)

if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
        st.success(f"{num1} + {num2} = {result}")
    elif operation == "Subtract":
        result = subtract(num1, num2)
        st.success(f"{num1} - {num2} = {result}")
    elif operation == "Multiply":
        result = multiply(num1, num2)
        st.success(f"{num1} * {num2} = {result}")
    elif operation == "Divide":
        result = divide(num1, num2)
        if isinstance(result, str):
            st.error(result)
        else:
            st.success(f"{num1} / {num2} = {result}")
