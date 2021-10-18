import time
from find_vanity_numbers import find_words

def time_test(test_numbers):
  for count, phone_number in enumerate(test_numbers):
    t0fw = time.time()
    find_words_result = find_words(phone_number)
    t1fw = time.time()
    fw_total_time = t1fw - t0fw
    print("=================================================")
    print(f"Test No. {count} Phone Number: {phone_number}\n")
    print(f"Find Word Time: {fw_total_time}")
    print(f"{find_words_result}\n")


# "+14199374482" - Has seven letter word
# "+14193204052" - Has limited word combinations
test_phon_numbers = ["+14199374482", "+14193204052"]

time_test(test_phon_numbers)
