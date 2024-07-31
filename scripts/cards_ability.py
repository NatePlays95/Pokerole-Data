import json
import os
import re
import pandas as pd
from shutil import copy, move
import copy 
import io 
import fire

pokedex_path = '../Version20/Pokedex/'
# moves_path = '../Version20/Moves/'
abilities_path = '../Version20/Abilities/'

def create_json():

    template = {
        "count": "1",
        "color": "black",
        "title": "Damp",
        "icon": "dna1",
        "icon_back": "",
        "contents": [
            "subtitle | The Pokemon gathers the humidity in the air around itself. Lighting a spark or keeping a fire on, will be almost impossible close to it.",
            "rule",
            "property | Effect | No ally or foe will be able to use the moves Explosion or Self-Destruct in an area around this Pokemon."
        ],
        "tags": [],
        "title_size": "14",
        "card_font_size": "12"
    }

    cards = []
    for fname in sorted(os.listdir(abilities_path)):
        if '.json' not in fname: continue
        path = abilities_path+fname
        data = json.loads(open(path).read())
        card = copy.deepcopy(template)
        card['title'] = data['Name']
        card['contents'] = [
            f"subtitle | {data['Description']}",
            "rule",
            f"property | Effect | {data['Effect']}"
        ]
        abilityname = data['Name']
        tags = []
        for fname in sorted(os.listdir(pokedex_path)):
            if '.json' not in fname: continue
            path = pokedex_path+fname
            dex = json.loads(open(path).read())
            
            if abilityname in [dex['Ability1'],dex['Ability2'],dex['HiddenAbility'],dex['EventAbilities']]:
                tags.append(dex['Name'].lower())
        
        card['tags'] = tags
        cards.append(card)
        print(f"finished ability {abilityname}")


    open('../Version20/ability_cards.json','w').write(json.dumps(cards, indent=4))

def name_fix():
    for name, card in zip(
            sorted([x for x in os.listdir(abilities_path) if '.json' in x]),
            sorted([x for x in os.listdir('../Version20/Ability Cards') if '.png' in x])):
        
        move(f'../Version20/Ability Cards/{card}',
             f"../Version20/Ability Cards/{name.split('.')[0]}.png")
        
if __name__ == '__main__':
    # print(os.listdir('..'))
    create_json()
    # name_fix()

