from statistictests import ChiSquare
import numpy

"""
This file should be used to keep all necessary code that is used for the verification section in part 6
of the programming assignment. It contains task 6.2.1.
"""

def task_6_2_1(alpha, mu, sigma,norm_camp=True,num_bins = 10):
    """
    This task is used to verify the implementation of the chi square test.
    First, 100 samples are drawn from a normal distribution. Afterwards the chi square test is run on them to see,
    whether they follow the original or another given distribution.
    """
    # TODO Task 6.2.1: Your code goes here
    data = numpy.random.normal(mu, sigma, 100)
    emp_x = [-100.0]
    for i in range(num_bins-1):
        emp_x.append(-(float(num_bins)/4-0.5) + i*0.5)
    emp_x.append(100.0)
    emp_x = numpy.array(emp_x)
    for i in range(len(emp_x)):
        emp_x[i] += mu
    classif = numpy.histogram(data, bins=emp_x)
    emp_n = classif[0]
    chi2 = ChiSquare(emp_x,emp_n,"normal distribution")
    if norm_camp:
        [chisq, p] = chi2.test_distribution(alpha, 0.0, 1.0)
    else:
        [chisq, p] = chi2.test_distribution(alpha, mu, sigma*sigma)
    if norm_camp:
        if chisq<=p:
            print "The samples follow the standard normal distribution : alpha=",alpha,"mu=",mu,"sigma=",sigma
        else:
            print "The samples don't follow the standard normal distribution : alpha=",alpha,"mu=",mu,"sigma=",sigma
    else:
        if chisq<=p:
            print "The samples follow the given normal distribution : alpha=",alpha,"mu=",mu,"sigma=",sigma
        else:
            print "The samples don't follow the given normal distribution : alpha=",alpha,"mu=",mu,"sigma=",sigma

if __name__ == '__main__':
    """print "*** Comparing to the standard normal distribution : "
    print "* varying the significance level :"
    task_6_2_1(0.05,0.0,1.0)
    task_6_2_1(0.1,0.0,1.0)
    task_6_2_1(0.2,0.0,1.0)
    task_6_2_1(0.3,0.0,1.0)
    task_6_2_1(0.4,0.0,1.0)

    print "* varying the number of bins : "
    task_6_2_1(0.05,0.0,1.0,True,20)
    task_6_2_1(0.05,0.0,1.0,True,18)
    task_6_2_1(0.05,0.0,1.0,True,16)
    task_6_2_1(0.05,0.0,1.0,True,14)
    task_6_2_1(0.05,0.0,1.0,True,12)

    print "* varying the mu : "
    task_6_2_1(0.05,1.0,1.0)
    task_6_2_1(0.05,2.0,1.0)

    print "* varying the variance : "
    task_6_2_1(0.05,0.0,2.0)
    task_6_2_1(0.05,0.0,3.0)
    task_6_2_1(0.05,0.0,4.0)

    print ""

    print "*** Comparing to the same normal distribution as generating : "
    print "* varying the mu : "
    task_6_2_1(0.05,1.0,1.0,False)
    task_6_2_1(0.05,2.0,1.0,False)

    print "* varying the variance : "
    task_6_2_1(0.05,0.0,2.0,False)
    task_6_2_1(0.05,0.0,3.0,False)
    task_6_2_1(0.05,0.0,4.0,False)"""
