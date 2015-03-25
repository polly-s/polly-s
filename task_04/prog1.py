import matplotlib.pyplot as plt
data=np.genfromtxt("https://raw.githubusercontent.com/anaderi/lhcb_trigger_ml/master/hep_ml/datasets/dalitzplot/bkgd.csv"
                   ,skip_header=1,delimiter="\t")
num_bins=30
plt.figure()
n,bins,patches=plt.hist(data.T[0],num_bins,histtype='step')
plt.xlabel('M2AB')
plt.ylabel('N')
plt.show()
