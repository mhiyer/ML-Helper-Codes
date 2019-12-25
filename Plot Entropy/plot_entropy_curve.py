import math
import numpy as np
import matplotlib.pyplot as plt

eps = 0.00000001

def get_entropy(prob1, prob2):
    # to avoid math domain error add a very small epsilon
    entropy = -1*(prob1*math.log2(prob1+eps) + prob2*math.log2(prob2+eps))
    return entropy
    
if __name__ == "__main__":
    
    # define a set of probabilities- take these to be the probabilities of positive examples
    a=np.arange(0,1.001,0.001)
    
    # get (1-prob) for each of the probabilities defined in a - take these to be the probabilities of negative examples
    b=1-a
    
    # define empty list to fill in entropy values
    entropy=[]
    
    # loop through a and b to get entropies 
    for i in range(0,len(a)):
        entropy.append(get_entropy(a[i], b[i]))
        
    # plot entropy
    plt.scatter(a, entropy, color='green')
    plt.xlabel('Probability of Positive Examples')
    plt.ylabel('Entropy')
    plt.title('Entropy across Different Probabilities of Positive Examples')
    plt.show()