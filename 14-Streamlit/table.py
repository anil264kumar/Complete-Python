import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello Streamlit")

df = pd.DataFrame(
    np.random.randn(10,20),
    columns=('col %d' % i for i in range(20))
)


st.dataframe(df.style.highlight_min(axis=0))

