import unittest

def volCube(l, w, h):
    if l < 0 or w < 0 or h < 0:
        raise ValueError('Can not be negative number!')
    return l * w * h

class testCase(unittest.TestCase):

    def test_def(self):
        result = volCube(4, 4, 3)
        self.assertEqual(result, 48)

    def test_negV(self):
        with self.assertRaises(ValueError):
            volCube(5, 5, -5)

    def test_typo(self):
        self.assertIsInstance(volCube(4, 4, 3), int)

        


if __name__ == '__main__':
    unittest.main()