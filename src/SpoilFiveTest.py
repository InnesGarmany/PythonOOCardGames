import unittest
from SpoilFive import *
from PlayingCard import *
from TestInput import TestInput

class Test(unittest.TestCase):

    test = SpoilFive()

    def test_start_round(self):
        test_input = TestInput()
        test_input.set_test_inputs([4])
        self.test.set_user_input(test_input)
        result = self.test.start_round()
        self.assertTrue(len(result) == 4)

    def test_determine_trump(self):
        result = self.test.determineTrump(["H6", "S8", "DK"])
        self.assertEqual("D", result )

    def test_player_turn(self):
        test_input = TestInput()
        test_input.set_test_inputs(["C5"])
        self.test.set_user_input(test_input)
        result = self.test.player_turn(["C5", "D7", "H2"])
        self.assertTrue(result == "C5")

    def test_set_hierarchy(self):
        result = self.test.setHierarchy("H", "S")
        self.assertTrue(result[0] == "H5")

def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()

