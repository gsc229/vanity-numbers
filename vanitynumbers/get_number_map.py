import json

def get_number_map():
  with open("vanitynumbers/data/number_map.json", "r", encoding="utf8") as file:
    all_words = json.load(file)
    return all_words
