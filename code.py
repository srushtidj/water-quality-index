import streamlit as st
import pandas as pd
import plotly.express as px


st.write('# Water Quality dashboard')
st.markdown(''' This is a dashboard showing the water quality of the given sample.''')

temp_input = st.number_input("Temperature (in degree celcius)", step=0.5)
pH_input = st.number_input("pH", step=0.5)
sal_input = st.number_input("Salinity (dS/m)", step=0.5)
nitro_input = st.number_input("Nitrogen content (mg/L)", step=0.5)
ars_input = st.number_input("Arsenic content (mg/L)", step=0.5)

wqi = int(temp_input+pH_input+sal_input+nitro_input+ars_input)/5

st.header(f'WQI: {wqi}')