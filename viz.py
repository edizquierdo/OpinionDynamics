import numpy as np
import matplotlib.pyplot as plt
import sys

g=1.618033
fs = 3.8

sigmarange = np.load("sigmarange.npy")
dataM = np.load("resourcedataM.npy")
dataL = np.load("resourcedataL.npy")
dataX = np.load("resourcedataX.npy")
dataY = np.load("resourcedataY.npy")

plt.figure(figsize=(fs*g,fs))
plt.plot(sigmarange,dataX,'o-')
plt.xlabel("Connectivity (sigma)")
plt.ylabel("Minority influence")
plt.legend(["0.1","0.2","0.3","0.4"], frameon=False)
plt.savefig("x.pdf")
plt.show()

plt.figure(figsize=(fs*g,fs))
plt.plot(sigmarange,dataY,'o-')
plt.xlabel("Connectivity (sigma)")
plt.ylabel("Average final opinion")
plt.legend(["0.1","0.2","0.3","0.4"], frameon=False)
plt.savefig("y.pdf")
plt.show()

plt.figure(figsize=(fs*g,fs))
plt.plot(sigmarange,dataM,'o-')
plt.xlabel("Connectivity (sigma)")
plt.ylabel("Average time to consensus")
plt.legend(["0.1","0.2","0.3","0.4"], frameon=False)
plt.savefig("m.pdf")
plt.show()

plt.figure(figsize=(fs*g,fs))
plt.plot(sigmarange,dataL,'o-')
plt.xlabel("Connectivity (sigma)")
plt.ylabel("Proportion where consensus reached")
plt.legend(["0.1","0.2","0.3","0.4"], frameon=False)
plt.savefig("l.pdf")
plt.show()




sigmarange = np.load("murange.npy")
dataM = np.load("resourcedataMc.npy")
dataL = np.load("resourcedataLc.npy")
dataX = np.load("resourcedataXc.npy")
dataY = np.load("resourcedataYc.npy")

plt.figure(figsize=(fs*g,fs))
plt.plot(dataX,'o-')
plt.xlabel("Connectivity (mu)")
plt.ylabel("Minority influence")
plt.legend(["0.1","0.2","0.3","0.4"], frameon=False)
plt.savefig("xc.pdf")
plt.show()

plt.figure(figsize=(fs*g,fs))
plt.plot(dataY,'o-')
plt.xlabel("Connectivity (mu)")
plt.ylabel("Average final opinion")
plt.legend(["0.1","0.2","0.3","0.4"], frameon=False)
plt.savefig("yc.pdf")
plt.show()


plt.figure(figsize=(fs*g,fs))
plt.plot(dataM,'o-')
plt.xlabel("Connectivity (mu)")
plt.ylabel("Average time to consensus")
plt.legend(["0.1","0.2","0.3","0.4"], frameon=False)
plt.savefig("mc.pdf")
plt.show()

plt.figure(figsize=(fs*g,fs))
plt.plot(dataL,'o-')
plt.xlabel("Connectivity (mu)")
plt.ylabel("Proportion where consensus reached")
plt.legend(["0.1","0.2","0.3","0.4"], frameon=False)
plt.savefig("lc.pdf")
plt.show()
