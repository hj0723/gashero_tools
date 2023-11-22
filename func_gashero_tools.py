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
