import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import smtplib
from email.message import EmailMessage

st.set_page_config(page_title="Email & Excel Report Bot", layout="wide")
st.title("Email & Excel Report Automation Bot")

uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    df['qty'] = pd.to_numeric(df['qty'], errors='coerce').fillna(0)
    df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0)
    df['revenue'] = df['qty'] * df['price']
    total_revenue = df['revenue'].sum()
    st.metric("Total Revenue", f"{total_revenue:,.2f}")

    revenue_by_product = df.groupby('product_name')['revenue'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots()
    revenue_by_product.plot(kind='bar', ax=ax)
    st.pyplot(fig)
