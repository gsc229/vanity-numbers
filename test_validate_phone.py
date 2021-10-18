import unittest
from validate_phone_number import validate_phone_number

class TestValidateNumber(unittest.TestCase):
  def test_non_number_str(self):
    # Test validy if string without numbers is passed
    self.assertFalse(validate_phone_number("PIZZA")["valid"])
    self.assertFalse(validate_phone_number(12345678912)["valid"])
    self.assertTrue(validate_phone_number("PIZZA+16185555555PIZZA")["valid"])

  def test_number_length(self):
    self.assertTrue(validate_phone_number("16185555555")["valid"])
    self.assertFalse(validate_phone_number("123")["valid"])

  def test_country_code(self):
    self.assertFalse(validate_phone_number("86185555555")["valid"])
    self.assertTrue(validate_phone_number("+16185555555")["valid"])
    self.assertTrue(validate_phone_number("+16185555555")["country_code"] == "1")

  def test_area_code(self):
    self.assertTrue(validate_phone_number("+16185555555")["area_code"] == "618")


if __name__ == '__main__':
  unittest.main()
