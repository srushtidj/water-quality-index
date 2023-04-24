import streamlit as st
import pandas as pd
import plotly.express as px


st.write('# Water Quality dashboard')
st.markdown(''' This is a dashboard showing the water quality of the given sample.''')

temp_input = st.number_input("Temperature (°C)", step=0.5)
pH_input = st.number_input("pH", step=0.5)
bod_input = st.number_input("Biochemical Oxygen Demand (mg/L)", step=0.5)
cod_input = st.number_input("Chemical Oxygen Demand (mg/L)", step=0.5)
tss_input = st.number_input("Total Suspended Solids (mg/L)", step=0.5)
fc_input = st.number_input("Fecal Coliform (MPN/100 ml)", step=0.5)
# nit_input = st.number_input("Nitrate (mg/L)", step=0.5)

temp = abs(temp_input-26.0125)
pH = abs(pH_input-7.3125)
bod = abs(bod_input-9)
cod = abs(cod_input-1231.25)
tss = abs(tss_input-4.175)
fc = abs(fc_input)


sub_temp = abs(100- (temp*100/(30-20)))
sub_pH = abs(100 - (pH*100/(8.5-6.5)))
sub_bod = abs(100 - (bod*100/14))
sub_cod = abs(100 - (cod*100/(2000-700)))
sub_tss = abs(100 - (tss*100/10))
# sub_fc = abs()

w_temp = 0.055
w_pH = 0.358
w_bod = 0.068
w_cod = 0.295
w_tss = 0.224
# w_fc = 

if temp_input==pH_input==bod_input==cod_input==tss_input == 0:
    wqi = 0
else:
    wqi = ((sub_temp**w_temp)*(sub_pH**w_pH)*(sub_bod**w_bod)*(sub_cod**w_cod)*(sub_tss**w_tss))
    wqi = round(wqi,2)

st.header(f'WQI-water quality index: {wqi}')
