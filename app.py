import streamlit as st
import pandas as pd

st.title("Hello guys")


data = pd.read_csv('spam.csv', sep=',', encoding='utf-8')


st.dataframe(data.head())
