import unittest

def calc_avg(num):
    sumNum = 0
    for i in num:
        sumNum = sumNum + i
    length = len(num)

    avg = ( sumNum / length) if length != 0 else 0
    return avg

class testCase(unittest.TestCase):

    def test_func(self):
        self.assertEqual(calc_avg([1,3,5,7,9]), 5)
        self.assertEqual(calc_avg([1,3,5,7,9]), 25)

    def test_emptyList(self):
        self.assertTrue(calc_avg([1,2,3,4,5]))
        self.assertTrue(calc_avg([]))

    def test_divZero(self):
        with self.assertRaises(ValueError):
            calc_avg([])
        with self.assertRaises(ValueError):
            calc_avg([1,2,3,4])    


if __name__ == '__main__':
    unittest.main()
