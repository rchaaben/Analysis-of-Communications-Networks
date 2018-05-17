from simparam import SimParam
from simulation import Simulation
import random
import pylab
import numpy as np
from matplotlib.legend_handler import HandlerLine2D
"""
This file should be used to keep all necessary code that is used for the simulation study in part 1 of the programming
assignment. It contains the tasks 1.7.1, 1.7.2 and the bonus task 1.7.3.

The function do_simulation_study() should be used to run the simulation routine, that is described in the assignment.
"""

def task_1_7_1():
    """
    Execute task 1.7.1 and perform a simulation study according to the task assignment.
    :return: Minimum number of buffer spaces to meet requirements.
    """
    sim_param = SimParam()
    random.seed(sim_param.SEED)
    sim = Simulation(sim_param)
    return do_simulation_study(sim)


def task_1_7_2():
    """
    Execute task 1.7.2 and perform a simulation study according to the task assignment.
    :return: Minimum number of buffer spaces to meet requirements.
    """
    sim_param = SimParam()
    random.seed(sim_param.SEED)
    sim_param.SIM_TIME = 1000000
    sim_param.MAX_DROPPED = 100
    sim_param.NO_OF_RUNS = 100
    sim = Simulation(sim_param)
    return do_simulation_study(sim)

def task_1_7_3(queue_size):
    """
    Execute bonus task 1.7.3.
    """
    # TODO Bonus Task 1.7.3: Your code goes here (if necessary)
    sim_param = SimParam()
    random.seed(sim_param.SEED)
    sim = Simulation(sim_param)
    sim.sim_param.S=queue_size
    result_set=[]
    for i in range(sim.sim_param.NO_OF_RUNS):
        sim.reset()
        sim_result=sim.do_simulation()
        result_set.append(sim_result.blocking_probability)
    result_length=len(result_set)
    n, bins, patches = pylab.hist(result_set)
    nc=np.cumsum(n/result_length)
    cdf=[0.0]
    for i in nc:
        cdf.append(i)

    sim_param = SimParam()
    random.seed(sim_param.SEED)
    sim_param.SIM_TIME = 1000000
    sim_param.MAX_DROPPED = 100
    sim_param.NO_OF_RUNS = 100
    sim = Simulation(sim_param)
    sim.sim_param.S=queue_size
    result_set=[]
    for i in range(sim.sim_param.NO_OF_RUNS):
        sim.reset()
        sim_result=sim.do_simulation()
        result_set.append(sim_result.blocking_probability)
    result_length=len(result_set)
    n1, bins1, patches1 = pylab.hist(result_set)
    nc1=np.cumsum(n/result_length)
    cdf1=[0.0]
    for i in nc:
        cdf1.append(i)

    pylab.figure(1)
    pylab.xlabel('blocking_probability')
    pylab.ylabel('density')
    pylab.title('Histogram of the probability density function')
    pylab.hist(n, bins)
    pylab.hist(n1, bins1)
    pylab.figure(2)
    pylab.xlim(0.0,1.0)
    pylab.ylim(0.0,1.0)
    pylab.xlabel('blocking_probability')
    pylab.ylabel('CDF')
    pylab.title('CDF function')
    line1, = pylab.plot(bins,cdf, marker='o', label='100000 ms, 10 MAX_DROPPED, 1000 runs')
    line2, = pylab.plot(bins1,cdf1, marker='o', label='1000000 ms, 100 MAX_DROPPED, 100 runs')
    pylab.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
    pylab.show()

def do_simulation_study(sim):
    """
    Implement according to task description.
    """
    # TODO Task 1.7.1: Your code goes here
    for i in range(4,20):
        successful_run=0
        sim.sim_param.S=i
        for j in range(sim.sim_param.NO_OF_RUNS):
            sim.reset()
            sim_result=sim.do_simulation()
            if sim_result.packets_dropped < sim.sim_param.MAX_DROPPED:
                successful_run+=1
        print "The percentage of less than ",sim.sim_param.MAX_DROPPED," packets are lost in at least 80% of ",sim.sim_param.NO_OF_RUNS," simulation runs :",float(successful_run)/float(sim.sim_param.NO_OF_RUNS)," for a buffer length of ",i
        if successful_run >= int(sim.sim_param.NO_OF_RUNS*0.8):
            return sim.sim_param.S

print "---Question 1.7.1---"
l1=task_1_7_1()
print "The queue length required such that after 100 s less than 10 packets are lost in at least 80% of 1000 simulation runs is : " ,l1
print "\n", "---Question 1.7.2---"
l2=task_1_7_2()
print "The queue length required such that after 1000 s less than 100 packets are lost in at least 80% of 100 simulation runs is : ",l2
task_1_7_3(4)
