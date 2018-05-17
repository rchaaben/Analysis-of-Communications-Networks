import unittest
from counter import TimeIndependentAutocorrelationCounter, TimeIndependentCrosscorrelationCounter
import numpy
class DESTest(unittest.TestCase):

    """
    This python unittest class checks the fourth part of the programming assignment for basic functionality.
    """

    def test_cross_correlation(self):
        """
        Test the basic implementation of the cross covariance counter.
        """
        ticcc = TimeIndependentCrosscorrelationCounter()

        ticcc.count(1, 5)
        ticcc.count(2, 7)
        ticcc.count(6, 3)
        ticcc.count(3, 3)
        ticcc.count(4, 5)
        self.assertAlmostEqual(ticcc.get_cov(), -1.52, delta=.01,
                               msg="Error in TimeIndependentCrosscorrelationCounter. Covariance calculation is wrong.")
        self.assertAlmostEqual(ticcc.get_cor(), -.4722, delta=.01,
                               msg="Error in TimeIndependentCrosscorrelationCounter. Correlation calculation is wrong.")

    def test_auto_correlation(self):
        """
        Test the basic implementation of the auto covariance counter.
        """
        tiacc = TimeIndependentAutocorrelationCounter(max_lag=5)

        tiacc.count(1)
        tiacc.count(2)
        tiacc.count(3)
        tiacc.count(1)
        tiacc.count(2)
        tiacc.count(3)

        results_cov = [2./3., -.2, -.5, 2./3., 0., -1.]
        results_cor = [5./6., -.25, -.625, 5./6., 0., -1.25]

        for lag in range(5):
            self.assertAlmostEqual(tiacc.get_auto_cov(lag), results_cov[lag], delta=.01,
                               msg="Error in TimeIndependentAutocorrelationCounter. Covariance calculation is wrong.")
            self.assertAlmostEqual(tiacc.get_auto_cor(lag), results_cor[lag], delta=.01,
                               msg="Error in TimeIndependentAutocorrelationCounter. Correlation calculation is wrong.")

if __name__ == '__main__':
    unittest.main()
