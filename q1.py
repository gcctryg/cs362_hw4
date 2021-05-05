import unittest

def volCube(l, w, h):
    if l < 0 or w < 0 or h < 0:
        raise ValueError('Can not be negative number!')
    return l * w * h

class testCase(unittest.TestCase):

    def test_def(self):
        result = volCube(4, 4, 3)
        #pass
        self.assertEqual(result, 48)
        #fail
        self.assertEqual(result, 5)

    def test_negV(self):
        #pass
        with self.assertRaises(ValueError):
            volCube(5, 5, -5)
        #fail
        with self.assertRaises(ValueError):
            volCube(5, 5, 5)

    def test_typo(self):
        #pass
        self.assertIsInstance(volCube(4, 4, 3), int)
        #fail
        self.assertIsInstance(volCube(4, 4, 4.5), int)

        


if __name__ == '__main__':
    unittest.main()