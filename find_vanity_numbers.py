import json
import re

def find_words(phone_number):
  """ Checks a phone number against a list of words that can be made
      by the phone number or parts of the phone number
  """
  sanitized_number = "".join(re.findall(r"\d", phone_number))
  # print("SANITIZED", sanitized_number, sanitized_number[-7:])
  word_rankings = []

  # The keys to the word groups are the indicies of which the word starts
  three_letter_words = {}
  four_letter_words = {}
  five_letter_words = {}
  six_letter_words = {}
  seven_letter_words = {}

  with open("number_map.json", "r", encoding="utf8") as file:
    number_map = json.load(file)
    if sanitized_number[-7:] in number_map:
      seven_letter_words[len(sanitized_number) - 7] = number_map[sanitized_number[-7:]]
    # print(number_map)

    for i in range(len(sanitized_number), 0, -1):

      if i >= 4:
        key = sanitized_number[i-3:i]

        if key in number_map:
          three_letter_words[i-3] = number_map[key]

      if i >= 3:
        key = sanitized_number[i-4:i]
        if key in number_map:
          four_letter_words[i-4] = number_map[key]

      if i >= 2:
        key = sanitized_number[i-5:i]
        if key in number_map:
          five_letter_words[i-5] = number_map[key]

      if i >= 1:
        key = sanitized_number[i-6:i]
        if key in number_map:
          six_letter_words[i-6] = number_map[key]

  word_groups = [
    seven_letter_words,
    six_letter_words,
    five_letter_words,
    four_letter_words,
    three_letter_words
  ]

  for word_group in word_groups:
    if len(word_group.keys()) != 0:
      for index, word_list in word_group.items():
        for word in word_list:
          vanity_number = splice_phone_number(index, sanitized_number, word).upper()
          word_rankings.append(vanity_number)

  next_number = ""
  level = 0
  while len(word_rankings) < 5:
    for num in sanitized_number:
      if num == "1":
        next_number += "1"
      else:
        if num in number_map:
          if level < len(number_map[num]):
            next_number += number_map[num][level]
          else:
            next_number += num
      level += 1
    word_rankings.append(next_number)
    next_number = ""

  return word_rankings[0:5]
  # print(f"Three Letter Words: {three_letter_words}")
  # print(f"Four Letter Words: {four_letter_words}")
  # print(f"Five Letter Words: {five_letter_words}")
  # print(f"Six Letter Words: {six_letter_words}")
  # print(f"Seven Letter Word: {seven_letter_words}")

def splice_phone_number(start, phone_number, letters):
  phone_split = list(phone_number)
  # print(phone_split)

  for i in range(start, start + len(letters)):
    # print(i)
    phone_split[i] = letters[i - start]

  return "".join(phone_split)

