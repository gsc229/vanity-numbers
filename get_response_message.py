def get_response_message(vanity_numbers_list):

  message = "Your vanity numbers are "

  spaced_numbers = [
    insert_spaces(vanity_number) + "<break/>next number<break/>"
    if i < len(vanity_numbers_list) - 1 else insert_spaces(vanity_number)
    for i, vanity_number in enumerate(vanity_numbers_list)
  ]

  return message + "".join(spaced_numbers)

def insert_spaces(vanity_number=str):
  spaced_number = ""

  for char in vanity_number:
    if char.isalpha() or char.isnumeric():
      spaced_number += f"<break/>{char}"


  return spaced_number
