import streamlit as st
from const_gashero_tools import *
from func_gashero_tools import *

st.set_page_config(
    page_title="Gas Hero tools",
    page_icon="https://framerusercontent.com/images/wMXHA9cBuudtI8kf36EHXH329rA.svg",
)


st.header('Gas Hero tools :sunglasses:', divider='rainbow')
tab1, tab2, tab3 = st.tabs(["Hero Upgrade Cost", "Energy Calculator", "Just a Cute Doggy"])

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

with tab3:
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

   st.markdown('''
    If you want to thank me, feel free to donate to animal rescue group to be a hero!
    
    This is the best way to thank me! :rose:''')