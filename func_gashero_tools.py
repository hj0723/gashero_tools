import streamlit as st
from const_gashero_tools import *
from re import sub, IGNORECASE

def get_hero_cost(hero_cost_start_level, hero_cost_target_level):
    # (1, 2): {'pu': 1, 'gmt': 0}

    pu = 0
    gmt = 0
    for level, cost in HERO_LEVEL_PU_COST.items():
        level_1 = level[0]
        level_2 = level[1]
        if hero_cost_start_level<=level_1 and hero_cost_target_level>=level_2:
            pu += cost['pu']
            gmt += cost['gmt']

    return pu, gmt

def get_total_energy(base_level, common_hero_amount, uncommon_hero_amount, rare_hero_amount, epic_hero_amount, legendary_hero_amount):
    return 30+(base_level-1)*2 + min(30, 1*common_hero_amount + 2*uncommon_hero_amount + 3*rare_hero_amount + 4*epic_hero_amount + 5*legendary_hero_amount)

def find_heroes(primary_attribute, sex, position, weapon, pet):
    heroes = []
    for hero in hero_db:
        if primary_attribute != 'any' and primary_attribute not in hero['full_skill_str']:
            continue
        if sex != 'both' and sex != hero['sex']:
            continue
        if position != 'any' and position != hero['position']:
            continue
        if weapon != 'any' and weapon not in hero['full_skill_str']:
            continue
        if pet != 'any' and pet not in hero['full_skill_str']:
            continue

        heroes.append(hero)
    
    return heroes

def get_highlighted_skill(skill, primary_attribute, weapon, pet):
    highlighted_skill = skill
    if primary_attribute != 'any':
        highlighted_skill = case_insensitive_replace(highlighted_skill, primary_attribute, f':orange[{primary_attribute}]')
    if weapon != 'any':
        highlighted_skill = case_insensitive_replace(highlighted_skill, weapon, f':green[{weapon}]')
    if pet != 'any':
        highlighted_skill = case_insensitive_replace(highlighted_skill, pet, f':blue[{pet}]')
    return highlighted_skill

def get_display_str(heroes, primary_attribute, sex, weapon, pet):
    body = ''
    for hero in heroes:
        sex_emoji = ':man:'
        if hero['sex'] == 'female':
           sex_emoji = ':woman:'
        body += f"# {hero['codename'].title()} ({hero['position']}) {sex_emoji}\n"
        body += f"![Example Image]({CODENAME_MAP_URL[hero['codename']]})\n"
        for skill in hero['skills']:
            body += f"- {get_highlighted_skill(skill, primary_attribute, weapon, pet)}\n"
    
    return body

def case_insensitive_replace(input_string, search_pattern, replacement):
    return sub(search_pattern, replacement, input_string, flags=IGNORECASE)

def turn_hero_indexes_to_names(hero_indexes):
    names = []
    for i in range(len(hero_indexes)):
        if hero_indexes[i]:
            names.append(HERO_CODENAMES[i])
    
    return names

def update_hero_picked(state, codename):
    if codename in state['hero_picked_in_planner']:
        state['hero_picked_in_planner'].remove(codename)
    else:
        state['hero_picked_in_planner'].append(codename)

def show_picked_heroes():
    hero_picked_in_planner = st.session_state['hero_picked_in_planner']
    
    if hero_picked_in_planner:
        st.subheader('Hero You Picked:')
    while hero_picked_in_planner:
        _hero_picked_in_planner = hero_picked_in_planner[:4]
        hero_picked_in_planner = hero_picked_in_planner[4:]
        _columns = [None]*4    
        _columns[0], _columns[1], _columns[2], _columns[3] = st.columns(4)
        for i in range(len(_hero_picked_in_planner)):
            with _columns[i]:
                st.image(CODENAME_MAP_URL[_hero_picked_in_planner[i]], caption=_hero_picked_in_planner[i])

def hero_picker():
    st.header('Tank Heroes')
    tank_hero_index = [False]*16
    for i in range(4):
        tab4_col1, tab5_col2, tab5_col3, tab5_col4 = st.columns(4)
        with tab4_col1:
            tank_hero_index[i*4] = st.checkbox(f'{TANK_HERO_CODENAMES[i*4]}', on_change=update_hero_picked, args=(st.session_state, TANK_HERO_CODENAMES[i*4]))
            st.image(CODENAME_MAP_URL[TANK_HERO_CODENAMES[i*4]])
        with tab5_col2:
            tank_hero_index[i*4+1] = st.checkbox(f'{TANK_HERO_CODENAMES[i*4+1]}', on_change=update_hero_picked, args=(st.session_state, TANK_HERO_CODENAMES[i*4+1]))
            st.image(CODENAME_MAP_URL[TANK_HERO_CODENAMES[i*4+1]])
        with tab5_col3:
            tank_hero_index[i*4+2] = st.checkbox(f'{TANK_HERO_CODENAMES[i*4+2]}', on_change=update_hero_picked, args=(st.session_state, TANK_HERO_CODENAMES[i*4+2]))
            st.image(CODENAME_MAP_URL[TANK_HERO_CODENAMES[i*4+2]])
        with tab5_col4:
            tank_hero_index[i*4+3] = st.checkbox(f'{TANK_HERO_CODENAMES[i*4+3]}', on_change=update_hero_picked, args=(st.session_state, TANK_HERO_CODENAMES[i*4+3]))
            st.image(CODENAME_MAP_URL[TANK_HERO_CODENAMES[i*4+3]])
    
    st.header('Damage Heroes')
    damage_hero_index = [False]*16
    for i in range(4):
        tab4_col1, tab5_col2, tab5_col3, tab5_col4 = st.columns(4)
        with tab4_col1:
            damage_hero_index[i*4] = st.checkbox(f'{DAMAGE_HERO_CODENAMES[i*4]}', on_change=update_hero_picked, args=(st.session_state, DAMAGE_HERO_CODENAMES[i*4]))
            st.image(CODENAME_MAP_URL[DAMAGE_HERO_CODENAMES[i*4]])
        with tab5_col2:
            damage_hero_index[i*4+1] = st.checkbox(f'{DAMAGE_HERO_CODENAMES[i*4+1]}', on_change=update_hero_picked, args=(st.session_state, DAMAGE_HERO_CODENAMES[i*4+1]))
            st.image(CODENAME_MAP_URL[DAMAGE_HERO_CODENAMES[i*4+1]])
        with tab5_col3:
            damage_hero_index[i*4+2] = st.checkbox(f'{DAMAGE_HERO_CODENAMES[i*4+2]}', on_change=update_hero_picked, args=(st.session_state, DAMAGE_HERO_CODENAMES[i*4+2]))
            st.image(CODENAME_MAP_URL[DAMAGE_HERO_CODENAMES[i*4+2]])
        with tab5_col4:
            damage_hero_index[i*4+3] = st.checkbox(f'{DAMAGE_HERO_CODENAMES[i*4+3]}', on_change=update_hero_picked, args=(st.session_state, DAMAGE_HERO_CODENAMES[i*4+3]))
            st.image(CODENAME_MAP_URL[DAMAGE_HERO_CODENAMES[i*4+3]])
    
    st.header('Support Heroes')
    support_hero_index = [False]*16
    for i in range(4):
        tab4_col1, tab5_col2, tab5_col3, tab5_col4 = st.columns(4)
        with tab4_col1:
            support_hero_index[i*4] = st.checkbox(f'{SUPPORT_HERO_CODENAMES[i*4]}', on_change=update_hero_picked, args=(st.session_state, SUPPORT_HERO_CODENAMES[i*4]))
            st.image(CODENAME_MAP_URL[SUPPORT_HERO_CODENAMES[i*4]])
        with tab5_col2:
            support_hero_index[i*4+1] = st.checkbox(f'{SUPPORT_HERO_CODENAMES[i*4+1]}', on_change=update_hero_picked, args=(st.session_state, SUPPORT_HERO_CODENAMES[i*4+1]))
            st.image(CODENAME_MAP_URL[SUPPORT_HERO_CODENAMES[i*4+1]])
        with tab5_col3:
            support_hero_index[i*4+2] = st.checkbox(f'{SUPPORT_HERO_CODENAMES[i*4+2]}', on_change=update_hero_picked, args=(st.session_state, SUPPORT_HERO_CODENAMES[i*4+2]))
            st.image(CODENAME_MAP_URL[SUPPORT_HERO_CODENAMES[i*4+2]])
        with tab5_col4:
            support_hero_index[i*4+3] = st.checkbox(f'{SUPPORT_HERO_CODENAMES[i*4+3]}', on_change=update_hero_picked, args=(st.session_state, SUPPORT_HERO_CODENAMES[i*4+3]))
            st.image(CODENAME_MAP_URL[SUPPORT_HERO_CODENAMES[i*4+3]])

def count_weapon_keyword(heroes_skill_string):
    heroes_skill_string = heroes_skill_string.lower()
    weapon_counts = {weapon: heroes_skill_string.count(weapon) for weapon in WEAPONS}
    weapon_counts = {weapon:count for weapon, count in weapon_counts.items() if count > 1}
    sorted_weapon_counts = dict(sorted(weapon_counts.items(), key=lambda item: item[1], reverse=True))

    return dict(list(sorted_weapon_counts.items())[:4])

def weapon_plan_result(weapon_counts):
    st.header('Weapon Combo Suggestion')
    _columns = [None]*4    
    weapon_counts_items = list(weapon_counts.items())

    _columns[0], _columns[1], _columns[2], _columns[3] = st.columns(4)
    for i in range(len(weapon_counts_items)):
        weapon, count = weapon_counts_items[i]
        with _columns[i]:
            st.image(WEAPON_MAP_URL[weapon], caption=f'Appear in Skills: {count} times')

def count_pet_keyword(heroes_skill_string):
    heroes_skill_string = heroes_skill_string.lower()
    pet_counts = {pet: heroes_skill_string.count(pet) for pet in PETS}
    pet_counts = {pet:count for pet, count in pet_counts.items() if count > 1}
    sorted_pet_counts = dict(sorted(pet_counts.items(), key=lambda item: item[1], reverse=True))

    return dict(list(sorted_pet_counts.items())[:4])

def pet_plan_result(pet_counts):
    st.header('Pet Combo Suggestion')
    _columns = [None]*4    
    pet_counts_items = list(pet_counts.items())

    _columns[0], _columns[1], _columns[2], _columns[3] = st.columns(4)
    for i in range(len(pet_counts_items)):
        pet, count = pet_counts_items[i]
        with _columns[i]:
            st.image(PET_MAP_URL[pet], caption=f'Appear in Skills: {count} times')

def plan_result():
    # st.header('Hero Combo Suggestion')
    picked_heroes = st.session_state['hero_picked_in_planner']
    heroes_info = [hero for hero in hero_db if hero['codename'] in picked_heroes]
    heroes_skill_string = ' '.join([hero['full_skill_str'] for hero in heroes_info])
    
    weapon_counts = count_weapon_keyword(heroes_skill_string)
    weapon_plan_result(weapon_counts)

    pet_counts = count_pet_keyword(heroes_skill_string)
    pet_plan_result(pet_counts)

def go_to_plan_page():
    st.session_state['go_plan'] = True

def reset_hero_picker():
    st.session_state['hero_picked_in_planner'] = []
    st.session_state['go_plan'] = False
