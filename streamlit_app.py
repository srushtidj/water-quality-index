import streamlit as st
import pandas as pd
import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
from PIL import Image

# page setting
st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# data
water_quality = pd.read_csv("original_data.csv")

# row A
a1, a2, a3 = st.columns(3)
a1.metric("Temperature", "30 deg celcius")
# idea: we can also show whether the value of the parameter has changed or not, and by how much.
a2.metric("pH", "7.2")
a3.metric("Salinity", "0.6 dS/m")
# ds = deciSiemens

# row B
b1, b2 = st.columns(2)
b1.metric("Nitrogen", "10 mg/L")
b2.metric("Arsenic", "1.2 ml/L")

wqi = (30+7.2+0.6+10+1.2)/5

# row C
c2 = st.columns({7,3})
# with c1:
#     fig, ax = plt.subplots()
#     sns.heatmap(water_quality.corr(), ax=ax)
#     st.write(fig)
    
c2.metric("WQI", wqi)
