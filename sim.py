import opinion as op
import numpy as np
import matplotlib.pyplot as plt
import sys

########################
# Part 1: Example
########################
# size = 100
# steps = int(100*size)
# prop = 20
# sigma = 0.8
# a = op.Opinion(size,prop)
# a.growConnections(sigma)
# data = np.zeros(steps+1)
# data[0] = np.mean(a.opinions)
# for i in range(steps):
#     a.step()
#     data[i+1] = np.mean(a.opinions)
# print(np.mean(a.opinions) < 0.5)
# plt.plot(data)
# plt.show()

####################################
# Part 2: Testing Across Sigma (Spatial)
####################################
def sim(size,steps,sigma,prop):
    a = op.Opinion(size,prop)
    a.growConnections(sigma)
    for i in range(steps):
        if a.step():
            return i/size, np.mean(a.opinions)
    return 0, np.mean(a.opinions)

def simR(reps,size,steps,sigma,prop):
    data = []
    dataX = np.zeros(reps)
    for r in range(reps):
        t,x = sim(size,steps,sigma,prop)
        dataX[r] = x
        if t > 0:
            data.append(t)
    data = np.array(data)
    if len(data) == 0:
        return 0, 0, np.count_nonzero(dataX<0.5)/reps, np.mean(dataX)
    else:
        return np.mean(data), len(data)/reps, np.count_nonzero(dataX<0.5)/reps, np.mean(dataX)

####################################
# Part 2: Testing Across Sigma (Spatial)
####################################
size = 100
steps = int(100*size)
reps = 100
sigmasteps = 8
propsteps = 4
sigmarange = [0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2] #np.linspace(0.0,0.2,sigmasteps)
proprange = np.linspace(10,40,propsteps)
influence = 1

dataM = np.zeros((sigmasteps,propsteps))
dataL = np.zeros((sigmasteps,propsteps))
dataX = np.zeros((sigmasteps,propsteps))
dataY = np.zeros((sigmasteps,propsteps))

k = 0
for prop in proprange:
    print("Prop:",int(prop))
    i = 0
    for sigma in sigmarange:
        print("\tSigma:",sigma)
        d,l,x,y = simR(reps,size,steps,sigma,int(prop))
        dataM[i][k] = d
        dataL[i][k] = l
        dataX[i][k] = x
        dataY[i][k] = y
        i+=1
    k+=1

np.save("sigmarange.npy",sigmarange)
np.save("resourcedataM.npy",dataM)
np.save("resourcedataL.npy",dataL)
np.save("resourcedataX.npy",dataX)
np.save("resourcedataY.npy",dataY)

####################################
# Part 3: Testing Across Mu (Community)
####################################

def simc(size,steps,ncomn,in_group,prop):
    a = op.Opinion(size,prop)
    a.set_community(ncomn,in_group)
    for i in range(steps):
        if a.step():
            return i/size, np.mean(a.opinions)
    return 0, np.mean(a.opinions)

def simRc(reps,size,steps,ncomn,in_group,prop):
    data = []
    dataX = np.zeros(reps)
    for r in range(reps):
        t,x = simc(size,steps,ncomn,in_group,prop)
        dataX[r] = x
        if t > 0:
            data.append(t)
    data = np.array(data)
    if len(data) == 0:
        return 0, 0, np.count_nonzero(dataX<0.5)/reps, np.mean(dataX)
    else:
        return np.mean(data), len(data)/reps, np.count_nonzero(dataX<0.5)/reps, np.mean(dataX)

####################################
# Part 3: Testing Across Mu (Community)
####################################
# size = 100
# steps = int(100*size)
# reps = 100
# ncomn = 5
# propsteps = 4
# murange = [0.2, 0.4, 0.8, 0.9, 0.95, 0.9875, 0.99]
# proprange = np.linspace(10,40,propsteps)
# influence = 1
#
# dataM = np.zeros((7,propsteps))
# dataL = np.zeros((7,propsteps))
# dataX = np.zeros((7,propsteps))
# dataY = np.zeros((7,propsteps))
#
# k = 0
# for prop in proprange:
#     print("Prop:",int(prop))
#     i = 0
#     for mu in murange:
#         print("\tMu:",mu)
#         d,l,x,y = simRc(reps,size,steps,ncomn,mu,int(prop))
#         dataM[i][k] = d
#         dataL[i][k] = l
#         dataX[i][k] = x
#         dataY[i][k] = y
#         i+=1
#     k+=1
#
# np.save("murange.npy",murange)
# np.save("resourcedataMc.npy",dataM)
# np.save("resourcedataLc.npy",dataL)
# np.save("resourcedataXc.npy",dataX)
# np.save("resourcedataYc.npy",dataY)
