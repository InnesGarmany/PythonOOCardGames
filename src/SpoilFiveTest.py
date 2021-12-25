import unittest
from SpoilFive import *
from PlayingCard import *
from TestInput import TestInput
from Player import *

class Test(unittest.TestCase):

    test = SpoilFive(["D2", "S6", "S2"])
    testPlayer = Player(["C5", "D7", "H2", "SK"])

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
        self.test.leadingSuit = "S"
        test_input = TestInput()
        test_input.set_test_inputs(["H2", "SK"])
        self.test.set_user_input(test_input)
        result = self.test.player_turn(self.testPlayer)
        self.assertTrue(result == "SK")

    def test_player_turn_going_first(self):
        test_input = TestInput()
        test_input.set_test_inputs(["H2", "C5"])
        self.test.set_user_input(test_input)
        result = self.test.player_turn(self.testPlayer, True)
        self.assertTrue(result == "C5")

    def test_player_turn_illegal_play(self):
        self.test.leadingSuit = "C"
        test_input = TestInput()
        test_input.set_test_inputs(["C2", "SK"])
        self.test.set_user_input(test_input)
        result = self.test.player_turn(self.testPlayer)
        self.assertTrue(result == "C2")

    def test_set_hierarchy(self):
        result = self.test.setHierarchy("H", "S")
        self.assertTrue(result[0] == "H5")
    
    def test_CPU_turn_isLeading(self):
        result = self.test.CPU_turn(self.testPlayer, True)
        if result in self.testPlayer.hand:
            testPassed = True
        else:
            testPassed = False
        self.assertTrue(testPassed)
        
    def test_CPU_turn_isntLeading(self):
        result = self.test.CPU_turn(self.testPlayer)
        self.assertEqual(result, "H2")



def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()

