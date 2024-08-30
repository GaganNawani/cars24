import yfinance as yf
import streamlit as st
import pandas as pd
import numpy as np
import datetime


st.header('Stock Analysis App')

stock = st.text_input('INPUT THE NAME OF THE STOCK','MSFT')
data = yf.Ticker(stock)

col1, col2 = st.columns(2)

st.write('Currently Analysing: ', stock)

with col1:
    start_date = st.date_input("Enter Start Date", datetime.date(2024, 1, 1))

with col2:
    end_date = st.date_input("Enter End Date", datetime.date(2024, 1, 31))

hist = data.history(period="1d", start = start_date, end = end_date)

st.write(hist)

st.subheader('Trend in closing prices')
st.line_chart(hist['Close'])

st.subheader('Trend in Volumes')
st.bar_chart(hist['Volume'])




