import unittest
from vanitynumbers import get_word_groups, get_number_map

number_map = get_number_map()

class TestWordGroups(unittest.TestCase):
  def test_if_six_groups(self):
    self.assertTrue(len(get_word_groups("5555555", number_map)) == 6)


if __name__ == '__main__':
  unittest.main()
