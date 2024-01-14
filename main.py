import numpy as np

from Polygon import Polygon
from Polygon_Hist import Polygon_Hist

def main():
    Image=np.ones((20,20))
    pList=[(2,10),(10,5),(13,18)]

    polygon1=Polygon(pList)

    print(polygon1.C)

if __name__ == "__main__":
    main()