#--- Day 1: Chronal Calibration ---

input_data = open('C:/Users/Aoi_B/Documents/adventofcode2018/day1/input.txt', 'r')

current_frequency = 0

for element in input_data:
    if(element[:0] == '-'):
        current_frequency = current_frequency - int(element)
    else:
        current_frequency = current_frequency + int(element)
        
print('The resulting frequency is ' + str(current_frequency) + '!')
        
    
    
