import requests

class Pokemon:
    def __init__(self, name, number, height, weight, stats, types):
        self.name = name
        self.number = number
        self.height = height
        self.weight = weight
        #hp, atk, def, spa, spd, spe
        self.stats = stats
        self.types = types

    def __str__(self):
        output_string = ""
        output_string += str(self.number) + "\n"
        output_string += self.name.capitalize() + "\n"
        output_string += f"Height: {self.height}cm, Weight: {self.weight}g" + "\n"
        output_string += f"Stats: HP:{self.stats[0]}, ATK:{self.stats[1]}, DEF:{self.stats[2]}, SPA:{self.stats[3]}, SPD:{self.stats[4]}, SPE:{self.stats[5]}" + "\n"
        output_string += f"Type(s): " + ", ".join(self.types) + "\n"
        return output_string

r = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")

data = r.json()
results = data["results"]

for result in results[:10]:
    r = requests.get(result["url"])
    data = r.json()
    stats = []

    for stat in data["stats"]:
        stats.append(stat["base_stat"])
    
    types = []
    for poketype in data["types"]:
        types.append(poketype["type"]["name"])

    pokemon = Pokemon(data["name"], data["id"], data["height"], data["weight"], stats, types)
    print(pokemon)
    