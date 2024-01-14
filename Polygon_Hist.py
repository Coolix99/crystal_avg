import numpy as np
from typing import List

from Polygon import Polygon
from Triangular_Hist import Triangular_Hist

class Polygon_Hist:
    def __init__(self,N_poly:int,N_bin:int = 50,dtype=np.float16):
        '''
        :param N_poly: number of edges of the polygon
        :param N_bin: N_bin of each triangular segment
        :param dtype: data type for storing
        '''
        self.Data:List[Triangular_Hist]=[]
        for i in range(N_poly):
            self.Data.append(Triangular_Hist(N_bin,dtype))


    def fill(self, polygon:Polygon, position, value, guess_segment=0):
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