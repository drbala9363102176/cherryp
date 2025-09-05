# streamlit_addition.py

import streamlit as st

# Input values
a = 10
b = 20

# Addition
result = a + b

# Streamlit app
st.title("Addition App")
st.write(f"The sum of {a} and {b} is: {result}")
