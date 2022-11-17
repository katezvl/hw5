import unittest
from issue3 import fit_transform


class TestIssue3(unittest.TestCase):
    def test_1(self):
        actual = fit_transform('cold', 'hot')
        expected = [('cold', [0, 1]), ('hot', [1, 0])]
        self.assertEqual(actual, expected)

    def test_2(self):
        actual = fit_transform('cold', 'hot', 'warm')
        expected = [('cold', [0, 0, 1]), ('hot', [0, 1, 0]), ('warm', [1, 0, 0])]
        self.assertEqual(actual, expected)

    def test_3(self):
        actual = fit_transform('red', 'blue')
        expected = [([1, 1], [1, 1])]
        self.assertNotIn(actual, expected)

    def test_4(self):
        with self.assertRaises(TypeError):
            fit_transform(5)
