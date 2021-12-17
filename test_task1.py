import unittest
from main import count_digit


class CountDigitsTest(unittest.TestCase):

    def setUp(self) -> None:
        self.num_list = [1, 1, 3, 2, 1, 3, 4]
        self.answer = {
            1: 3,
            2: 1,
            3: 2,
            4: 1
        }

    def test_succesful_work(self):
        self.assertEqual(count_digit(self.num_list), self.answer)


if __name__ == '__main__':
    unittest.main()

