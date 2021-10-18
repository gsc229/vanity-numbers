def get_word_groups(seven_digit_phone_number, number_map):
  # The keys to the word groups are the indicies of which the word starts
  word_groups = []
  three_letter_words = {}
  four_letter_words = {}
  five_letter_words = {}
  six_letter_words = {}
  seven_letter_words = {}

  if seven_digit_phone_number in number_map:
    seven_letter_words[0] = number_map[seven_digit_phone_number]
  # print(number_map)

  for i in range(0, 7):

    if i <= 4:
      key = seven_digit_phone_number[i:i+3]

      if key in number_map:
        three_letter_words[i] = number_map[key]

    if i <= 3:
      key = seven_digit_phone_number[i:i+4]
      if key in number_map:
        four_letter_words[i-4] = number_map[key]

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
    three_letter_words
  ])

  return word_groups
