def get_response_message(vanity_numbers_list):

  message = "Your vanity numbers are "

  spaced_numbers = [
    insert_spaces(vanity_number) + " next number"
    if i < len(vanity_numbers_list) - 1 else insert_spaces(vanity_number)
    for i, vanity_number in enumerate(vanity_numbers_list)
  ]

  print(spaced_numbers)
  print(message + "".join(spaced_numbers))

  return message

def insert_spaces(vanity_number=str):
  spaced_number = ""

  for char in vanity_number:
    if char.isalpha():
      spaced_number += f"{char}"
    elif char == " ":
      spaced_number += ""
    elif not char.isalpha() and not char.isnumeric():
      spaced_number += " "
    else:
      spaced_number += f" {char} "


  return spaced_number
test = ['+1-419-DORK132', '+1-419-FORK132', '+1-419-FORL132', '+1-419-DOP5132', '+1-419-DOR5132']
get_response_message(test)
