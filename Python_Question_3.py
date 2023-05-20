import xlsxwriter
from urllib.request import urlopen
import json

class jsonToExcel:

    #Constructor takes in the link
    def __init__(self, link):
        self.link = link

    def list_to_string(self, list):
        #This function converts the given list to string
        #Because we cannot all a list to a Excel cell
        str = ""
        for item in list:
            str = str + f",{item}"

        #First character is ommited because it contains a comma
        return str[1:-1]


    def link_to_json(self):
        try:
            #This function converts JSON link to python readable format(dictionary)
            #And returns all the keys and a list of dictionaries (Individual pokemon)

            url = self.link
            response = urlopen(url)

            pokemon_json_data = json.loads(response.read())
            #all_keys contains all the keys
            all_keys = list(pokemon_json_data["pokemon"][1].keys())

            #List of individual pokemons
            pokemon_list = pokemon_json_data["pokemon"]

            return all_keys, pokemon_list
        except Exception:
            raise Exception("Error in getting the data")


    def write_to_excel(self, all_keys, pokemon_list):
        try:
            #Given name to workbook and worksheet
            #This will be stored in the same folder
            workbook = xlsxwriter.Workbook("pokemon_data.xlsx")
            worksheet = workbook.add_worksheet("data")

            #Created the first row with all the keys
            for i in range(0, 17):
                worksheet.write(0, i, all_keys[i])

            # Go through all the rows and columns and add the data
            # i is row & j is column
            # first row is already taken by the headings to we start from i+1
            for i in range(0, len(pokemon_list)):
                for j in range(0, len(all_keys)):
                    if pokemon_list[i].get(all_keys[j]): #Check if the key exist or not
                        if type(pokemon_list[i][all_keys[j]]) == list: #Check if the key is a list because we cannot add list to excel cell
                            #The list is converted to a string
                            #And added to Excel cell
                            str = self.list_to_string(pokemon_list[i][all_keys[j]])
                            worksheet.write(i+1, j, str)
                        else:
                            worksheet.write(i+1, j, pokemon_list[i][all_keys[j]])
                    else:
                        #If the key does not exist then add #####
                        worksheet.write(i+1, j, "#####")

            workbook.close()
        except Exception:
            raise Exception("Error in Excel making")




url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"

#Created an instance
pokemon = jsonToExcel(url)

all_keys, pokemon_list = pokemon.link_to_json()

pokemon.write_to_excel(all_keys=all_keys, pokemon_list=pokemon_list)




















