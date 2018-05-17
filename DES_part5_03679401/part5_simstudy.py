from counter import TimeIndependentCounter
from simulation import Simulation
from simparam import SimParam
from simresult import SimResult
from matplotlib import pyplot
import random
import warnings

"""
This file should be used to keep all necessary code that is used for the simulation section in part 5
of the programming assignment. It contains tasks 5.2.1, 5.2.2, 5.2.3 and 5.2.4.
"""

colors = ['k','y','g', 'r', 'c', 'm' ]
def task_5_2_1():
    """
    Run task 5.2.1. Make multiple runs until the blocking probability distribution reaches
    a confidence level alpha. Simulation is performed for 100s and 1000s and for alpha = 90% and 95%.
    """
    results = [None, None, None, None]
    TIC = TimeIndependentCounter("bp")

    # TODO Task 5.2.1: Your code goes here
    #SIM TIME:  100s; ALPHA: 10%
    sim_param = SimParam()
    random.seed(sim_param.SEED)
    sim = Simulation(sim_param)
    sim.sim_param.SIM_TIME = 100000
    sim.sim_param.S = 4
    sim.sim_param.RHO = 0.9
    for i in range(10000):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            TIC.count(sim.do_simulation().blocking_probability)
            if TIC.report_confidence_interval(0.1)<0.0015:
                results[0] = i
                break
            sim.reset()
    #SIM TIME:  100s; ALPHA:  5%
    TIC.reset()
    for i in range(10000):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            TIC.count(sim.do_simulation().blocking_probability)
            if TIC.report_confidence_interval(0.05)<0.0015:
                results[1] = i
                break
            sim.reset()
    #SIM TIME: 1000s; ALPHA: 10%
    sim.sim_param.SIM_TIME = 1000000
    TIC.reset()
    for i in range(10000):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            TIC.count(sim.do_simulation().blocking_probability)
            if TIC.report_confidence_interval(0.05)<0.0015:
                results[2] = i
                break
            sim.reset()
    #SIM TIME: 1000s; ALPHA:  5%
    sim.sim_param.SIM_TIME = 1000000
    TIC.reset()
    for i in range(10000):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            TIC.count(sim.do_simulation().blocking_probability)
            if TIC.report_confidence_interval(0.05)<0.0015:
                results[3] = i
                break
            sim.reset()

    # print and return results
    print "SIM TIME:  100s; ALPHA: 10%; NUMBER OF RUNS: " + str(results[0])
    print "SIM TIME:  100s; ALPHA:  5%; NUMBER OF RUNS: " + str(results[1])
    print "SIM TIME: 1000s; ALPHA: 10%; NUMBER OF RUNS:  " + str(results[2])
    print "SIM TIME: 1000s; ALPHA:  5%; NUMBER OF RUNS:  " + str(results[3])
    return results

def task_5_2_2():
    """
    Run simulation in batches. Start the simulation with running until a customer count of n=100 or (n=1000) and
    continue to increase the number of customers by dn=n.
    Count the blocking proabability for the batch and calculate the confidence interval width of all values, that have
    been counted until now.
    Do this until the desired confidence level is reached and print out the simulation time as well as the number of
    batches.
    """
    num_batches1 = 0
    num_batches2 = 0
    num_batches3 = 0
    num_batches4 = 0
    TIC = TimeIndependentCounter("bp")

    # TODO Task 5.2.2: Your code goes here
    sim_param = SimParam()
    random.seed(sim_param.SEED)
    sim = Simulation(sim_param)
    sim.sim_param.S = 4
    sim.sim_param.RHO = 0.9
    ## n = 100
    # ALPHA: 5%
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        TIC.count(sim.do_simulation_n_limit(100).blocking_probability)

    for i in range(10000):
        sim.sim_result = SimResult(sim)
        sim.sim_state.stop = False
        sim.sim_state.num_packets = 0
        sim.sim_state.num_blocked_packets = 0
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            TIC.count(sim.do_simulation_n_limit(100,True).blocking_probability)
            print TIC.report_confidence_interval(0.05)
            if TIC.report_confidence_interval(0.05)<0.0015:
                num_batches1 = i+1
                break
    t1 = sim.sim_state.now

    # ALPHA: 10%
    sim.reset()
    TIC.reset()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        TIC.count(sim.do_simulation_n_limit(100).blocking_probability)
    for i in range(10000):
        sim.sim_result = SimResult(sim)
        sim.sim_state.stop = False
        sim.sim_state.num_packets = 0
        sim.sim_state.num_blocked_packets = 0
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            TIC.count(sim.do_simulation_n_limit(100,True).blocking_probability)
            print TIC.report_confidence_interval(0.1)
            if TIC.report_confidence_interval(0.1)<0.0015:
                num_batches2 = i+1
                break
    t2 = sim.sim_state.now

    sim.reset()
    ## n = 1000
    # ALPHA: 5%
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        TIC.count(sim.do_simulation_n_limit(100).blocking_probability)

    for i in range(10000):
        sim.sim_result = SimResult(sim)
        sim.sim_state.stop = False
        sim.sim_state.num_packets = 0
        sim.sim_state.num_blocked_packets = 0
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            TIC.count(sim.do_simulation_n_limit(1000,True).blocking_probability)
            print TIC.report_confidence_interval(0.05)
            if TIC.report_confidence_interval(0.05)<0.0015:
                num_batches3 = i+1
                break
    t3 = sim.sim_state.now

    # ALPHA: 10%
    sim.reset()
    TIC.reset()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        TIC.count(sim.do_simulation_n_limit(100).blocking_probability)
    for i in range(10000):
        sim.sim_result = SimResult(sim)
        sim.sim_state.stop = False
        sim.sim_state.num_packets = 0
        sim.sim_state.num_blocked_packets = 0
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            TIC.count(sim.do_simulation_n_limit(1000,True).blocking_probability)
            print TIC.report_confidence_interval(0.1)
            if TIC.report_confidence_interval(0.1)<0.0015:
                num_batches4 = i+1
                break
    t4 = sim.sim_state.now

    # print and return both results
    print "N:  100; ALPHA:  5%; NUMBER OF BATCHES: " + str(num_batches1) +" and SIM TIME: " + str(t1)
    print "N:  100; ALPHA: 10%; NUMBER OF BATCHES: " + str(num_batches2) +" and SIM TIME: " + str(t2)
    print "N: 1000; ALPHA:  5%; NUMBER OF BATCHES: " + str(num_batches3) +" and SIM TIME: " + str(t3)
    print "N: 1000; ALPHA: 10%; NUMBER OF BATCHES: " + str(num_batches4) +" and SIM TIME: " + str(t4)

    return [t1, t2, t3, t4]

def task_5_2_4(rho, alpha, sim_time,num):
    """
    Plot confidence interval as described in the task description for task 5.2.4.
    We use the function plot_confidence() for the actual plotting and run our simulation several times to get the
    samples. Due to the different configurations, we receive eight plots in two figures.
    """
    # TODO Task 5.2.4: Your code goes here

    #rho = 0.5 / alpha = 0.1 / Sim time = 100s
    TIC_SU = TimeIndependentCounter("System Utilization")
    TIC_CI = []
    sim_param = SimParam()
    random.seed(sim_param.SEED)
    sim = Simulation(sim_param)
    sim.sim_param.SIM_TIME = sim_time
    sim.sim_param.S = 100000
    sim.sim_param.RHO = rho
    random.seed(sim.sim_param.SEED_IAT)
    random.seed(sim.sim_param.SEED_ST)
    for i in range(100):
        for j in range(30):
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", category=RuntimeWarning)
                TIC_SU.count(sim.do_simulation().system_utilization)
                sim.reset()
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            TIC_CI.append((TIC_SU.get_mean()- TIC_SU.report_confidence_interval(alpha),TIC_SU.get_mean()+ TIC_SU.report_confidence_interval(alpha)))
        TIC_SU.reset()
    plot_confidence(sim, 100, TIC_CI, rho, "alpha="+str(alpha),num,alpha)

def plot_confidence(sim, x_num, TIC_CI, act_mean, ylabel,num,alpha):
    """
    Plot confidence levels in batches. Inputs are given as follows:
    :param sim: simulation, the measurement object belongs to.
    :param x: defines the batch ids (should be an array).
    :param y_min: defines the corresponding lower bound of the confidence interval.
    :param y_max: defines the corresponding upper bound of the confidence interval.
    :param calc_mean: is the mean calculated from the samples.
    :param act_mean: is the analytic mean (calculated from the simulation parameters).
    :param ylabel: is the y-label of the plot
    :return:
    """
    # TODO Task 5.2.3: Your code goes here
    """
    Note: You can change the input parameters, if you prefer to.
    """
    x = range(1,x_num+1)
    err = []
    calc_mean = []
    act_mean_line = []
    for i in range(len(TIC_CI)):
        err.append(TIC_CI[i][1] - TIC_CI[i][0])
        calc_mean.append((TIC_CI[i][1] + TIC_CI[i][0])/2.0)
        act_mean_line.append(act_mean)
    pyplot.figure(num)
    pyplot.errorbar(x, calc_mean, yerr=err, label=ylabel, linestyle='--', ecolor=colors[num])
    pyplot.plot(x, act_mean_line, label="rho", linewidth=3)
    pyplot.legend()
    pyplot.xlabel('sample id')
    pyplot.ylim((0.4+(sim.sim_param.RHO-0.5)/2.0,0.65+sim.sim_param.RHO-0.5))
    pyplot.ylabel('System Utilization')
    pyplot.title('TIME:'+str(sim.sim_param.SIM_TIME/1000)+'s, ALPHA:'+str(alpha)+' RHO:'+str(sim.sim_param.RHO))
    pyplot.show()




#task_5_2_1()
#task_5_2_2()
"""
task_5_2_4(0.5,0.1,100000,1)
task_5_2_4(0.5,0.05,100000,2)
task_5_2_4(0.5,0.1,1000000,3)
task_5_2_4(0.5,0.05,1000000,4)
"""
"""

task_5_2_4(0.9,0.1,100000,1)
task_5_2_4(0.9,0.05,100000,2)
task_5_2_4(0.9,0.1,1000000,3)
task_5_2_4(0.9,0.05,1000000,4)
"""
