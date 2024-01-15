import numpy as np

class Triangular_Hist:
    def __init__(self,N_bin=50,dtype=np.float32):
        '''
        :param N_bin: Number of Bins in one direction, total number will  N_bin*(N_bin+1)/2
        :param dtype: data type for storing
        ''' 
        self.N_bin=N_bin
        self.Data=np.zeros(int(N_bin*(N_bin+1)/2),dtype)
        self.count=np.zeros_like(self.Data,dtype=np.unsignedinteger)

    def getIndex(self,position):
        i0=int(position[0]*self.N_bin)
        i1=int(position[1]*self.N_bin)
        #print('i0',i0,'i1',i1)
        return i0+int((2*self.N_bin*i1+i1-i1*i1)/2)

    def fill(self, position, value):
        """
        :param position: Position in the standard triangular
        :param value: value to be added
        """
        i=self.getIndex(position)
        #print('i',i)
        self.Data[i]+=value
        self.count[i]+=1

    def get_entry(self, position):
        """
        Retrieves the value associated with a given key in the histogram.
        :param position: Position in the standard triangular
        :return: The value associated with the position and number of filles
        """
        i=self.getIndex(position)
        return self.Data[i], self.count[i]
    

    def sample(self):
        x=np.zeros_like(self.Data,dtype=np.float32)
        y=np.zeros_like(self.Data,dtype=np.float32)
        v=np.zeros_like(self.Data,dtype=np.float32)
        for i1 in range(self.N_bin):
            for i0 in range(self.N_bin-i1):
                i=i0+int((2*self.N_bin*i1+i1-i1*i1)/2)
                if self.count[i]==0:
                    continue
                x[i],y[i],v[i]=(i0+0.5)/self.N_bin, (i1+0.5)/self.N_bin, self.Data[i]/self.count[i]
        return x,y,v

