'''
Day 3: rucksack reorganization
  - things need to be raranged
  - each rucksack has 2 large compartments
'''
import string
FILENAME = 'input.txt'
inputFile = open(FILENAME, 'r')
lines = inputFile.readlines()

priority_dict = {}
lower_case_letters = string.ascii_lowercase
upper_case_letters = string.ascii_uppercase
for idx, (lower,upper) in enumerate( zip(lower_case_letters, upper_case_letters), start=1 ):
  priority_dict[lower] = idx
  priority_dict[upper] = idx + 26
  
#### Question 1 ####
total_sum = 0
for line in lines:
  line_length = len(line)
  first_compartment, second_compartment = line[:line_length//2], line[line_length//2:]
  common_letters = ''.join( set(first_compartment).intersection(second_compartment) )
  if common_letters != '':
    total_sum += priority_dict.get(common_letters)
print(total_sum)



#### Question 2 ####
array_of_priorities = [0, 0, 0]

group = 0
group_array = []
line_in_group = 1

for line in lines:
  group_array.append(line)
  line_in_group += 1

  if line_in_group == 4:
    common_letter = ''.join( set(group_array[0]).intersection(group_array[1]).intersection(group_array[2]) ).strip()
    array_of_priorities[group] += priority_dict.get(common_letter)
    group_array = []
    line_in_group = 1
    group += 1
    if group == 3:
      group = 0

print(sum(array_of_priorities))

   


inputFile.close()
