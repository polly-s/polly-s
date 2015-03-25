import numpy as np
import matplotlib.pyplot as plt
data=np.genfromtxt("https://raw.githubusercontent.com/anaderi/lhcb_trigger_ml/master/hep_ml/datasets/dalitzplot/bkgd.csv"
                   ,skip_header=1,delimiter="\t")
num_bins=30
plt.figure()
n,bins,patches=plt.hist(data.T[0],num_bins,histtype='step')
num_bins=30
plt.figure()
n,bins,patches=plt.hist(data.T[0],num_bins,range=[0,0.5],histtype='step')
plt.xlabel('M2AB')
plt.ylabel('N')
yerr = 0.1 + 2*sqrt(n)
plt.errorbar(bins[:len(n)], n,yerr=yerr, fmt='.',color='red')
plt.show()
