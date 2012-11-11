import numpy as np
import matplotlib.pyplot as plt

def savePlot( arr, filename, show=False ):
    for name in arr:
        x = np.arange(0, len(arr[name]), 1);
        plt.plot(x, arr[name])
    plt.savefig( filename )
    if ( show ):
        plt.show(plt)
    


