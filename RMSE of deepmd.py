import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("lcurve copy.out", names=True)
for name in data.dtype.names[1:-1]:
    plt.plot(data['step'], data[name], label=name)
    plt.legend()
    plt.xlabel('Step')
    plt.ylabel('Loss')
    plt.xscale('linear')
    plt.yscale('log')
    plt.grid()
    plt.show()
