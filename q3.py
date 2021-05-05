import unittest

def getFull(fn, ln):
    return '{} {}'.format(fn, ln)

class testCase(unittest.TestCase):

    def test_def(self):
        #pass
        self.assertEqual(getFull('travis', 'scott'), 'travis scott')
        #fail
        self.assertEqual(getFull('bruce', 'lee'), 'bruceLee')

    def test_str(self):
        #pass
        self.assertIsInstance(getFull('Ali', 'Wilson'), str)
        #fail
        self.assertIsInstance(getFull('Ali', 'Wilson'), int)

    def test_empty(self):
        
        container = 'James bond : Spectre'
        #pass
        self.assertIn(getFull('James', 'bond'), container)
        #fail
        self.assertIn(getFull('daniel', 'craig'), container)

if __name__ == '__main__':
    unittest.main()