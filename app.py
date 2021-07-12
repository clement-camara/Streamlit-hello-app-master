import streamlit as st
import pandas as pd

st.title("Hello guys")


data = pd.read_csv('spam.csv', sep=',')


st.dataframe(data.head())
