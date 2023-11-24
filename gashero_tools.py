import streamlit as st
from const_gashero_tools import *
from func_gashero_tools import *

st.set_page_config(
    page_title="Gas Hero tools",
    page_icon="https://framerusercontent.com/images/wMXHA9cBuudtI8kf36EHXH329rA.svg",
)

if 'hero_picked_in_planner' not in st.session_state:
    st.session_state['hero_picked_in_planner'] = []
if 'go_plan' not in st.session_state:
    st.session_state['go_plan'] = False


st.header('Gas Hero tools :sunglasses:', divider='rainbow')
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Hero Upgrade Cost", "Energy Calculator", "Hero Finder", "Hero Planner","Just a Cute Doggy"])

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
    st.title('Hero Finder')
    primary_attribute = st.selectbox(
        'Primary Attribute in hero Skills',
        ('any', 'attack', 'defense', 'hp', 'mp', 'speed')
    )
    sex = st.selectbox(
        'Hero Gender',
        ('both', 'male', 'female',)
    )
    position = st.selectbox(
        'Hero Position',
        ('any', 'tank', 'damage', 'support',)
    )
    weapon = st.selectbox(
        'Hero Weapon',
        ('any', 'dagger', 'sword', 'axe', 'hammer', 'bow', 'gun', 'staff', 'book',)
    )
    pet = st.selectbox(
        'Hero Pet',
        ('any', 'dragon', 'treant', 'crab', 'panda',)
    )

    st.subheader('Match Heroes', divider='violet')
    heroes = find_heroes(primary_attribute, sex, position, weapon, pet)
    body = get_display_str(heroes, primary_attribute, sex, weapon, pet)
    st.markdown(body, unsafe_allow_html=True)

with tab4:
    st.title('Hero Planner')

    show_picked_heroes()
    
    if st.session_state['go_plan']:
        st.button("Click To pick hero again!", on_click=reset_hero_picker)
    else:
        st.button("Click To get your Hero Plan!", on_click=go_to_plan_page, disabled=not is_picked_heroes())


    if st.session_state['go_plan']:
        plan_result()
    else:
        hero_picker()
    

    # st.session_state['hero_picked_in_planner'] = turn_hero_indexes_to_names(tank_hero_index+damage_hero_index+support_hero_index)

with tab5:
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

   st.markdown('''
    If you want to thank me, feel free to donate to animal rescue group to be a hero!
    
    This is the best way to thank me! :rose:''')
   
