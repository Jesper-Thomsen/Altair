import pandas as pd
import streamlit as st
import altair as alt



def time_series(df):
    options3 = st.selectbox(
        'What would you like to see',
        (df["Country name"].unique())
    )
    options4 = st.selectbox(
        'What would you like to see',
        (df.columns[3:])
    )
    scatter = alt.Chart(df[df["Country name"]==options3]).mark_point().encode(
        alt.X('year:O',
            scale=alt.Scale(zero=False)
        ),        
        y=options4,
        
        )

    st.write(scatter)