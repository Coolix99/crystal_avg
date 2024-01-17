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

    refCoord=np.array((re0-re1*e0e1,re1-re0*e0e1))/(1-e0e1*e0e1)
    refCoord[0]=refCoord[0]/np.linalg.norm(p0-center)
    refCoord[1]=refCoord[1]/np.linalg.norm(p1-center)
    return refCoord

def isIn(refCoord):
    if refCoord[0]>1 or refCoord[1]>1 or refCoord[0]<0 or refCoord[1]<0:
        return False
    if refCoord[0]+refCoord[1]>1:
        return False
    return True

class Polygon_Hist:
    def __init__(self,N_poly:int,N_bin:int = 50,dtype=np.float32):
        '''
        :param N_poly: number of edges of the polygon
        :param N_bin: N_bin of each triangular segment
        :param dtype: data type for storing
        '''
        self.Data:List[Triangular_Hist]=[]
        for i in range(N_poly):
            self.Data.append(Triangular_Hist(N_bin,dtype))
        self.N_segments=len(self.Data)

    def findCoord(self, polygon:Polygon, position, guess_segment=0):
        """
        :param polygon: Polygon geometry
        :param position: Position in the polygon
        :param guess_segment: guess in which segement the position could be
        :return: segemnt in which position was found. None if it was outside
        """
        if polygon.Points.shape[0]!=self.N_segments:
            raise ValueError('not correct polygon')
        for i in range(self.N_segments):
            segment=(i+guess_segment)%self.N_segments
            refCoord=getRefCoordinates(polygon.Points[segment,:],polygon.Points[(segment+1)%self.N_segments,:],polygon.C,position)
            if isIn(refCoord):
                return segment,refCoord
        return None


    def fill(self, polygon:Polygon, position, value, guess_segment=0):
        """
        :param polygon: Polygon geometry
        :param position: Position in the polygon
        :param value: value to be added
        :param guess_segment: guess in which segement the position could be
        :return: segemnt in which position was found. None if it was outside
        """
        
        res= self.findCoord(polygon, position, guess_segment)
        if res is None:
            return None
        segment=res[0]
        refCoord=res[1]
        self.Data[segment].fill(refCoord,value)
        return segment

    def get_entry(self, polygon:Polygon, position, guess_segment=0):
        """
        Retrieves the value associated with a position in the histogram.
        :param position: Position in the polygon
        :param polygon: geometry
        :param guess_segment: guess in which segment the position could be
        :return: The value associated with the position
        """
        res= self.findCoord(polygon, position, guess_segment)
        if res is None:
            return None
        segment=res[0]
        refCoord=res[1]
        return self.Data[segment].get_entry(refCoord)
    
    def sample_Segment(self, segment:int,polygon:Polygon):
        x,y,val=self.Data[segment].sample()
        v1=polygon.Points[segment,:]-polygon.C
        v2=polygon.Points[(segment+1)%self.N_segments,:]-polygon.C
        p=np.outer(x, v1)+np.outer(y, v2)+polygon.C
        return p,val

    def sample_Polygon(self,polygon:Polygon):
        all_p=[]
        all_val=[]
        for i in range(self.N_segments):
            p,val=self.sample_Segment(i,polygon)
            all_p.append(p)
            all_val.append(val)
        p=np.vstack(all_p)
        print(p.shape)
        val=np.concatenate(all_val)
        return p,val

    def plot(self,polygon:Polygon):
        p,z=self.sample_Polygon(polygon)

        import matplotlib.pyplot as plt
        import matplotlib.tri as tri
   
        x = p[:, 0]
        y = p[:, 1]

        triang = tri.Triangulation(x, y)
        # Refine data
        refiner = tri.UniformTriRefiner(triang)
        tri_refi, z_test_refi = refiner.refine_field(z, subdiv=3)
        # Plot the triangulation and the high-res iso-contours
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.triplot(triang, lw=0.5, color='white')
        levels = np.linspace(np.min(z), np.max(z), 5)
        contour=ax.tricontourf(tri_refi, z_test_refi, levels=levels, cmap='RdBu_r')
        ax.tricontour(tri_refi, z_test_refi, levels=levels,
                    colors=['0.25', '0.5', '0.5', '0.5', '0.5'],
                    linewidths=[1.0, 0.5, 0.5, 0.5, 0.5])
        cbar = plt.colorbar(contour, ax=ax)
        plt.show()
        return