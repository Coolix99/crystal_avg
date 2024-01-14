import numpy as np
from typing import List

from Polygon import Polygon
from Triangular_Hist import Triangular_Hist

def getRefCoordinates(p0,p1,center,position):
    e0=p0-center
    e0=e0/np.linalg.norm(e0)
    e1=p1-center
    e1=e1/np.linalg.norm(e1)
    r=position-center

    e0e1=np.dot(e0,e1)
    re0=np.dot(r,e0)
    re1=np.dot(r,e1)

    return np.array((re0-re1*e0e1,re1-re0*e0e1))/(1-e0e1*e0e1)

def isIn(refCoord):
    if refCoord[0]>1 or refCoord[1]>1 or refCoord[0]<0 or refCoord[0]<0:
        return False
    return True

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
        self.N_segments=len(self.Data)


    def fill(self, polygon:Polygon, position, value, guess_segment=0):
        """
        :param polygon: Polygon geometry
        :param position: Position in the polygon
        :param value: value to be added
        :param guess_segment: guess in which segement the position could be
        """
        if polygon.Points.shape[0]!=self.N_segments:
            raise ValueError('not correct polygon')
        for i in range(self.N_segments):
            segment=(i+guess_segment)%self.N_segments
            refCoord=getRefCoordinates(polygon.Points[segment,:],polygon.Points[(segment+1)%self.N_segments,:],polygon.C,position)
            if isIn(refCoord):
                self.Data[segment].fill(refCoord,value)
                return segment
        return None

    def get_entry(self, key):
        """
        Retrieves the value associated with a given key in the histogram.
        :param position: Position in the standard triangular
        :return: The value associated with the position
        """
        return #TODO