from validate_phone_number import validate_phone_number
from get_number_map import get_number_map
from get_word_groups import get_word_groups
from get_word_rankings import get_rankings

def find_words(phone_number):
  """ Checks a seven digit phone number against a dictionary of number keys and word-list values.
      Words can be made from either the entire phone number or parts of the phone number.
      Retuns the top five vanity numbers by word length.
  """
  validated_phone_number = validate_phone_number(phone_number)

  if validated_phone_number["valid"] is not True:
    return "Error: Invalid Phone Number"

  last_seven_digits = validated_phone_number["seven_digit_phone_number"]
  country_code = validated_phone_number["country_code"]
  area_code = validated_phone_number["area_code"]

  number_map = get_number_map()

  word_groups = get_word_groups(last_seven_digits, number_map)

  word_rankings = get_rankings(word_groups, country_code, area_code, last_seven_digits, number_map)

  return word_rankings[0:5]
