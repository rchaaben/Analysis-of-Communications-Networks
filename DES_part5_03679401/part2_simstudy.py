from simparam import SimParam
from simulation import Simulation
from histogram import Histogram,TimeDependentHistogram,TimeIndependentHistogram
from counter import Counter,TimeDependentCounter,TimeIndependentCounter
import numpy
from matplotlib import pyplot
from pylab import *
import random

"""
This file should be used to keep all necessary code that is used for the simulation study in part 2 of the programming
assignment. It contains the tasks 2.7.1 and 2.7.2.

The function do_simulation_study() should be used to run the simulation routine, that is described in the assignment.
"""

def task_2_7_1():
    """
    Here, you should execute task 2.7.1 (and 2.7.2, if you want).
    """
    # TODO Task 2.7.1: Your code goes here
    sim_param = SimParam()
    random.seed(sim_param.SEED)
    sim = Simulation(sim_param)
    do_simulation_study(sim)

def task_2_7_2():
    """
    Here, you can execute task 2.7.2 if you want to execute it in a separate function
    """
    # TODO Task 2.7.2: Your code goes here or in the function above
    sim_param = SimParam()
    random.seed(sim_param.SEED)
    sim_param.SIM_TIME = 1000000
    sim = Simulation(sim_param)
    return do_simulation_study(sim)


def do_simulation_study(sim, print_queue_length=False, print_waiting_time=True):
    """
    This simulation study is different from the one made in assignment 1. It is mainly used to gather and visualize
    statistics for different buffer sizes S instead of finding a minimal number of spaces for a desired quality.
    For every buffer size S (which ranges from 5 to 7), statistics are printed (depending on the input parameters).
    Finally, after all runs, the results are plotted in order to visualize the differences and giving the ability
    to compare them. The simulations are run first for 100s, then for 1000s. For each simulation time, two diagrams are
    shown: one for the distribution of the mean waiting times and one for the average buffer usage
    :param sim: the simulation object to do the simulation
    :param print_queue_length: print the statistics for the queue length to the console
    :param print_waiting_time: print the statistics for the waiting time to the console
    """
    # TODO Task 2.7.1: Your code goes here
    # TODO Task 2.7.2: Your code goes here
    for i in sim.sim_param.S_VALUES:
        sim.sim_param.S=i
        mean_waiting_time_histogram = TimeIndependentHistogram(sim,"bp")
        for j in range(sim.sim_param.NO_OF_RUNS):
            sim.reset()
            sim_result=sim.do_simulation()
            mean_waiting_time_histogram.count(sim.counter_collection.cnt_wt.get_mean())
        mean_waiting_time_histogram.report()

    mean_queue_length_histogram1 = TimeIndependentCounter("1")
    mean_queue_length_histogram2 = TimeIndependentCounter("2")
    mean_queue_length_histogram3 = TimeIndependentCounter("3")
    width = 0.1
    sim.sim_param.S=5
    for j in range(sim.sim_param.NO_OF_RUNS):
        sim.reset()
        sim_result=sim.do_simulation()
        mean_queue_length_histogram1.count(sim.counter_collection.cnt_ql.get_mean())
    sim.sim_param.S=6
    for j in range(sim.sim_param.NO_OF_RUNS):
        sim.reset()
        sim_result1=sim.do_simulation()
        mean_queue_length_histogram2.count(sim.counter_collection.cnt_ql.get_mean())
    sim.sim_param.S=7
    for j in range(sim.sim_param.NO_OF_RUNS):
        sim.reset()
        sim_result2=sim.do_simulation()
        mean_queue_length_histogram3.count(sim.counter_collection.cnt_ql.get_mean())

    histogram1, bins1 = numpy.histogram(mean_queue_length_histogram1.values,25,(0.0,7.0))
    histogram2, bins2 = numpy.histogram(mean_queue_length_histogram2.values,25,(0.0,7.0))
    histogram3, bins3 = numpy.histogram(mean_queue_length_histogram3.values,25,(0.0,7.0))
    fig, ax = pyplot.subplots()
    bins2 = array(bins2.tolist())
    bins2 = bins2+ones(len(bins2.tolist()))*width
    bins3 = array(bins3.tolist())
    bins3 = bins3+ones(len(bins3.tolist()))*2.0*width
    rects1 = ax.bar(bins1.tolist(), histogram1.tolist()+[0], width, color='r')
    rects2 = ax.bar(bins2.tolist(), histogram2.tolist()+[0], width, color='g')
    rects3 = ax.bar(bins3.tolist(), histogram3.tolist()+[0], width, color='b')
    ax.legend((rects1[0], rects2[0],rects3[0]), ('S5', 'S6','S7'))	
    pyplot.show()


#task_2_7_1()
#task_2_7_2()
