import unittest
import CasinoGame


class DummyCroupier:
	pass

class TestCasinoGame(unittest.TestCase):
	"""
	Unit test for the class Roulette
	"""

	def setUp(self):
		# To test this cass we will use
		# fixed values instead of randoms
		# and we will use only one minimum
		# bet in a list to be selected
		# delebretly
		# we also use a dummy croupoier just
		# for testing purpuses
		dummyCroupier = DummyCroupier()
		self.gameUnerTest = CasinoGame.CasinoGame(
			(0, 40),
			[20],
			lambda: 1,
			lambda x, y: x*y,
			dummyCroupier
		)

	def test_minimum_bet(self):
		# This is the only element we put in the list 20
		self.assertEqual(self.gameUnerTest.minimum_bet, 20)

	def test_guess_not_acceptable(self):
		with self.assertRaises(ValueError):
			self.gameUnerTest.Start([57])

	def test_amount_not_acceptable(self):
		with self.assertRaises(TypeError):
			self.gameUnerTest.AboveMinimum(['300'])

	def test_AboveMinimum(self):
		self.assertEqual(
			self.gameUnerTest.AboveMinimum([100, 10, 122]),
			[1, 0, 1])

	def test_Start(self):
		self.assertEqual(
			self.gameUnerTest.Start([1, 24, 29, 12]),
			(1, [1, 0, 0, 0])
		)

	def test_SimulateGame_case_1_winner(self):
		self.assertEqual(
			self.gameUnerTest.SimulateGame([19, 10, 122]),
			[29, [0, 0, 122]]
		)

	def test_SimulateGame_case_2_winner(self):
		self.assertEqual(
			self.gameUnerTest.SimulateGame([100, 122]),
			[0, [100, 122]]
		)

if __name__ == '__main__':
    unittest.main()
