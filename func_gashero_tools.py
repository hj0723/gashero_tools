import streamlit as st
from const_gashero_tools import *
from re import sub, IGNORECASE

def init_state():
    if 'hero_picked_in_planner' not in st.session_state:
        st.session_state['hero_picked_in_planner'] = []
    if 'go_plan' not in st.session_state:
        st.session_state['go_plan'] = False
    if 'hero_state_for_strength' not in st.session_state:
        st.session_state['hero_state_for_strength'] = []
        for i in range(6):
            st.session_state['hero_state_for_strength'].append({
                'hero_rarity': 0,
                'hero_skill_amount': 0,
                'hero_is_max_level': 0,
                'pet_rarity': 0,
                'pet_tier': 0,
                'weapon_rarity': 0,
                'weapon_attributes': 0,
            })

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
    else:
        st.subheader('Pick hero before click button')

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

def is_picked_heroes():
    return len(st.session_state['hero_picked_in_planner']) > 0

def strength_calculator():
    st.title('Strength Calculator')
    hero_infos = [{} for _ in range(6)]
    _columns = [None]*18

    base_level_strength = st.number_input('Base Level', min_value=1, max_value=21, step=1, key='strength_base_level')
    skill_tree_level_strength = st.number_input('Skill Tree Level', min_value=0, step=1)
    total_erergy_strength = st.number_input('Total Energy', min_value=30, max_value=100, step=1)
    st.divider()

    for i in range(6):
        _columns[3*i+0], _columns[3*i+1], _columns[3*i+2] = st.columns(3)

    for row in range(6):
        hero_number = row
        hero_state_for_strength = st.session_state['hero_state_for_strength'][hero_number]
        with _columns[3*row+0]:
            st.subheader(f'Hero {hero_number+1}')
            hero_infos[hero_number]['hero_rarity'] = st.selectbox('Hero rarity', RARITIES, key=f'hero_rarity_{hero_number}')
            hero_infos[hero_number]['hero_skill_amount'] = st.selectbox('Skills amount', SKILLS_AMOUNT, key=f'hero_skills_amount_{hero_number}')
            hero_infos[hero_number]['hero_is_max_level'] = st.selectbox('Is hero Max level?', IS_HERO_MAX, key=f'is_hero_max_{hero_number}')
        with _columns[3*row+1]:
            st.subheader(f'Pet {hero_number+1}')
            hero_infos[hero_number]['pet_rarity'] = st.selectbox('Pet rarity', RARITIES, key=f'pet_rarity_{hero_number}')
            hero_infos[hero_number]['pet_tier'] = st.selectbox('Pet Tier', PET_TIER, key=f'pet_tier{hero_number}')
            st.button(f'reset hero {hero_number+1}', use_container_width=True, key=f'reset_button_{hero_number}', on_click=reset_hero_for_strength_calculator, args=(hero_number,))
        with _columns[3*row+2]:
            st.subheader(f'Weapon {hero_number+1}')
            hero_infos[hero_number]['weapon_rarity'] = st.selectbox('Weapon rarity', RARITIES, key=f'weapon_rarity_{hero_number}')
            hero_infos[hero_number]['weapon_attributes'] = st.selectbox('Weapon attributes', WEAPON_ATTRIBUTES, key=f'weapon_attributes_{hero_number}')
            st.button(f'Apply hero {hero_number+1} setup to other', use_container_width=True, key=f'apply_to_other_button_{hero_number}', on_click=apply_to_other_hero_forstrength_calculator, args=(hero_number,))

    st.divider()
    strength = get_strength(hero_infos, base_level_strength, skill_tree_level_strength, total_erergy_strength)
    st.title('Strength')
    st.header(strength)

def get_strength(hero_infos, base_level_strength, skill_tree_level_strength, total_erergy_strength):
    strength = 0
    for hero_info in hero_infos:
        if hero_info['hero_is_max_level']:
            strength += HERO_RARITIES_MAP_SCORE[hero_info['hero_rarity']]*2
        strength += int(hero_info['hero_skill_amount'])
        
        strength += WEAPON_RARITIES_MAP_SCORE[hero_info['weapon_rarity']]
        strength += int(hero_info['weapon_attributes'])

        strength += PET_RARITIES_MAP_SCORE[hero_info['pet_rarity']]
        strength += int(hero_info['pet_tier'])

    strength += (int(base_level_strength)-1)*2
    strength += int(skill_tree_level_strength)
    strength += int(total_erergy_strength)-30

    return strength

def set_css():
    with open('style.css', 'r') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True) 
            
def reset_hero_for_strength_calculator(hero_number):
    st.session_state[f'hero_rarity_{hero_number}'] = RARITIES[0]
    st.session_state[f'hero_skills_amount_{hero_number}'] = SKILLS_AMOUNT[0]
    st.session_state[f'is_hero_max_{hero_number}'] = IS_HERO_MAX[0]

    st.session_state[f'pet_rarity_{hero_number}'] = RARITIES[0]
    st.session_state[f'pet_tier{hero_number}'] = PET_TIER[0]

    st.session_state[f'weapon_rarity_{hero_number}'] = RARITIES[0]
    st.session_state[f'weapon_attributes_{hero_number}'] = WEAPON_ATTRIBUTES[0]

def apply_to_other_hero_forstrength_calculator(hero_number):
    apply_to_hero_numbers = list(range(6))
    apply_to_hero_numbers.remove(hero_number)
    for apply_to_hero_number in apply_to_hero_numbers:
        st.session_state[f'hero_rarity_{apply_to_hero_number}'] = st.session_state[f'hero_rarity_{hero_number}']
        st.session_state[f'hero_skills_amount_{apply_to_hero_number}'] = st.session_state[f'hero_skills_amount_{hero_number}']
        st.session_state[f'is_hero_max_{apply_to_hero_number}'] = st.session_state[f'is_hero_max_{hero_number}']

        st.session_state[f'pet_rarity_{apply_to_hero_number}'] = st.session_state[f'pet_rarity_{hero_number}']
        st.session_state[f'pet_tier{apply_to_hero_number}'] = st.session_state[f'pet_tier{hero_number}']

        st.session_state[f'weapon_rarity_{apply_to_hero_number}'] = st.session_state[f'weapon_rarity_{hero_number}']
        st.session_state[f'weapon_attributes_{apply_to_hero_number}'] = st.session_state[f'weapon_attributes_{hero_number}']
