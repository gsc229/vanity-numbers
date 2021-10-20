import unittest
# from find_vanity_numbers import find_words

from time_test import test_phone_numbers, time_test


class TestFindVainityNumbers(unittest.TestCase):
  def test_less_fifty_ms(self):
    self.assertLess(time_test(test_phone_numbers)[0], 0.05)
    self.assertLess(time_test(test_phone_numbers)[1], 0.05)
    self.assertLess(time_test(test_phone_numbers)[2], 0.05)



if __name__ == '__main__':
  unittest.main()
