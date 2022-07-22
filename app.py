import streamlit as st

st.write("""
# Multiplication of 2 numbers TDS GA-8 21f1000957

This app returns the product of two numbers
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():

    Number1 = st.number_input("NUMBER_1",min_value=-10**(100),max_value=10**(100))
    Number2 = st.number_input("NUMBER_2",min_value=-10**(100),max_value=10**(100))


    data = {'NUMBER_1': Number1,
            'NUMBER_2': Number2
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())

result=Number1*Number2
st.write('result')
