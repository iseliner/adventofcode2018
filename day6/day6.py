# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 22:55:49 2018

@author: Aoi_B

--- Day 6: Chronal Coordinates ---
"""

from math import *

x_list = []
y_list = []
with open('C:/Users/Aoi_B/Documents/adventofcode2018/day6/input.txt', 'r') as myfile:
    for line in myfile:
        experiment1, experiment2 = line.split(', ')
        x_list.append(int(experiment1))
        y_list.append(int(experiment2))

def manhattanDistance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def findLargestDistance(target_list_x,target_list_y):
    largest_distance = 0
    for x in range(x_list):
        new_distance = manhattanDistance(x_list[x], y_list[x],x_list[x+1], y_list[x+1])
        if new_distance > largest_distance:
            largest_distance = new_distance
    return largest_distance


print(findLargestDistance(x_list,y_list))
    
        
        





