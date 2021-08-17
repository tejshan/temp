import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px



df = pd.read_csv('airline-passenger-traffic.csv')

input_date = st.sidebar.selectbox('Select Date Column',df.columns.tolist() )
input_pred = st.sidebar.selectbox('Select Prediction Column',df.columns.tolist())
input_pred = st.sidebar.selectbox('Select Data Level',['Monthly','Weekly','Quarterly','Yearly','Daily'])
input_pred = st.sidebar.selectbox('Select aggregation function',['sum','average'])
input_pred = st.sidebar.selectbox('Select Seasonality',[1,4,7,12,30,52,365])


ff = st.sidebar.radio('Select an option',['Overview','Personas','Advanced Analytics','Tech Specs'])

    

if ff == 'Overview':
    st.title('Overview')
    fig = px.line(df, x='Month', y='Passengers',color_discrete_sequence=['blue'],title='Distribution of Passenegers')
    st.plotly_chart(fig)
    st.header('Data Overview')
    st.table(df.head())

if ff == 'Personas':
    st.title('Personas')
    val = st.number_input('Select Forecast Period',min_value = 1,max_value = 100,   value = 10)
    temp = df.copy()
    temp.rename(columns = {'Passengers':'Passenegers Forecasted'},inplace=True)
    st.table(temp.tail(val))
    plotly_df = temp.copy()
    st.header('Forecast Plot')
    fig1 = px.line(plotly_df.iloc[-val:], x='Month', y='Passenegers Forecasted')
    st.plotly_chart(fig1)

if ff == 'Advanced Analytics':
    st.title('Advanced Analytics')
    st.header('Actual Vs Predicted')
    st.image('11.jpeg')
    st.header('Eror Histogram')
    st.image('hist.png')

if ff == 'Tech Specs':
    st.title('Tech Specs')
    st.image('12.jpeg')
    st.header('Algorithm Performance Summary')
    st.image('13.jpeg')

 