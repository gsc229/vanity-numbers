import time
from find_vanity_numbers import find_words

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

# "+14199374482" - Has seven letter word
# "+14193204052" - Has limited word combinations
test_phone_numbers = ["+14199374482", "+14193204052", "14193673981"]

time_test(test_phone_numbers)
