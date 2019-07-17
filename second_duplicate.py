def firstDuplicate(a) :
        pos = len(a)
        for i in range(len(a)-1) :
                for j in range(i+1,len(a)) :
                        if a[i] == a[j] :
                                if pos > j :
                                        pos = j
        if pos == len(a) :
                return -1
        else :
                return a[pos]


def alternative(a) :
        if len(a) == len(set(a)) :
                return -1
        all_repeated_elemets = set([x for x in a if a.count(x) > 1])
        pos = []
        for i in all_repeated_elemets :
                pos.append([j for j, x in enumerate(a) if x == i][1])
        return a[min(pos)]

import unittest
class TestDups(unittest.TestCase) :
        def test_case1(self) :
                self.assertEqual(firstDuplicate([2,1,3,5,3,2]),3)
                print('Test case #1 is passed')
        def test_case2(self) :
                self.assertEqual(firstDuplicate([2,2]),2)
                print('Test case #2 is passed')
        def test_case3(self) :
                self.assertEqual(firstDuplicate([2,4,3,5,1]),-1)
                print('Test case #3 is passed')
        def test_case4(self) :
                self.assertEqual(alternative([2,1,3,5,3,2]),3)
                print('Test case #1 is passed')
        def test_case5(self) :
                self.assertEqual(alternative([2,2]),2)
                print('Test case #2 is passed')
        def test_case6(self) :
                self.assertEqual(alternative([2,4,3,5,1]),-1)
                print('Test case #3 is passed')

if __name__ == '__main__':
        unittest.main()

