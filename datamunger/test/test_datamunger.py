import unittest
import datamunger


class TestDatamunger(unittest.TestCase):
    def test_total(self):
        row = [811, 78, 146, 55, 51, 254, 103, 57, 67, 0]
        result = datamunger.calc_total(row)
        self.assertEqual(result, 811)

    def test_row1(self):
        n = 20
        prev = ['811', '78', '146', '55', '51', '254', '103', '57', '67', '0']
        curr = [823, 82, 147, 55, 53, 256, 104, 58, 68, 0]
        result = datamunger.check_row(n, prev, curr)
        self.assertEqual(result, True)

    def test_row2(self):
        n = 53
        prev = ['1856', '232', '279', '169', '254',
                '358', '314', '109', '141', '190']
        curr = [1955, 240, 295, 175, 270, 366, 357, 119, 133, 192]
        result = datamunger.check_row(n, prev, curr)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
