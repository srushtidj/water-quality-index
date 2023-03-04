import streamlit as st
import pandas as pd
import plotly.express as px


st.write('# Water Quality dashboard')
st.markdown(''' This is a dashboard showing the water quality of the given sample.''')

temp_input = st.number_input("Temperature (°C)", step=0.5)
pH_input = st.number_input("pH", step=0.5)
do_input = st.number_input("Dissolved Oxygen (mg/L)", step=0.5)
tss_input = st.number_input("Total Suspended Solids (mg/L)", step=0.5)
cond_input = st.number_input("Conductivity (mg/L)", step=0.5)
nit_input = st.number_input("Nitrate (µS/L)", step=0.5)

wqi = int(temp_input+pH_input+tss_input+cond_input+nit_input)/6

st.header(f'WQI-water quality index: {wqi}')