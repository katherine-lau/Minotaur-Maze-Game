from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
from itertools import product
import numpy as np

# 1. Define the model structure
model = DiscreteBayesianNetwork([
    ('hero_hp', 'combat_outcome'),
    ('attack_artifact', 'combat_outcome'),
    ('defense_artifact', 'combat_outcome'),
    ('special_artifact', 'combat_outcome'),
    ('minotaur_strength', 'combat_outcome'),
    ('hero_speed', 'combat_outcome'),
    ('minotaur_speed', 'combat_outcome')
])

# 2. Define CPDs

cpd_hero_hp = TabularCPD(
    variable='hero_hp', variable_card=2,
    values=[[0.6], [0.4]],
    state_names={'hero_hp': ['low', 'high']}
)

cpd_attack_artifact = TabularCPD(
    variable='attack_artifact', variable_card=2,
    values=[[0.5], [0.5]],
    state_names={'attack_artifact': ['no', 'yes']}
)

cpd_defense_artifact = TabularCPD(
    variable='defense_artifact', variable_card=2,
    values=[[0.6], [0.4]],
    state_names={'defense_artifact': ['no', 'yes']}
)

cpd_special_artifact = TabularCPD(
    variable='special_artifact', variable_card=2,
    values=[[0.7], [0.3]],
    state_names={'special_artifact': ['no', 'yes']}
)

cpd_minotaur_strength = TabularCPD(
    variable='minotaur_strength', variable_card=2,
    values=[[0.4], [0.6]],
    state_names={'minotaur_strength': ['weak', 'strong']}
)

cpd_hero_speed = TabularCPD(
    variable='hero_speed', variable_card=2,
    values=[[0.5], [0.5]],
    state_names={'hero_speed': ['slow', 'fast']}
)

cpd_minotaur_speed = TabularCPD(
    variable='minotaur_speed', variable_card=2,
    values=[[0.5], [0.5]],
    state_names={'minotaur_speed': ['slow', 'fast']}
)

# Simplified combat outcome CPD (in practice you'd expand with real data or logical estimates)
# For brevity, this version keeps other nodes constant; add full conditional structure as needed.
'''
cpd_combat_outcome = TabularCPD(
    variable='combat_outcome', variable_card=2,
    values=[[0.6], [0.4]],
    state_names={'combat_outcome': ['lose', 'win']}
)
'''
# Define the order of evidence variables and their cardinalities
evidence_vars = [
    'hero_hp',
    'attack_artifact',
    'defense_artifact',
    'special_artifact',
    'minotaur_strength',
    'hero_speed',
    'minotaur_speed'
]

evidence_card = [2] * len(evidence_vars)

# Generate all combinations of evidence (binary states)
combinations = list(product([0, 1], repeat=7))  # 0=unfavorable, 1=favorable

# Calculate win probabilities logically for each row
win_probs = []
for combo in combinations:
    hp, atk, def_, spec, min_str, h_speed, m_speed = combo

    # Start with a base win chance
    win_chance = 0.1

    # Add logical boosts
    if hp: win_chance += 0.2
    if atk: win_chance += 0.2
    if def_: win_chance += 0.1
    if spec: win_chance += 0.1
    if min_str == 0: win_chance += 0.1  # easier if minotaur is weak
    if h_speed and not m_speed: win_chance += 0.15  # speed advantage
    elif not h_speed and m_speed: win_chance -= 0.1  # speed disadvantage

    win_chance = min(max(win_chance, 0.05), 0.95)  # clamp between [0.05, 0.95]
    win_probs.append([1 - win_chance, win_chance])  # [lose, win]

# Transpose to match pgmpy format (each row is one outcome)
win_prob_matrix = np.array(win_probs).T.tolist()

cpd_combat_outcome = TabularCPD(
    variable='combat_outcome',
    variable_card=2,
    values=win_prob_matrix,
    evidence=evidence_vars,
    evidence_card=evidence_card,
    state_names={
        'combat_outcome': ['lose', 'win'],
        'hero_hp': ['low', 'high'],
        'attack_artifact': ['no', 'yes'],
        'defense_artifact': ['no', 'yes'],
        'special_artifact': ['no', 'yes'],
        'minotaur_strength': ['weak', 'strong'],
        'hero_speed': ['slow', 'fast'],
        'minotaur_speed': ['slow', 'fast']
    }
)

# 3. Add CPDs to the model
model.add_cpds(
    cpd_hero_hp,
    cpd_attack_artifact,
    cpd_defense_artifact,
    cpd_special_artifact,
    cpd_minotaur_strength,
    cpd_hero_speed,
    cpd_minotaur_speed,
    cpd_combat_outcome
)

# Validate the model
assert model.check_model()

# 4. Create an inference engine
inference = VariableElimination(model)
'''
# 5. Example evidence from current game state
evidence = {
    'hero_hp': 'high',
    'attack_artifact': 'yes',
    'defense_artifact': 'yes',
    'special_artifact': 'no',
    'minotaur_strength': 'strong',
    'hero_speed': 'fast',
    'minotaur_speed': 'slow'
}

# Query the probability of winning
result = inference.query(variables=['combat_outcome'], evidence=evidence)
win_prob = result.values[1]
'''
def win_prob(hero_hp, min_hp, sword, shield, hp_amulet, ow_amulet, ow_min_amulet, t_speed_amulet, min_speed_amulet):
    #default values of prob 
    attack = 'no'
    defense = 'no'
    hp_special = 'no'
    hero_speed = 'slow'
    minotaur_speed = 'slow'
    h_hp = 'high'
    m_hp = 'strong'


    #check the items and set the evidence accordingly
    if sword:
        attack = 'yes'
    if shield:
        defense = 'yes'
    if hp_amulet:
        hp_special = 'yes'
    if t_speed_amulet:
        hero_speed = 'fast'
    if min_speed_amulet:
        minotaur_speed = 'fast'
    if hero_hp or ow_amulet:
        h_hp = 'low'
    if min_hp or ow_min_amulet:
        m_hp = 'weak'

    #calculate the win probability based on the evidence
    evidence = {
        'hero_hp': h_hp,
        'attack_artifact': attack,
        'defense_artifact': defense,
        'special_artifact': hp_special,
        'minotaur_strength': m_hp,
        'hero_speed': hero_speed,
        'minotaur_speed': minotaur_speed
    }
    result = inference.query(variables=['combat_outcome'], evidence=evidence)
    return result.values[1]


#print(result)
