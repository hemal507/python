def isMonotonous(sequence):
    if len(sequence) == 1 :
        return True
    isAscending = sequence[1] > sequence[0]
    for i in range(len(sequence)-1) :
        if isAscending :
            if sequence[i] >= sequence[i+1] :
                return False
        elif not isAscending :
            if sequence[i] <= sequence[i+1] :
                return False
    return True
    
import unittest
class TestMonotonous(unittest.TestCase) :
        def test_case1(self) :
                self.assertEqual(isMonotonous(1,4,7),True)
                print('Test case 1 passed')
        def test_case2(self) :
                self.assertEqual(isMonotonous(9),True)
                print('Test case 2 passed')
        def test_case3(self) :
                self.assertEqual(isMonotonous(1,9,7),False)
                print('Test case 3 passed')

if __name__ == '__main__' :
        unittest.main()
