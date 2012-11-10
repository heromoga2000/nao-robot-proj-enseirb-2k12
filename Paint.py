import numpy as np
import matplotlib.pyplot as plt

def tst( arr ):
    for name in arr:
        x = np.arange(0, len(arr[name]), 1);
        plt.plot(x, arr[name])
    plt.show(plt)


