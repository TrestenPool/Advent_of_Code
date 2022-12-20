FILENAME = 'Day8/input.txt'
input_file = open(FILENAME, 'r')
lines = input_file.readlines()
lines = [x.strip() for x in lines] #remove the new line character from each of the lines

length = len(lines)
width = len(lines[0])

# 0 if not visable, 1 if it is visable
visable_array = [[0 for i in range(width)] for j in range(length)]
for line_number, line in enumerate(visable_array):
  if line_number == 0 or line_number == length-1:
    visable_array[line_number] = [1 for x in range(width)]
  else:
    visable_array[line_number][0], visable_array[line_number][width-1] = 1,1

def is_visable(tree_height, constant_metric, starting_i, ending_i, i_adder, row_changing):
  global lines
  i = starting_i
  if row_changing:
    while i != ending_i:
      if int( lines[i][constant_metric] ) >= tree_height:
        return False
      i += i_adder
    return True
  else:
    while i != ending_i:
      if int( lines[constant_metric][i] ) >= tree_height:
        return False
      i += i_adder
    return True

def num_houses_visable(tree_height, constant_metric, starting_i, ending_i, i_adder, row_changing):
  global lines
  i = starting_i
  num_houses = 0
  if row_changing:
    while i != ending_i:
      num_houses += 1
      if int( lines[i][constant_metric] ) >= tree_height:
        return num_houses
      i += i_adder
    return num_houses
  else:
    while i != ending_i:
      num_houses += 1
      if int( lines[constant_metric][i] ) >= tree_height:
        return num_houses
      i += i_adder
    return num_houses

  
def question_1(i, j):
  global lines
  global visable_array

  current_tree_height = int(lines[i][j])

  # check top
  if is_visable(current_tree_height, j, i-1, -1, -1, True):
    visable_array[i][j] = 1

  # check bottom
  elif is_visable(current_tree_height, j, i+1, length, 1, True):
    visable_array[i][j] = 1

  # check left
  elif is_visable(current_tree_height, i, j-1, -1, -1, False):
    visable_array[i][j] = 1

  # check right
  elif is_visable(current_tree_height, i, j+1, width, 1, False):
    visable_array[i][j] = 1
  

scenic_scores = [[0 for i in range(width)] for x in range(length)]
def question_2(i, j):
  global lines, visable_array, scenic_scores
  current_tree_height = int(lines[i][j])

  # calculate the number of houses visable from each of the houses
  num_houses_above = num_houses_visable(current_tree_height, j, i-1, -1, -1, True)
  num_house_below = num_houses_visable(current_tree_height, j, i+1, length, 1, True)
  num_houses_left = num_houses_visable(current_tree_height, i, j-1, -1, -1, False)
  num_houses_right = num_houses_visable(current_tree_height, i, j+1, width, 1, False)

  scenic_scores[i][j] = num_houses_above * num_house_below * num_houses_left * num_houses_right
  

# Go through all except the first and last row, and 1st and last columns for each of those rows
for i in range(1, length-1):
  for j in range(1, width-1):
    question_1(i,j)
    question_2(i, j)

question_1_answer = sum(list(map(sum, visable_array)))
print(f"Question 1: {question_1_answer}")

question_2_answer = max(list(map(max, scenic_scores)))
print(f"Question 2: {question_2_answer}")

# close the file
input_file.close()