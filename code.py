import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown('# WATER QUALITY DASHBOARD')
st.markdown(''' This is a dashboard showing the water quality of the given sample based on the following parameters.''')


# INPUT VALUES
temp_in = st.number_input("Temperature (°C)", step=0.5)
pH_in = st.number_input("pH", step=0.5)
bod_in = st.number_input("Biochemical Oxygen Demand (mg/L)", step=0.5)
cod_in= st.number_input("Chemical Oxygen Demand (mg/L)", step=0.5)
tss_in = st.number_input("Total Suspended Solids (mg/L)", step=0.5)
fc_in = st.number_input("Fecal Coliform (MPN/100 ml)", step=0.5)


# SUB-INDEX CALCULATION:

## Temperature:
if temp_in>=0 and temp_in<=25:
    temp = abs(((((1-0.6)*(temp_in - 18))/(25-18))+0.6)*100)
else:
    temp = abs((((-0.44)*(temp_in -25)/9) + 0.49)*100)

## pH:
ph = abs(((0.2*(pH_in - 7.5)/1.5)+0.8)*100)

## BOD:
bod = abs(((0.2*(bod_in - 5)/5)+0.8)*100)

## COD:
cod = abs(((0.2*(cod_in - 20)/30)+0.8)*100)

## TSS:
if tss_in>=0 and tss_in<=10:
    tss = abs(((0.4*(tss_in - 3)/7)+0.6)*100)
else:
    tss = abs(((-0.44)*(tss_in - 10)/9)*100)

## Fecal Coliform:
fc = abs((((-0.44)*(fc_in - 230)/530)+0.49)*100)


# WEIGHTAGE OF EACH PARAMETER:
w_temp = 0.237710643
w_pH = 0.164377828
w_bod = 0.102280499
w_cod = 0.290074603
w_tss = 0.091850428
w_fc = 0.113705998


wqi = ((temp**w_temp)*(ph**w_pH)*(bod**w_bod)*(cod**w_cod)*(tss**w_tss)*(fc**w_fc))
wqi = round(wqi,2)

# CLASSIFY BASED ON WQI:

if wqi!=0:
    st.header(f'WQI: {wqi}')

    if wqi>=0 and wqi<20:
        st.header('Water Quality Status: Heavily Polluted')
    elif wqi>=20 and wqi<40:
        st.header('Water Quality Status: Poor')
    elif wqi>=40 and wqi<60:
        st.header('Water Quality Status: Fair')
    elif wqi>=60 and wqi<80:
        st.header('Water Quality Status: Good')
    elif wqi>=80 and wqi<100:
        st.header('Water Quality Status: Excellent')
