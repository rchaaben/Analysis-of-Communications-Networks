from rng import RNG, ExponentialRNS, UniformRNS
from histogram import TimeIndependentHistogram
from simparam import SimParam
from simulation import Simulation
import random
"""
This file should be used to keep all necessary code that is used for the verification section in part 3 of the
programming assignment. It contains tasks 3.2.1 and 3.2.2.
"""

def task_3_2_1():
    """
    This function plots two histograms for verification of the random distributions.
    One histogram is plotted for a uniform distribution, the other one for an exponential distribution.
    """
    # TODO Task 3.2.1: Your code goes here
    sim_param = SimParam()
    random.seed(sim_param.SEED)
    sim_param.RHO = 0.01
    sim = Simulation(sim_param)
    rns_iat = ExponentialRNS(1.0)
    rns_st = ExponentialRNS(1.0/sim.sim_param.RHO)
    rns_uniform = UniformRNS((2,4))
    hist1 = TimeIndependentHistogram(sim, "Line")
    hist2 = TimeIndependentHistogram(sim, "Line")
    hist3 = TimeIndependentHistogram(sim, "bp")
    for i in range(1000000):
        hist1.count(rns_iat.next())
        hist2.count(rns_st.next())
        hist3.count(rns_uniform.next())
    hist1.report()
    hist2.report()
    hist3.report()

def task_3_2_2():
    """
    Here, we execute task 3.2.2 and print the results to the console.
    The first result string keeps the results for 100s, the second one for 1000s simulation time.
    """
    # TODO Task 3.2.2: Your code goes here
    rho = [.01, .5, .8, .9]
    system_utilization_result = []
    sim_param = SimParam()
    random.seed(sim_param.SEED)
    sim = Simulation(sim_param)
    sim.sim_param.SIM_TIME = 100000
    sim.sim_param.S = 5
    for r in rho:
        sim.sim_param.RHO = r
        sim.reset()
        system_utilization_result.append(sim.do_simulation().system_utilization)
    print "The system utilization results for a simulation time of 100s :"
    print system_utilization_result
    rho = [.01, .5, .8, .9]
    system_utilization_result = []
    sim_param = SimParam()
    random.seed(sim_param.SEED)
    sim = Simulation(sim_param)
    sim.sim_param.SIM_TIME = 1000000
    sim.sim_param.S = 5
    for r in rho:
        sim.sim_param.RHO = r
        sim.reset()
        system_utilization_result.append(sim.do_simulation().system_utilization)
    print "The system utilization results for a simulation time of 1000s :"
    print system_utilization_result

#task_3_2_1()
#task_3_2_2()
