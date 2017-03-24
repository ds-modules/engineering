import numpy as np
import unittest
import lab2


def assertTuple(self, t1, t2, err=""):
    for v1, v2 in zip(t1, t2):
        if np.isnan(v1):
            self.assertTrue(np.isnan(v2))
        elif type(v1) is float:
            self.assertAlmostEqual(v1, v2, 7, err)
        else:
            self.assertEquals(v1, v2, err)


class TestQ1(unittest.TestCase):
    def test_q1(self):
        ans1 = (0.8414709848078965, 0.84146825396825398, -2.7308396425285153e-06, -3.2453164658457615e-06)
        ans2 = (-0.9589242746631385, -5.2926587301587276, -4.3337344554955894, 4.5193708929915157)
        ans3 = (0.9589242746631385, 5.2926587301587276, 4.3337344554955894, 4.5193708929915157)
        ans4 = (0.0, 0.0, 0.0, np.nan)
        assertTuple(self, lab2.my_sin_approx(1), ans1)
        assertTuple(self, lab2.my_sin_approx(5), ans2)
        assertTuple(self, lab2.my_sin_approx(-5), ans3)
        assertTuple(self, lab2.my_sin_approx(0), ans4)
        print('Question 1 Passed!')


if __name__ == '__main__':
    unittest.main()
