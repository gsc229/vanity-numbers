def get_word_groups(seven_digit_phone_number, number_map):
  """ Checks a seven digit phone number against a dictionary (number_map) of number-keys
      and word-list-values. Words can be made from either the entire phone number
      or parts of the phone number.

      There are six vanity number groups/dictionaries ordered from high to low:
      seven letter words, six letter words, five letter words,
      four letter words, three letter words and two letter words.
      The keys in the dictionaries are also indices which represent
      at which index of the seven digit phone number the word begins.
  """
  word_groups = []

  two_letter_words = {}
  three_letter_words = {}
  four_letter_words = {}
  five_letter_words = {}
  six_letter_words = {}
  seven_letter_words = {}

  if seven_digit_phone_number in number_map:
    seven_letter_words[0] = number_map[seven_digit_phone_number]
  # print(number_map)

  for i in range(0, 7):

    # Find any three letter words
    if i <= 5:
      key = seven_digit_phone_number[i:i+2]

      if key in number_map:
        two_letter_words[i] = number_map[key]

    if i <= 4:
      key = seven_digit_phone_number[i:i+3]

      if key in number_map:
        three_letter_words[i] = number_map[key]

    if i <= 3:
      key = seven_digit_phone_number[i:i+4]
      if key in number_map:
        four_letter_words[i] = number_map[key]

    if i <= 2:
      key = seven_digit_phone_number[i:i+5]
      if key in number_map:
        five_letter_words[i] = number_map[key]

    if i <= 1:
      key = seven_digit_phone_number[i:i+6]
      if key in number_map:
        six_letter_words[i] = number_map[key]

  word_groups.extend([
    seven_letter_words,
    six_letter_words,
    five_letter_words,
    four_letter_words,
    three_letter_words,
    three_letter_words
  ])
  
  return word_groups
