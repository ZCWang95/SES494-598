# Calculates the distance between two 3d Cartesian coordinates

import numpy as np
x1=23.7
y1=-9.2
z1=-7.8
x2=-3.5
y2=4.8
z2=8.1
distance=sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
#distance=np.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
print("%.2f" % (distance))
