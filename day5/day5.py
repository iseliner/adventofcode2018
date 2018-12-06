# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:22:08 2018

--- Day 5: Alchemical Reduction ---
"""

with open('C:/Users/Aoi_B/Documents/adventofcode2018/day5/input.txt', 'r') as myfile:
    polymer=myfile.read().replace('\n', '')

old_length = len(polymer)

def reactPolymer(polymer):
    x = 0
    while x < len(polymer):
        if x != len(polymer)-1:
            if polymer[x].lower() == polymer[x+1].lower():
                if polymer[x] != polymer[x+1]:
                    polymer = polymer[:x] + polymer[x+2:]
                    x = 0
                else:
                    x = x + 1
            else:
                x = x + 1
        else:
            x = x + 1
    return polymer

def optimalPolymerEvaluator(element, polymer):
        experiment_polymer = polymer.replace(str(element),'')
        experiment_polymer = polymer.replace(str(element.upper()),'')
        return experiment_polymer
    
def polymerImprovementDevice(polymer):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    optimal_length = 100000
    optimal_element = ''
    for letter in alphabet:
        experiment_polymer = optimalPolymerEvaluator(letter, polymer)
        new_polymer = reactPolymer(experiment_polymer)
        print(len(new_polymer))
        if len(new_polymer) < optimal_length:
            optimal_length = len(new_polymer)
            optimal_element = letter
    print("After extensive experimentation the most optimal polymer improvement is removing " +
          optimal_element + " from the polymer, resulting in polymer length " + str(optimal_length)
          + "!")
    
polymerImprovementDevice(polymer)











