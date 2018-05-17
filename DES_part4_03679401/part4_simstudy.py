from counter import TimeIndependentAutocorrelationCounter, TimeIndependentCrosscorrelationCounter
from simulation import Simulation
from simparam import SimParam
import random
import warnings
import pylab
"""
This file should be used to keep all necessary code that is used for the verification and simulation section in part 4
of the programming assignment. It contains tasks 4.2.1, 4.3.1 and 4.3.2.
"""

def task_4_2_1():
    """
    Execute exercise 4.2.1, which is basically just a test for the auto correlation.
    """
    # TODO Task 4.2.1: Your code goes here
    list1 = [1.,-1., 1.,-1., 1.,-1.,1.,-1.,1.,-1., 1.,-1., 1.,-1.,1.,-1.,1.,-1., 1.,-1., 1.,-1.,1.,-1.]
    list2 = [1., 1.,-1., 1., 1.,-1.,1., 1.,-1.,1., 1.,-1., 1., 1.,-1.,1., 1.,-1.,1., 1.,-1., 1., 1.,-1.,1., 1.,-1.]
    TIAC1 = TimeIndependentAutocorrelationCounter("EX1")
    TIAC2 = TimeIndependentAutocorrelationCounter("EX2")
    for i in range(len(list1)):
        TIAC1.count(list1[i])
    for i in range(len(list2)):
        TIAC2.count(list2[i])
    print "The Autocorrelation for the example 1 with  (lag%2 = 0) : ",  TIAC1.get_auto_cov(0)
    print "The Autocorrelation for the example 1 with  (lag%2 = 1) : ",  TIAC1.get_auto_cov(1)
    print "The Autocorrelation for the example 2 with  (lag%3 = 0) : ",  TIAC2.get_auto_cov(0)
    print "The Autocorrelation for the example 2 with  (lag%3 = 1) : ",  TIAC2.get_auto_cov(1)
    print "The Autocorrelation for the example 2 with  (lag%3 = 2) : ",  TIAC2.get_auto_cov(2)

def task_4_3_1():
    """
    Run the correlation tests for given rho for all correlation counters in counter collection.
    After each simulation, print report results.
    SIM_TIME is set higher in order to avoid a large influence of startup effects
    """
    # TODO Task 4.3.1: Your code goes here
    rho =[0.01, 0.5, 0.8, 0.95]
    sim_param = SimParam()
    random.seed(sim_param.SEED)
    sim = Simulation(sim_param)
    sim.sim_param.SIM_TIME = 1000000
    sim.sim_param.S = 10000
    for r in rho:
        print "---------- rho = ,",r," ---------"
        sim.sim_param.RHO = r
        sim.reset()
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            sim.do_simulation()
        print "Correlation    between    IAT    and    waiting     time   of  a packet           : ", sim.counter_collection.cnt_iat_wt.get_cor()
        print "Correlation    between    IAT    and    serving     time   of  a packet           : ", sim.counter_collection.cnt_iat_st.get_cor()
        print "Correlation between IAT and system time (waiting time + serving time) of a packet : ", sim.counter_collection.cnt_iat_syst.get_cor()
        print "Correlation    between    service time and system   time   of a packet            : ", sim.counter_collection.cnt_st_syst.get_cor()
        print "Auto-correlation  of  waiting  time  with  lags  ranging  from  1  to  20         : ", sim.counter_collection.acnt_wt.get_auto_cor(2)

def task_4_3_2():
    """
    Exercise to plot auto correlation depending on lags. Run simulation until 10000 (or 100) packets are served.
    For the different rho values, simulation is run and the blocking probability is auto correlated.
    Results are plotted for each N value in a different diagram.
    Note, that for some seeds with rho=0.DES and N=100, the variance of the auto covariance is 0 and returns an error.
    """
    # TODO Task 4.3.2: Your code goes here
    data_n_100 = []
    data_n_10000 = []
    lags = range(21)
    del lags[0]
    sim_param = SimParam()
    random.seed(sim_param.SEED)
    sim = Simulation(sim_param)
    sim.sim_param.SIM_TIME = 1000000
    sim.sim_param.S = 10000
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        sim.do_simulation_n_limit(100)
    for i in lags:
        data_n_100.append(sim.counter_collection.acnt_wt.get_auto_cor(i))
    sim.reset()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        sim.do_simulation_n_limit(10000)
    for i in lags:
        data_n_10000.append(sim.counter_collection.acnt_wt.get_auto_cor(i))
    pylab.figure(1)
    pylab.xlabel('lag')
    pylab.ylabel('Auto Correlation')
    pylab.title('Auto Correlation of Waiting Times (n=100) for lags ranging from 1 to 20')
    pylab.plot(lags,data_n_100)
    pylab.figure(2)
    pylab.xlabel('lag')
    pylab.ylabel('Auto Correlation')
    pylab.title('Auto Correlation of Waiting Times (n=10000) for lags ranging from 1 to 20')
    pylab.plot(lags,data_n_10000)
    pylab.show()


#task_4_2_1()
task_4_3_1()
#task_4_3_2()