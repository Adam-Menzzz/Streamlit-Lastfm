import streamlit as st
import pandas as pd
import requests

response = requests.get('')
def time(starttime, endtime):
  total = endtime - starttime
  return total

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [time(9,30), 20, 30, 40]
})

df

