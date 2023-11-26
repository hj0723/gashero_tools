from json import loads

HERO_LEVEL_PU_COST = {
    (1, 2): {'pu': 1, 'gmt': 0},
    (2, 3): {'pu': 1, 'gmt': 0},
    (3, 4): {'pu': 1, 'gmt': 0},
    (4, 5): {'pu': 1, 'gmt': 0},
    (5, 6): {'pu': 1, 'gmt': 0},
    (6, 7): {'pu': 1, 'gmt': 0},
    (7, 8): {'pu': 1, 'gmt': 0},
    (8, 9): {'pu': 1, 'gmt': 0},
    (9, 10): {'pu': 1, 'gmt': 1},
    (10, 11): {'pu': 2, 'gmt': 0},
    (11, 12): {'pu': 2, 'gmt': 0},
    (12, 13): {'pu': 2, 'gmt': 0},
    (13, 14): {'pu': 2, 'gmt': 0},
    (14, 15): {'pu': 2, 'gmt': 0},
    (15, 16): {'pu': 2, 'gmt': 0},
    (16, 17): {'pu': 2, 'gmt': 0},
    (17, 18): {'pu': 2, 'gmt': 0},
    (18, 19): {'pu': 2, 'gmt': 0},
    (19, 20): {'pu': 2, 'gmt': 1},
    (20, 21): {'pu': 6, 'gmt': 0},
    (21, 22): {'pu': 6, 'gmt': 0},
    (22, 23): {'pu': 6, 'gmt': 0},
    (23, 24): {'pu': 6, 'gmt': 0},
    (24, 25): {'pu': 6, 'gmt': 0},
    (25, 26): {'pu': 6, 'gmt': 0},
    (26, 27): {'pu': 6, 'gmt': 0},
    (27, 28): {'pu': 6, 'gmt': 0},
    (28, 29): {'pu': 6, 'gmt': 0},
    (29, 30): {'pu': 6, 'gmt': 4},
    (30, 31): {'pu': 18, 'gmt': 0},
    (31, 32): {'pu': 18, 'gmt': 0},
    (32, 33): {'pu': 18, 'gmt': 0},
    (33, 34): {'pu': 18, 'gmt': 0},
    (34, 35): {'pu': 18, 'gmt': 0},
    (35, 36): {'pu': 18, 'gmt': 0},
    (36, 37): {'pu': 18, 'gmt': 0},
    (37, 38): {'pu': 18, 'gmt': 0},
    (38, 39): {'pu': 18, 'gmt': 0},
    (39, 40): {'pu': 18, 'gmt': 12},
    (40, 41): {'pu': 54, 'gmt': 0},
    (41, 42): {'pu': 54, 'gmt': 0},
    (42, 43): {'pu': 54, 'gmt': 0},
    (43, 44): {'pu': 54, 'gmt': 0},
    (44, 45): {'pu': 54, 'gmt': 0},
    (45, 46): {'pu': 54, 'gmt': 0},
    (46, 47): {'pu': 54, 'gmt': 0},
    (47, 48): {'pu': 54, 'gmt': 0},
    (48, 49): {'pu': 54, 'gmt': 0},
    (49, 50): {'pu': 54, 'gmt': 36},
    (50, 51): {'pu': 162, 'gmt': 0},
    (51, 52): {'pu': 162, 'gmt': 0},
    (52, 53): {'pu': 162, 'gmt': 0},
    (53, 54): {'pu': 162, 'gmt': 0},
    (54, 55): {'pu': 162, 'gmt': 0},
    (55, 56): {'pu': 162, 'gmt': 0},
    (56, 57): {'pu': 162, 'gmt': 0},
    (57, 58): {'pu': 162, 'gmt': 0},
    (58, 59): {'pu': 162, 'gmt': 0},
    (59, 60): {'pu': 162, 'gmt': 108}
}

with open('./data/hero_db.json', 'r') as f:
    hero_db = loads(f.read())

CODENAME_MAP_URL = {"iron lady":"https://framerusercontent.com/images/o1KVJxNHsinDcWfPsWVkmz3I.png","ape commander":"https://framerusercontent.com/images/Eamd9UYODYbyTrt0aCY0RD9Qlyo.png","biorobotic soldier":"https://framerusercontent.com/images/fxsMsucdxRr6WijW7IetyI4Mh8.png","black sapphire":"https://framerusercontent.com/images/ICypd7t22aMyfJHvu3pzTrfcp4.png","space captain":"https://framerusercontent.com/images/2sKPyNUZEdISWAcvIgfJysijYE.png","spore lord":"https://framerusercontent.com/images/ZnpUDJedzbK29RGfkJqtkkjcRk8.png","ruthless warden":"https://framerusercontent.com/images/0LNmAb3mrNOvKNAKUMtrTCW5Aj0.png","guardian angel":"https://framerusercontent.com/images/8IXQqFR5sAlUryMU2Hyn2Zgj7Yc.png","combat queen":"https://framerusercontent.com/images/xN1fbFl9CISGgSX2PbMwbScH1tA.png","lone werewolf":"https://framerusercontent.com/images/wQxI8kjKdNcW7s5Aa0uXzhPBXVY.png","the trailblazer":"https://framerusercontent.com/images/x4IL60pnGMZvmRFIbNKUki82Bw.png","nano swamp":"https://framerusercontent.com/images/CG6dw5emBoD7MI6FNcaIbgXk.png","the yokozuna":"https://framerusercontent.com/images/uxyn3wcU1cLvBV2QrE7A3f8KLMo.png","ascetic monk":"https://framerusercontent.com/images/7LofLGoJVRvBbgaQmWHaUwPTSU.png","tactical police":"https://framerusercontent.com/images/AlyojcIrJ5NcilAyO3U7IcTr2M.png","blessed kid":"https://framerusercontent.com/images/QIhyHGTyXK86wGFWHQ0nxc3h9w.png","junior shifu":"https://framerusercontent.com/images/lsMzVqN3ePGCpiWuuJuwpDQChSY.png","deadly nightshade":"https://framerusercontent.com/images/sdqPgo0O6DwaUDgcMKuHP7EaC8.png","meditating master":"https://framerusercontent.com/images/cVgVwp4Vgy8XIZNX928DC9LT4.png","unstoppable force":"https://framerusercontent.com/images/DdqlhnPCcuSfSUFZJLipuJtc8.png","amazon warrior":"https://framerusercontent.com/images/qVCBNLiIaXkSZxT860Ml79evGdc.png","blackmarket baroness":"https://framerusercontent.com/images/bSkFVvPg8lWzc31gDH974qowk.png","red mercury":"https://framerusercontent.com/images/WZd0Vm69W4GlZ8RHw3TDB8uZKx0.png","nuclear martyr":"https://framerusercontent.com/images/Kp7h0LqG2yhvx4j1HyGJA5VSpGY.png","swift blade":"https://framerusercontent.com/images/O1HAD3eKX1nj4RJpXsumNqW73oY.png","loan shark":"https://framerusercontent.com/images/PRjT7iCYH6XlT8Rjgc5Wi7AP7Y.png","altruistic banker":"https://framerusercontent.com/images/uRg5XeA9uqk5jGVpjojDPFPzEtI.png","devil's follower":"https://framerusercontent.com/images/abubuYyRLIT89cnmuPjj5iHQ8A.png","decommissioned unit":"https://framerusercontent.com/images/eZY2r2vYNReVoaL1PELaEV70N4.png","death's hand":"https://framerusercontent.com/images/bvXTqduHWVdPGuLb9Wkv9nEA.png","professor dark matter":"https://framerusercontent.com/images/tL5HS4ptuRtSbFAaLYHkfrKUHk.png","lil' bulldozer":"https://framerusercontent.com/images/8ELjE7UMu3UBubLE8JAADqryS4.png","artificial empathy":"https://framerusercontent.com/images/KXzOXa9hQVRYCmuwKG8RFlHONO0.png","praying nun":"https://framerusercontent.com/images/ivpGfJj7KRzKgHOhOC4WkTdUqw.png","arctic sheriff":"https://framerusercontent.com/images/PgV1JUNWcjNWv56ocNgP19j5n0.png","high priestess":"https://framerusercontent.com/images/a2W5AjiWQI5vuSiFR19ziWXB4.png","truth seeker":"https://framerusercontent.com/images/gS5sSEEtrGbeN8zhH0ZEFnDGE.png","faith healer":"https://framerusercontent.com/images/wp9ZATG6WCEBiUaqw4oeTyWB6M.png","street musician":"https://framerusercontent.com/images/YufYmsccpLcK89SZ8DAreNFZEM.png","media tycoon":"https://framerusercontent.com/images/1FMWQBaZHVjuY1Mz2YddZAoqIAA.png","the godfather":"https://framerusercontent.com/images/AXwB6Y7ZZQUlO1GWps1iCjfg8AU.png","leader of the pack":"https://framerusercontent.com/images/vk3WdyTChQLbavIvZB8sNCLKQ.png","historical linguist":"https://framerusercontent.com/images/d7Ff7UXJeuY1CGJ8Xdph7QOL34.png","tech tinker":"https://framerusercontent.com/images/6YWgCdSTSwFXKm3hTwydYjW0KZM.png","rocket scientist":"https://framerusercontent.com/images/NsV3dgSlqcsG7mtqNsCLMdLcYs.png","telekinetic woman":"https://framerusercontent.com/images/gVTIY4ZZ8LKCKoLAxkc2tcUR4CM.png","charming attorney":"https://framerusercontent.com/images/3KigptpAVD6PfsJZ0p8UiY774.png","field medic":"https://framerusercontent.com/images/zcayZjoUVlntakfd2WBOknSSGoE.png"}

HERO_CODENAMES = list(CODENAME_MAP_URL.keys())
TANK_HERO_CODENAMES = HERO_CODENAMES[:16]
DAMAGE_HERO_CODENAMES = HERO_CODENAMES[16:32]
SUPPORT_HERO_CODENAMES = HERO_CODENAMES[32:]

WEAPONS = ('dagger', 'sword', 'axe', 'hammer', 'bow', 'gun', 'staff', 'book',)

PETS = ('dragon', 'treant', 'crab', 'panda',)

WEAPON_MAP_URL = {
    'dagger':'https://framerusercontent.com/images/jS8PkW28RExcwieowzsHjJ6gp1U.png', 
    'sword':'https://framerusercontent.com/images/9EbRgS4qs1FDtM1tkEJOPFOUJo.png',
    'axe':'https://framerusercontent.com/images/ccirRcsTOPV7f3SihOpdK5564T4.png', 
    'hammer':'https://framerusercontent.com/images/GBy5mzpWANrr4DP5YvspJhTpg6U.png', 
    'bow':'https://framerusercontent.com/images/jX4GMfHah7aH61KxlNk9HFiMxjY.png', 
    'gun':'https://framerusercontent.com/images/R27IhrmrjyQqrbsGMcDgpAJIkg.png', 
    'staff':'https://framerusercontent.com/images/dGpwiC4nBMmid2Uhr7rID4yXvCA.png', 
    'book':'https://framerusercontent.com/images/v1xGPLadsoMY8JAnQnVvZSsQEk.png',
}

PET_MAP_URL = {
    'dragon':'https://framerusercontent.com/images/8lkce0pFlNgcdoYwLAEyToxR9zM.png', 
    'treant':'https://framerusercontent.com/images/GXU4PlbdYOk9DGUgk5sXNXMyuo.png', 
    'crab':'https://framerusercontent.com/images/JiTPdqUW9pKL95v2YJL19nbJkw.png', 
    'panda':'https://framerusercontent.com/images/16JeAfT8Soywv93Y9ux36SnXw.png',    
}

RARITIES = (
    'None',
    'common',
    'uncommon',
    'rare',
    'epic',
    'legendary',
)

SKILLS_AMOUNT = tuple(range(1,8))
IS_HERO_MAX = ('Yes', 'No')
PET_TIER = tuple(range(1,6))
WEAPON_ATTRIBUTES = SKILLS_AMOUNT

HERO_RARITIES_MAP_SCORE = {
    'common': 3,
    'uncommon': 6,
    'rare': 9,
    'epic': 12,
    'legendary': 15,
}

WEAPON_RARITIES_MAP_SCORE = {
    'common': 2,
    'uncommon': 4,
    'rare': 6,
    'epic': 8,
    'legendary': 10,
}

PET_RARITIES_MAP_SCORE = WEAPON_RARITIES_MAP_SCORE

BASE_UPGRADE_COST = {
    1:400,
    2:510,
    3:660,
    4:860,
    5:1100,
    6:1400,
    7:1800,
    8:2400,
    9:3100,
    10:4000,
    11:5100,
    12:6600,
    13:8600,
    14:11000,
    15:14000,
    16:18000,
    17:24000,
    18:31000,
    19:40000,
    20:51000,
}
