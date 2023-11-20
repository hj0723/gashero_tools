from const_gashero_tools import *

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
