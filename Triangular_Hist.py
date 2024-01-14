import numpy as np

class Triangular_Hist:
    def __init__(self,N_bin=50,dtype=np.float16):
        '''
        :param N_bin: Number of Bins in one direction, total number will be approx. N*N/2
        :param dtype: data type for storing
        ''' 
        self.Data=np.zeros((),dtype)

    def fill(self, position, value):
        """
        :param position: Position in the standard triangular
        :param value: value to be added
        """
        #TODO

    def get_entry(self, key):
        """
        Retrieves the value associated with a given key in the histogram.
        :param position: Position in the standard triangular
        :return: The value associated with the position
        """
        return #TODO