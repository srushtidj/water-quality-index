import streamlit as st
import pandas as pd
import plotly.express as px


st.write('## Water Quality dashboard')
# st.markdown(''' This is a dashboard showing the water quality of the given sample.''')

temp = st.number_input("Temperature (°C)", step=0.5)
pH = st.number_input("pH", step=0.5)
bod = st.number_input("Biochemical Oxygen Demand (mg/L)", step=0.5)
cod= st.number_input("Chemical Oxygen Demand (mg/L)", step=0.5)
tss = st.number_input("Total Suspended Solids (mg/L)", step=0.5)
fc = st.number_input("Fecal Coliform (MPN/100 ml)", step=0.5)

# nit_input = st.number_input("Nitrate (mg/L)", step=0.5)

# temp = abs(temp_input-26.0125)
# pH = abs(pH_input-7.3125)
# bod = abs(bod_input-9)
# cod = abs(cod_input-1231.25)
# tss = abs(tss_input-4.175)
# fc = abs(fc_input)


# sub_temp = abs(100- (temp*100/(30-20)))
# sub_pH = abs(100 - (pH*100/(8.5-6.5)))
# sub_bod = abs(100 - (bod*100/14))
# sub_cod = abs(100 - (cod*100/(2000-700)))
# sub_tss = abs(100 - (tss*100/10))
# sub_fc = abs()

w_temp = 0.226
w_pH = 0.156
w_bod = 0.097
w_cod = 0.275
w_tss = 0.087
w_fc = 0.157


wqi = ((temp**w_temp)*(pH**w_pH)*(bod**w_bod)*(cod**w_cod)*(tss**w_tss)*(fc**w_fc))
wqi = round(wqi,2)

if wqi!=0:
    st.header(f'WQI: {wqi}')

    if wqi>=0 and wqi<20:
        st.markdown('Water Quality Status: Heavily Polluted')
    elif wqi>=20 and wqi<40:
        st.markdown('Water Quality Status: Poor')
    elif wqi>=40 and wqi<80:
        st.markdown('Water Quality Status: Fair')
    elif wqi>=80 and wqi<100:
        st.markdown('Water Quality Status: Good')
    elif wqi == 100:
        st.markdown('Water Quality Status: Excellent')
