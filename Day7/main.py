FILENAME='Day7/input.txt'
inputFile = open(FILENAME, 'r')
lines = inputFile.readlines()

directory_tree = {
  'a': 123,
  'b': {
    'file.txt': 123,
    'passwords.txt': 54,
    'mydir': {
      'newdir': {
        '..': ['b', 'mydir'],
        '.': 'newdir',
      },
      'other.txt': 32,
      '..': ['b'],
      '.': 'mydir'
    },
    '..': [],
    '.': 'b'
  },
  '..': [],
  '.': '/'
}

directory_tree = {
  '..': [],
  '.': '/'
}

global_array = []

def print_out_directory_tree_sizes(temp_dir):
  directory_size = 0
  dict_array_keys = []
  file_array_keys = []
  for key in temp_dir.keys():
    if key == '.' or key == '..':
      continue
    if type(temp_dir[key]) is dict:
      dict_array_keys.append(key)
    else:
      file_array_keys.append(key)
  
  for dict_key in dict_array_keys:
    directory_size += print_out_directory_tree_sizes(temp_dir.get(dict_key))

  for file_key in file_array_keys:
    directory_size += temp_dir[file_key]
  
  global_array.append( (temp_dir['.'], directory_size) )
  return directory_size
    

# start at the root
current_directory = directory_tree

def process_command(line_array):
  global current_directory
  global directory_tree
  if line_array[1] == 'cd':
    if line_array[2] == '..':
      directory_list = current_directory.get('..')
      current_directory = directory_tree
      for next_dir in directory_list:
        current_directory = current_directory.get(next_dir)
    elif line_array[2] == '/':
      current_directory = directory_tree
    else:
      current_directory = current_directory.get(line_array[2])
  
def process_line(line_array):
  global current_directory
  global directory_tree
  if line_array[0] == 'dir':
    if current_directory.get(line_array[1]) == None:
      if current_directory.get('.') == '/':
        prev_directory = []
      else:
        prev_directory = current_directory.get('..') + [current_directory.get('.')]

      current_directory[line_array[1]] = {'.': line_array[1], '..': prev_directory}

  else:
    if current_directory.get(line_array[1]) == None:
      current_directory[line_array[1]] = int(line_array[0])


for line_number, line in enumerate(lines, start=1):
  line = line.strip()
  line_array = line.split(' ')

  if line_array[0] == '$':
    process_command(line_array)
  else:
    process_line(line_array)
  
print_out_directory_tree_sizes(directory_tree)
question_1_answer = sum([x[1] for x in global_array if x[1] <= 100000])
print(f"Question1: {question_1_answer}")

root_directory_size = [x[1] for x in global_array if x[0] == '/']
root_directory_size = root_directory_size[0]
total_size = 70000000
space_needed = 30000000
total_used_space = total_size - root_directory_size
min_space_to_delete = space_needed - total_used_space

min_directory_to_delete = min([x[1] for x in global_array if x[1] >= min_space_to_delete])

print(f"Question 1: {min_directory_to_delete}")

# close the file
inputFile.close()