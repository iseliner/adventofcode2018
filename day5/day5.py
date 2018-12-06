# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:22:08 2018

--- Day 5: Alchemical Reduction ---
"""

with open('C:/Users/Aoi_B/Documents/adventofcode2018/day5/input.txt', 'r') as myfile:
    polymer=myfile.read().replace('\n', '')

word = "Chupacabra"
word = word[:2]+[4]

x = 0
while x < len(polymer):
    if x != len(polymer)-1:
        if polymer[x].lower() == polymer[x+1].lower():
            if polymer[x] != polymer[x+1]:
                polymer = polymer[:x-1] + polymer[x+2:]
                print('removed: ' + str(polymer[x]) + str(polymer[x+1]))
                x = 0
            else:
                x = x + 1
        else:
            x = x + 1
    else:
        x = x + 1
print('The remaining polymer is: ' + str(polymer))
print(len(polymer))
        

