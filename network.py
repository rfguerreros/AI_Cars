import numpy as np

class Network: 
    def __init__(self, nlayers, shape, inherit, *args):
        self.nlayers = nlayers
        self.shape = shape
        self.weights = []
        self.bias = []
        if inherit == True:
            self.build(nlayers,shape,inherit,args[0])
        else:
            self.build(nlayers,shape,inherit)
            assert nlayers + 2  == len(shape)
    
    def __del__(self):
        print("Brain dead")
    
    def build(self,nlayers,shape,inherit,*args):
        np.random.seed(0)
        if inherit == False:
            for i in range(nlayers+1):
                self.weights.append(np.random.randn(shape[i],shape[i+1]))
            for i in range(1,nlayers+2):
                self.bias.append(np.random.randn(1,shape[i]))
        else:
            self.weights = args[0].weights
            self.bias = args[0].bias
            self.mutate()
    
    def mutate(self):
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + np.random.randn(self.weights[i].shape[0],self.weights[i].shape[1])/100.
        for i in range(len(self.bias)):
            self.bias[i] = self.bias[i] + np.random.randn(self.bias[i].shape[0],self.bias[i].shape[1])/100.   

    def decide(self, in_v):
        a = []
        for i in range(self.nlayers):
            if i==0:
                a.append(np.maximum(np.matmul(in_v,self.weights[0])+self.bias[0],0))
            else:
                a.append(np.maximum(np.matmul(a[i-1],self.weights[i])+self.bias[i],0))
        return np.maximum(np.matmul(a[len(a)-1],self.weights[len(a)])+self.bias[len(a)],0)