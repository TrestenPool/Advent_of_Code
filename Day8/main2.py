FILENAME = 'Day8/input.txt'
input_file = open(FILENAME, 'r')
lines = input_file.readlines()
lines = [x.strip() for x in lines] #remove the new line character from each of the lines

length = len(lines)
width = len(lines[0])

def is_visable(tree_height, constant_metric, starting_i, ending_i, i_adder, row_changing):
  global lines

  total_trees_visable = 0
  i = starting_i
  if row_changing:
    while i != ending_i:
      if int( lines[i][constant_metric] ) < tree_height:
        total_trees_visable += 1
      else:
        total_trees_visable += 1
        return total_trees_visable
      i += i_adder
    return True
  else:
    while i != ending_i:
      if int( lines[constant_metric][i] ) >= tree_height:
        return False
      i += i_adder
    return True