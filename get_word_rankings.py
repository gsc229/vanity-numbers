def get_rankings(word_groups, country_code, area_code, phone_number, number_map):

  word_rankings = []

  for word_group in word_groups:
    if len(word_group.keys()) != 0:
      for index, word_list in word_group.items():
        for word in word_list:
          vanity_number = splice_words_in_number(
            index,
            country_code,
            area_code,
            phone_number,
            word
          ).upper()

          word_rankings.append(vanity_number)

  next_number = ""
  level = 0

  while len(word_rankings) < 5:
    for num in phone_number:
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

  return word_rankings

def splice_words_in_number(start_index, country_code, area_code, phone_number, word):
  phone_split = list(phone_number)
  # print(phone_split)

  for i in range(start_index, start_index + len(word)):
    # print(i)
    phone_split[i] = word[i - start_index]

  return f"+{country_code}-{area_code}-{''.join(phone_split)}"