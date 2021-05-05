import unittest

def calc_avg(num):
    if len(num) == 0:
        raise ValueError('Can not divided by zero!')
    sumNum = 0
    for i in num:
        sumNum = sumNum + i

    avg = sumNum / len(num)
    return avg

class testCase(unittest.TestCase):

    def test_func(self):
        self.assertEqual(calc_avg([1,3,5,7,9]), 5)

    def test_emptyList(self):
        self.assertTrue(calc_avg([1,2,3,4,5]))

    def test_divZero(self):
        with self.assertRaises(ValueError):
            calc_avg([])



if __name__ == '__main__':
    unittest.main()
