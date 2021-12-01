import unittest
from BlackJack import *
#from PlayingCard import *
from TestInput import TestInput

class Test(unittest.TestCase):

    test = BlackJack()


    
    def test_valid_deal_input(self):
        test_input = TestInput()
        self.test.set_user_input(test_input)
        test_input.set_test_inputs(["D","S"])
        result = self.test.valid_deal_input()
        self.assertTrue("D"== result)
        
    def test_score(self):
        result = self.test.score_hand(["A6", "S7"])
        self.assertGreater(result, 0)

    def test_deal_to_player(self):
        result = self.test.deal_to_player(["H4", "H4", "S10", "C5"], ["SK", "HK"])
        self.assertFalse(result)

    def test_initialise_comp_risk(self):
        for x in range(10000):
            result = self.test.initialise_computer_risk(2)
            riskCorrect = False
            for i in range (0, len(result)):
                if result[i+1]>1  and result[i+1] < 10:
                    riskCorrect = True
            self.assertTrue(riskCorrect)
    
    

def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()