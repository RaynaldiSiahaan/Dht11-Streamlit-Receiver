import streamlit as st
import requests

st.set_page_config(page_title="Environment Monitor", layout="centered")

st.title("🌡️ Smart Environment Monitor")

# Input IP or URL of the Pico
device_url = st.text_input("Enter the IP or URL of the device", "http://192.168.4.1")

# Refresh button
if st.button("🔄 REFRESH"):
    try:
        response = requests.get(device_url, timeout=3)
        if response.status_code == 200:
            data = response.json()
            st.success("Data received successfully!")
            st.metric("Temperature (°C)", f"{data['temperature']}°C")
            st.metric("Humidity (%)", f"{data['humidity']}%")
        else:
            st.error(f"Failed to fetch data. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error connecting to device: {e}")
