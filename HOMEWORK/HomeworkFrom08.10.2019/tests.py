import unittest

from main import test_money, test_answer, test_recorder


class BotTest(unittest.TestCase):
    def test_money(self):
        self.assertEqual(test_money, 'BYN')

    def test_answer(self):
        self.assertIsInstance(test_answer, dict)

    def test_recorder(self):
        self.assertIsNone(test_recorder)


if __name__ == '__main__':
    unittest.main()
