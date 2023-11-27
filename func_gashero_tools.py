import streamlit as st
from const_gashero_tools import *
from re import sub, IGNORECASE
from pandas import DataFrame

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
    return min(100, 30+(base_level-1)*2 + 1*common_hero_amount + 2*uncommon_hero_amount + 3*rare_hero_amount + 4*epic_hero_amount + 5*legendary_hero_amount)

def find_heroes(primary_attribute, special_ability, sex, position, weapon, pet):
    heroes = []
    for hero in hero_db:
        if primary_attribute != 'any' and primary_attribute not in hero['full_skill_str']:
            continue
        if special_ability != 'any' and special_ability not in hero['full_skill_str']:
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

def get_highlighted_skill(skill, primary_attribute, special_ability, weapon, pet):
    highlighted_skill = skill
    if primary_attribute != 'any':
        highlighted_skill = case_insensitive_replace(highlighted_skill, primary_attribute, f':orange[{primary_attribute}]')
    if special_ability != 'any':
        highlighted_skill = case_insensitive_replace(highlighted_skill, special_ability, f':rainbow[{special_ability}]')
    if weapon != 'any':
        highlighted_skill = case_insensitive_replace(highlighted_skill, weapon, f':green[{weapon}]')
    if pet != 'any':
        highlighted_skill = case_insensitive_replace(highlighted_skill, pet, f':blue[{pet}]')
    return highlighted_skill

def get_display_str(heroes, primary_attribute, special_ability, sex, weapon, pet):
    body = ''
    for hero in heroes:
        sex_emoji = ':man:'
        if hero['sex'] == 'female':
           sex_emoji = ':woman:'
        body += f"# {hero['codename'].title()} ({hero['position']}) {sex_emoji}\n"
        body += f"![Example Image]({CODENAME_MAP_URL[hero['codename']]})\n"
        for skill in hero['skills']:
            body += f"- {get_highlighted_skill(skill, primary_attribute, special_ability, weapon, pet)}\n"
    
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
        if hero_info['hero_rarity'] != 'None':
            if hero_info['hero_is_max_level']:
                strength += HERO_RARITIES_MAP_SCORE[hero_info['hero_rarity']]*2
            strength += int(hero_info['hero_skill_amount'])
        
        if hero_info['weapon_rarity'] != 'None':
            strength += WEAPON_RARITIES_MAP_SCORE[hero_info['weapon_rarity']]
            strength += int(hero_info['weapon_attributes'])

        if hero_info['pet_rarity'] != 'None':
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

def apy_calculator():
    st.title('APY Calculator')
    st.header('Account Info and Cost')
    col1, col2 = st.columns(2)
    apy_calculator_input = {}
    with col1:
        apy_calculator_input['base_level'] = st.number_input('Base level', min_value=1, max_value=21, step=1)
    with col2:
        apy_calculator_input['energy'] = st.number_input('Energy', min_value=30, max_value=100, step=1)

    col1, col2, col3 = st.columns(3)
    with col1:
        apy_calculator_input['bcv_price'] = st.number_input('BCV Price (GMT)', min_value=1, step=1, value=900)
        apy_calculator_input['bcv_bought'] = st.number_input('BCV You Bought', min_value=0, step=1, value=1)
    with col2:
        apy_calculator_input['hero_price'] = st.number_input('Heroes Price (GMT)', min_value=1, step=1, value=1000)
        apy_calculator_input['hero_bought'] = st.number_input('Heroes You Bought', min_value=0, step=1, value=1)
    with col3:
        apy_calculator_input['pet_price'] = st.number_input('Pet Price (GMT)', min_value=1, step=1, value=900)
        apy_calculator_input['pet_bought'] = st.number_input('Pet You Bought', min_value=0, step=1, value=1)
    
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:    
        apy_calculator_input['weapon_price'] = st.number_input('Weapon Price (GMT)', min_value=1, step=1, value=1900)
        apy_calculator_input['weapon_bought'] = st.number_input('Weapon You Bought', min_value=0, step=1, value=1)
    with col2:
        apy_calculator_input['hero_exp_price'] = st.number_input('Hero Exp Price (GMT)', min_value=1, step=1, value=1300)
        apy_calculator_input['hero_exp_bought'] = st.number_input('Hero Exp You Bought', min_value=0, step=1, value=1)
    with col3:
        apy_calculator_input['move_price'] = st.number_input('Move Price (GMT)', min_value=1, step=1, value=700)
        apy_calculator_input['move_bought'] = st.number_input('Move You Bought', min_value=0, step=1, value=1)

    total_cost = get_total_cost(apy_calculator_input)
    st.subheader(f'Total Cost: {total_cost} GMT')
    st.divider()

    apy_calculator_input['is_upgrade_base_level'] = st.toggle('Upgrade Base Level (To increase energy)')
    apy_calculator_input['is_synthesis_to_hero'] = st.toggle('Synthesis DNA Fragment to HERO (To increase energy)')

    st.header('Earn Per day')
    col1, col2, col3 = st.columns(3)
    with col1:
        apy_calculator_input['dna_fragment_price'] = st.number_input('DNA Fragment Price (GMT)', min_value=1, step=1, value=50)
        apy_calculator_input['dna_fragment_earn'] = st.number_input('DNA Fragment Earn', min_value=0, step=1, value=8)
    with col2:
        apy_calculator_input['ancient_fragment_price'] = st.number_input('Ancient Fragment Price (GMT)', min_value=1, step=1, value=10)
        apy_calculator_input['ancient_fragment_earn'] = st.number_input('Ancient Fragment Earn', min_value=0, step=1, value=30)
    with col3:
        apy_calculator_input['blueprint_fragment_price'] = st.number_input('Blueprint Fragment Price (GMT)', min_value=1, step=1, value=10)
        apy_calculator_input['blueprint_fragment_earn'] = st.number_input('Blueprint Fragment Earn', min_value=0, step=1, value=30)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        apy_calculator_input['evolution_cookie_price'] = st.number_input('Evolution Cookie Price (GMT)', min_value=1, step=1, value=60)
        apy_calculator_input['evolution_cookie_earn'] = st.number_input('Evolution Cookie Earn', min_value=0, step=1, value=5)
    with col2:
        apy_calculator_input['hero_potion_price'] = st.number_input('Hero Potion Price (GMT)', min_value=1, step=1, value=5)
        apy_calculator_input['hero_potion_earn'] = st.number_input('Hero Potion Earn', min_value=0, step=1, value=30)
    with col3:
        apy_calculator_input['power_can_price'] = st.number_input('Power Can Price (GMT)', min_value=1, step=1, value=2)
        apy_calculator_input['power_can_earn'] = st.number_input('Power Can Earn', min_value=0, step=1, value=400)
    
    apy_calculator_input['simulation_days'] = st.number_input('Amount of Simulation days for APY', min_value=1, step=1, value=20)
    st.divider()

    show_apy_result(apy_calculator_input, total_cost)

def get_total_cost(apy_calculator_input):
    total_cost = 0
    total_cost += int(apy_calculator_input['bcv_price']) * int(apy_calculator_input['bcv_bought'])
    total_cost += int(apy_calculator_input['hero_price']) * int(apy_calculator_input['hero_bought'])
    total_cost += int(apy_calculator_input['pet_price']) * int(apy_calculator_input['pet_bought'])
    total_cost += int(apy_calculator_input['weapon_price']) * int(apy_calculator_input['weapon_bought'])
    total_cost += int(apy_calculator_input['hero_exp_price']) * int(apy_calculator_input['hero_exp_bought'])
    total_cost += int(apy_calculator_input['move_price']) * int(apy_calculator_input['move_bought'])
    
    return total_cost

def can_upgrade_base(base_level, current_power_can):
    return current_power_can > BASE_UPGRADE_COST[base_level]

def adjust_earn_by_energy(earn_each_day, origin_energy, current_energy):
    return int(earn_each_day * current_energy / origin_energy)

def can_synthesis_hero(current_dna_fragment):
    return current_dna_fragment >= 100

def rename_apy_progress_columns(df):
    rename_rule = {
        'day': 'Day',
        'current_power_can': 'Power Can amount',
        'current_dna_fragment': 'DNA Fragment amount',
        'is_upgrade_base_today': 'Upgrade Base?',
        'is_synthesis_hero_today': 'Synthesis Hero?',
        'earn_each_day': 'Earn GMT / day',
        'current_energy': 'Max Energy',
        'base_level': 'Base lvl',
    }
    df = df.rename(columns=rename_rule)
    return df

def reorder_apy_progress_columns(df):
    desired_order = ['Day', 'Base lvl', 'Max Energy', 'Earn GMT / day', 'Upgrade Base?', 'Synthesis Hero?']

    df = df[desired_order]
    return df

def get_apy_progress(apy_calculator_input):
    apy_progress = []
    cost_earn_each_day = {}
    is_upgrade_base_level = apy_calculator_input['is_upgrade_base_level']
    is_synthesis_to_hero = apy_calculator_input['is_synthesis_to_hero']
    base_level = apy_calculator_input['base_level']
    origin_energy = apy_calculator_input['energy']
    current_energy = apy_calculator_input['energy']
    current_power_can = 0
    current_dna_fragment = 0
    for day in range(int(apy_calculator_input['simulation_days'])):
        cost_earn_each_day = {
            'day': day+1,
            'current_power_can': current_power_can,
            'current_dna_fragment': current_dna_fragment,
            'is_upgrade_base_today': False,
            'is_synthesis_hero_today': False,
        }
        if is_upgrade_base_level and can_upgrade_base(base_level, current_power_can):
            current_power_can -= BASE_UPGRADE_COST[base_level]
            current_energy += 2
            base_level += 1
            cost_earn_each_day['is_upgrade_base_today'] = True

        if is_synthesis_to_hero and can_synthesis_hero(int(current_dna_fragment)):
            current_dna_fragment -= 100
            current_energy += 1
            cost_earn_each_day['is_synthesis_hero_today'] = True

        earn_each_day = 0
        earn_each_day += int(apy_calculator_input['ancient_fragment_price'])*int(apy_calculator_input['ancient_fragment_earn'])
        earn_each_day += int(apy_calculator_input['blueprint_fragment_price'])*int(apy_calculator_input['blueprint_fragment_earn'])
        earn_each_day += int(apy_calculator_input['evolution_cookie_price'])*int(apy_calculator_input['evolution_cookie_earn'])
        earn_each_day += int(apy_calculator_input['hero_potion_price'])*int(apy_calculator_input['hero_potion_earn'])
        if not is_upgrade_base_level:
            earn_each_day += int(apy_calculator_input['power_can_price'])*int(apy_calculator_input['power_can_earn'])
        else:
            current_power_can += int(apy_calculator_input['power_can_earn'])
        
        if not is_synthesis_to_hero:
            earn_each_day += int(apy_calculator_input['dna_fragment_price'])*int(apy_calculator_input['dna_fragment_earn'])
        else:
            current_dna_fragment += int(apy_calculator_input['dna_fragment_earn'])

        cost_earn_each_day['earn_each_day'] = adjust_earn_by_energy(earn_each_day, origin_energy, current_energy)
        cost_earn_each_day['current_energy'] = current_energy
        cost_earn_each_day['base_level'] = base_level
        
        apy_progress.append(cost_earn_each_day)

    df = DataFrame(apy_progress)
    return df

def get_total_earn(apy_progress, apy_calculator_input):
    total_earn = 0
    total_earn += sum(apy_progress['earn_each_day'])
    total_earn += apy_progress['current_power_can'].iloc[-1]*int(apy_calculator_input['power_can_price'])
    total_earn += apy_progress['current_dna_fragment'].iloc[-1]*int(apy_calculator_input['dna_fragment_price'])

    return total_earn

def calculate_apy(total_cost, total_earn, day):
    return round(total_earn / total_cost / day * 365 * 100, 2)

def show_apy_string_result(total_cost, total_earn, day):
    apy = calculate_apy(total_cost, total_earn, day)
    multiplier = round(apy / 100, 2)
    st.markdown(f'## You use :red[{total_cost}] GMT earned :green[{total_earn}] GMT within :orange[{day}] days , resulting in an APY of :rainbow[{apy}%] :sunglasses:.')
    st.markdown(f'## This means :rainbow[X{multiplier}] return in a year.')

def show_apy_result(apy_calculator_input, total_cost):
    st.header('APY Result')
    apy_progress = get_apy_progress(apy_calculator_input)
    total_earn = get_total_earn(apy_progress, apy_calculator_input)
    show_apy_string_result(total_cost, total_earn, apy_calculator_input['simulation_days'])

    apy_progress = rename_apy_progress_columns(apy_progress)
    apy_progress = reorder_apy_progress_columns(apy_progress)
    st.divider()
    st.subheader('Earn Progress')
    st.dataframe(apy_progress, hide_index=True)


