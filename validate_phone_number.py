import re

def validate_phone_number(phone_number):
  """ Takes in a phone number and performs checks:
      1. The phone number is a string
      2. Checks for and removes any non-numerical characters.
      3. The phone number has 11 digits
      4. The area code of the phone number is 1
      Returns a dictionary with, valid: boolean, country_code: string (1), area_code: string
      and seven_digit_phone_number: string.
  """
  if isinstance(phone_number, str) is False:
    return { "valid": False }

  # use regex to get only digits
  sanitized_number = "".join(re.findall(r"\d", phone_number))

  if len(sanitized_number) != 11:
    return { "valid": False }

  if sanitized_number[0] != "1":
    return { "valid": False }

  return {
    "valid": True,
    "country_code": sanitized_number[0],
    "area_code": sanitized_number[1:4],
    "seven_digit_phone_number": sanitized_number[-7:]
  }
