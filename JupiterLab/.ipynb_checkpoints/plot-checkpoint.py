import numpy as np
import matplotlib.pyplot as plt 
xdata, ydata = np.loadtxt('./data/wavePulseData.txt', unpack=True)
x = np.linspace(-10., 10., 200)
y = np.sin(x) * np.exp(-(x/5.0)**2)
plt.figure(1, figsize = (6,4) )
plt.plot(x, y, 'b-', label='theory')
plt.plot(xdata, ydata, 'ro', label="data")
plt.xlabel('x')
plt.ylabel('transverse displacement')
plt.legend(loc='upper right')
plt.savefig('./data/WavyPulse.pdf') # display plot on screen
plt.show()