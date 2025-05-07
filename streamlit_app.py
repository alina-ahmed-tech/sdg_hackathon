import streamlit as st
import requests

st.title("🌿 Green AI Coach")

code = st.text_area("Paste your training code here")
gpu  = st.text_input("GPU model", "Apple M1")
cpu  = st.text_input("CPU model", "8-core")

if st.button("Get eco-tips"):
    payload = {"code": code, "hardware": {"GPU": gpu, "CPU": cpu}}
    resp = requests.post("http://localhost:8001/recommend", json=payload)
    if resp.ok:
        st.markdown("**Recommendations:**")
        st.write(resp.json()["recommendations"])
    else:
        st.error(f"Error {resp.status_code}: {resp.text}")
