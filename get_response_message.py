def get_response_message(vanity_numbers_list):

  message = "Your vanity numbers are "

  spaced_numbers = [
    insert_spaces(vanity_number) + " next number"
    if i < len(vanity_numbers_list) - 1 else insert_spaces(vanity_number)
    for i, vanity_number in enumerate(vanity_numbers_list)
  ]

  return message + "".join(spaced_numbers)

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
