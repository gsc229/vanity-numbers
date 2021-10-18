import re
from get_number_map import get_number_map
from get_word_groups import get_word_groups
from get_word_rankings import get_rankings

def find_words(seven_digit_number):
  """ Checks a seven digit phone number against a dictionary of number keys and word-list values.
      Words can be made from either the entire phone number or parts of the phone number.
      Retuns the top five vanity numbers by word length.
  """
  number_map = get_number_map()
  sanitized_number = "".join(re.findall(r"\d", seven_digit_number))
  country_code = sanitized_number[0]
  area_code = sanitized_number[1:4]
  last_seven_digits = sanitized_number[-7:]
  word_groups = get_word_groups(last_seven_digits, number_map)

  word_rankings = get_rankings(word_groups, country_code, area_code, last_seven_digits, number_map)

  return word_rankings[0:5]
