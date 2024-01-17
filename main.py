import numpy as np
from typing import List

from Polygon import Polygon
from Polygon_Hist import Polygon_Hist

def sum_Hist(poly_Hist_List: List[Polygon_Hist]):
    first=poly_Hist_List[0]
    #check wether all have same properties
    for i in range(1,len(poly_Hist_List)):
        if poly_Hist_List[i].N_segments!=first.N_segments:
            print('not all hist have the same number of segments (edges)')
            return None
        if poly_Hist_List[i].Data[0].N_bin!=first.Data[0].N_bin:
            print('not all hist have the same number of bins')
            return None
    res_Hist=Polygon_Hist(first.N_segments,first.Data[0].N_bin,np.float32)

    
    for i in range(res_Hist.N_segments):
        poly_Hist_Data_List=[]
        poly_Hist_Count_List=[]
        for j in range(len(poly_Hist_List)):
            poly_Hist_Data_List.append(poly_Hist_List[j].Data[i].Data)
            poly_Hist_Count_List.append(poly_Hist_List[j].Data[i].count)
        poly_Hist_Data=np.array(poly_Hist_Data_List)
        poly_Hist_Count=np.array(poly_Hist_Count_List)
        sum_Data=np.sum(poly_Hist_Data,axis=0)
        sum_count=np.sum(poly_Hist_Count,axis=0)
        res_Hist.Data[i].count=sum_count
        res_Hist.Data[i].Data=sum_Data
    return res_Hist

def main():
    Image=np.ones((50,50))
    pList=[(2.1,40),(10,20),(30,45)]
    polygon=Polygon(pList)

    Image1 = Image+np.random.normal(0, 0.1, Image.shape)
    hist1=Polygon_Hist(3,6)
    for i in range(Image1.shape[0]):
        for j in range(Image1.shape[1]):
            p=np.array((i,j),dtype=int)
            hist1.fill(polygon,p,Image1[p[0],p[1]])
    
    
    Image2 = Image+np.random.normal(0, 0.1, Image.shape)
    hist2=Polygon_Hist(3,6)
    for i in range(Image2.shape[0]):
        for j in range(Image2.shape[1]):
            p=np.array((i,j),dtype=int)
            hist2.fill(polygon,p,Image2[p[0],p[1]])

    hist=sum_Hist([hist1,hist2])
    hist.plot(polygon)

if __name__ == "__main__":
    main()