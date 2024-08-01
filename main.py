import streamlit as st
import pandas as pd
st.header("Luke's Cool New App")

grid = []
dim = 3
for i in range(0,3):
    row = {}
    for j in range(0,3):
        row[j] = j
    grid.append(row)



df = pd.DataFrame(
    grid
)

st.table(df)