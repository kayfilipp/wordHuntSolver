import streamlit as st
import pandas as pd
st.header("Luke's Cool New App")

grid = []
for i in range(0,4):
    row = {}
    for j in range(0,4):
        row[j] = j
    grid.append(row)



df = pd.DataFrame(
    grid
)

st.table(df)