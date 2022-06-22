import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class Opinion:

    def __init__(self,size,prop):
        self.popsize = size
        #self.opinions = np.random.choice(2, size = size, p = [prob,1-prob])
        self.opinions = np.ones(size)
        self.opinions[:prop] = 0
        np.random.shuffle(self.opinions)
        self.adjmat = np.zeros((size,size),dtype=int)
        self.influenceability = np.ones(size)

    def set_community(self, ncomm, in_group):
        out_group = (1-in_group)/(ncomm-1)
        pmatrix = np.eye(ncomm) * in_group + np.where(np.eye(ncomm) == 1, 0, 1) * out_group
        csizes = [int(self.popsize / ncomm)] * ncomm
        graph = nx.stochastic_block_model(sizes=csizes, p=pmatrix)
        self.adjmat = nx.to_numpy_array(graph)

    def growConnections(self,sigma):
        d = int(np.sqrt(self.popsize))
        self.posx = np.array([np.linspace(-1,1,d)]*d).flatten()
        self.posy = np.array([np.linspace(-1,1,d)]*d).T.flatten()
        for i in range(self.popsize):
            for j in range(self.popsize):
                # Calculate distance between tree i and tree j
                dist = np.sqrt((self.posx[i]-self.posx[j])**2+(self.posy[i]-self.posy[j])**2)
                # Collect proportional to distance (assume some Gaussian or Normal Distribution)
                prob = (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-(dist**2) / (2*(sigma**2)))
                # Determine if fungal connection is made or not based on proximity
                if np.random.random() < prob:
                    self.adjmat[i,j] = 1

    # def determineInfluenceabilityIncoming(self):
    #     for i in range(self.popsize):
    #         self.influenceability[i] = np.count_nonzero(self.adjmat[i,:])/self.popsize
    #
    # def determineInfluenceabilityOutgoing(self):
    #     for i in range(self.popsize):
    #         self.influenceability[i] = np.count_nonzero(self.adjmat[:,i])/self.popsize

    def neighbors(self, i):
        return [j for j in range(self.popsize) if self.adjmat[i, j] == 1]

    def step(self):
        # 1. Pick an agent at random
        i = np.random.randint(self.popsize)
        # 2. Find its neighbors
        neighbors = self.neighbors(i)
        if (len(neighbors)>0):
            # 3. Calculate neighbors' opinions
            neighbors_opinions = self.opinions[neighbors]
            # 4. Count the proportion of opinions that are different from one's own out of all neighbors
            propdiff = np.sum(neighbors_opinions!=self.opinions[i])/len(neighbors)
            # 5. Multiply by one's influenciability to calculate the change of changing opinion
            changeprob = self.influenceability[i]*propdiff
            # 6. Throw a coin to see if opinion changes (flip)
            if np.random.random() < changeprob:
                self.opinions[i] = np.abs(1-self.opinions[i])
            # See if consensus is reached
            sum = np.sum(self.opinions)
            if ((sum == 0) or (sum == self.popsize)):
                return 1
        return 0
