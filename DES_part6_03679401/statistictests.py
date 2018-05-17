import scipy.stats
import math
import numpy

class ChiSquare(object):

    def __init__(self, emp_x, emp_n, name="default"):
        """
        Initialize chi square test with observations and their frequency.
        :param emp_x: observation values (bins)
        :param emp_n: frequency
        :param name: name for better distinction of tests
        """
        self.name = name
        # TODO Task 6.1.1: Your code goes here
        self.emp_x = emp_x.tolist()
        self.emp_n = emp_n.tolist()

    def test_distribution(self, alpha, mean, var):
        """
        Test, if the observations fit into a given distribution.
        :param alpha: significance of test
        :param mean: mean value of the gaussian distribution
        :param var: variance of the gaussian distribution
        """
        # TODO Task 6.1.1: Your code goes here
        #combination of neighboring intervals
        b = True
        for i in range(len(self.emp_n)):
            if self.emp_n[i]<5:
                b = False
        while not b:
            self.emp_n[0] +=self.emp_n[1]
            self.emp_n[len(self.emp_n)-1] += self.emp_n[len(self.emp_n)-2]
            del self.emp_n[len(self.emp_n)-2]
            del self.emp_n[1]
            del self.emp_x[len(self.emp_x)-2]
            del self.emp_x[1]
            b = True
            for i in range(len(self.emp_n)):
                if self.emp_n[i]<5:
                    b = False
            if len(self.emp_n)<6:
                b = True

        #test distribution
        emp_n_excepted = []
        sum = float(numpy.sum(self.emp_n))
        for i in range(len(self.emp_n)):
            emp_n_excepted.append((scipy.stats.norm.cdf(self.emp_x[i+1],loc=mean,scale=math.sqrt(var))
                                  - scipy.stats.norm.cdf(self.emp_x[i],loc=mean,scale=math.sqrt(var)))*sum)
        [chisq, p_value] = scipy.stats.chisquare(self.emp_n, emp_n_excepted, len(self.emp_n)-2)
        p = scipy.stats.chi2.ppf(q=1-alpha, df=len(self.emp_n)-1)
        return [chisq, p]
