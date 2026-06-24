import streamlit as st
import requests

st.title("Weather Intelligence System")

city = st.text_input("Enter City")

if st.button("Get Weather"):

    response = requests.get(
        f"http://127.0.0.1:8000/temperature/{city}"
    )

    data = response.json()

    st.success(
        f"Temperature: {data['temperature']}°C"
    )