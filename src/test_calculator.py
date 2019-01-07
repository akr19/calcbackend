import unittest
from calculator import Calculator
from calculator import DBTest

class TddInPythonExample(unittest.TestCase):

    def test_calculator_add_method_returns_correct_result(self):
        """
        ensure calc adding number works
        """
        calc = Calculator()
        result = calc.add(2,2)
        self.assertEqual(4, result)

    def test_calculator_add_method_works_with_minus_values(self):
        """
        Ensure calc works with minus values
        """
        calc = Calculator()
        result = calc.add(-2,2)
        self.assertEqual(0, result)

    def test_calculator_get_values_from_db(self):
	"""
	Ensure calc can get values from database
	"""
        dbtest = DBTest()
        result = dbtest.get_values()
	self.assertEqual("[<MyTable(b040e5fa-0610-11e9-89a0-000d3a22998e, me)>\n]", result)

if __name__ == '__main__':
    unittest.main()



