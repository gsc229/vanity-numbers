def get_response_message(vanity_numbers_list):

  message = "Your top five vanity numbers are "

  spaced_numbers = [insert_spaces(vanity_number) for vanity_number in vanity_numbers_list]

  for i, vanity_number in enumerate(spaced_numbers):
    if i < len(spaced_numbers) + 1:
      spaced_numbers[i] = f"{vanity_number} next number"

  print(spaced_numbers)
  print(message + "".join(spaced_numbers))

  return message

def insert_spaces(vanity_number=str):
  spaced_number = ""

  for i, char in enumerate(vanity_number):
    if char.isalpha() and vanity_number[i+1].isnumeric():
      spaced_number += f"{char} "
    elif not char.isalpha() and not char.isnumeric():
      spaced_number += " "
    else:
      spaced_number += char


  return spaced_number
test = ['+1-419-DORK132', '+1-419-FORK132', '+1-419-FORL132', '+1-419-DOP5132', '+1-419-DOR5132']
get_response_message(test)
