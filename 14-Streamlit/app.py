import streamlit as st
import pandas as pd
import numpy as np
import time

## Title of the application
st.title("Hello streamlit")


## Display a simple text
st.write("This is a imple text")

## create a simple Dataframe

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column':[10,20,30,40]
    })

## display dataframe
st.write("Here is the dataframe")
st.write(df)

## create a line chart

chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)

st.line_chart(chart_data)



latest_iteration=st.empty()
bar = st.progress(0)


for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)

'...and'
