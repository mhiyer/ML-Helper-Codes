# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 15:41:39 2019

@author: mh iyer

Description: Code to:
            1) Define sigmoid function
            2) Plot it
            3) Get sigmoid function value for an input x
"""
 
import numpy as np
import math
import matplotlib.pyplot as plt

# create sigmoid class
class Sigmoid:
    # initialize
    def __init__(self):
        pass

    # define sigmoid function
    def sigmoid_function(self,x):
        return (1./(1+math.exp(-x)))
    
    # plot sigmoid curve
    def visualize_sigmoid(self):
        
        # initialize list to store x
        x = []
        # initialize list to store sigmoid(x)
        sigmoid_fcn = []
        
        # loop through a set of values
        for i in np.arange(-20,20,0.1):
            sigmoid_fcn.append(self.sigmoid_function(i))
            x.append(i)
            
        # plot
        plt.scatter(x, sigmoid_fcn, color='blue')
        plt.title('Sigmoid Function')
        plt.xlabel('x')
        plt.ylabel('Sigmoid(x)')
        
# example usage
if __name__ == "__main__":
    
    # initialize Sigmoid object
    s=Sigmoid()
    
    # visualize sigmoid function
    s.visualize_sigmoid()
    
    # calculate sigmoid for a value
    val=0.2
    print('Sigmoid output for',val,' is :',s.sigmoid_function(val))