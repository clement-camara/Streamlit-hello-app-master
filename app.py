import streamlit as st
import pandas as pd

st.title("Hello guys")


data = pd.read_csv('spam.csv', sep=',', skip_blank_lines=True, a_filter=True)


st.dataframe(data.head())
