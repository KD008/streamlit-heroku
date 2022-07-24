import streamlit as st

st.write("""
# Multiplication of 2 numbers TDS GA-8 21f1000957

This app returns the product of two numbers
""")
#Get Input
#st.title('Odd-Even Finder')
x = st.number_input('Enter Number1')
y = st.number_input('Enter Number2')
prod=x*y
st.write('The product of the two numbers is ',prod)

