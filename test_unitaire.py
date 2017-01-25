import unittest
import Roulette

from unittest import mock


# to avoid wasting time with random range
# we will mock it to return the save value all the
# time during our testing


class TestRoulette(unittest.TestCase):
    """
    Unit test for the class Roulette
    """

    def setUp(self):
        self.gameUnerTest = Roulette.Roulette(100)

    def test_minimum_bet(self):
        self.assertEqual(self.gameUnerTest.minimum_bet, 100)

    def test_guess_not_acceptable(self):
        with self.assertRaises(ValueError):
            self.gameUnerTest.SpinTheWheel([37])

    def test_amount_not_acceptable(self):
        with self.assertRaises(TypeError):
            self.gameUnerTest.AboveMinimum(['300'])

    def test_AboveMinimum(self):
        self.assertEqual(
            self.gameUnerTest.AboveMinimum([100, 10, 122]),
            [1, 0, 1])

    @mock.patch('Roulette.random.randrange')
    def test_SpinTheWheel(self, fake_random):
        # This will mock the random
        fake_random.return_value = 24
        self.assertEqual(
            self.gameUnerTest.SpinTheWheel([24, 29, 12]),
            (24, [1, 0, 0])
        )

    @mock.patch('Roulette.random.randrange')
    def test_SimulateGame_case_1_winner(self, fake_random):
        fake_random.return_value = 24
        self.assertEqual(
            self.gameUnerTest.SimulateGame([24, 29, 12], [100, 10, 122]),
            [132, [3000, 0, 0]]
        )

    @mock.patch('Roulette.random.randrange')
    def test_SimulateGame_case_2_winner(self, fake_random):
        fake_random.return_value = 4
        self.assertEqual(
            self.gameUnerTest.SimulateGame([24, 4, 29, 4, 12], [100, 122, 10, 390, 122]),
            [232, [0, 3660, 0, 11700, 0]]
        )


if __name__ == '__main__':
    unittest.main()