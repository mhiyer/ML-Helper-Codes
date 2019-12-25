# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 16:53:01 2019

@author: mh iyer

Description: Code to:
            1) Define tanh function
            2) Plot it
            3) Get tanh function value for an input x
"""
 
import numpy as np
import matplotlib.pyplot as plt

# create tanh class
# inspired by : https://www.geeksforgeeks.org/numpy-tanh-python/
class tanh:
    # initialize
    def __init__(self):
        pass

    # define sigmoid function
    def tanh_function(self,x):
        return np.tanh(x)
    
    # plot sigmoid curve
    def visualize_tanh(self):
        
        # initialize list to store x
        x = []
        # initialize list to store sigmoid(x)
        tanh_fcn = []
        
        # loop through a set of values
        for i in np.linspace(-np.pi, np.pi, 60):
            tanh_fcn.append(self.tanh_function(i))
            x.append(i)
            
        # plot
        plt.plot(x, tanh_fcn, color='violet',marker='o')
        plt.title('tanh Function')
        plt.xlabel('x')
        plt.ylabel('tanh(x)')
        
# example usage
if __name__ == "__main__":
    
    # initialize object
    t=tanh()
    
    # visualize tanh function
    t.visualize_tanh()
    
    # calculate tanh for a value
    val=np.pi/5
    print('tanh output for',val,' is :',t.tanh_function(val))