from get_response_message import get_response_message
from find_vanity_numbers import find_words
from time_test import test_phone_numbers


def test_get_reponse_output(phone_number):
  vanity_numbers_list = find_words(phone_number)

  response_message = get_response_message(vanity_numbers_list)


  print(response_message)



test_get_reponse_output(test_phone_numbers[0])
