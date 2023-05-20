import xlsxwriter
from urllib.request import urlopen
import json

url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"

response = urlopen(url)

pokemon_json_data = json.loads(response.read())
all_keys = list(pokemon_json_data["pokemon"][1].keys())

pokemon_list = pokemon_json_data["pokemon"]

workbook = xlsxwriter.Workbook("pokemon_data.xlsx")
worksheet = workbook.add_worksheet("data")

for i in range(0, 17):
    worksheet.write(0, i, all_keys[i])


for i in range(0, len(pokemon_list)):
    for j in range(0, len(all_keys)):
        if pokemon_list[i].get(all_keys[j]):
            if type(pokemon_list[i][all_keys[j]]) == list:
                worksheet.write(i+1, j, "#####")
            else:
                worksheet.write(i+1, j, pokemon_list[i][all_keys[j]])
        else:
            worksheet.write(i+1, j, "#####")

workbook.close()

