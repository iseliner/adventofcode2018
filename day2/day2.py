#--- Day 2: Inventory Management System ---

id_list = open('C:/Users/Aoi_B/Documents/adventofcode2018/day2/input.txt', 'r')

def findPatterns(box_id):
    letter_list = []
    for letter in box_id:
        if letter not in letter_list:
            letter_list.append(letter)
    return(letter_list)
    
def validate(box_id):
    print('scanning id...')
    letter_list = findPatterns(box_id)
    print(str(letter_list))
    print('identifying box id...')
    largest_letter_number = 0
    for letter in letter_list:
        letter_number = 0
        for char in box_id:
            if(str(letter) == str(char)):
                letter_number = letter_number + 1
        if letter_number < largest_letter_number:
            largest_letter_number = letter_number
    return largest_letter_number
        

def run_scan(target_ids):
    print('')
    print('initializing id class...')
    three_id_count = 0
    two_id_count = 0
    for target_id in id_list:
        scan_result = validate(target_id)
        print('The validation result of box id ' + str(target_id) + "is " 
              + str(scan_result))
        if scan_result == '3':
            two_id_count = two_id_count + 1
        if scan_result == '2':
            three_id_count = three_id_count + 1
    print("The final checksum is : " + str(three_id_count * two_id_count))
    
run_scan(id_list)

            
            
        
