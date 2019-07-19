'''
Two players - "black" and "white" are playing a game. The game consists of several rounds. If a player wins in a round, he is to move again during the next round. If a player loses a round, it's the other player who moves on the next round. Given whose turn it was on the previous round and whether he won, determine whose turn it is on the next round.
'''
def whoseMove(lastPlayer, win):
    if (lastPlayer == "black" and win == True) or (lastPlayer == "white" and win == False):
        return "black"
    elif (lastPlayer == "black" and win == False) or (lastPlayer == "white" and win == True):
        return "white"

import unittest

class TestMove(unittest.TestCase) :
	def test_case1(self) :
		self.assertEqual(whoseMove("black" , False),"white")
		print('Test case 1 is passed')
        def test_case2(self) :
                self.assertEqual(whoseMove("white" , False),"black")
                print('Test case 2 is passed')
        def test_case3(self) :
                self.assertEqual(whoseMove("black" , True),"black")
                print('Test case 3 is passed')
        def test_case4(self) :
                self.assertEqual(whoseMove("white" , True),"white")
                print('Test case 4 is passed')

if __name__ == '__main__':
	unittest.main()

