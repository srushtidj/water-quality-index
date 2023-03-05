import streamlit as st
import pandas as pd
import plotly.express as px


st.write('# Water Quality dashboard')
st.markdown(''' This is a dashboard showing the water quality of the given sample.''')

temp_input = st.number_input("Temperature (°C)", step=0.5)
pH_input = st.number_input("pH", step=0.5)
do_input = st.number_input("Dissolved Oxygen (mg/L)", step=0.5)
# tss_input = st.number_input("Total Suspended Solids (mg/L)", step=0.5)
cond_input = st.number_input("Conductivity (µS/cm)", step=0.5)
nit_input = st.number_input("Nitrate (mg/L)", step=0.5)

t = abs(temp_input-26.0125)
p = abs(pH_input-7.3125)
d = abs(do_input-9)
c = abs(cond_input-1231.25)
n = abs(nit_input-4.175)

sub_temp = abs(100- (t*100/(30-20)))
sub_pH = abs(100 - (p*100/(8.5-6.5)))
sub_do = abs(100 - (d*100/14))
sub_cond = abs(100 - (c*100/(2000-700)))
sub_nit = abs(100 - (n*100/10))

wt = 0.055
wp = 0.358
wd = 0.068
wc = 0.295
wn = 0.224

if temp_input==pH_input==do_input==cond_input==nit_input == 0:
    wqi = 0
else:
    wqi = ((sub_temp**wt)*(sub_pH**wp)*(sub_do**wd)*(sub_cond**wc)*(sub_nit**wn))
    wqi = round(wqi,2)

st.header(f'WQI-water quality index: {wqi}')
