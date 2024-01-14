import numpy as np
from typing import List

class Polygon:
    def __init__(self,pointList:List[np.array]):
        '''
        :param pointList: List of edge points in right order (2D)
        '''
        self.Points=np.array(pointList)
        # calculate the centroid
        A=0
        N=self.Points.shape[0]
        for i in range(N):
            A+=(self.Points[i,0]*self.Points[(i+1)%N,1]-self.Points[i,1]*self.Points[(i+1)%N,0])
        A=A/2

        self.C=np.zeros(2)
        for i in range(N):
            self.C[0]+=(self.Points[i,0]+self.Points[(i+1)%N,0])*(self.Points[i,0]*self.Points[(i+1)%N,1]-self.Points[i,1]*self.Points[(i+1)%N,0])
            self.C[1]+=(self.Points[i,1]+self.Points[(i+1)%N,1])*(self.Points[i,0]*self.Points[(i+1)%N,1]-self.Points[i,1]*self.Points[(i+1)%N,0])
        self.C=self.C/6/A