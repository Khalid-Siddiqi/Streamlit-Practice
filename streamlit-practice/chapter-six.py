import streamlit as st
import requests

st.title("Currency Exchange project")

target_currency = st.selectbox("Select target currency", ["PKR", "EUR", "GBP", "JPY", "AUD"])
amount = st.number_input("Enter amount in USD", min_value=1)

if st.button("Convert"):
    response = requests.get(f"https://v6.exchangerate-api.com/v6/a17ba7b88919aa4544be8da9/latest/USD")
    data = response.json()
    exchange_rate = data["conversion_rates"].get(target_currency)
    if response.status_code == 200:
        converted_amount = amount * exchange_rate
        st.write(f"{amount} USD is equal to {converted_amount:.2f} {target_currency}.")
    else:
        st.error("Currency not supported.")