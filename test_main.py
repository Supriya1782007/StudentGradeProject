
import unittest

def calculate_grade(average):
    if average >= 90:
        return "S"
    elif average >= 80:
        return "A"
    elif average >= 65:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


class TestGrade(unittest.TestCase):

    def test_s_grade(self):
        self.assertEqual(calculate_grade(95), "S")

    def test_a_grade(self):
        self.assertEqual(calculate_grade(85), "A")

    def test_b_grade(self):
        self.assertEqual(calculate_grade(70), "B")

    def test_c_grade(self):
        self.assertEqual(calculate_grade(55), "C")

    def test_d_grade(self):
        self.assertEqual(calculate_grade(45), "D")

    def test_f_grade(self):
        self.assertEqual(calculate_grade(30), "F")


if __name__ == "__main__":
    unittest.main()
