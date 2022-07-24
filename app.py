import streamlit as st

st.write("""
# TDS GA-8 21f1000957

Multiplication of 2 numbers
""")
#Get Input
#st.title('Odd-Even Finder')
x = st.number_input('Enter Number1')
y = st.number_input('Enter Number2')
prod=x*y
st.write('The product of the two numbers is ',prod)

