import streamlit as st
import yfinance as yf
import datetime
st.title("Stock Price Analyzer")
stock_name=st.text_input("which stock do you want to analyze?","MSFT")
ticker_data=yf.Ticker(stock_name)
start_date=st.date_input("please enter starting date",datetime.date(2023,12,1))
end_date=st.date_input("please enter ending date",datetime.date(2024,12,1))
ticker_df=ticker_data.history(period='1d',start=start_date,end=end_date)

st.subheader("This is raw stock price")
st.dataframe(ticker_df.head())
st.subheader("Price moment over time")
st.line_chart(ticker_df['Close'])
st.subheader("Volume moment over time")
st.line_chart(ticker_df['Volume'])
