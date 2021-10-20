import json

def generate_number_map():
  """ Loops through every word in the word list and
      converts letters to phone dial pad digits. The digits are
      used as dictionary keys and the value is a list of all words with the same
      digit conversions. In this way we can have O(1) access to meaningful,
      common words associated with any or all number sequences in a phone number.
   """

  print("working...")
  alpha_num_dict = {
    'a': '2', 'b': '2', 'c': '2',\
    'd': '3', 'e': '3', 'f': '3',\
    'g': '4', 'h': '4', 'i': '4',\
    'j': '5', 'k': '5', 'l': '5',\
    'm': '6', 'n': '6', 'o': '6',\
    'p': '7', 'q': '7', 'r': '7', 's': '7',\
    't': '8', 'u': '8', 'v': '8',\
    'w': '9', 'x': '9', 'y': '9', 'z': '9'
  }

  with open("words.json", "r") as file:
    word_list = json.load(file)
    print(word_list)
    number_map = {}
    for word in word_list:
      word_number = ""
      
      for letter in word:
        word_number += alpha_num_dict[letter]

      if word_number not in number_map:
        number_map[word_number] = []

      number_map[word_number].append(word.upper())

  print(number_map)

  with open("number_map.json", "w") as outfile:
    json.dump(number_map, outfile)

  print("done.")

generate_number_map()