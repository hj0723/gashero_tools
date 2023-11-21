import streamlit as st
from const_gashero_tools import *
from func_gashero_tools import *

st.header('Gas Hero tools :sunglasses:', divider='rainbow')

tab1, tab2 = st.tabs(["Hero Upgrade Cost", "Energy Calculator",])

with tab1:
    st.title('Hero Upgrade Cost')
    hero_cost_start_level = st.number_input('Start Level', step=1, min_value=1, max_value=59)
    hero_cost_target_level = st.number_input('Target Level', step=1, min_value=2, max_value=60)

    st.subheader('Total Cost', divider='violet')
    pu, gmt = get_hero_cost(hero_cost_start_level, hero_cost_target_level)

    col1, col2= st.columns(2)
    col1.metric("Hero Potion", pu)
    col2.metric("GMT", gmt)

with tab2:
#    st.header("A dog")
#    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
    st.title('Energy Calculator')
    base_level = st.number_input('Base Level', step=1, min_value=1, max_value=21)
    col1, col2 = st.columns(2)
    common_hero_amount = col1.number_input('Common Hero Amount:', step=1, min_value=0)
    uncommon_hero_amount = col2.number_input('Uncommon Hero Amount:', step=1, min_value=0)
    col3, col4 = st.columns(2)
    rare_hero_amount = col3.number_input('Rare Hero Amount:', step=1, min_value=0)
    epic_hero_amount = col4.number_input('Epic Hero Amount:', step=1, min_value=0)
    col5, = st.columns(1)
    legendary_hero_amount = col5.number_input('Legendary Hero Amount:', step=1, min_value=0)

    st.subheader('Total Energy', divider='violet')
    total_energy = get_total_energy(base_level, common_hero_amount, uncommon_hero_amount, rare_hero_amount, epic_hero_amount, legendary_hero_amount)    
    st.title(total_energy)
