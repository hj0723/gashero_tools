import streamlit as st
from const_gashero_tools import *
from func_gashero_tools import *

st.header('Cost Calculator :sunglasses:', divider='rainbow')

st.title('Hero Upgrade Cost')

hero_cost_start_level = st.number_input('Start Level', step=1, min_value=1, max_value=59)
hero_cost_target_level = st.number_input('Target Level', step=1, min_value=2, max_value=60)

st.subheader('Total Cost', divider='violet')
pu, gmt = get_hero_cost(hero_cost_start_level, hero_cost_target_level)

col1, col2= st.columns(2)
col1.metric("Hero Potion", pu)
col2.metric("GMT", gmt)
