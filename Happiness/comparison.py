#This goes to the Comparison site where you can compare two countries

import streamlit as st
import altair as alt
import pandas as pd

#Displays the data

def show_data(dataframe):
    st.write(dataframe)

def compare_countries(dataframe):
    option1 = st.selectbox(
        'Select country',
    (dataframe["Country"])
    )
    option2 = st.selectbox(
        'select country to compare with',
    (dataframe["Country"])
    )
    st.write(dataframe[dataframe['Country'].isin([option1, option2])])



#Makes altair plot that allows several different scatter plots with an interactive select box and a descriptive bar chart
def compare_box(dataframe):
    df=dataframe
    factors=df.columns[13:]
    select_factor =st.selectbox(
            "Select the factor for comparison",
            factors
            )

    select_factor3 =st.selectbox(
                "Select the factor for comparison",
                factors,
                key="sdfdsf"
                )
    select_factor=select_factor+":Q"
    multi = alt.selection_multi(fields=['Happiness score'])
    interval = alt.selection_interval()
    scatter = alt.Chart(df).mark_point().encode(
        x=select_factor,
        y=select_factor3,
        color=alt.condition(multi, 'Happiness score', alt.value('lightgray'), sort="ascending"),
        tooltip='Country',
    ).properties(
        selection=interval
    )

    bar = alt.Chart(df).mark_bar().encode(
        y='Country',
        x='Happiness score:Q',
        color=alt.condition(multi, 'Happiness score', alt.value('lightgray'))
    ).properties(
        selection=multi
    ).transform_filter(
        interval
    )

    st.write(scatter & bar)