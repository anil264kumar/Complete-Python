import streamlit as st
import pandas as pd


st.title("Streamlit Text Input")

name=st.text_input("Enter your name",key="name")

st.session_state.name
# slider

age=st.slider("Select your age:",0,100,25)
print("Your age is ",age)



options = ["Python","Java","C++","JavaScript"]
choice = st.selectbox("Choose your favourite lang:",options)
st.write(f"You seleced {choice}.")

if name:
    st.write(f"Hello, {name}")



data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampleData.csv")
st.write(df)


uploaded_file=st.file_uploader("Choode a CSV file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email','Home phone','Mobile phone')
)




