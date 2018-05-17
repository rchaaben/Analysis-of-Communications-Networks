from finitequeue import FiniteQueue
from packet import Packet
import random

class SystemState(object):
    
    """
    This class represents the state of our system.

    It contains information about whether the server is busy and how many customers
    are waiting in the queue (buffer). The buffer represents the physical buffer or
    memory of our system, where packets are stored before they are served.

    The integer variable buffer_content represents the buffer fill status, the flag
    server_busy indicates whether the server is busy or idle.

    The simulation object is only used to determine the maximum buffer space as
    determined in its object sim_param.
    """

    def __init__(self, sim):
        """
        Create a system state object
        :param sim: simulation object for determination of maximum number of stored
        packets in buffer
        :return: system_state object
        """
        # TODO Task 1.1.1: Your code goes here
        self.server_busy = False
        """
        self.buffer_content = 0
        """
        self.buffer = FiniteQueue(sim)
        self.served_packet = Packet(sim,None)
        self.last_arrival=0
        self.sim = sim

    def add_packet_to_server(self):
        """
        Try to add a packet to the server unit.
        :return: True if server is not busy and packet has been added successfully.
        """
        # TODO Task 1.1.2: Your code goes here
        """
        if self.server_busy==False:
            self.server_busy=True
            return True
        else:
            return False
        """
        p = Packet(self.sim,self.sim.sim_param.IAT)
        if not self.server_busy:
            self.served_packet = Packet(self.sim, self.sim.sim_state.now - self.last_arrival)
            self.last_arrival = self.sim.sim_state.now
            self.served_packet.start_service()
            self.server_busy=True
            return True
        else:
            return False

    def add_packet_to_queue(self):
        """
        Try to add a packet to the buffer.
        :return: True if buffer/queue is not full and packet has been added successfully.
        """
        # TODO Task 1.1.2: Your code goes here
        """
        if self.buffer_content<self.sim.sim_param.S:
            self.buffer_content+=1
            return True
        else:
            return False
        """
        if self.buffer.add(Packet(self.sim, self.sim.sim_state.now - self.last_arrival)):
            self.last_arrival = self.sim.sim_state.now
            return True
        else:
            return False


    def complete_service(self):
        """
        Reset server status to idle after a service completion.
        """
        # TODO Task 1.1.3: Your code goes here
        self.server_busy = False
        p = self.served_packet
        p.complete_service()
        # TODO Task 2.4.3: Your code goes here somewhere
        self.sim.counter_collection.count_packet(p)
        self.served_packet = None
        return p

    def start_service(self):
        """
        If the buffer is not empty, take the next packet from there and serve it.
        :return: True if buffer is not empty and a stored packet is being served.
        """
        # TODO Task 1.1.3: Your code goes here
        """
        if self.buffer_content>0:
            self.buffer_content-=1
            self.server_busy=True
            return True
        else:
            return False
        """
        if self.buffer.is_empty():
            return False
        else:
            self.served_packet = self.buffer.remove()
            self.served_packet.start_service()
            self.server_busy = True
            return True

    def get_queue_length(self):
        """
        :return: fill status of the queue
        """
        return self.buffer.get_queue_length()
