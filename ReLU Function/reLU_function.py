# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 17:09:44 2019

@author: mh iyer

Description: Code to:
            1) Define ReLU function
            2) Plot it
            3) Get ReLU function value for an input x
"""
 
import numpy as np
import matplotlib.pyplot as plt

# create ReLU class
class relu:
    # initialize
    def __init__(self):
        pass

    # define ReLU function
    def relu_function(self,x):
        return(max(0,x))
    
    # plot relu curve
    def visualize_relu(self):
        
        # initialize list to store x
        x = []
        # initialize list to store relu(x)
        r_fcn = []
        
        # loop through a set of values
        for i in np.arange(-40,40,0.1):
            r_fcn.append(self.relu_function(i))
            x.append(i)
            
        # plot
        plt.plot(x, r_fcn, color='green',marker='o')
        plt.title('ReLU Function')
        plt.xlabel('x')
        plt.ylabel('ReLU(x)')
        
# example usage
if __name__ == "__main__":

    # initialize object
    r=relu()
    
    # visualize function
    r.visualize_relu()
    
    # calculate relu for a value
    val=-10
    print('ReLU output for',val,' is :',r.relu_function(val))
