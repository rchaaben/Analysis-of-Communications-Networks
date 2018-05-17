import math
from random import Random


class RNG(object):
    
    """
    Class RNG contains two random number streams, one for IAT and one for ST.

    Both RNS can be set during initialization or separately. The next random numbers are generated by the functions
    get_iat() or get_st().
    """
    
    def __init__(self, rns1, rns2):
        """
        Initialize a RNG object with two RNS given.
        :param rns1: represents the RNS for the inter-arrival times.
        :param rns2: represents the RNS for the service times.
        """
        self.iat_rns = rns1
        self.st_rns = rns2
    
    def set_iat_rns(self, rns1):
        """
        Set a new RNS for the inter-arrival times.
        """
        self.iat_rns = rns1
        
    def set_st_rns(self, rns2):
        """
        Set a new RNS for the service times.
        """
        self.st_rns = rns2
        
    def get_iat(self):
        """
        Return a new sample of the IAT RNS
        """
        return self.iat_rns.next()*1000
    
    def get_st(self):
        """
        Return a new sample of the ST RNS
        """
        return self.st_rns.next()*1000


class RNS(object):
    
    """
    Basic abstract class for random number streams.

    To be implemented in subclass.
    Contains a Random class r in order to allow different seeds for different RNS
    """

    def __init__(self, the_seed=None):
        """
        Initialize the general RNS with an optional seed.
        All further initialization is done in subclass.
        """
        self.r = Random(the_seed)

    def set_parameters(self, *args):
        NotImplementedError("Implement in subclass")

    def next(self):
        """
        Method should be overwritten in subclass.
        """
        return 0
    

class ExponentialRNS(RNS):
    
    """
    Class to provide exponentially distributed random numbers. After initialization, new numbers can be generated
    using next(). Initialization with given lambda and optional seed.
    :param lambda_x: the inverse of the mean of the exponential distribution
    :param the_seed: optional seed for the random number stream
    """
    
    def __init__(self, lambda_x, the_seed=None):
        """
        Initialize Exponential RNS and set the parameters.
        """
        super(ExponentialRNS, self).__init__(the_seed)
        self.mean = 0
        self.set_parameters(lambda_x)
        
    def set_parameters(self, lambda_x):
        """
        Set parameter lambda, hence the mean of the exponential distribution.
        """
        self.mean = 1./float(lambda_x)
        
    def next(self):
        """
        Generate the next random number using the inverse transform method.
        """
        return -math.log(self.r.random()) * self.mean
        

class UniformRNS(RNS):
    
    """
    Class to provide exponentially distributed random numbers. After initialization, new numbers can be generated
    using next(). Initialization with upper and lower bound and optional seed.
    :param a: the lower bound of the uniform distribution
    :param b: the upper bound of the uniform distribution
    :param the_seed: optional seed for the random number stream
    """
    
    def __init__(self, a, b, the_seed=None):
        """
        Initialize Uniform RNS and set the parameters.
        """
        super(UniformRNS, self).__init__(the_seed)
        self.upper_bound = a
        self.lower_bound = b
        self.width = self.upper_bound - self.lower_bound
        
    def set_parameters(self, a, b):
        """
        Set parameters a and b, the upper and lower bound of the distribution
        """
        self.upper_bound = a
        self.lower_bound = b
        self.width = self.upper_bound - self.lower_bound
        
    def next(self):
        """
        Generate the next random number using the inverse transform method.
        """
        return self.lower_bound + self.width * self.r.random()