# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 17:01:45 2019

@author: mh iyer

Description: Code to:
            1) Define leaky relu function
            2) Plot it
            3) Get leaky relu function value for an input x
"""
 
import numpy as np
import matplotlib.pyplot as plt

# create leaky relu class
class leaky_relu:
    # initialize
    def __init__(self, alpha):
        self.alpha = alpha

    # define leaky relu function
    def leaky_relu_function(self,x):
        if x<0:
            return(self.alpha * x)
        else:
            return(x)
    
    # plot leaky relu curve
    def visualize_leaky_relu(self):
        
        # initialize list to store x
        x = []
        # initialize list to store leaky relu(x)
        lr_fcn = []
        
        # loop through a set of values
        for i in np.arange(-40,40,0.1):
            lr_fcn.append(self.leaky_relu_function(i))
            x.append(i)
            
        # plot
        plt.plot(x, lr_fcn, color='red',marker='o')
        plt.title('Leaky Relu Function')
        plt.xlabel('x')
        plt.ylabel('leaky_relu(x)')
        
# example usage
if __name__ == "__main__":
    
    # define alpha
    alpha = 0.1
    # initialize object
    lr=leaky_relu(alpha)
    
    # visualize function
    lr.visualize_leaky_relu()
    
    # calculate leaky relu for a value
    val=-10
    print('Leaky relu output for',val,' with alpha',alpha,' is :',lr.leaky_relu_function(val))
