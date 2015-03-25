import numpy as np
import matplotlib.pyplot as pl
data=np.genfromtxt("https://raw.githubusercontent.com/anaderi/lhcb_trigger_ml/master/hep_ml/datasets/dalitzplot/bkgd.csv"
                   ,skip_header=1,delimiter="\t")

pl.hist2d(data.T[0],data.T[1],bins=40,cmap=pl.cm.Blues)
pl.xlabel('M2AB')
pl.ylabel('M2AC')
pl.colorbar()
pl.show()
