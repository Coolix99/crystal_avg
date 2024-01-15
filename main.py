import numpy as np

from Polygon import Polygon
from Polygon_Hist import Polygon_Hist

def main():
    Image=np.ones((20,20))
    pList=[(2.1,10),(10,5),(13,18)]

    polygon1=Polygon(pList)
    print(polygon1.C)
    hist=Polygon_Hist(3,10)
    for i in range(Image.shape[0]):
        for j in range(Image.shape[1]):
            p=np.array((i,j),dtype=int)
            hist.fill(polygon1,p,Image[p[0],p[1]])
    p=np.array((3,10),dtype=int)
    print(hist.get_entry(polygon1,p))

    hist.plot(polygon1)

if __name__ == "__main__":
    main()