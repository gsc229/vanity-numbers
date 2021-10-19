import os
import time
from find_vanity_numbers import find_words

TEST_NUMBER_1 = os.getenv("TEST_NUMBER_1")
TEST_NUMBER_2 = os.getenv("TEST_NUMBER_2")
TEST_NUMBER_3 = os.getenv("TEST_NUMBER_3")
TEST_NUMBER_4 = os.getenv("TEST_NUMBER_4")
TEST_NUMBER_5 = os.getenv("TEST_NUMBER_5")

def time_test(test_numbers):
  print(f"TEST NUMBERS: {test_numbers}")
  total_times = []
  for count, phone_number in enumerate(test_numbers):
    t0fw = time.time()
    find_words_result = find_words(phone_number)
    t1fw = time.time()
    fw_total_time = t1fw - t0fw
    total_times.append(fw_total_time)
    print("=================================================")
    print(f"Test No. {count} Phone Number: {phone_number}\n")
    print(f"Find Word Time: {fw_total_time}")
    print(f"{find_words_result}\n")

  return total_times


test_phone_numbers = [
  TEST_NUMBER_1,
  TEST_NUMBER_2,
  TEST_NUMBER_3,
  TEST_NUMBER_4,
  TEST_NUMBER_5,
]

time_test(test_phone_numbers)
