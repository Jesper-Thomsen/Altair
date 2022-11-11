import streamlit as st
import pandas as pd
import altair as alt
import comparison
import time_series

df=pd.read_csv("data/merged.csv")
df = df.drop(df.columns[0],axis = 1)

sidebar=st.sidebar
sidebar.header("Select data viz")

option = sidebar.selectbox(
    'What would you like to see ',
    ('Static data', 'Time series')
    )

if option == 'Static data':
    st.header("Country statistics and happiness score")
    st.subheader("Full dataframe")
    comparison.show_data(df)

    st.subheader("Compare two countries")
    comparison.compare_countries(df)

    st.subheader("Choose factors for scatterplot")
    comparison.compare_box(df)




if option=='Time series':
    st.header("Time series analysis")
    st.subheader("Dataframe")
    t_df = pd.read_csv("Data/Data2022.csv")
    t_df
    st.subheader("See the development of a country")
    time_series.time_series(t_df)




