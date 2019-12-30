# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 11:52:59 2019

@author: mh iyer

Define functions from scratch (without using numpy) to compute distances between feature vectors
Currently, the following distances are defined:
    1) L1- Manhattan distance
    2) L2- Euclidean distance
    3) L_inf -  Max distance
    
A good resource to understand distances:
    https://www.cs.utah.edu/~jeffp/teaching/cs5955/L7-Distances.pdf
        
"""

 
import math

# get manhattan distance between two vectors
def L1_dist(vector1, vector2):
    dist = 0
    number_of_features = len(vector1)
    if len(vector2) == number_of_features:
        for i in range(0, number_of_features):
            dist+=abs(vector1[i]-vector2[i])
        return(dist)
    else:
        print('The two vectors have a different number of features!')
        
# get euclidean distance between two vectors
def L2_dist(vector1, vector2):
    dist = 0
    number_of_features = len(vector1)
    if len(vector2) == number_of_features:
        for i in range(0, number_of_features):
            dist+=(vector1[i]-vector2[i])**2
        dist_sqrt = math.sqrt(dist)
        return(dist_sqrt)
    else:
        print('The two vectors have a different number of features!')
        
        
# get L-inf or max distance between two vectors
def Linf_dist(vector1, vector2):
    # define max
    max_val = 0
    number_of_features = len(vector1)
    if len(vector2) == number_of_features:
        for i in range(0, number_of_features):
            dist=abs(vector1[i]-vector2[i])
            if dist>max_val:
                max_val = dist
            return(max_val)
    else:
        print('The two vectors have a different number of features!')